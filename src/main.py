import logging
from fastapi import FastAPI
import uvicorn

from core.config import app_config
from api.v1.routers import router


app = FastAPI(
    title="My app API",
    docs_url="/docs",
    openapi_url="/openapi.json",
    description=(
        f"**🟢 Branch**: {app_config.CI_COMMIT_REF_NAME}"
        f"<br/>\n"
        f"**🦎 Release**: {app_config.CI_COMMIT_SHA}"
        f"<br/>\n"
        f"**🧑‍💻 Deployed by**: {app_config.GITLAB_USER_NAME}\n"
    ),
)

app.include_router(router, prefix="/api/v1")


@app.get("/api/v1/health", tags=["healthcheck"])
async def check_health():
    return "ok"


@app.on_event("startup")
async def startup():
    pass


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        log_level=logging.DEBUG,
        reload=app_config.ENVIRONMENT == "local",
    )
