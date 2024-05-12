#!/bin/bash

# Function to check if a command exists
command_exists() {
  command -v "$1" >/dev/null 2>&1
}

echo "Checking dependencies..."

# Check if Python3 is installed, if not, exit with error message
if ! command_exists python3; then
  echo "Python3 is not installed. Please install it from https://www.python.org/downloads/"
  exit 1
fi

# Check if Node.js is installed, if not, exit with error message
if ! command_exists node; then
  echo "Node.js is not installed. Please install it from https://nodejs.org/"
  exit 1
fi

# Check if the backend/key.py file exists, if not, exit with error message
if [ ! -f "backend/key.py" ]; then
  echo "You need an 'key.py' file in the 'backend' directory with the format:"
  echo "api_key1 = <API_KEY>"
  exit 1
fi

echo "Dependencies are met."

# Install Python3 dependencies
pip3 install flask flask-cors python-docx openai > /dev/null 2>&1

# Start the frontend server
echo "Starting frontend server..."
cd frontend
npm install
npm run dev &
FRONTEND_PID=$!
cd ..

# Start the backend server
echo "Starting backend server..."
cd backend
python3 app.py &
BACKEND_PID=$!
cd ..

echo "Servers started successfully."
echo "Access the frontend at http://localhost:5173"

# Function to stop servers
stop_servers() {
  echo ""
  echo "Stopping servers..."
  kill $FRONTEND_PID $BACKEND_PID
  echo "Servers stopped."
}

# Trap Ctrl+C to stop servers
trap stop_servers INT

# Wait for background processes to finish
wait $FRONTEND_PID $BACKEND_PID
