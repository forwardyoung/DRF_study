## Concept

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

## Setting

1. `DRF`를 설치한다.

```python
pip install djangorestframework
```

2. 프로젝트 폴더의 `settings.py` 파일 - `INSTALLED_APPS`에 `rest_framework`를 추가한다.

**🍯 option**

 [pagination style](https://www.django-rest-framework.org/api-guide/pagination/#setting-the-pagination-style)을 설정한다.

➡️ `DEFAULT_PAGINATION_CLASS`과  `PAGE_SIZE` 모두 기본값이 `None`이다.

```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20
}
```

3. 브라우저를 통해 API를 테스트하고자 할 때, 인증하기 위한 과정에 필요한 다음 코드를 루트 `urls.py`에 추가한다.

```python
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

4. 서버를 실행시킨 후, api-auth로 경로를 입력하면 로그인과 로그아웃 페이지를 확인할 수 있다.

![image-20230310171434839](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20230310171434839.png)

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

즉, serializer를 사용하면 쿼리셋 및 모델 인스턴와 같은 복잡한 데이터를 Python 데이터 타입으로 변환한 다음 `JSON`, `XML` 또는 다른 콘텐츠 유형으로 쉽게 렌더링할 수 있다.

Serializer는 Django의 `Form` 및 `ModelForm` 클래스와 매우 유사하게 작동한다.

📍form과의 차이점

:`form`은 **HTML form**을 생성하는데, `Serializer`는 결과물이 Json



**serializer 사용 예시**

Comment class를 만들고 comment 인스턴스를 만든다.

```python
from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
        
comment = Comment(email='leila@example.com', content='foo bar')
```

serializer를 만든다. 이는 `form`을 만드는 것과 유사하다.	

```python
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

serializer 클래스를 사용해 인스턴스를 직렬화한다.

```python
serializer = CommentSerializer(comment)
serializer.date
# {'email': 'leila@example.com', 'content': 'foo bar', 'created': '2016-01-27T15:17:10.375877'}
```

모델 인스턴스를 Python 네이티브 데이터 타입으로 변환한다. 직렬화 프로세스를 완료하기 위해 데이터를 json으로 렌더링한다.

```python
from rest_framework.renders import JSONRenderer

json = JSONRenderer().render(serializer.data)
json
# b'{"email":"leila@example.com","content":"foo bar","created":"2016-01-27T15:17:10.375877"}'
```

### Deserializing objects(역직렬화)

역직렬도 유사하다.

먼저 파이썬 네이티브 데이터 타입으로 파싱한다.

```python
import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)
```

네이티브 데이터 타입을 `validated_data` 딕셔너리에 복원한다.

```python
serializer = CommentSerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data
# {'content': 'foo bar', 'email': 'leila@example.com', 'created': datetime.datetime(2012, 08, 22, 16, 20, 09, 822243)}
```

## Class-based Views

REST 프레임워크는 Django의 View 클래스를 하위 클래스로 분류하는 `APIView` 클래스를 제공한다.

APIView는 기본적으로 다음과 같이 구현 가능하다.

```python
class Class_name(APIView):
	def method_name(self, request, format=None):
    	# 해당 HTTP method를 어떻게 동작시키고 처리할지 개발자가 정의
```

`method_name`으로는 HTTP method인 get, post, delete 등이 존재한다.

> function based view가 아닌, class-based view를 사용하여 API view를 작성할 수 있다.
>
> 이는 코드를 재사용하고, Django의 설계 철학 중 하나인 DRY(Don't Repeat Yourself) 원칙을 따르는 데 도움이 되는 강력한 패턴이다.

