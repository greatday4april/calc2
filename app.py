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
            raise Exception(f"unsupported operation type: {operation}")

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
    except Exception as error:
        flash(str(error))
        return render_template("calculator.html")


@app.route("/pylint", methods=["GET"])
def pylint_get():
    items = [
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/travis.png",
            "text": "Pylint is a tool to enforce coding styles and best practices, as well as make sure no basic syntax errors for your python programs. Such as no unused variables, or the code is properly indented etc. https://app.travis-ci.com/github/greatday4april/calc2 is a travis link with pylint check on the repository.",
        },
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/pylint-disable.png",
            "text": "pylint uses .pylintrc to control the settings. To disable some of the warnings from pylint, you can simply add the warning tags to the disable section and those warnings will be suppressed. Be careful not overdoing it though, because that would defeat the whole purpose of using pylint to enforce your coding style.",
        },
        {
            "image": "https://miro.medium.com/max/840/1*RJMxLdTHqVBSijKmOO5MAg.jpeg",
            "text": "Now we are going to explain some terms in Python programming.\nFactory: use a static / class method to create object instances of different child classes. for example the create function here that creates Addition, Subtraction, Multiplication or Division instances.",
        },
    ]
    return render_template(
        "article.html", title="Pylint and best practices", content=items
    )


@app.route("/aaatesting", methods=["GET"])
def aaatesting_get():
    items = [
        {
            "image": "https://miro.medium.com/max/1400/1*jLgrNjNC4vglYJKsmpRqmQ.png",
            "text": "AAA(Arrange-Act-Assert) pattern is standard for testing in software engineer industry. Basically it means a test needs to be composed of these 3 stages: Arrange means having setup, such as having mocks etc; then Act, basically invocate the method to be tested; and the last step is to verify the result meets expectation after the act (Assert).",
        },
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/pytest.png",
            "text": "Testing is super important because it helps us verify the code we've written matches our expectation and has no bug. It also prevents other people from breaking the code while they are making changes. This allows collaboration between more developers on the same project.",
        },
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/test-example.png",
            "text": 'https://github.com/greatday4april/calc2/blob/calc_part2/tests/calculator_test.py#L26-L33 is an example of how tests are usually implemented. The test "test_calculator_add" does clear_history as the setup (Arrange) to clear history of the calculator to avoid side effects. And then perform actions, aka, adding different numbers. (Act) And then verify the results to be expected values. (Assert)',
        },
        {
            "image": "https://user-images.githubusercontent.com/60717299/144320178-4df43bbc-fb21-4d18-b6b8-1e4338b61bc4.png",
            "text": "https://github.com/greatday4april/calc2/blob/calc_csv/main.py#L27-L28 is a code example where we read input values from an external file, in this case CSV file as test cases and perform operations based on the values within the CSV file, and then output the results into a different file, as well as outputing errors and verify against the expected values.",
        },
    ]
    return render_template(
        "article.html", title="Pylint and best practices", content=items
    )


@app.route("/oops", methods=["GET"])
def oops_get():
    items = [
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/encapsulation.png",
            "text": "Encapsulation refers bundling all characterics and functionalities related to one entity into one object. In the case of our calculator, our calculator itself is one kind of encapsulation because it wraps all its functionalities in the Calculator class. And another example is we use calculation as one unit and bundles the input elements, the operation type and output. For example: https://github.com/greatday4april/calc2/blob/calc_part2/calculator/calculator.py#L11-L30.",
        },
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/inheritance.png",
            "text": 'Inheritance represents a "is a" relationship. For example in the calculator case, each of "Addition", "Subtraction", "Multiplication" and "Division" is one calculation. As you can see from https://github.com/greatday4april/calc2/tree/calc_part2/calc, each type of calculation has a classed named by it and inherits Calculation class, meaning they are all calculation types. And we call the class inherits "child class", the class get inherited "base class" or "parent class". Addition is the child class, while Calculation is the parent / base class here.',
        },
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/polymorphism.png",
            "text": "In programming, polymorphism means different child classes may have different behavior for the same function. For example, here https://github.com/greatday4april/calc2/blob/calc_part2/calculator/calculator.py#L33-L34 get_result is a function that every child class of Calculation class has. But when it was used, it can have different behaviors depend on whether this calculation is an Addition or Multiplication, etc. Which is expected as different calculation is supposed to output different result.",
        },
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/abstraction.png",
            "text": "Abstraction means the class doesn't refer to a concrete type but only refers to an abstract category. For example, if we have a Fruit class it will be abstract. In our calculator example, Calculation (https://github.com/greatday4april/calc2/blob/calc_part2/calc/calculation.py#L4-L10) is an abstract class and cannot initialized directly because it doesn't make sense to have a calculation without the calculation type defined. For example, in our simple calculator, it must be one of Addition, Subtraction, Multiplication or Division.",
        },
    ]
    return render_template(
        "article.html", title="Pylint and best practices", content=items
    )


@app.route("/sop", methods=["GET"])
def sop_get():
    items = [
        {
            "image": "https://aspiringcraftsman.com/wp-content/uploads/2010/01/horizontalLayers.png",
            "text": "Separation of Concerns is an important software engineering concept. It's very easy to understand but in practice people maybe easy to steer away from it. It means separating independent components so that each component only needs to worry about their own responsibility so that can easily decoupled or reorganized. It also helps keeping the scope of each component relatively small and easy to manage. It avoids making the program too complex and hard to maintain.",
        },
        {
            "image": "https://zealous-hill-03f97ab1e.azurestaticapps.net/sop.png",
            "text": "In our calculator example, if we look at the project layout here https://github.com/greatday4april/calc2/tree/calc_part2, you would find tests, calculator and calculations are separated. Calculator is the presentation layer which provide interface for all the functionalities including the history of calculations. It doesn't need to worry about the individual calculations while the calculation classes will take care of the implementation of different types of calculations. While tests folder will test the functionalities. This separation of concerns enables multiple developers work on the project and help the program scale.",
        },
    ]
    return render_template(
        "article.html", title="Pylint and best practices", content=items
    )


@app.route("/flash/")
def dashboard():
    flash("Now you should be able to use flash to pass a dismissable message")
    flash("This is the dismissable message")
    return render_template("flash.html")
