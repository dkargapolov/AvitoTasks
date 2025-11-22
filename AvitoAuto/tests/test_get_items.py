import pytest

class TestGetItems:
    """GET-01 - GET-03: Тесты получения объявлений"""
    
    def test_get_01_successful_get_existing_item(self, api_client, created_item_id):
        """GET-01 Успешное получение существующего объявления"""
        
        
        response = api_client.get_item(created_item_id)
        assert response.status_code == 200
        
        item_data = response.json()
        assert isinstance(item_data, list)
        assert len(item_data) > 0
        
        item = item_data[0]
        assert "id" in item
        assert item["id"] == created_item_id
        assert "name" in item
        assert "price" in item
        assert "sellerId" in item
        assert "statistics" in item
    
    def test_get_02_get_nonexistent_item(self, api_client):
        """GET-02 Попытка получения объявления по несуществующему ID"""
        invalid_id = "123ABC!@#"
        response = api_client.get_item(invalid_id)
        
        assert response.status_code == 400
        response_data = response.json()
        assert response_data["status"] == "400"
        assert "ID айтема не UUID" in response_data["result"]["message"]
    
    def test_get_03_get_item_empty_id(self, api_client):
        """GET-03 Попытка получения объявления с пустым ID"""
        # Для эмуляции пустого ID в пути
        response = api_client.get_item("")
        assert response.status_code == 404
    
    def test_gal_01_get_seller_items_existing_seller(self, api_client):
        """GAL-01 Успешное получение списка объявлений существующего продавца"""
        seller_id = 123
        response = api_client.get_seller_items(seller_id)
        
        assert response.status_code == 200
        items = response.json()
        assert isinstance(items, list)
    
    def test_gal_02_get_seller_items_no_ads(self, api_client):
        """GAL-02 Запрос объявлений продавца, у которого нет объявлений"""
        seller_id = 2918361964  # Новый, неиспользованный ID
        response = api_client.get_seller_items(seller_id)
        
        assert response.status_code == 200
        items = response.json()
        assert items == []
    
    def test_gal_03_get_seller_items_invalid_seller_id(self, api_client):
        """GAL-03 Попытка запроса с несуществующим sellerID"""
        invalid_seller_id = "291836196411111111111"
        response = api_client.get_seller_items(invalid_seller_id)
        
        assert response.status_code == 400
        response_data = response.json()
        assert "передан некорректный идентификатор продавца" in response_data["result"]["message"]
    
    def test_gal_04_get_seller_items_string_seller_id(self, api_client):
        """GAL-04 Попытка запроса с некорректным типом sellerID (string)"""
        string_seller_id = "abc"
        response = api_client.get_seller_items(string_seller_id)
        
        assert response.status_code == 400
        response_data = response.json()
        assert "передан некорректный идентификатор продавца" in response_data["result"]["message"]