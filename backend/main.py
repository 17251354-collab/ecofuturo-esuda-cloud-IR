from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, usuarios, parceiros, atividades, beneficios, resgates, relatorios, transferencias, gamificacao, notificacoes

app = FastAPI(
    title="EcoFuturo ESUDA API",
    version="1.0.0",
    description="RF01 a RF36 | RN001 a RN014 | RNF01 a RNF22 | Python + FastAPI + Supabase (PostgreSQL) + JWT + Bcrypt | Swagger | Documentação OpenAPI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- INCLUSÃO DOS ROUTERS (SEM OS NOMES DOS REQUISITOS) ---
app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(parceiros.router)
app.include_router(atividades.router)
app.include_router(beneficios.router)
app.include_router(resgates.router)
app.include_router(relatorios.router)
app.include_router(transferencias.router)
app.include_router(gamificacao.router)
app.include_router(notificacoes.router)

@app.get("/", tags=["Status da API"])
def raiz():
    return {"mensagem": "API do EcoFuturo ESUDA está funcionando!"}
