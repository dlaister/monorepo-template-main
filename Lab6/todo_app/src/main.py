#--------------------IMPORTS--------------------#
from fastapi import FastAPI, Body

#--------------------OBJECTS--------------------#
app = FastAPI()

#--------------------FUNCTIONS--------------------#
# GET ReST API
@app.get("/api")
def first_api():
    return {"Message": "First API"}

# GET ReST API with path parameters
@app.get("/books/{path_param}")
def first_apiV2(path_param: str):
    return {"Message": path_param}

# GET ReST API with query parameters
@app.get("/books/")
def first_apiV3(title: str):
    return {"Message": title}

# GET ReST API with path parameters AND query parameters
@app.get("/books/{path_param}/")
def first_apiV7(path_param: str, query: str):
    print(path_param, query)
    return {"Message": path_param, "Message": query}

# POST ReST API
@app.post("/books/create_book")
def first_apiV4(new_book=Body()):
    # print(new_book)
    return {"Message": new_book}

# PUT ReST API
@app.put("/books/update_book")
def first_apiV5(update_book=Body()):
    # print(update_book)
    return {"Message": update_book}

# DELETE ReST API
#TODO - check this is right?
@app.delete("/books/delete_book")
def first_apiV6(delete_book: str):
    # print(delete_book)
    return {"Message": delete_book}
