#******************************************************************************

''' Project9
In this project we have created functions to ectractv data from a file which 
has information related to COVID-19 and we have used these functions mainly to 
sort and segregate the data.  '''

import csv
import matplotlib.pyplot as plt  # inporting the required formats
plt.style.use("ggplot")
from operator import itemgetter


def open_file():
    '''
        This functions accepts no input but returns the file pointer and 
        opens ncov.csv by default if there is no input.
    '''

    fp = input("Data file: ")   #pluging in the value for the file
    
    while fp != '':     #if string is not empty
        
        try:
            
            fp = open(fp, encoding='utf-8')
            
            break # when file succesfully opens.
        
        except FileNotFoundError: 
            print("Error. Try again.")
        
        fp = input("Data file: ")
    
    else: 
        fp = open("ncov.csv")   #opening the default file if nothing is entered.
    
    return fp   #returning the appropriate value



def build_dictionary(fp):
    '''
This function starts reading the data in the file and extracts and sorts them 
in the required format. We have to take into account N/A in the area while 
evaluating the data and it returns the master_Dict which is used in all the 
later functions.
    '''
    file = csv.reader(fp)   
    next(file, None)    #to skip the header line.
    
    master_dict={}  #creating empty dictionary.
    for line in file:   # iterating the data to read the lines.
        D1={}
        country=line[2].strip() #removing spaces by using.strip
        area=line[1].strip()
        if area=='':    # if the area is empty we have to assume N/A.
            area = 'N/A'
        else:   # else take the regular data into account.
            area=line[1]    # indexing the values.
        lastupdate=line[3]
        cases=int(line[4])  #converting values to integers
        deaths=int(line[5])
        recovered=int(line[6])
        D1={area:(lastupdate,cases,deaths,recovered)}   #setting the format
        l1=[]
        l1.append(D1)   #we cant append in dictionary so we use a list.

        if country not in master_dict:
            master_dict[country]=l1
        else:
            master_dict[country]+=l1
            
    
    return master_dict      #returning the appropriate value.
    

def top_affected_by_spread(master_dict):
    '''
        This function takes the master_dict into account and returns values in
        form of list. It gives country,val format.
    '''
    l=[]
    for country,value in master_dict.items():
    
        length=len(value)   # based on length
        l.append((country,length))
    
    l=sorted(l,key=itemgetter(1),reverse=True)
    l=sorted(l,key=itemgetter(0))   #sorting the values
    l=sorted(l,key=itemgetter(1),reverse=True)       
    l=l[0:10]   # we want only top 10 values
    return l
            

        


def top_affected_by_numbers(master_dict):
    '''
         This function takes the master_dict as input into account and returns values in
        form of list. It gives country,area affected format. RReturns top 10 
        areas in country.
    '''
    l1=[]
    for country, val in master_dict.items():    # iterating 3 tiems to extract area
        case=0
        for D in val:
            
            for value in D.values():
                
                case+=value[1]  # adding the cases accordingly
        l1.append((country,case))
            
    l1=sorted(l1,key=itemgetter(1),reverse=True)
    l1=l1[0:10] # top 10 values are required
    return l1           
    
    
    

def is_affected(master_dict, country):
    '''
        This function takes county and amster_dict into account and checks if 
        the country is in master_dict that is is it affected or not and returns
        appropriate value
        
    '''
    l=[]
    for k in master_dict:   #checing if the value exists in master_dict
        k=k.lower()
        l.append(k) #appending if it exists.
       
    return country in l #returning apppropriate values.



def plot_by_numbers(list_of_countries, list_of_numbers):
    '''
        This function plots the number of areas/people inffected by country.
        
        parameters: 
            list_of_countries: list of countries
            list_of_numbers: list of the number of areas/people inffected
            
        Returns: None
    '''
    fig, ax = plt.subplots()
    
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    
    plt.show()

 
