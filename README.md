# api_final 
## Описание
Доступ к API сети Yatube
***

## Установка зависимостей

`pip install -r requirements.txt`
***

# Примеры:

## Получение JWT токена
Отправьте **POST** запрос `/api/v1/token/`, передав  поля `username` и `password`

## Пример ответа
~~~~
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
~~~~

## Обновление JWT токена
`/api/v1/token/refresh/`
***

## Отправка запроса
При отправке запроса токен необходимо передать в заголовке `Authorization` : `Bearer` `<токен>`

## Работа с постами
`GET` `/api/v1/posts/` - Получить список всех постов  
`POST`  `/api/v1/posts/` - Создать новый пост  
`GET`  `/api/v1/posts/{post_id}/` - Получить пост по id  
`PUT` `/api/v1/posts/{post_id}/` - Обновить пост по id  
`PATCH` `/api/v1/posts/{post_id}/` - Частично обновить пост по id  
`DELETE` `/api/v1/posts/{post_id}/` - Удалить пост по id  


## Работа с комментариями
`GET` `/api/v1/posts/{post_id}/comments/` - Получить список всех комментариев поста  
`POST`  `/api/v1/posts/comments/` - Создать новый комментария для поста  
`GET`  `/api/v1/posts/{post_id}/comments/{comment_id}/` - Получить комментарий поста по id  
`PUT` `/api/v1/posts/{post_id}/comments/{comment_id}/` - Обновить комментарий поста по id  
`PATCH` `/api/v1/posts/{post_id}/comments/{comment_id}/` - Частично Обновить комментарий поста по id  
`DELETE` `/api/v1/posts/{post_id}/comments/{comment_id}/` - Удалить комментарий поста по id   

## Работа с группами
`GET` `/api/v1/group/` - Получить список всех групп  
`POST`  `/api/v1/group/` - Создать новую группу  

## Работа с подписчиками
`GET` `/api/v1/follow/` - Получить список всех подписчиков  
`POST`  `/api/v1/follow/` - Создать подписку  