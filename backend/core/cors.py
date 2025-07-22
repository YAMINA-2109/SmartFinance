from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()


# CORS set up
def add_cors_middleware(app):

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[os.getenv("ALLOWED_ORIGINS")],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

