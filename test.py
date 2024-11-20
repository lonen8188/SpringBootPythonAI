import requests

url = "http://127.0.0.1:8000/detect"
message = "Test message"
file_path = "sample.jpg"

with open(file_path, "rb") as file: # https://velog.io/@37writes/with-openfilepath-rb-as-f-%EC%9D%98-%EC%9D%98%EB%AF%B8
    response = requests.post(url, data={"message": message},
                             files={"file": file})


print(response.json())