#--------------------IMPORTS--------------------#
from ..src.main import app
from fastapi.testclient import TestClient

#--------------------OBJECTS--------------------#
client = TestClient(app)

#--------------------FUNCTIONS TO TEST--------------------#
# GET ReST API
def test_first_api():
    response = client.get("/api")
    assert response.status_code == 200
    print (response.json())
    assert response.json() == {"Message": "First API"}
# Example test from class
# def test_first_api():
#     assert first_api()
#     print (first_api())

# GET ReST API with path parameters
def test_first_apiV2():
    response = client.get("/books/Path%20Parameters")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"Message": "Path Parameters"}

# GET ReST API with query parameters
def test_first_apiV3():
    response = client.get("/books/Query%20Parameters")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"Message": "Query Parameters"}

# GET ReST API with path parameters AND query parameters
# def test_first_apiV7():
#     response = client.get("/books/Path%20Parameters/Query%20Parameters")
#     assert response.status_code == 200
#     print(response.json())
#     assert response.json() == {"Message": "Path Parameters/Query Parameters"}




# POST ReST API
# def test_first_apiV4():




# PUT ReST API
# def test_first_apiV5():




# DELETE ReST API
# def test_first_apiV6():

