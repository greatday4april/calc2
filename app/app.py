from flask import Flask, render_template, flash, request
from calculator.calculator import Calculator

app = Flask(__name__, template_folder="templates")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=["GET"])
def index_get():
    return render_template("index.html")


@app.route("/result", methods=["GET"])
def result_get():
    Calculator.load_history()
    return render_template(
        "result.html",
        result=None,
        history=[
            c.to_dict()
            for c in sorted(
                Calculator.get_history(), key=lambda c: c.time.timestamp(), reverse=True
            )
        ],
    )


@app.route("/calculator", methods=["GET"])
def calculator_get():
    return render_template("calculator.html")


@app.route("/calculator", methods=["POST"])
def calculator_post():
    values_str = request.form["values"]
    operation = request.form["operation"]
    try:
        assert len(values_str) != 0, "values field is required for calculation"
        assert len(operation) != 0, "operation field is required for calculation"

        values = [float(v) for v in values_str.split(",")]
        assert len(values) != 0, 'please use "," as delimeter for values'

        Calculator.load_history()
        operation = operation.lower()
        if operation == "addition":
            Calculator.add_number(values)
        elif operation == "subtraction":
            Calculator.subtract_number(values)
        elif operation == "multiplication":
            Calculator.multiply_numbers(values)
        elif operation == "division":
            Calculator.divide_numbers(values)
        else:
            raise Exception("unsupported operation type: {}".format(operation))

        return render_template(
            "result.html",
            calculation=Calculator.get_last_calculation().to_dict(),
            history=[
                c.to_dict()
                for c in sorted(
                    Calculator.get_history(),
                    key=lambda c: c.time.timestamp(),
                    reverse=True,
                )
            ],
        )
    except Exception as e:
        flash(str(e))
        return render_template("calculator.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
