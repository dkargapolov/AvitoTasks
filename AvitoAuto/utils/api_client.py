import requests
import uuid
import re
from config import Config

class ApiClient:
    def __init__(self, base_url=Config.BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(Config.JSON_HEADERS)
    
    def create_item(self, item_data):
        """Создание объявления"""
        url = f"{self.base_url}{Config.ITEM_ENDPOINT}"
        response = self.session.post(url, json=item_data)
        return response
    
    def get_item(self, item_id):
        """Получение объявления по ID"""
        url = f"{self.base_url}{Config.ITEM_ENDPOINT}/{item_id}"
        response = self.session.get(url)
        return response
    
    def get_seller_items(self, seller_id):
        """Получение объявлений продавца"""
        url = f"{self.base_url}{Config.API_VERSION_1}/{seller_id}/item"
        response = self.session.get(url)
        return response
    
    def get_statistics(self, item_id):
        """Получение статистики объявления"""
        url = f"{self.base_url}{Config.STATISTICS_ENDPOINT}/{item_id}"
        response = self.session.get(url)
        return response
    
    def delete_item(self, item_id):
        """Удаление объявления"""
        url = f"{self.base_url}{Config.DELETE_ITEM_ENDPOINT}/{item_id}"
        response = self.session.delete(url)
        return response
    
    def is_valid_uuid(self, uuid_string):
        """Проверка валидности UUID"""
        try:
            uuid.UUID(uuid_string)
            return True
        except ValueError:
            return False
    
    def extract_item_id_from_response(self, response_data):
        """Извлечение ID объявления из ответа"""
        status_text = response_data.get("status", "")
        
        # Пробуем разные разделители
        separators = ["–", "-", "—"]  # разные типы дефисов
        
        for separator in separators:
            if separator in status_text:
                parts = status_text.split(separator)
                if len(parts) > 1:
                    item_id = parts[1].strip()
                    if self.is_valid_uuid(item_id):
                        return item_id
        
        # Если не нашли через разделитель, ищем UUID в тексте
        uuid_pattern = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
        match = re.search(uuid_pattern, status_text, re.IGNORECASE)
        if match:
            return match.group()
        
        return None