# Unnecessary Calculator

This is a simple calculator web application with a Python backend and a plain JavaScript frontend.

## Usage

To run the application, use the `make` command:

```bash
make
```

This will start a web server on `http://localhost:8000`.

## Testing

The backend has a suite of unit tests. To run the tests, use the `make tests` command:

```bash
make tests
```

## Backend

The backend is a simple Python application that provides basic calculator functionality. The available operations are:

*   `sum(a, b)`: Adds two numbers.
*   `sub(a, b)`: Subtracts two numbers.
*   `mult(a, b)`: Multiplies two numbers.
*   `div(a, b)`: Divides two numbers.

## Frontend

The frontend is a single-page application built with HTML, CSS, and vanilla JavaScript. It provides a simple calculator interface that communicates with the backend to perform calculations.

The frontend sends the numbers and the selected operation to the backend via a `POST` request to a CGI script. The result is then displayed on the calculator's display.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
