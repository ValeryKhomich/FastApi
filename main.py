import uvicorn
from fastapi import FastAPI, Depends, HTTPException, status

app = FastAPI()

# Функция-зависимость



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)