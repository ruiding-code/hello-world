def create():
    coefficients = [] # creates empty list of coefficients
    powers = [] # creates empty list of powers
    polynomial_entered = input("Enter polynomial: ")
    list_polynomial = polynomial_entered.split() # creates a list: ["C0xP0", "C1xP1", ...]
    for term in list_polynomial: # each term is a string "CixPi"
        coefficient_with_power = term.split("x") # splits the term in 2: coefficient and corresponding power
        coefficients.append(float(coefficient_with_power[0])) # list of ordered float numbers representing coefficients
        powers.append(int(coefficient_with_power[1])) # list of ordered int representing powers
    dict_polynomial = {} # creates empty dict
    for i in range(len(powers)): # or in range(len(coefficients))
        dict_polynomial[powers[i]] = coefficients[i] # each key (power) is assigned the corresponding coefficient value
    return dict_polynomial # returns dict of int keys (powers) and float coefficient values

def display(polynomial): # argument polynomial entered will be a dictionary type     
    for power in polynomial: # iterates through each key
        print("{:.2f}x{}".format(polynomial[power], power), end=" ") # prints each term separated by a space. 2 decimals displayed for coefficient values
    print("") # next line will be printed after the line displaying the polynomial

def derivative(polynomial, order=1): # argument polynomial entered will be a dictionary type
    derivative = {} # creates an empty dict for derivative
    no_zero = True
    for power in polynomial: # iterates through the powers
        if power >= 0 and (power-order) < 0 and no_zero: # when a positive power, and order bigger than highest degree
             derivative[0] = float(0) # assigns the power 0 to coefficient 0
        elif (power > 0 and (power-order) >= 0) or power < 0:
            derivative[power-order] = polynomial[power] # sets the value of coefficient to be multiplied by
            for i in range(order):
                derivative[power-order] *= (power-i) # depending on the order, the coefficient will be multiplied by the values power-0, power-1, etc.
        if (power-order) == 0: # there would already be a coefficient value associated to the 0 power that we don't want to rewrite over in the next iteration of the for loop
            no_zero = False
    return derivative # returns dict with int keys (powers) and float coefficients

def integral(polynomial): # argument polynomial entered will be a dict   
    integral = {} # creates an empty dict
    for power in polynomial: # iterates over each key in the dict
        integral[power+1] = polynomial[power] / (power+1) # works for all cases as long as power isn't -1
    return integral # returns a dict

polynomial = create()
display(polynomial)
user_input = input('Enter order of derivative: ')
print('Derivative: ')
display(derivative(polynomial, order=int(user_input)))
print('Integral: ')
display(integral(polynomial))
