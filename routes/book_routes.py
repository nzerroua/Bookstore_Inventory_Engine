from flask import Blueprint, request, jsonify
from models import book_model

book_bp = Blueprint("books", __name__)

@book_bp.route("/", methods=["GET"])
def get_books():
    books = book_model.get_all_books()
    return jsonify(books)

@book_bp.route("/<int:id>", methods=["GET"])
def get_book(id):
    book = book_model.get_book(id)
    return jsonify(book) if book else ("Not found", 404)

@book_bp.route("/", methods=["POST"])
def create_book():
    data = request.get_json()
    required_fields = ["title", "author", "price", "quantity"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    book = book_model.create_book(data)
    return jsonify(book), 201

@book_bp.route("/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()
    required_fields = ["title", "author", "price", "quantity"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    book = book_model.update_book(id, data)
    return jsonify(book) if book else ("Not found", 404)

@book_bp.route("/<int:id>", methods=["DELETE"])
def delete_book(id):
    book_model.delete_book(id)
    return "", 204
