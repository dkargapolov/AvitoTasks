class Config:
    BASE_URL = "https://qa-internship.avito.com"
    API_VERSION_1 = "/api/1"
    API_VERSION_2 = "/api/2"
    
    # Endpoints
    ITEM_ENDPOINT = f"{API_VERSION_1}/item"
    SELLER_ITEMS_ENDPOINT = f"{API_VERSION_1}/{{sellerID}}/item"
    STATISTICS_ENDPOINT = f"{API_VERSION_1}/statistic"
    DELETE_ITEM_ENDPOINT = f"{API_VERSION_2}/item"
    
    # Headers
    JSON_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }