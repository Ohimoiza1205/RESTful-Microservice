## Developing a RESTful micro service in Python

# RESTful Microservice with Flask

This project demonstrates how to build a RESTful microservice using Flask, a lightweight web server that makes it easy to develop and deploy Python-based microservices. 

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ohimoiza1205/RESTful-Microservice.git
   cd RESTful-Microservice

2. Install Flask:

   pip install flask

## Running the Application
- Navigate to the project directory.
- Start the Flask server:
  python atelier.py
- The server will be available at http://127.0.0.1:5000.

## REST Endpoints
- GET /search: Returns the search page.
- POST /api/greet: Accepts a JSON body with a name field and returns a greeting message.

## Testing Your API
- You can test your API using curl, Postman, or a web browser.

- **For a GET Request**:
  
  ```bash
  curl http://127.0.0.1:5000/api/hello

- **For a POST Request**:
  
  ```bash
  curl -X POST http://127.0.0.1:5000/api/greet -H "Content-Type: application/json" -d '{"name": "Alice"}'
