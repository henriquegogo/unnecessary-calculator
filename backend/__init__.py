from backend import calculator

def run(req, res):
    # Set operations function
    func = {
        "sum": calculator.sum,
        "sub": calculator.sub,
        "mult": calculator.mult,
        "div": calculator.div,
        "": lambda _, b: b
    }

    # Convert values to numbers
    a = float(req.params["num_a"] or 0)
    b = float(req.params["num_b"] or 0)

    # Get operation
    op = req.params["op"]

    # Calculate
    result = func[op](a, b)

    res.redirect(f"/?value={result}")
