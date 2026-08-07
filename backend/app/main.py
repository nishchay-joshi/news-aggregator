from fastapi import FastAPI

from app.api.accounts import router as accounts_router

app = FastAPI(title="Briefly API", version="1.0.0")

app.include_router(accounts_router)


@app.get("/", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "message": "Briefly API is running."
    }