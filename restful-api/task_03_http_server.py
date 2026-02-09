#!/usr/bin/env python3
"""
Simple HTTP Server using Python's built-in http.server module
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the simple API server
    """
    
    def _set_headers(self, status_code=200, content_type='text/plain'):
        """Helper method to set HTTP response headers"""
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self._handle_root()
        elif self.path == '/data':
            self._handle_data()
        elif self.path == '/status':
            self._handle_status()
        else:
            self._handle_not_found()
    
    def _handle_root(self):
        """Handle requests to the root path"""
        response_text = "Hello, this is a simple API!"
        self._set_headers(200, 'text/plain')
        self.wfile.write(response_text.encode('utf-8'))
    
    def _handle_data(self):
        """Handle requests to /data endpoint"""
        sample_data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self._set_headers(200, 'application/json')
        self.wfile.write(json.dumps(sample_data).encode('utf-8'))

    def _handle_status(self):
        """Handle requests to /status endpoint"""
        response_text = "OK"
        self._set_headers(200, 'text/plain')
        self.wfile.write(response_text.encode('utf-8'))

    def _handle_not_found(self):
        """Handle undefined endpoints"""
        response_text = "Endpoint not found"
        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_text.encode('utf-8'))


def run_server(port=8000):
    """
    Run the HTTP server on the specified port

    Args:
        port (int): Port number to run the server on
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)

    print(f"Server running on port {port}")
    print("Available endpoints:")
    print("  GET /       - Welcome message")
    print("  GET /data   - Sample JSON data")
    print("  GET /status - API status")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    run_server(8000)
