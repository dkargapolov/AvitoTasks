import pytest

class TestCreateItems:
    """POS-01 - POS-08: Тесты создания объявлений"""
    
    def test_pos_01_successful_creation_valid_data(self, api_client, valid_item_data):
        """POS-01 Успешное создание объявления с валидными данными"""
        response = api_client.create_item(valid_item_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert "status" in response_data
        assert "Сохранили объявление" in response_data["status"]
        
        # Извлекаем ID с помощью надежного метода
        item_id = api_client.extract_item_id_from_response(response_data)
        assert item_id is not None, "Не удалось извлечь ID из ответа"
        assert api_client.is_valid_uuid(item_id)
    
    def test_pos_02_creation_minimal_data(self, api_client, minimal_item_data):
        """POS-02 Создание объявления с минимально допустимыми данными"""
        response = api_client.create_item(minimal_item_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert "status" in response_data
        assert "Сохранили объявление" in response_data["status"]
        
        # Извлекаем ID с помощью надежного метода
        item_id = api_client.extract_item_id_from_response(response_data)
        assert item_id is not None, "Не удалось извлечь ID из ответа"
        assert api_client.is_valid_uuid(item_id)
    
    def test_pos_07_creation_long_name(self, api_client):
        """POS-07 Попытка создания объявления с очень длинным названием"""
        long_name = "Очень длинное название товара которое превышает стандартные лимиты длины " * 10
        
        item_data = {
            "sellerID": 1,
            "name": long_name,
            "price": 100,
            "statistics": {
                "likes": 1,
                "viewCount": 1,
                "contacts": 1
            }
        }
        
        response = api_client.create_item(item_data)
        
        # Если создание успешно - проверяем стандартный ответ
        if response.status_code == 200:
            response_data = response.json()
            assert "status" in response_data
            assert "Сохранили объявление" in response_data["status"]
            
            # Извлекаем ID с помощью надежного метода
            item_id = api_client.extract_item_id_from_response(response_data)
            assert item_id is not None, "Не удалось извлечь ID из ответа"
            assert api_client.is_valid_uuid(item_id)
        else:
            # Если не прошло - проверяем ошибку
            assert response.status_code == 400

    # Остальные тесты остаются без изменений...
    def test_pos_03_creation_without_seller_id(self, api_client):
        """POS-03 Попытка создания объявления без обязательного поля sellerID"""
        invalid_data = {
            "name": "a",
            "price": 1,
            "statistics": {
                "likes": 1,
                "viewCount": 1,
                "contacts": 1
            }
        }
        
        response = api_client.create_item(invalid_data)
        assert response.status_code == 400
        response_data = response.json()
        assert response_data["status"] == "400"
        assert "sellerID обязательно" in response_data["result"]["message"]
    
    def test_pos_04_creation_without_name(self, api_client):
        """POS-04 Попытка создания объявления без обязательного поля name"""
        invalid_data = {
            "sellerID": 1,
            "price": 1,
            "statistics": {
                "likes": 1,
                "viewCount": 1,
                "contacts": 1
            }
        }
        
        response = api_client.create_item(invalid_data)
        assert response.status_code == 400
        response_data = response.json()
        assert response_data["status"] == "400"
        assert "name обязательно" in response_data["result"]["message"]
    
    def test_pos_05_creation_price_as_string(self, api_client):
        """POS-05 Попытка создания объявления с неверным типом данных (price как string)"""
        invalid_data = {
            "sellerID": 1,
            "name": "a",
            "price": "1",
            "statistics": {
                "likes": 1,
                "viewCount": 1,
                "contacts": 1
            }
        }
        
        response = api_client.create_item(invalid_data)
        assert response.status_code == 400

    
    def test_pos_08_creation_incomplete_statistics(self, api_client):
        """POS-08 Попытка создания объявления с неполной структурой statistics"""
        invalid_data = {
            "sellerID": 1,
            "name": "recr",
            "price": 100,
            "statistics": {
                "likes": 1
            }
        }
        
        response = api_client.create_item(invalid_data)
        assert response.status_code == 400
        response_data = response.json()
        assert "contacts обязательно" in response_data["result"]["message"]

    def test_debug_creation_process(self, api_client):
        """Диагностический тест для отладки процесса создания объявления"""
        print("\n" + "="*50)
        print("DEBUG CREATION PROCESS")
        print("="*50)
        
        # Тестовые данные
        test_data = {
            "sellerID": 123,
            "name": "Телефон Iphone", 
            "price": 25000,
            "statistics": {
                "likes": 10,
                "viewCount": 100,
                "contacts": 5
            }
        }
        
        # Шаг 1: Создаем объявление
        print("1. Sending creation request...")
        response = api_client.create_item(test_data)
        print(f"   Status: {response.status_code}")
        print(f"   Headers: {response.headers}")
        print(f"   Response: {response.text}")
        
        # Шаг 2: Анализируем ответ
        if response.status_code == 200:
            print("2. Creation successful, parsing response...")
            try:
                data = response.json()
                print(f"   JSON: {data}")
                
                # Пробуем разные способы извлечения ID
                status = data.get('status', '')
                print(f"   Status field: '{status}'")
                
                # Способ 1: Через разделитель
                if '–' in status:
                    parts = status.split('–')
                    print(f"   Split by '–': {parts}")
                if '-' in status:
                    parts = status.split('-') 
                    print(f"   Split by '-': {parts}")
                
                # Способ 2: Через регулярное выражение
                import re
                uuid_pattern = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
                matches = re.findall(uuid_pattern, status, re.IGNORECASE)
                print(f"   Regex matches: {matches}")
                
                # Извлекаем ID
                item_id = api_client.extract_item_id_from_response(data)
                print(f"   Extracted ID: {item_id}")
                print(f"   Is valid UUID: {api_client.is_valid_uuid(item_id)}")
                
            except Exception as e:
                print(f"   ERROR parsing response: {e}")
        else:
            print("2. Creation failed!")
        
        print("="*50 + "\n")