## BUG-01 Создание объявления с отрицательной ценой

Шаги воспроизведения

1. Выполнить запрос:  
   `POST /api/1/item`  
   **Адрес сервиса:** https://qa-internship.avito.com  
   **Headers:**  
   Content-Type: application/json  
   Accept: application/json  
Тело запроса:  
   ```json
   {
     "sellerID": 123456,
     "name": "Телефон с отрицательной ценой",
     "price": -100,
     "statistics": {
       "likes": 10,
       "viewCount": 100,
       "contacts": 5
     }
   }
   ```

### Фактический результат

**Статус код:** 200 OK  
Тело ответа: Создается объявление с отрицательной значением цены
### Ожидаемый результат

**Статус код:** 400 Bad Request  
Тело ответа: Объект с ошибкой валидации, указывающей на недопустимость отрицательной цены

## BUG-02 Повторное удаление объявления возвращает в ошибке status: 500

Шаги воспроизведения

1. Создать объявление и сохранить его ID
2. Выполнить запрос:  
   `DELETE /api/2/item/:id`  
   **Адрес сервиса:** https://qa-internship.avito.com  
   **Headers:**  
   Accept: application/json  
   **Path parameter:**  
   id = сохраненный ID объявления
3. Повторно выполнить запрос:  
   `DELETE /api/2/item/:id`  
   **Адрес сервиса:** https://qa-internship.avito.com  
   **Headers:**  
   Accept: application/json  
   **Path parameter:**  
   id = тот же ID объявления

### Фактический результат

В параметре status отображается неправильный код ошибки

**Статус код:** 404 Internal Server Error  
Тело ответа:  

```json
{

"result": {

"message": "",

"messages": null

},

"status": "500"

}
```
### Ожидаемый результат

**Статус код:** 404 Not Found  
**Тело ответа:** 
```json
{

"result": {

"message": "",

"messages": null

},

"status": "404"

}
```
## Дополнительно
Также я бы обратился к аналитику по вопросу "Должна ли оставаться статистика при запросе статистики удаленного объявления?"
