    ###########################################################

    #  Computer Project #5

    #

    #  Algorithm

    #  make functions for usage in main function

    #   adhere to parameters

    # this function uses our knowledge of files, functions,try,except\
    # and uses main function to interact with the user.
    

    ###########################################################


def open_file():
    '''This function opens the file fp which is the file pointer and is 
    returned as well. It takes the input of file and only works when input is
    MMR.txt'''
    
    while True:
        input("Input a file name: ")        # take input of value

        try:                    # only works when the right input is right.
            input == 'MMR.txt'
            fp = open('MMR.txt', 'r')
            break


        except:             
            print("Error: file not found. Please try again.") 
            #input not equal to MMR.txt
            continue

    return fp


    
def get_us_value(fp):
    '''this function takes input fp which is the file pointer and returns the 
    float value for the percentage of United States to return'''
    fp.seek(0)
    fp.readline()       # skips first line
    fp.readline()       #skips second line
    for line in fp:
        state = line[:25].strip()       #strip to clear extra spaces
        percentage = line[25:29].strip()

        if state == 'United States':
            
            return float(percentage) #output should be a float value

    
def get_min_value_and_state(fp):
    '''this function takes an input of the file pointer to open files and then 
    gives the value for the minimum mmr coverage'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    min_value = 200

    for line in fp:         #for loop to read lines and give us the minimum val
        percentage = line[25:29].strip()
        if percentage == 'NA':  # reloop incase of na 
            continue
        else:   # for all numerical cases.
            percentage = float(percentage)      
            if percentage < min_value:
                min_value = percentage
                min_state = line[:25].strip()

    return min_state, min_value
  # insert your code here.

def get_max_value_and_state(fp):
    ''' this funvtion takes an input of the file pointer and then gives us an 
    output of the maximum mmr coverage state and value'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    max_value = 0

    for line in fp:
        percentage = line[25:29].strip()
        if percentage == 'NA':      # reloop in case of na.
            continue
        else:               # for all numerical cases.
            percentage = float(percentage)
            if percentage > max_value:
                max_value = percentage
                max_state = line[:25].strip()
    return max_state, max_value             # gives us the output of max value.


    
        
def display_herd_immunity(fp):
    '''This function also takes the input of file pointer and then gives us an
    output of all functions that are lesser tahn 90%.'''
    fp.seek(0)
    fp.readline()
    fp.readline()
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    percent=90
    
    for line in fp:
        percentage = line[25:29].strip()
        state = line[:25].strip()

        if percentage =='NA':       #reloop in case of na.
            continue
        else:# for all teh other numerical values.
            percentage= float(percentage)
        
            if percentage < percent:
                print("{:<25s}{:>5.1f}%".format(state,percentage))
                continue
                
                

def write_herd_immunity(fp):
    '''This function takes an input of file pointer as wll and writes a new 
    text document named herd.txt and prints all values of mmr that are less 
    than 90%'''
    herd_file=open('herd.txt','w')
    fp.seek(0)  
    fp.readline()
    fp.readline()
    herd_file.write("\nStates with insufficient Measles herd immunity.\n")      
    herd_file.write("{:<25s}{:>5s}\n".format("State","Percent"))    
    percent=90
    
    for line in fp:     # to read all the lines.
        percentage = line[25:29].strip()    
        state = line[:25].strip()

        if percentage =='NA':   # reloop in case of na.
            continue
        else:
            percentage= float(percentage)   # output should be float.
        
            if percentage < percent:
            
                herd_file.write("{:<25s}{:>5.1f}%\n".format(state,percentage))
                continue
                
    


def main():   
    '''This function interacts with the user and displays tehr equired value.'''
    tp= open_file()
    
    print(tp.readline())    # to print firstline. 
    
     
    a=get_us_value(tp)
    print("Overall US MMR coverage: {}%".format(a)) # print value of USA.
    
    b1,b2 = get_min_value_and_state(tp)
    print("State with minimal MMR coverage: {} {}%".format(b1, b2))
    # print value of minimum and state.
    
    c1,c2=get_max_value_and_state(tp)
    print("State with maximum MMR coverage: {} {}%".format(c1,c2))
    #print max value and state.
    
    
    display_herd_immunity(tp)   
    
    write_herd_immunity(tp)
    
    
    

if __name__ == "__main__":      #helps run main function.
    main()    