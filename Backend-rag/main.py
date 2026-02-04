from fastapi import FastAPI
from app.API.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Production RAG System")

# 🔍 Health check (used by Docker / AWS / Load Balancers)
@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

# ✅ REQUIRED for frontend ↔ backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
