def inputcleaner(input_str):
    # Function to clean the input string by removing unwanted symbols
    valid_symbols = {'+', '-', '='}
    cleaned_input = ""

    for symbol in input_str:
        if symbol.isdigit() or symbol.isalpha() or symbol in valid_symbols or symbol == '.':
            cleaned_input += symbol

    return cleaned_input


def combineliketerms(listoftuples):
    # Function to combine like terms in a list of tuples
    result = {}
    for coefficient, variable in listoftuples:
        if variable in result:
            result[variable] += coefficient
        else:
            result[variable] = coefficient
    combined_terms = [(coeff, var) for var, coeff in result.items()]
    return combined_terms


def assign_variable(string):
    # Function to parse a string and extract variables and coefficients
    list_of_tuples = []
    current_number = ""

    for char in string:
        if char.isdigit() or char == '.':
            current_number += char
        elif char.isalpha():
            if current_number:
                list_of_tuples.append((float(current_number), ''))
                current_number = ""
            list_of_tuples.append((1.0, char))
        else:
            # Handle other characters (operators or special characters)
            pass

    # Check if there's a number left at the end
    if current_number:
        list_of_tuples.append((float(current_number), ''))  # Assuming an empty string for constant

    return combineliketerms(list_of_tuples)


def linear_equations_solver(equation):
    # Function to solve linear equations
    eparts = equation.lower().split("=")

    if equation.count('=') != 1:  # Check if there is exactly one equal sign
        return "Error: Please enter a valid linear equation with exactly one equal sign."

    equation_dict = {}
    count = 0

    for group in eparts:
        if any(char.isalpha() for char in group):
            # Process variables and coefficients; there should only be 1 group in this
            list_of_equation = assign_variable(group)
            for coeff, var in list_of_equation:
                equation_dict[var] = equation_dict.get(var, 0.0) + coeff
        else:
            # Process constant; can only be 1 per group
            equation_dict['c'] = float(group)
            count += 1

    if count != 1:
        return "Error: Please enter a valid constant with only numbers after or before your equal sign."

    # Now solve for the variable ('x' in this case)
    if 'x' in equation_dict:
        x_coefficient = equation_dict['x']
        print(x_coefficient)
        constant_term = equation_dict.get('c', 0.0)

        if x_coefficient == 0:
            return "Error: The coefficient of 'x' is zero. This equation has no solution."

        x_value = -(constant_term / x_coefficient)  # Solve for 'x'

        return f"The solution is x = {x_value}"

    else:
        return "Error: The equation does not contain the variable 'x.'"


# Example usage with the equation "2x + 3 = 5"
input_str = input("Enter a linear equation (e.g., 2x + 3 = 5): ")
equation = inputcleaner(input_str)
result = linear_equations_solver(equation)
print(result)