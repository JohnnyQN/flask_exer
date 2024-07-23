from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Dictionary to map operation names to functions
OPERATIONS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def math_operation(operation):
    """Perform a math operation based on the operation parameter."""
    if operation in OPERATIONS:
        try:
            a = int(request.args.get('a'))
            b = int(request.args.get('b'))
            result = OPERATIONS[operation](a, b)
            return str(result)
        except (TypeError, ValueError, KeyError):
            return "Invalid input. Please provide valid integers for a and b.", 400
    else:
        return "Operation not supported.", 404

if __name__ == '__main__':
    app.run(debug=True)
