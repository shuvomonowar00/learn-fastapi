from fastapi import APIRouter, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time
from typing import Callable

# Create APIRouter
middleware_router = APIRouter(
    prefix="/middleware",
    tags=["Middleware"]
)

# =============================================================================
# 1. TIMING MIDDLEWARE - Using @app.middleware("http")
# =============================================================================
# This is the simpler approach using FastAPI's decorator
# Perfect for straightforward request/response processing
async def add_process_time_header(request: Request, call_next: Callable) -> Response:
    """
    Measures how long each request takes to process.
    
    Args:
        request: The incoming request object
        call_next: A function that will receive the request and pass it to the
                   corresponding path operation, then return the response
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Note: @app.middleware("http") decorators are added automatically

# =============================================================================
# SAMPLE ROUTES TO TEST MIDDLEWARE
# =============================================================================

@middleware_router.get("/")
async def root():
    """Public endpoint - no auth required"""
    return {"message": "Welcome to the Middleware Demo API"}

@middleware_router.get("/health")
async def health_check():
    """Health check endpoint - no auth required"""
    return {"status": "healthy"}