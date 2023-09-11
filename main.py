import os
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
# from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware

# from middlewares.correlation_id_middleware import CorrelationIdMiddleware
from routers import keep_active, test, discord

app = FastAPI(
    title="floats-api",
    description="floats-api",
    version="0.1.0",
    # root_path=os.environ.get("WORKDIR", ""),
)

# CORSを回避
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=["http://18.183.224.26"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_middleware(
#     DBSessionMiddleware,
#     db_url=f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASS']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/floats-dev"
# )

@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


# app.include_router(test.router)
# app.include_router(search.router)
# app.include_router(retrieve_words_info.router)
# app.include_router(click.router)
# app.include_router(get_corpus.router)

app.include_router(test.router, prefix="/test", tags=["test"])
app.include_router(keep_active.router, prefix="/keep_active", tags=["searckeep_activeh"])
app.include_router(discord.router,prefix="/discord",tags=["discord"],)

handler = Mangum(app=app)
# handler = Mangum(app=app, lifespan="off")

# if __name__ == "__main__":
#     # uvicorn.run(app, host=os.environ["HOST"], port=os.environ["PORT"])
#     uvicorn.run(app, host="http://localhost", port=5001)
