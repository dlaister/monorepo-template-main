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
    response = client.get("/books/?title=Query%20Parameters")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"Message": "Query Parameters"}

# GET ReST API with path parameters AND query parameters
# def test_first_apiV7():
#     response = client.get("/books/Path%20Parameters/?query=Query%20Parameters")
#     assert response.status_code == 200
#     print(response.json())
#     assert response.json() == {"Message": "Query Parameters"}

def test_first_apiV7_2():
    response = client.get("/books/path%20param/?query=query%20param")
    assert response.status_code == 200
    # print(response.json())
    assert response.json() == {"Message": "path param", "Message": "query param"}

# POST ReST API
def test_first_apiV4():
    # new_book = {"Book": "New Book Test Title"}
    new_book = "New Book Test Title"

    response = client.post("/books/create_book", json=new_book)
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"Message": new_book}

# PUT ReST API
def test_first_apiV5():
    # update_book = {"Updated Book": "Updated Book Test"}
    update_book = "Updated Book Test"

    response = client.put("/books/update_book", json=update_book)
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"Message": update_book}

# DELETE ReST API
def test_first_apiV6():
    book_to_delete = "Delete Book Test"

    response = client.delete("/books/delete_book", params={"delete_book": book_to_delete})
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"Message": book_to_delete}
