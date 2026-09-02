"""
Assesment 1
Goal: Use loops, control flow, and  addition and subtraction 
operators to replace integer division, modulo, and multiplication operators

Input Variables:
input_a: user input for integer A (may not be an int)
input_b: user input for integer A (may not be an int)

Intermediate Variables: 
valid_a: tracker variable to count data validation issues for input_a
valid_b: tracker variable to count data validation issues for input_b
int_a: validated input A
int_b: validated input B

Output Variables:
quotient: output of integer division
remainder: output of modulo operator
product: output of multiplication

Test Inputs:
-1 -1 | invalid | pass
0 -1 | invalid | pass
-1 0 | invalid: zero division error | pass
0 0 | invalid: zero division error | pass
1 1 | valid | pass
0 1 | valid | pass
1 0 | invalid: zero division error | pass
999 999 | valid | pass
1000 1000 | invalid | pass
1000 999 | invalid | pass
999 1000 | invalid | pass
"""

# set program level scope for output variables 
quotient = 0
remainder = 0
product = 0  

# A. Reprompt logic
while True: 

    # B. take user inputs in terminal
    print("Please enter two inputs with the following requirements")
    input_a = input("Integer, between 0 and 999: ")
    input_b = input("Integer, betewen 1 and 999: ")

    ## C. variables to manage validation 
    valid_a = 0
    valid_b = 0
    
    ### C.1. integer data type checks w/o using type() function 
    try:
        int_a = int(input_a)
    except:
        valid_a += 1

    try:
        int_b = int(input_b)
    except:
        valid_b += 1

    ### C.2. validate ranges
    ### note that int_b actually needs to be > 0, \
    ###  this is to prevent a divide by zero error
    if int_a >= 0 and int_a <= 999:
        pass
    else:
        valid_a += 1

    if int_b > 0 and int_b <= 999:
        pass
    else:
        valid_b += 1

    ### C.3 provide error message
    if valid_a != 0 and valid_b != 0:
        print("Both inputs do not meet criteria")
    elif valid_a != 0:
        print("The first input does not meet the criteria")
    elif valid_b !=0: 
        print("The second input does not meet the criteria")

    # C.4 Data validation control flow 
    # include calculators in else clause
    if valid_a != 0 or valid_b != 0:
        pass
    else:

        #D. Subtraction-based quotient & remainder calculator        
        remainder = int_a
        quotient = 0

        for i in range(0, int_a, int_b):
            while remainder >= int_b:
                quotient += 1
                remainder -= int_b

        #E. Addition-based product calculator
        product = 0

        for i in range(int_b):
            product += int_a

        #F. Output 
        print("""
        Integer A | {}
        Integer B | {}
        Quotient  | {}
        Remainder | {}
        Product   | {}
        """.format(int_a, int_b, quotient, remainder, product))

        break