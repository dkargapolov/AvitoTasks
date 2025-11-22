import pytest
import uuid
from utils.api_client import ApiClient

@pytest.fixture
def api_client():
    return ApiClient()

@pytest.fixture
def valid_item_data():
    return {
        "sellerID": 123,
        "name": "Телефон Iphone",
        "price": 25000,
        "statistics": {
            "likes": 10,
            "viewCount": 100,
            "contacts": 5
        }
    }

@pytest.fixture
def minimal_item_data():
    return {
        "sellerID": 1,
        "name": "a",
        "price": 1,
        "statistics": {
            "likes": 1,
            "viewCount": 1,
            "contacts": 1
        }
    }

@pytest.fixture
def created_item_id(api_client, valid_item_data):
    """Фикстура для создания тестового объявления и получения его ID"""
    response = api_client.create_item(valid_item_data)
    if response.status_code == 200:
        # Извлекаем ID из ответа
        status_text = response.json().get("status", "")
        if "Сохранили объявление –" in status_text:
            item_id = status_text.split("–")[1].strip()
            yield item_id
            # Удаляем объявление после теста
            api_client.delete_item(item_id)
        else:
            yield None
    else:
        yield None


@pytest.fixture
def created_item_id(api_client, valid_item_data):
    """Фикстура для создания тестового объявления и получения его ID"""
    print("\n=== DEBUG created_item_id fixture ===")
    
    # Шаг 1: Создаем объявление
    print("1. Creating item...")
    response = api_client.create_item(valid_item_data)
    print(f"   Status code: {response.status_code}")
    print(f"   Response text: {response.text}")
    
    if response.status_code != 200:
        print("   ERROR: Failed to create item!")
        yield None
        return
    
    # Шаг 2: Парсим ответ
    print("2. Parsing response...")
    try:
        response_data = response.json()
        print(f"   Response JSON: {response_data}")
    except Exception as e:
        print(f"   ERROR: Failed to parse JSON: {e}")
        yield None
        return
    
    # Шаг 3: Извлекаем ID
    print("3. Extracting item ID...")
    item_id = api_client.extract_item_id_from_response(response_data)
    print(f"   Extracted ID: {item_id}")
    
    if not item_id:
        print("   ERROR: Failed to extract item ID!")
        print(f"   Status text: {response_data.get('status', 'No status field')}")
        yield None
        return
    
    # Шаг 4: Проверяем валидность UUID
    print("4. Validating UUID...")
    if api_client.is_valid_uuid(item_id):
        print(f"   ID is valid UUID: {item_id}")
        yield item_id
        # Удаляем объявление после теста
        print("5. Cleaning up - deleting item...")
        api_client.delete_item(item_id)
    else:
        print(f"   ERROR: Invalid UUID format: {item_id}")
        yield None
    
    print("=====================\n")