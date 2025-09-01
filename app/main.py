# this is the main entry point of the fastapi application 
from fastapi import FastAPI
import uvicorn
from app.routes import user, transaction, transfer, wallet
app = FastAPI(
    title = "Digital Wallet", 
    version= "1.0", 
    description="A simple digital wallet application")

app.include_router(user.router)
app.include_router(transaction.router)
app.include_router(transfer.router)
app.include_router(wallet.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Digital Wallet API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)