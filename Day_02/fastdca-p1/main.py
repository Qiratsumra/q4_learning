from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World": "From Senior Student Qirat Saeed"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}






# def main():
#     print("Hello from fastdca-p1!")


# if __name__ == "__main__":
#     main()
