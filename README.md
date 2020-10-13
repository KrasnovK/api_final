# api_final 
<h2>Описание</h2>
Доступ к API сети Yatube
***

<h3>Установка зависимостей</h3>

`pip install -r requirements.txt`
***

<h3>Получение JWT токена</h3>
Отправьте POST запрос `localhost:8000/api/v1/token/`, передав  поля `username` и `password`

<h3>Пример ответа</h3>
{
    "refresh":
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMjY3NjM5NCwianRpIjoiNzg1YWMwYTc4ZTNiNDdhMTg1MTE3NWU1ZjVlZDAyMTkiLCJ1c2VyX2lkIjoxfQ.
bqXf9Tyt0hfziZ9Jkq5csJ5BdOBEgAIlwtB8oNaSKpY",
    "access": 
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAyNTkwMjk0LCJqdGkiOiJjMjliNzk3OGQxMTI0YTI0OWNlOGRkZmRiZWQ3MzdmOCIsInVzZXJfaWQiOjF9.
LIw_pnJcqPzgDgdvWoUGP1_Se44A90nuYuFw4cQ5e3Q"
}