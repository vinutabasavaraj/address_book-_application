# Address Book Application

This is a simple address book application where users can perform CRUD (Create, Read, Update, Delete) operations on addresses. The application is built using Python and FastAPI framework, and it uses SQLite database to store address information.

## Features
Create new addresses with coordinates (latitude and longitude)
Update existing addresses
Delete addresses
Validate address data before saving
Retrieve addresses within a given distance from a specified location

# Technologies Used
- Python
- FastAPI
- SQLite

# Setup Instructions
1. Clone the repository to your local machine.
2. Install Python if you haven't already.
3. Install the required dependencies using pip:
       pip install -r requirements.txt
4. Run the FastAPI application:
     uvicorn main:app --host 0.0.0.0 --port 8000(port number)
5. The application should now be running locally. You can access the API documentation and test the endpoints by visiting http://localhost:8000/docs in your web browser.

# API Endpoints
- POST /addresses: Create a new address
- PUT /addresses/{address_id}: Update an existing address
- DELETE /addresses/{address_id}: Delete an address
- GET /addresses/nearby: Retrieve addresses within a given distance from a specified location
- POST /create_table :  Database connection and table creation
