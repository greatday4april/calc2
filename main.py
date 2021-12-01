import os
import pandas as pd
from pathlib import Path
import datetime
from calculator.calculator import Calculator
import shutil


def absolutepath(filepath):
    relative = Path(filepath)
    return relative.absolute()


if __name__ == "__main__":
    files = os.listdir('input')
    print("Calculator main test is running")
    open(absolutepath('results/results.csv'), 'w+').write(
        'unix time stamp, filename, record number, operation and result of the calculation\n'
    )
    open(absolutepath('results/errors.csv'), 'w+').write(
        'filename, record number, error message\n'
    )
    for f in files:
        if not f.endswith('.csv'):
            continue

        abs_path = absolutepath('input/' + f)
        df = pd.read_csv(abs_path)

        for index, row in df.iterrows():
            print("processing no.{} calculation".format(index + 1))
            try:
                operation_type = row["Operation Type"]
                first_value = float(row["First Value"])
                second_value = float(row["Second Value"])
                values = [first_value, second_value]
                if operation_type == "addition":
                    result = Calculator.add_number(values)
                elif operation_type == "subtraction":
                    result = Calculator.subtract_number(values)
                elif operation_type == "multiplication":
                    result = Calculator.multiply_numbers(values)
                elif operation_type == "division":
                    result = Calculator.divide_numbers(values)
                else:
                    raise Exception("unsupported operation type: {}".format(operation_type))

                open(absolutepath('results/results.csv'), 'a').write(
                    "{},{},{},{},{}\n".format(
                        datetime.datetime.now().timestamp(),
                        f,
                        row["Record Number"],
                        row["Operation Type"],
                        result,
                    )
                )
            except Exception as e:

                open(absolutepath('results/errors.csv'), 'a').write(
                    "{},{},{}\n".format(
                        f,
                        row["Record Number"],
                        e,
                    )
                )
        shutil.move(absolutepath('input/' + f), absolutepath('done/' + f))
