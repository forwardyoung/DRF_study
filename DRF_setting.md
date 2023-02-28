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

Serializer는 Django `Form` 클래스와 매우 유사한 개념으로, 다양한 필 `required`, `max_length` and `default`와 같은 유사한 유효성 검사 flag를 포함한다. 

📍form과의 차이점

:`form`은 **HTML form**을 생성하는데, `Serializer`는 결과물이 Json



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



## Detail view

> 특정 primary_key에 해당하는 모델에 대한 세부사항을 보여주는 뷰

```python
@action(detail=True, methods=["get", "post"])
    def add_browser_today(self, request, pk=None):
        queryset = self.get_queryset().filter(pk=pk, creator_id=request.users_id).first()
        new_history = Statistic()
        new_history.record(request, queryset, {})
        return MsgOk()
```

`@action` 매핑, `detail=True`

