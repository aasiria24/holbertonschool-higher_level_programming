#!/usr/bin/env python3
"""
Flask API with Basic Authentication and JWT Token-based Authentication
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, verify_jwt_in_request
)
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key-for-jwt'  # In production, use environment variable
app.config['JWT_SECRET_KEY'] = 'jwt-super-secret-key'  # In production, use environment variable

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}



@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic authentication"""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@auth.error_handler
def auth_error(status):
    """Error handler for basic authentication"""
    return jsonify({"error": "Unauthorized"}), 401



@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired JWT token"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked JWT token"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle need for fresh JWT token"""
    return jsonify({"error": "Fresh token required"}), 401



def admin_required():
    """Decorator to require admin role"""
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user not in users or users[current_user]["role"] != "admin":
                return jsonify({"error": "Admin access required"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper



@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        "message": "Welcome to the Secure API",
        "endpoints": {
            "GET /basic-protected": "Basic authentication protected",
            "POST /login": "Get JWT token (username, password required)",
            "GET /jwt-protected": "JWT protected endpoint",
            "GET /admin-only": "Admin only endpoint (requires admin role)"
        }
    })


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Endpoint protected by basic authentication"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to get JWT token"""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400
    
    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401
    
    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    
    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Endpoint protected by JWT"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@admin_required()
def admin_only():
    """Endpoint for admin users only"""
    return "Admin Access: Granted"



@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """Handle 405 errors"""
    return jsonify({"error": "Method not allowed"}), 405


if __name__ == '__main__':
    app.run(debug=True, port=5000)