def affected_states_in_country(master_dict, country):

    '''
        This function takes into account master_dict and country as an input
        and returns value by checking if it exists in the for loop and then 
        returning the appropriate value as a set database.  
    '''
    s=set()
    
    for key,val in master_dict.items(): #iterating
        if key.lower() == country.lower():  #.lower() used to account for all values
                
            for D in val:
                for k in D:
                    s.add(k)    #appending/ adding the values in empty set
                    
    
    return s            

                
def main():
    ''' The main function is the heart of the programa and uses all the other 
    functions to allow the program to run. '''
   
    
    BANNER = '''
  .__   __.   ______   ______   ____    ____  
  |  \ |  |  /      | /  __  \  \   \  /   /  
  |   \|  | |  ,----'|  |  |  |  \   \/   /  
  |  . `  | |  |     |  |  |  |   \      /    
  |  |\   | |  `----.|  `--'  |    \    /    
  |__| \__|  \______| \______/      \__/      
    '''
    print(BANNER)
    MENU = '''
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit

Choice: '''
    fp = open_file()    # opening the file
    a = build_dictionary(fp)
    empty = ''
    
    while empty != '5':     # making a while loop
        choice = input(MENU)
       
        if choice == '1':   #option1
            print("{:<20s} {:15s}".format("Country", "Areas affected"))
            print("-"*40)
            z = top_affected_by_spread(a)   
            for value in z: # iterating through the function and printing at appropriate indices.
                print("{:<20s} {:5d}".format(value[0], value[1]))
            
            print() #empty line according to requirment
            
            plot = input('Plot? (y/n) ').lower()
            
            
            if plot == 'n': # if plot answer is not yes then reloop else
                continue
                
            
            else:
                
                five= z[0:5] # we want to plot only first 5 
                lista = []
                listb = []  #creating empty lists
                
                for value in five:
                    lista.append(value[0])
                    listb.append(value[1])
                
                plot_by_numbers(lista, listb)   #using the plotting function.
       
        elif choice == '2': #choice 2
            
            print("{:<20s} {:15s}".format("Country", "People affected"))
            
            print("-"*40)# printing the star values.
            z = top_affected_by_numbers(a)  # setting the function =z for ease
            
            for value in z:
                print("{:<20s} {:5d}".format(value[0], value[1]))   #choosing the appropriate indices
            
            print()
            
            inp = input('Plot? (y/n) ')
            if inp == 'n':
                continue
                
            else:
                
                top_five1 = z[1:6]  #choosing the appropriate indices for top 5 values.
                lista = []  #empty lists
                listb = []
                
                for value in top_five1:
                    lista.append(value[0])
                    listb.append(value[1])
                plot_by_numbers(lista, listb)
           
        
        
        
        elif choice == '3':
            #choice 3
                    country = input("Country name: ")#taking the country name as an input.
                    
                    print("-"*30)#printing stars.
                    
                    z = affected_states_in_country(a, country)
                    if len(z) != 0:
                        
                        print("{:<30s}".format("Affected area"))
                        print("-"*30)
                        
                        lista = []  #creating an empty list
                        for value in z:
                            lista.append(value)     # Appending the values for iterating later.
                        
                        lista.sort()
                        
                        for c, d in enumerate(lista):   #iterating through the list
                            print( "[{:02d}] {:<30s}".format((c+1),d))
                    else:
                        print("Error. Country not found.")
               
        elif choice == '4': 
            #option 4
            country = input("Country name: ")   #input the value for taking in later.
            
            print("-"*30)   # printing the stars.
            z = is_affected(a, country)
            
            if z==True: # when the country is there in the function
                
                print("{} is affected.".format(country))
            
            if z==False:    # when the country is not there in the function
                
                print("{} is not affected.".format(country))
           
            
        elif choice == '5': 
            #choice 5
            print("Stay at home. Protect your community against COVID-19")
            break   # breaking and exiting from the loop
       
        
        else:
            print("Error. Try again.")  # printing the error message
   

   
if __name__ == "__main__":    
    main()  # running the main function

    

#*****************************************************************************
    
    




    
    
      