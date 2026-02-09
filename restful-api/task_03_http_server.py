#!/usr/bin/env python3
"""
Simple HTTP Server using Python's built-in http.server module
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the simple API server
    """

    def _set_headers(self, status_code=200, content_type='text/plain'):
        """Helper method to set HTTP response headers"""
        self.send_response(status_code)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def _send_response(self, data, status_code=200, content_type='text/plain'):
        """Helper method to send HTTP response"""
        self._set_headers(status_code, content_type)

        if isinstance(data, (dict, list)):
            response = json.dumps(data).encode('utf-8')
        else:
            response = str(data).encode('utf-8')

        self.wfile.write(response)

    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)

        if path == '/':
            self._handle_root()
        elif path == '/data':
            self._handle_data()
        elif path == '/status':
            self._handle_status()
        elif path == '/info':
            self._handle_info()
        else:
            self._handle_not_found()
    
    def do_POST(self):
        """Handle POST requests (bonus implementation)"""
        if self.path == '/data':
            self._handle_post_data()
        else:
            self._send_response(
                {"error": "Endpoint not found"},
                status_code=404,
                content_type='application/json'
            )

    def _handle_root(self):
        """Handle requests to the root path"""
        response_text = "Hello, this is a simple API!"
        self._send_response(response_text)

    def _handle_data(self):
        """Handle requests to /data endpoint"""
        sample_data = {
            "name": "John",
            "age": 30,
            "city": "New York",
            "country": "USA"
        }
        self._send_response(
            sample_data,
            content_type='application/json'
        )

    def _handle_status(self):
        """Handle requests to /status endpoint"""
        self._send_response("OK")
    
    def _handle_info(self):
        """Handle requests to /info endpoint (bonus)"""
        info_data = {
            "version": "1.0",
            "description": "A simple API built with http.server",
            "endpoints": {
                "/": "Welcome message",
                "/data": "Sample JSON data",
                "/status": "API status check",
                "/info": "API information"
            }
        }
        self._send_response(
            info_data,
            content_type='application/json'
        )

    def _handle_not_found(self):
        """Handle undefined endpoints"""
        error_response = {
            "error": "Endpoint not found",
            "message": f"The requested path '{self.path}' does not exist on this server",
            "available_endpoints": ["/", "/data", "/status", "/info"]
        }
        self._send_response(
            error_response,
            status_code=404,
            content_type='application/json'
        )

    def _handle_post_data(self):
        """Handle POST requests to /data endpoint (bonus)"""
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            try:
                data = json.loads(post_data)
                response = {
                    "message": "Data received successfully",
                    "received_data": data,
                    "status": "processed"
                }
                self._send_response(
                    response,
                    content_type='application/json'
                )
            except json.JSONDecodeError:
                self._send_response(
                    {"error": "Invalid JSON data"},
                    status_code=400,
                    content_type='application/json'
                )
        else:
            self._send_response(
                {"error": "No data provided"},
                status_code=400,
                content_type='application/json'
            )
    def log_message(self, format, *args):
        """Override to customize log format"""
        print(f"{self.address_string()} - {self.log_date_time_string()} - {format % args}")


def run_server(port=8000):
    """
    Run the HTTP server on the specified port

    Args:
        port (int): Port number to run the server on
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Starting HTTP server on port {port}...")
    print(f"Server running at http://localhost:{port}")
    print("Available endpoints:")
    print("  GET  /         - Welcome message")
    print("  GET  /data     - Sample JSON data")
    print("  GET  /status   - API status")
    print("  GET  /info     - API information")
    print("  POST /data     - Submit data (bonus)")
    print("Press Ctrl+C to stop the server")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()


if __name__ == "__main__":
    run_server(8000)
