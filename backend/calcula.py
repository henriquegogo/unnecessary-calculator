#!/usr/bin/env python
from sys import stdin, argv, modules, exit

def sum(a, b):
    """Sum two numbers"""
    return a + b

def sub(a, b):
    """Subtract two numbers"""
    return a - b

def mult(a, b):
    """Multiply two numbers"""
    return a * b

def div(a, b):
    """Divide two numbers"""
    return a / b

def main():
    # Get values
    args = dict(arg.split("=") for arg in stdin.read().split("&"))

    # Set operations function
    func = {
        "sum": sum,
        "sub": sub,
        "mult": mult,
        "div": div,
        "": lambda _, b: b
    }

    # Convert values to numbers
    a = float(args["num_a"] or 0)
    b = float(args["num_b"] or 0)

    # Get operation
    op = args["op"]

    # Calculate
    result = func[op](a, b)

    # Print result
    print(f"Status: 302 Found\nLocation: /?value={result}\n")

if __name__ == "__main__":
    if "--help" in argv or "-h" in argv:
        import pydoc
        print(pydoc.render_doc(modules[__name__], "Help for %s"))
        exit(0)
    else:
        main()
