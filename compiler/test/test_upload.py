import json
import requests
from requests import Response

url_upload = 'http://127.0.0.1:8000/compiler/upload'

def test():
    response = requests.get(url_upload)
    print(response)  # Print the response object
    assert response.status_code == 404

# def test():
#     # TEST_NAME = 'my file'
#     response: Response = requests.get(url_upload)
#     print(Reponse)
#     assert response.status_code == 404
    # response: Response = requests.get(url_upload, params={
    #     'name': TEST_NAME
    # })
    # found: dict = json.loads(response.content.decode('utf-8'))
    # assert found.get('name') == TEST_NAME