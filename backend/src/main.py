from fastapi import FastAPI
from .routes.routes import ApiRouter
from fastapi.middleware.cors import CORSMiddleware
# import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ApiRouter().getRoutes(app)

# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8000)

