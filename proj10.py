

###############################################################################
''' CSE Project 10. This projects basic aim is to make the game Montana on 
python using appropriate data bases. It consists of 6 functions  '''
###############################################################################

import cards, random
random.seed(100) #random number generator will always generate 
                 #the same random number (needed to replicate tests)


def initialize():
    '''This function returns tableau and extracts data from the cards program 
    and sorts them into 4 lists inside tableau. The idea was to create a basic
    function'''
    s = cards.Deck()        # extracting cards
    s.shuffle()
    tableau = [[], [], [], []]  #creating the empty list of 4 lists

    
    for i in tableau:                 #deals 4 cards to the tableau
        
        for j in range(13):
            i.append(s.deal())  # put deck into tableaus list of lists
    return tableau
    
    
def display(tableau):
    '''
        This function displays the current state of the game.
        It display four rows of 13 cards with row and column labels.
        Ace is displayed with a blank.
        
        parameters: 
            tableau: data structure representing the tableau 
        
        Returns: None
    '''

    print("{:3s} ".format(' '), end = '')
    for col in range(1,14):
        print("{:3d} ".format(col), end = '')
    print()
        
    for r,row_list in enumerate(tableau):
        print("{:3d}:".format(r+1), end = '')
        for c in row_list:
            if c.rank() == 1:
                print("  {}{}".format(' ',' '), end = '')
            else:
                print("{:>4s}".format(str(c)),end = '')
        print()

def validate_move(tableau,source_row,source_col,dest_row,dest_col):
    '''
       The basic idea of the function is to check if the moves are appropriate 
       or not and to return True and returns false for an inappropriate move
       '''
    
    if source_row not in range(4):  # we create the appropriate functions based
        #on the given conditions and we try to negate them to return False. 
        return False
    if dest_row not in range(4):    
        
        return False
    if source_col not in range (13):
        return False
    if dest_col not in range(13):
        return False   
    
    if tableau[dest_row][dest_col].rank()!=1:
        return False
    if dest_col==0 and tableau[source_row][source_col].rank()==2:
        return True
    if dest_col!=0:
        if tableau[dest_row][dest_col-1].suit()==tableau[source_row][source_col].suit():
            if tableau[dest_row][dest_col-1].rank()+1==tableau[source_row][source_col].rank():
                return True

    return False
    

    
    
def move(tableau,source_row,source_col,dest_row,dest_col):
    '''
The main idea of this function is to  move and change cards based on the input 
and rules and to return boolean based on the move function usage.
    '''
    if not validate_move(tableau,source_row,source_col,dest_row,dest_col):
        return False        # returning false based on the condition.
    temp_card=tableau[dest_row][dest_col]
    tableau[dest_row][dest_col]=tableau[source_row][source_col]
    tableau[source_row][source_col]=temp_card   #interchanging the values.
    return True     #returning true when possible.
    
  
def shuffle_tableau(tableau):
    '''
This is the hardest part of the whole programming code and we dont really 
return anything but we shuffle the tablaeu that we obtained from initialize() in
this function
    '''
    remove_cards=[]
    for j,row in enumerate(tableau):
        current_rank=2
        current_suit=row[0].suit()
        for i, card in enumerate(row):
            if card.rank()!=current_rank or card.suit()!=current_suit:
                remove_cards+= row[i:]
                tableau[j]=row[0:i]
                break
            else:
                current_rank+=1
                if current_rank==14:
    
                    current_rank=1
    random.shuffle(remove_cards) 
    aces=[]                
    for card in remove_cards:
        if card.rank()==1:
            
            aces.append(card)
#            remove_cards.remove(card)
    for card in aces:
        remove_cards.remove(card)         
    
   
    for j,row in enumerate(tableau):

                    if len(aces)>0:
                        tableau[j].append(aces.pop(0))
                    while len(tableau[j]) < 13:
                        tableau[j].append(remove_cards.pop(0))
    return



def check_win(tableau):
    '''
In this function a boolean is returned as w check if he person has won the game
or not! We return all the true statements first and then we return the a True
to satisfy the given conditions
    '''
    
    for row in tableau:
        for a,b in enumerate(row):  #extracting the roe and enumerating it.
            
            
            
            if a == 12 and b.rank() != 1:   #this is position 13 and it shouldnt be A for false
                return False
            
            if a == 0 and b.rank() != 2:
                return False
            
            if b.suit() != row[a-1].suit() and 0 < a < 12:  #appropriate conditions
                return False
            
            if 0 < a < 12 and b.rank() - row[a-1].rank() != 1:
                return False
            
            
                
    return True     # one seperate true to be true for all other conditions 
                    #except in the for loop false conditions.
             
def main():
    '''
        This function utilizes all other functions to run the essential 
        program. We have created an original True while loop so that we dont 
        have to make multiple functions. Then we have called all tehf unction 
        inside the loop according to the requirmnets given in the pdf file. 
    '''

    
    while True:         # creating an orignal true while loop
        
        shuffles_available = 2 # we set this so that we can shuffle for
                                    # a maximum time of 2
        
        tableau = initialize()      # according to pdf
                        
        print("Montana Solitaire.")
        display(tableau)
        
        win = False
        
        choice = ''
        
        while not(choice == 'q' or win):        # essentially a false statement 
            a="Enter choice:\n (q)uit, (s)huffle, or space-separated: source_row,source_col,dest_row,dest_col: "
            choice = (input(a))
            
            if choice == 's':
                if True:
                    if shuffles_available:
                        shuffle_tableau(tableau)        #option no 1 for shuffling
                                                    # a maximum of 2 times we subtract from initial shuffles
                        display(tableau)
                        shuffles_available -= 1
                    
                    else:
                         
                        print("No more shuffles remain.")
            
            elif choice != 'q' :        # for all the conditions except for q
                
                try:
                    
                    Sr, Sc, Dr, Dc = [int(num)-1 for num in choice.split()]     # if the required functions are ther in the input
                
                
                except:
                    if True:
                        print("Error: invalid input.  Please try again.")
                    
                
                else:
                    
                    if not ((Sr in range(4)) and (Dr in range(4)) and Sc in range(13) and (Dc in range(13))):
                        if True:
                            
                            print("Error: row and/or column out of range. Please Try again.")
                    
                    elif  not move (tableau, Sr, Sc, Dr, Dc):
                        if True:
                            
                            print("Error: invalid move.  Please try again.")
                    
                    else:
                        
                        
                        win = check_win(tableau)    # first we check if it is a 
                                                    # winner.
                        display(tableau)    #then we display the tableau.
                    
        else:                       # this part of the main gives final touches 
            if win:                 #and loops according to the answer.
                
                print("You won!")
            
            re = input("Do you want to play again (y/n)?").lower()
            
            if re == 'y':
                
                continue    # sinc e the player wants to play agin therefore
                            # we will go back into the loop
            
            else:
                
                print("Thank you for playing.")
                
                
                break    #the functiona nd program ends here!
            
   

if __name__ == "__main__":  #this allows us to run the main function.
    main()  
    
    