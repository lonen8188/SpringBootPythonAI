from http.client import responses

from binstar_client import STATUS_CODES
from fastapi import FastAPI, HTTPException # FastAPI 임포트
from pydantic import BaseModel # 데이터 유효성 검사와 설정 관리에 사용되는 라이브러리(모델링이 쉽고 강력함)
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint  # 요청과 응답사이에 특정 작업 수행
# 미들웨어는 모든 요청에 대해 실행되며, 요청을 처리하기 전에 응답을 반환하기 전에 특정 작업을 수행할 수 있음
# 예를 들어 로깅, 인증, cors처리, 압축등...
import logging

from starlette.requests import Request
from starlette.responses import Response

app = FastAPI(
    title="My API",
    description = "This is a sample API",
    version="1.0.0",
   # docs_url=None,  # Swagger UI 비활성화 http://localhost:8000/docs
   # redoc_url=None  # ReDoc 비활성화 http://localhost:8000/redoc
    # Swagger UI와 ReDoc은 모두 API 문서화 도구(OpenAPI) 사양을 기반으로 작동
    # 엔드포인트, 요청 및 응답 형식, 모델 등을 시각적으로 보여줌(postman)
) # 객체 생성후 app 변수에 넣음

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next) :
        logging.info(f"Req: {request.method}{request.url}")
        response = await call_next(request)
        logging.info(f"Status Code : {response.status_code}")
        return response
app.add_middleware(LoggingMiddleware)

class Item(BaseModel):
    name : str
    description : str = None # https://blog.naver.com/youndok/222085870181dsffffffffffffffffff
    price : float
    tax : float = None

items = {}

# 위에 정의된 클래스를 아래 앱 함수 매개변수로 설정하면 FastAPI가 요청 본문을 자동으로 Item 모델로 변환하고 유효성검사를 함
# 잘못된 데이터인 경우에는 442 (Unprocessable Entity) 응답을 반환 https://wha-haha.tistory.com/128
@app.post("/items/")
async def crate_item(item: Item):
    return item

@app.get("/") # http://localhost/ 의 라우트
async def read_root():
    return {"Hello" : "World"}

# 동적 매개변수 item_id를 사용하여 특정 아이템을 조회한다.
@app.get("/items/{item_id}") # http://localhost/items/kkk 의 동적라우트
# async def read_item(item_id: int, q: str= None):
#         return {"item_id": item_id, "q": q}
        # item_id : 경로 매개변수
        # q : 쿼리 매개변수 (기본값은 : None)
async def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(STATUS_CODE=404, detail="Item net found")
    return items[item_id]