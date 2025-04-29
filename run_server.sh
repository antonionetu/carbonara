#!/bin/bash

source venv/bin/activate
pip install -r requirements.txt

cd src
uvicorn backend:app --reload &
BACKEND_PID=$!

cd ../frontend
npm install
npm run dev & 
FRONTEND_PID=$!

echo ""
echo "==========================================="
echo "Frontend running at: http://localhost:5173"
echo "Backend  running at: http://localhost:8000"
echo "==========================================="
echo ""

wait $BACKEND_PID $FRONTEND_PID
