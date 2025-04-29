#!/bin/bash

# Parar o servidor backend (uvicorn)
echo "Stopping backend server (uvicorn)..."
pkill -f "uvicorn backend:app"

# Parar o servidor frontend (Vite)
echo "Stopping frontend server (npm run dev)..."
pkill -f "vite"

# Só para garantir
kill -9 $(jobs -p)

echo ""
echo "======================================="
echo "All servers have been stopped."
echo "======================================="
echo ""
