#!/bin/bash
# Startup script for Railway deployment

# Use PORT environment variable or default to 8000
PORT=${PORT:-8000}

# Start uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port $PORT --timeout-keep-alive 120

