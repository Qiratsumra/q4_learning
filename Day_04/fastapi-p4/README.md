# Types of FastAPI parameter

## 1.Path Parameter
Used for captured value directly from the *URL Path*

**Example**
<pre lang="markdown">
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
</pre>

## 2.Query Parameter
Used to get data from the query string (after ? in the URL).

**Example**
<pre lang="markdown">
@app.get("/search")
def search_items(q: str = None):
    return {"query": q}
</pre>


## 3. Request Body Parameters
Used to recive *JSON form data or files* in the body of POST/PUT request.

**Example**
<pre lang="markdown">
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return item

</pre>

## 4.Form Parameter
Used to handle HTML form submission 

**Example**
<pre lang="markdown">
from fastapi import Form

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
</pre>

## 5.File Parameter
Used for file uploads

**Example**
<pre lang='markdown'>
from fastapi import File, UploadFile

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

</pre>

## 6.Hander Parameter
Used to extract values from the *HTTP header*

**Example**
<pre lang='markdown'>
from fastapi import Header

@app.get("/agent")
def get_user_agent(user_agent: str = Header(...)):
    return {"User-Agent": user_agent}
</pre>


## 7.Cookie Parameter
Used to extract values from *cookies*

**Example**
<pre lang='markdown'>
from fastapi import Cookie

@app.get("/cookies")
def read_cookie(session_id: str = Cookie(None)):
    return {"session_id": session_id}

</pre>