def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("It has a division by zero error")
    except ValueError:
        print("Invalid input: please enter numeric values")

