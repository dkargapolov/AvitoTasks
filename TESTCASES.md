## POS-01 Успешное создание объявления с валидными данными 

### Шаги воспроизведения

1. Выполнить запрос:  

   `POST /api/1/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Content-Type: application/json  

   Accept: application/json  

   Тело запроса:

   ```json
{
	"sellerID": 123,
	"name": "Телефон Iphone",
	"price": 25000,
	"statistics": {
		"likes": 10,
		"viewCount": 100,
		"contacts": 5
	}
}
   ```
   
### Ожидаемый результат

**Статус код:** 200 OK  

Тело ответа:  

```json
{
    "status": "Сохранили объявление - 7e93da8e-c8d2-4b4b-a6e4-440a34e228b1"
}
```

ID пробивается по /api/1/item/:id 
## POS-02 Создание объявления с минимально допустимыми данными 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `POST /api/1/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Content-Type: application/json  

   Accept: application/json  

   Тело запроса:: 

   ```json
{
	"sellerID": 1,
	"name": "a",
	"price": 1,
	"statistics": {
		"likes": 1,
		"viewCount": 1,
		"contacts": 1
	}
}
   ```
### Ожидаемый результат

**Статус код:** 200 OK  

Тело ответа:  

```json
{
    "status": "Сохранили объявление - 7e93da8e-c8d2-4b4b-a6e4-440a34e228b1"
}
```

ID пробивается по /api/1/item/:id 
## POS-03 Попытка создания объявления без обязательного поля sellerID 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `POST /api/1/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Content-Type: application/json  

   Accept: application/json  

   Тело запроса:: 

   ```json
{
	"name": "a",
	"price": 1,
	"statistics": {
		"likes": 1,
		"viewCount": 1,
		"contacts": 1
	}
}
   ```
### Ожидаемый результат

**Статус код:** 400 Bad Request  

Тело ответа:  

```json

{

"result": {

"message": "поле sellerID обязательно",

"messages": {}

},

"status": "400"

}

```

Объект с ошибкой валидации, содержащий сообщения.
## POS-04 Попытка создания объявления без обязательного поля name 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `POST /api/1/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Content-Type: application/json  

   Accept: application/json  

   Тело запроса:: 

   ```json
{
	"sellerID": 1,
	"price": 1,
	"statistics": {
		"likes": 1,
		"viewCount": 1,
		"contacts": 1
	}
}
   ```

### Ожидаемый результат

**Статус код:** 400 Bad Request  

Тело ответа:  

```json

{

"result": {

"message": "поле name обязательно",

"messages": {}

},

"status": "400"

}

```

Объект с ошибкой валидации.
## POS-05 Попытка создания объявления с неверным типом данных (price как string) 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `POST /api/1/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Content-Type: application/json  

   Accept: application/json  

   Тело запроса:: 

   ```json
{
	"sellerID": 1,
	"name": "a",
	"price": "1",
	"statistics": {
		"likes": 1,
		"viewCount": 1,
		"contacts": 1
	}
}
   ```

### Ожидаемый результат

**Статус код:** 400 Bad Request  

Тело ответа:  

```json
{

"result": {

"message": "",

"messages": {}

},

"status": "не передано тело объявления"

}
```

Объект с ошибкой валидации.
## POS-06 Попытка создания объявления с отрицательной ценой 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `POST /api/1/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Content-Type: application/json  

   Accept: application/json  

   Тело запроса:: 

   ```json
{
	"sellerID": 1,
	"name": "a",
	"price": -100,
	"statistics": {
		"likes": 1,
		"viewCount": 1,
		"contacts": 1
	}
}
   ```

### Ожидаемый результат

**Статус код:** 400 Bad Request  

Тело ответа:  

```json
{

"result": {

"message": "",

"messages": {}

},

"status": "не передано тело объявления"

}
```

Объект с ошибкой валидации.
## POS-07 Попытка создания объявления с очень длинным названием 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `POST /api/1/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Content-Type: application/json  

   Accept: application/json  

   Тело запроса:: 

   ```json
{
	"sellerID": 1,
	"name": "Очень длинное название товара которое превышает стандартные лимиты длины для поля названия в системе и должно быть обработано соответствующим образом в зависимости от установленных ограничений сервиса на максимальную длину наименования объявления при создании новых записей в базе данных через API интерфейс микросервиса объявлений предназначенного для работы с пользовательскими объявлениями на торговой площадке",
	"price": 100,
	"statistics": {
		"likes": 1,
		"viewCount": 1,
		"contacts": 1
	}
}
   ```

### Ожидаемый результат

**Статус код:** 200 OK  

Тело ответа:  

```json
{
    "status": "Сохранили объявление - 7e93da8e-c8d2-4b4b-a6e4-440a34e228b1"
}
```

ID пробивается по /api/1/item/:id 

## POS-08 Попытка создания объявления с неполной структурой statistics 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `POST /api/1/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Content-Type: application/json  

   Accept: application/json  

   Тело запроса:: 

   ```json
{
	"sellerID": 1,
	"name": "тест",
	"price": 100,
	"statistics": {
		"likes": 1
	}
}
   ```

### Ожидаемый результат

**Статус код:** 400 Bad Request  

Тело ответа:  

```json
{

"result": {

"message": "поле contacts обязательно",

"messages": {}

},

"status": "400"

}
```

Объект с ошибкой валидации.
## GET-01 Успешное получение существующего объявления 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `GET /api/1/item/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = (сохраненный ID объявления, например 2f8b03f5-12ae-48a7-a60c-d4558e8ce79a)

### Ожидаемый результат

