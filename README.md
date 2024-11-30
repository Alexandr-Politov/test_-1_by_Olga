# FastAPI Product Management API
A simple RESTful API built with FastAPI for managing products. This application allows users to create, retrieve, update, and delete products.

## Features
* CRUD Operations for Products:
  - Create a product.
  - Retrieve all products or a specific product.
  - Update a product's details.
  - Delete a product.
* Validation for fields like name, description, and price.
* Built-in OpenAPI Documentation for easy API exploration.

## Getting Started
### Installation
1. Clone the repository:
```shell
git clone https://github.com/your-username/fastapi-product-api.git
cd fastapi-product-api

```
2. Create a virtual environment:

```shell
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. Install dependencies:
```shell
pip install -r requirements.txt
```

## Running the Application
1. Start the FastAPI development server:

```shell
uvicorn main:app --reload
```
* The app will be available at http://127.0.0.1:8000/.
2. Explore the API documentation:
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc
* Or you can use file 'Products test task.postman_collection.json' to test API via Postman.