import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

# Функция-зависимость
def verify_token(token: str):
    if token != "supersecrettoken":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return {"user": "authorized_user"}

# Эндпоинт с зависимостью
@app.get("/protected/")
async def protected_route(user: dict = Depends(verify_token)):
    return {"message": "Access granted", "user": user}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)