**Статус код:** 200 OK  

Тело ответа:  

Получение данных о запрашиваемом объявлении

```json
[

{

"createdAt": "2025-11-22 16:46:57.276199 +0300 +0300",

"id": "2f8b03f5-12ae-48a7-a60c-d4558e8ce79a",

"name": "тест",

"price": 100,

"sellerId": 1,

"statistics": {

"contacts": 1,

"likes": 1,

"viewCount": 1

}

}

]
```

Массив с одним объектом объявления. Данные должны полностью совпадать с данными, возвращенными при создании.
## GET-02 Попытка получения объявления по несуществующему ID 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `GET /api/1/item/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = 123ABC!@#

### Ожидаемый результат

**Статус код:** 400 

Тело ответа:  

```json
{

"result": {

"message": "ID айтема не UUID: 123ABC!@#",

"messages": {}

},

"status": "400"

}
```

Объект с ошибкой.
## GET-03 Попытка получения объявления с пустым ID 

### Шаги воспроизведения
1.   Выполнить запрос:  

   `GET /api/1/item/`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id не передан

### Ожидаемый результат

**Статус код:** 400 

Тело ответа:  

```json
{

"result": {

"message": "ID айтема не UUID: :id",

"messages": {}

},

"status": "400"

}
```

Объект с ошибкой.
## GAL-01 Успешное получение списка объявлений существующего продавца 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `GET /api/1/:sellerID/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   sellerID = существующий ID (например 123)
### Ожидаемый результат

**Статус код:** 200 OK  

Ожидается массив объектов объявлений. Количество элементов должно совпадать с количеством созданных объявлений.

## GAL-02 Запрос объявлений продавца, у которого нет объявлений 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `GET /api/1/:sellerID/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   sellerID = новый, неиспользованный ID (например 2918361964)
### Ожидаемый результат

**Статус код:** 200 OK  

Тело ответа:  

```json

[]

```

Пустой массив.

## GAL-03 Попытка запроса с несуществующим sellerID (за пределами диапазона) 
### Шаги воспроизведения

1.   Выполнить запрос:  

   `GET /api/1/:sellerID/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   sellerID = 2918361964111111111111

### Ожидаемый результат

**Статус код:** 400 Bad request  

Тело ответа:  

```json
{

"result": {

"message": "передан некорректный идентификатор продавца",

"messages": {}

},

"status": "400"

}
```

Объект с ошибкой.

## GAL-04 Попытка запроса с некорректным типом sellerID (string) 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `GET /api/1/:sellerID/item`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   sellerID = abc
### Ожидаемый результат

**Статус код:** 400 Bad Request  

Тело ответа:  

```json
{

"result": {

"message": "передан некорректный идентификатор продавца",

"messages": {}

},

"status": "400"

}
```

Объект с ошибкой валидации.
## STA-01 Успешное получение статистики существующего объявления 
### Шаги воспроизведения

1.   Выполнить запрос:  

   `GET /api/1/statistic/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = сохраненный ID объявления (например 2f8b03f5-12ae-48a7-a60c-d4558e8ce79a)

### Ожидаемый результат

**Статус код:** 200 OK  

Тело ответа:  (возможный ответ)

```json
[

{

"contacts": 1,

"likes": 1,

"viewCount": 1

}

]
```

Массив с объектом статистики выбранного объявления. Поля должны совпадать с изначально созданным объявлением. Поля likes, viewCount, contacts должны иметь тип integer и значения, переданные при создании.
## STA-02 Попытка получения статистики по несуществующему ID 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `GET /api/1/statistic/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = nonExistingId123
### Ожидаемый результат

**Статус код:** 404 Not Found  

Тело ответа:  

```json
{

"result": {

"message": "передан некорректный идентификатор объявления",

"messages": {}

},

"status": "400"

}
```


## DEL-01 Успешное удаление существующего объявления 

### Шаги воспроизведения

1. С помощью запроса /api/1/:sellerID/item (где :sellerID может быть равно 333333) выберите объявление для удаления, скопируйте значение "id" одного из объявлений, 

2.   Выполнить запрос:  

   `DELETE /api/2/item/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = выбранный вами ID объявления

### Ожидаемый результат

**Статус код:** 200 OK  

Тело ответа: Пустое тело

При запросе отображения удаленного объявления по ID возникает ошибка 404 not found

## DEL-02 Попытка повторного удаления объявления 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `DELETE /api/2/item/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = только что удаленный ID
### Ожидаемый результат

**Статус код:** 404 Not Found  

Тело ответа:  

```json
{

"result": {

"message": "",

"messages": null

},

"status": "404"

}
```


## DEL-03 Попытка удаления несуществующего объявления 

### Шаги воспроизведения

1.   Выполнить запрос:  

   `DELETE /api/2/item/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = nonExistingId123

### Ожидаемый результат

**Статус код:** 400 Bad request

Тело ответа:  

```json
{
    "result": {
        "message": "переданный id айтема некорректный",
        "messages": {}
    },
    "status": "400"
}
```
## INT-01 Интеграция: получение удаленного объявления 

### Шаги воспроизведения
1.   Выполнить запрос:  

   `DELETE /api/2/item/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = сохраненный ID объявления

2.   Выполнить запрос:  

   `GET /api/1/item/:id`  

   **Адрес сервиса:** https://qa-internship.avito.com  

   Заголовки:

   Accept: application/json  

   **Path parameter:**  

   id = сохраненный ID объявления
### Ожидаемый результат

**Шаг 1:** Статус код: 200 OK  

**Шаг 2:** Статус код: 404 Not Found
