from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="Save Que$t API",
        version="0.1.0",
        description=(
            "API da Plataforma Save Que$st para gerenciamento de "
            "transações financeiras e controle de gastos."
        ),
    )

    @app.get("/")
    async def read_root() -> dict[str, str]:
        return {"message": "Welcome to my FastAPI application!"}

    return app


app = create_app()
