# Concept

`SPA(Single-page application)` 체제가 트렌드가 되면서 back-end에서 비동기로 작동시키고자 DRF를 사용한다.

## DRF란?

> Django 안에서 `RESTful API` 서버를 쉽게 구축할 수 있도록 도와주는 라이브러리

- Micro Framework

ex)

```python
GET http://abc.com/users
GET http://abc.com/user/1
POST http://abc.com/users
PUT http://abc.com/user/1
DELETE http://abc.com/user/1
GET http://abc.com/user/1/todos
```

## RestAPI

`REST(REpresentational State Transfer)`

- 프로토콜 아님
- 표준 아님

**특징**

- uniform
- Stateless
- Cacheable

**구현**

- Method로 하는 행위 구별
- Item과 id만 URL에 사용
- `"-"`는 가독성을 위해 사용
- `"_"`는 사용하지 않음
- 파일 확장자는 url에 포함하지 않음
- 언제나 **소문자만** 사용

## Serializer(직렬화)

front-end와 back-end의 통신은 **Json** 포맷으로 한다.

> Json ➡️ Python 객체

Python 객체 ➡️ Json (front-end에 return)

```python
{
    "name": "Chaming",
    "age": 20
}
```

```
class foo:
	name: str
	age: int
```



# setting

1. `DRF`를 설치한다.

```python
pip install djangorestframework
```

2. 프로젝트 폴더의 `settings.py` 파일 - `INSTALLED_APPS`에 `rest_framework`를 추가한다.

3. [pagination style](https://www.django-rest-framework.org/api-guide/pagination/#setting-the-pagination-style)을 설정한다.

   ➡️ `DEFAULT_PAGINATION_CLASS`과  `PAGE_SIZE` 모두 기본값이 `None`이다.

```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}
```

