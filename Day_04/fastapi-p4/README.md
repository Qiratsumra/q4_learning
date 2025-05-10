# Types of FastAPI parameter

## Path Parameter
used for captured value directly from the *URL Path*

**Example**
<pre lang="markdown">
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
</pre>

