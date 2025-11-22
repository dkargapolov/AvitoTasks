import pytest

class TestDeleteItems:
    """DEL-01 - DEL-03: Тесты удаления объявлений"""
    
    def test_del_01_successful_delete_existing_item(self, api_client, valid_item_data):
        """DEL-01 Успешное удаление существующего объявления"""
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
        assert delete_response.text == ""  # Пустое тело ответа
        
        # Проверяем что объявление больше не доступно
        get_response = api_client.get_item(item_id)
        assert get_response.status_code == 404
    
    def test_del_02_redelete_item(self, api_client, created_item_id):
        """DEL-02 Попытка повторного удаления объявления"""
        if not created_item_id:
            pytest.skip("Не удалось создать тестовое объявление")
        
        # Первое удаление
        first_delete = api_client.delete_item(created_item_id)
        assert first_delete.status_code == 200
        
        # Повторное удаление
        second_delete = api_client.delete_item(created_item_id)
        assert second_delete.status_code == 404
    
    def test_del_03_delete_nonexistent_item(self, api_client):
        """DEL-03 Попытка удаления несуществующего объявления"""
        invalid_id = "nonExistingId123"
        response = api_client.delete_item(invalid_id)
        
        assert response.status_code == 400
        response_data = response.json()
        assert "переданный id айтема некорректный" in response_data["result"]["message"]