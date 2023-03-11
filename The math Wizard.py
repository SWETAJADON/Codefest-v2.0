def check_formula(formula, expected_answer):
    # Parse the formula into a format that can be evaluated
    formula = formula.replace('^', '*')  # Replace ^ with * for exponentiation
    formula = formula.replace('÷', '/')  # Replace ÷ with / for division
    formula = formula.replace('x', '*')   # Replace x with * for multiplication
    formula = formula.replace('X', '*')   # Replace X with * for multiplication

    # Evaluate the formula using the standard BODMAS rules
    result = eval(formula)

    # Compare the result to the expected answer
    if result == expected_answer:
       print("True")
    else:
        print("false")
        
 
check_formula('4**2', 16)
check_formula('30/15', 2) 
check_formula('40*2', 80)
check_formula('3*4', 56)
