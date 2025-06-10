# 📚 Bookstore Inventory API

A simple RESTful API for managing bookstore inventory, built with **Flask** and **PostgreSQL**.

## Features

- Add, update, delete, and retrieve books
- Input validation and error handling
- PostgreSQL backend
- Environment variable support with `.env`
- Clean project structure with Blueprints

## Tech Stack

- **Backend**: Flask
- **Database**: PostgreSQL
- **ORM**: psycopg2
- **Environment**: python-dotenv

## Project Structure

```
Bookstore-Inventory/
├── app.py                # Main application entry
├── db.py                 # DB connection and table creation
├── models/
│   └── book_model.py     # Database operations
├── routes/
│   └── book_routes.py    # API endpoints
├── .env                  # Environment variables
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Bookstore-Inventory.git
cd Bookstore-Inventory
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up your `.env` file**

```
DATABASE_URL=postgresql://username:password@localhost:5432/yourdbname
```

4. **Start the server**

```bash
python app.py
```

## API Endpoints

| Method | Endpoint          | Description    |
| ------ | ----------------- | -------------- |
| GET    | `/api/books`      | Get all books  |
| GET    | `/api/books/<id>` | Get book by ID |
| POST   | `/api/books`      | Add a new book |
| PUT    | `/api/books/<id>` | Update a book  |
| DELETE | `/api/books/<id>` | Delete a book  |

## Postman Collection

Import the provided [Bookstore Inventory.postman_collection.json](#) to test all routes.
