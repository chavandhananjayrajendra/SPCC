
def get_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"

# Define a function to generate three address code for arithmetic expressions
def gen_tac(op, arg1, arg2):
    global label_count
    global code
    if op == "+":
        temp = get_temp()
        code.append(f"{temp} = {arg1} + {arg2}")
        return temp
    elif op == "-":
        temp = get_temp()
        code.append(f"{temp} = {arg1} - {arg2}")
        return temp
    elif op == "*":
        temp = get_temp()
        code.append(f"{temp} = {arg1} * {arg2}")
        return temp
    elif op == "/":
        temp = get_temp()
        code.append(f"{temp} = {arg1} / {arg2}")
        return temp

# Define the main program
if __name__ == "__main__":
    # Initialize the temporary variable count and code list
    temp_count = 0
    code = []

    # Generate three address code for an arithmetic expression
    result = gen_tac("+", "a", "b")
    result = gen_tac("*", result, "c")
    result = gen_tac("-", result, "d")

    # Print the generated three address code
    print("Generated three address code:")
    for line in code:
        print(line)
