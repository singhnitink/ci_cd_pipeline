from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo App")


@app.get("/")
def read_root():
    return {"message": "Welcome to the CI/CD Pipeline API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Get test
@app.get("/add")
def add_numbers(a: float, b: float):
    return {"result": a + b}
# http://127.0.0.1:8000/add?a=5&b=10a


# Post test
@app.post("/subtract")
def subtract_numbers(data: dict):
    return {"result": data["a"] - data["b"]}
