from flask import Flask
from routes.book_routes import book_bp
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# Register the books blueprint with a URL prefix
app.register_blueprint(book_bp, url_prefix="/api/books")

if __name__ == "__main__":
    app.run(debug=True)
