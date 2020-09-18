''' This is project 6. In this project have to evaluate data froma .csv file and 
create appropraite function that can be run in the main function..'''

import csv
from operator import itemgetter

def open_file():
    '''This functions accepts no input but helps us to open the file and return
    the file pointer that can be used in teh enxt function'''
    
    
    while True:                 # we create a loop which will use try except
        file = input('Enter filename: ')     #taking the input
    
        try:
            fp = open( file ,'r')       
        
            break   
        
        except:
            FileNotFoundError
            print("File not found! Please try again!")  #print error message
        continue        #reloop if the input is not correct.
    
    return fp  
        

def read_file(fp):
    '''This function takes the input fp from the above function and reads the
    dat inside the file by appending all of them and returning the master_list
    ehich is going to be the input for all the later fuctions'''
    reader= csv.reader(fp)
    fp.readline()       #skip the first line
    masterlist=[]
    for line in reader:     
        masterlist.append(line)     #adding all the values in the empty master
                                    #list
    return masterlist    
    
    
def shoots_left_right(master_list):
    '''This functions takes the master_list into account and then gives us our
    count of the players are either left or right.Both of teh returned values
    are integers.'''
    
    count_R=0   #setting up two counts to 0 so that we can append later in the
                #for loop
    count_L=0
    
    for direction in master_list:
        if direction[1]=='R':   # according to the output the count will
                                #increase        
            count_R+=1
        if direction[1]=='L':
            count_L+=1
    return (count_L,count_R)            #the returned value


def position(master_list):
    
    '''This functions takes amster_list to be the input and evaluates the 
    position of the players and gives us a count of all them returned in 
    integer values..'''
    count_l=0
    count_r=0       #initializing the values for counts according to position
    count_d=0
    count_c=0
    
    for position in master_list:
        if position[2]=='L':
            count_l+=1
        if position[2]=='R':      #adding the counts by value of 1 accordingly
            count_r+=1
        if position[2]=='C':
            count_c+=1
        if position[2]=='D':
            count_d+=1
    return (count_l,count_r,count_c,count_d) # the required value.       

def off_side_shooter(master_list):
    '''This function takes in the input from master_list and evaluates the
    players and giving us a count of players who play left win but shoot right
    and players who play right winga nd shoot left.'''
    count_lr=0          #initializing the counts to be 0
    count_rl=0
    
    for line in master_list:
        if line[1]=='R':
            if line[2]=='L':
                count_rl+=1
        if line[1]=='L':
            if line[2]=='R':
                count_lr+=1
                
    return (count_rl,count_lr)          #returning the value of counts obtained
                                        #from the for loop.

def points_per_game(master_list):
    '''THis function accepts as input the master lista dn return a sorted list
    of tuples which include points per game,player name and position. '''
    fn_list=[]  # the first empty list which shall contain the appended values
    final=[]    #the second list which shall sort the fn_list[]

    
    for line in master_list:
        fn_list.append((float(line[18]),line[0],line[2]))
    fn_list.sort(key=itemgetter(0),reverse=1)
    fn_list.sort(reverse=1)

    for i in range(0,10):       #only top 10 required so range is set 
        final.append(fn_list[i]) #accordingly.
            
    return final

def games_played(master_list):
    '''This function accepts the input as master_list and returns the value
    for games played and the name of teh players in a list of tuples.'''
    fn_list=[]  # the first empty list which shall contain the appended values
    final=[]    #the second list which shall sort the fn_list[]
    
    for line in master_list:
        line[3]= line[3].replace(',','')    # replacing all , with simple space
        a=int(line[3]),line[0]      #converting line [3] t an integer 
        fn_list.append(a)
        
    fn_list.sort(key=itemgetter(0),reverse=1)   #sorting the values 
    fn_list.sort(reverse=1)

    for i in range(0,10):       # top 10 required
        final.append(fn_list[i])
            
    return final

def shots_taken(master_list):
    '''THis function also take sinto account the master_list and returns 
    the shots taken and the corresponding name of the player in a sorted list 
    of tuples.'''
    fn_list=[]  # the first empty list which shall contain the appended values
    final=[]    #the second list which shall sort the fn_list[]

    
    for line in master_list:
        line[9]=line[9].replace(',','') #handling the comma problem
        while line[9]!='--':# creating awhile llop to handle the hyphen problem 
        
            a=int(line[9]),line[0]      #making line[9] as an integer.
            fn_list.append(a)
            break
        else:
            continue    #reloop 
        
    fn_list.sort(key=itemgetter(0),reverse=1)
    fn_list.sort(reverse=1)

    for i in range(0,10):
        final.append(fn_list[i])
            
    return final        #returns the final sorted values
    
    
    
def main():
    '''This function callls all the previous functions and we are supposed 
    to be printing the outputs from the previous function this function. '''
    
    #all the functions called in order.   
    fp=open_file()  # opening the .csv file
    master_list=read_file(fp)   # setting the master_list as it is input of 
    print()                     #most functions
    print()
    
    print("{:^10s}".format("Shooting"))     # printing the count of l and r
    count_L,count_R=shoots_left_right(master_list)  
    print("left:  {:4d}".format(count_L))       #formatting according to
    print("right: {:4d}".format(count_R))       #requirment and printing
    print()
    
    print("{:^12s}".format("Position"))# printing the count of positions 
    count_l,count_r,count_c,count_d=position(master_list)  #of the players
    print("left:    {:4d}".format(count_l))
    print("right:   {:4d}".format(count_r))
    print("center:  {:4d}".format(count_c)) #formatting according to need
    print("defense: {:4d}".format(count_d)) # printing required values
    print()
    
    print("{:^24s}".format("Off-side Shooter")) # printing the count of off
    count_rl,count_lr=off_side_shooter(master_list) # side shooter.
    print("left-wing shooting right: {:4d}".format(count_rl))
    print("right-wing shooting left: {:4d}".format(count_lr))
    #formatting and printing according to the requirment
    print()
    
    print("{:^36s}".format("Top Ten Points-Per-Game"))
    #printing the values for the top 10 players and games played
    print("{:<20s}{:>8s}{:>16s}".format('Player','Position','Points Per Game'))
    for values in points_per_game(master_list): # for loop created to break 
        vala,valb,valc=values                   #down the values for formatting
    
        print("{:<20s}{:>8s}{:>16.2f}".format(valb,valc,vala))
        #printing and formatting according to the requirment
    print()
    
    print("{:^36s}".format("Top Ten Games-Played"))
    print("{:<20s}{:>16s}".format('Player','Games Played'))
    for values in games_played(master_list):# for loop created to break
        vala,valb = values                  #down the values for formatting 
        print("{:<20s}{:>16,d}".format(valb,vala))
        #printing and formatting according to the requirment
    print()    
    
    print("{:^36s}".format("Top Ten Shots-Taken"))
    print("{:<20s}{:>16s}".format('Player','Shots Taken'))
    for values in shots_taken(master_list):# for loop created to break
        vala,valb=values                   #down the values for formatting
        print("{:<20s}{:>16,d}".format(valb,vala))
        #printing and formatting according to the requirment
    
    

if __name__ == "__main__":  # opening the main function
    main()
    
    
    
