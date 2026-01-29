#!/usr/bin/env python
import sys, os

sys.path.append(os.path.abspath("../../"))
sys.dont_write_bytecode = True

import backend

class Request:
    def __init__(self):
        self.params = dict(arg.split("=") for arg in sys.stdin.read().split("&"))
        self.headers = dict(os.environ)
        self.method = os.environ["REQUEST_METHOD"]
        self.path = os.environ["PATH_INFO"]

class Response:
    def html(self, content):
        print("Content-Type: text/html\n")
        print(content)

    def json(self, content):
        print("Content-Type: application/json\n")
        print(content)

    def text(self, content):
        print("Content-Type: text/plain\n")
        print(content)

    def redirect(self, url):
        print(f"Status: 302 Found\nLocation: {url}\n")

    def error(self, code, message):
        print(f"Status: {code} {message}\n")


def main():
    backend.run(Request(), Response())

if __name__ == "__main__":
    main()
