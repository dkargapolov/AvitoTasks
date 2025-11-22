import pytest

class TestIntegration:
    """INT-01: Интеграционные тесты"""
    
    def test_int_01_get_deleted_item(self, api_client, valid_item_data):
        """INT-01 Интеграция: получение удаленного объявления"""
        response = api_client.create_item(valid_item_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert "status" in response_data
        assert "Сохранили объявление" in response_data["status"]
        
        # Извлекаем ID с помощью надежного метода
        item_id = api_client.extract_item_id_from_response(response_data)
        assert item_id is not None, "Не удалось извлечь ID из ответа"
        assert api_client.is_valid_uuid(item_id)
        
        # Удаляем объявление
        delete_response = api_client.delete_item(item_id)
        assert delete_response.status_code == 200
        
        # Пытаемся получить удаленное объявление
        get_response = api_client.get_item(item_id)
        assert get_response.status_code == 404