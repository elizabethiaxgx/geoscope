import os
import subprocess
import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class GeoScope:
    def __init__(self, port=8080):
        self.port = port
        self.server = None

    def start_secure_browser(self, url):
        try:
            # Start a local HTTP server
            self.server = TCPServer(("", self.port), SimpleHTTPRequestHandler)
            print(f"Serving on port {self.port}")

            # Open the URL in the default web browser
            webbrowser.open(f"http://localhost:{self.port}/{url}")

            # Run the server
            self.server.serve_forever()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.stop_server()

    def stop_server(self):
        if self.server:
            self.server.server_close()
            print("Server stopped.")

    def run_in_isolated_environment(self, url):
        try:
            # Create a new isolated environment
            os.environ["BROWSER"] = "none"

            # Run the browser in a subprocess to isolate it
            subprocess.run(["python", "-m", "http.server", str(self.port)], check=True)
            self.start_secure_browser(url)
        except subprocess.CalledProcessError as e:
            print(f"Subprocess error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "index.html"  # Example HTML file
    geo_scope = GeoScope()
    geo_scope.run_in_isolated_environment(url)