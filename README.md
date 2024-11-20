# SpringBootPythonAI

개발환경구축
1. 파이썬 인터프리터 : http://www.python.org/ -> 3.12버전 설치(3.8이상필수)
2. IDE 설치 : https://www.jetbrains.com/ko-kr/pycharm/download/?section=windows -> 커뮤니티 설치
3. FastAPI 설치 : pip install fastapi uvicorn
   uvicorn : ASGI(Asynchronus Server Gateway Interface) 는 파이썬에서 비동기 웹서버와 웹 애플케이션 간의 인터페이스 표준
   ASGI는 기존 WSGI(Web Server Gateway Interface)의 비동기 버전으로, 파이썬에서 비동기 처리를 지원하는 웹 애플리케이션을 구축하기 위함
   https://velog.io/@hwaya2828/WSGI-ASGI

   ASGI 특징
   - 비동기 지원 : ASGI는 비동기 코드 실행을 지원하며 높은 성능과 동시성을 제공, 웹소켓이나 서버 푸시와 같은 비동기 통신이 필요한 애플리케이션에 유용
   - 범용성 : HTTP뿐만 아니라, WebSocket, gRPC와 같은 다른 프로토콜로 지원
   - 유연성 : ASGI 애플리케이션은 다양한 서버 및 프레임워크와 호환되며, 모듈식으로 구성

   FastAPI와 ASGI
   - FastAPI는 ASGI 표준을 따르는 웹 프레임 워크임
   - FastAPI 애플리케이션은 비동기 처리를 기본으로 하며, Uvicorn과 같은 ASGI 서버를 사용하여 높은 성능을 제공
  
FastAPI 서버 실행
1. main.py 실행
2. Terminal에서 D:\phthonWorkSpace> uvicorn main:app --reload --port 8001 (위치확인)


![AI project](https://github.com/user-attachments/assets/2a93ded9-4075-48dd-a8b0-2ed79e97df97)

파이썬 필수 라이브러리 설치
pip install fastapi uvicorn pydantic Pillow numpy requests
pip install ultralytics opencv-python python-multipart

fastapi(0.111.1) : 비동기 웹 프레임워크, 자동 OpenAPI 문서 생성
uvicorn(0.30.1) : 고성능 비동기 서버, ASGI 표준 지원
pydantic(2.7.1) : 데이터검증 및 직렬화, 타입 힌팅, 설정 관리
Pillow(10.3.0) : 이미지 열기, 저장, 변환, 다양한 이미지 처리 작업
numpy(1.24.4) : 수치계산, 배열 및 행렬 연산, 다양한 수학 함수
requests(2.32.3) : 간단한 http 요청 및 응답 처리
ultraltics(8.2.58) : YOLOv8 객체 탐지 모델
opencv-python(4.10.0) : 이미지 및 비디오 처리, 컴퓨터 비전 기능
python-multipart(0.0.9) : 멀티파트 폼 데이터 파싱을 위해 사용
