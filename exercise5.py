''' Insert heading comments here.'''

import math
EPSILON = 1.0e-7

def display_options():
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the sum of squares of the first N natural numbers.
             B. Display the approximate value of Pi.
             C. Display the approximate value of the sine of X.
             D. Display the approximate value of the cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)
    
def sum_natural_squares(N):
    '''Insert docstring here.'''
    N=int(N)
    if N>0:
        summ = (N*(N+1)*(2*N+1))/6
        return  summ
        
    else:
        return None
    

    
    pass  # insert your code here

def approximate_pi():
    '''Insert docstring here.'''
    
    
    pass  # insert your code here
    
def approximate_sin(x):
    '''Insert docstring here.'''
    pass  # insert your code here
           
def approximate_cos(x):
    '''Insert docstring here.'''
    pass  # insert your code here

def main():
    pass  # insert your code here

if __name__ == "__main__": 
    main()