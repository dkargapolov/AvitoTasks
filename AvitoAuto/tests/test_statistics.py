import pytest

class TestStatistics:
    """STA-01 - STA-02: Тесты статистики"""
    
    def test_sta_01_successful_get_statistics(self, api_client, created_item_id):
        """STA-01 Успешное получение статистики существующего объявления"""
        if not created_item_id:
            pytest.skip("Не удалось создать тестовое объявление")
        
        response = api_client.get_statistics(created_item_id)
        assert response.status_code == 200
        
        stats_data = response.json()
        assert isinstance(stats_data, list)
        assert len(stats_data) > 0
        
        stats = stats_data[0]
        assert "contacts" in stats
        assert "Likes" in stats or "likes" in stats
        assert "viewCount" in stats
        
        # Проверяем типы данных
        assert isinstance(stats.get("contacts", 0), int)
        assert isinstance(stats.get("likes", stats.get("Likes", 0)), int)
        assert isinstance(stats.get("viewCount", 0), int)
    
    def test_sta_02_get_statistics_nonexistent_id(self, api_client):
        """STA-02 Попытка получения статистики по несуществующему ID"""
        invalid_id = "nonExistingId123"
        response = api_client.get_statistics(invalid_id)
        
        # В зависимости от реализации API, может быть 400 или 404
        assert response.status_code in [400, 404]