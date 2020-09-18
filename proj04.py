###########################################################

    #  Computer Project #5

    #

    #  Algorithm

    #    define various functions

    #    create one main function in which all the functions are executed.

    #    display closing message when exit from program is made.

    ###########################################################

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
#    
def sum_natural_squares(N):
    '''This function gives us an output of the sum of the first n natural
    numbers and tries to execute and give teh answer'''
    try:
        N=int(N)        #made into an integer
        if N>0:
            summ = (N*(N+1)*(2*N+1))/6      #FORMULA GIVEN
            summ = int(summ)
            return  summ
            
        else:
            return None     # if value is not 
    except:
        return None
    



def approximate_pi():
    '''This function gives us an estimate of teh approxiamte value of pi which
    an irrational number. We have rounded the answer to 10 decimal places.
    it takes in the term, and value of n upto the point where term is less than
    epsilon and then returns the approximate value.'''
    try:
        term=1
        sum_pi=0            # values set for the loop for usage.
        N=1
            
        while abs(term)> EPSILON:
                sum_pi+=term
                term = (-1)**N/(2*N+1)      # formula given
                N+=1
        return  round(4*sum_pi, 10)
    except:
        return None
    
         


    
    

    
def approximate_sin(x):
    '''This function takes in the value of x that is put in the main funtion
    and return the approximate value for that x'''
    try:
        
        x = float(x)    # the function demands float value from the string
        
        term=1
        sum_sin=0
        N=0
            
        while  abs(term) > EPSILON:
                sum_sin+=term
                term = (x**(2*N+1)*(-1)**N)/(math.factorial(2*N+1)) #teh formula with the usage of factorial.
                N+=1
        return  round(round(sum_sin, 10) - 1 , 10)     
    except:
        return None
        

           
def approximate_cos(x):
    ''' This function takes in the value of x that is put in the main funtion
    and return the approximate value for that x'''
    
    try:
        x = float(x)    # function requires float value to be converted from string
        
            
        term=1
        sum_cos=0
        N=1
            
        while abs(term)> EPSILON:
                sum_cos+=term
                term = x**(2*N)*(-1)**N/math.factorial(2*N) #the formula with the usage of factorial
                N+=1
        return  round(sum_cos, 10) 
    except:
        return None
        

def main():
    ''' In this function we have used all the functions taht we had defined 
    earlier. They print values from tehf unctions       '''
    display_options()
    while True:
        
        z=input("\n\tEnter option: ")
        z=z.upper()
        if z == "A":
            N = input("\nEnter N: ")
            
            if N.isdigit()==True:
                N=int(N)
                s = sum_natural_squares(N)
                if s != None:
                    print("\n\tThe sum: ",s)
                else:
                    print("\n\tError: N was not a valid natural number. [{}]".format(N))
                    continue
            else:
                print("\n\tError: N was not a valid natural number. [{}]".format(N))
                continue
                
        
        elif z == 'B':
            my_pi=approximate_pi()
    
            print("\n\tApproximation: {:.10f}".format(my_pi))
            print("\tMath module:   {:.10f}".format(math.pi))    
            print("\tdifference:    {:.10f}".format( math.pi-my_pi))  
            
            
        elif z== 'C':
            x=(input("\n\tEnter X: "))
            if not x.isalpha():
                x=float(x)
            
                my_sin = approximate_sin(x)
   
                print("\n\tApproximation: {:.10f}".format(my_sin))
                print("\tMath module:   {:.10f}".format(math.sin(x)))    
                print("\tdifference:    {:.10f}".format(math.sin(x)-my_sin))
            else:
                print("\n\tError: X was not a valid float. [{}]".format(x))
                continue      #continue for relooping when the input is not right
                
                
        elif z == 'D':
            
            x=(input("\n\tEnter X: "))
            
            if not x.isalpha():
                x=float(x)
                my_cos = approximate_cos(x)
#    
                print("\n\tApproximation: {:.10f}".format(my_cos))
                print("\tMath module:   {:.10f}".format(math.cos(x)))   
                print("\tdifference:    {:.10f}".format(my_cos-math.cos(x)))
            else:
                print("\n\tError: X was not a valid float. [{}]".format(x))
                continue            ##continue for relooping when the input is not right
            
            
           
            
        elif z=='M':
            display_options()
            
            continue
        elif z=='X':
            print('Hope to see you again.')
            break
        
        else:
            print("\nError:  unrecognized option [{}]".format(z))   
            display_options()       # for relooping.
            
            continue
            
    
    

    
if __name__ == "__main__": 
    main()
    