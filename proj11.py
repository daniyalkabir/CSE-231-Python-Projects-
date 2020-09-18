''' ############## Project 11###############################################
This project tests our knowledge of classes and we write four classes that
 implement a hectic morning of getting to class. '''


MAP = {"U":"Up","D":"Down","L":"Left","R":"Right"}

class Student(object):
    '''
This class is a fairly simple class. A student who knows the id of the 
classroom and has a list of the inventory that he or she posseses.
    '''
    def __init__(self, item_list=None, classroom_id=-1):
        '''Initializes yourself, with an empty backpack by default. The default position of the student is room -1.'''

        if item_list == None:
            self.backpack = []
        else:
            self.backpack = item_list
        self.classroom_id = classroom_id

    def __repr__(self):
        '''Returns a string representation of the student.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the student's inventory.'''
        s = "Backpack: "
        if len(self.backpack) == 0:
            s += "Empty"
        else:
            for item in self.backpack:
                s += item + ", "
            else:
                s = s[:-2] # remove trailing comma and space
        return s

    def __eq__( self, S ):
        '''
           This function returns booleans based on whether classroom id matches
           the students classroom id.
        '''
        if self.classroom_id==S.classroom_id:       # creating an if conditional.
            return True
        else:
            return False    # returning the appropriate booleans.
            
        
     
    def place(self, classroom_id):
        '''
        This method inside the class places a student in a classroom by initializing
        the classroom id.
        '''
        self.classroom_id = classroom_id    #placing the value.
        
    
    def add_item(self, item):
        '''
        This function adds an item to the classroom's inventory.
        '''
        if len(self.backpack) == 6:     # the lenght should not be greater than 6.
            print("Backpack is full.")
        else:
            self.backpack.append(item)  #otherwise we can add the values.
        
       
            

    def remove_item(self, item):
        '''
            This method removes items from the backpack.
        '''
        if item in self.backpack:   
            self.backpack.remove(item)      # we use remove() to cut teh avlue from the list. 
        else:    
            print("Failed to remove item from backpack.")
            


class Classroom(object):
    '''
This is a class that represents a single classroom at a  time. In this class we
Associated with each classroom is a unique id, an int, and a course, a 
string such as “CSE231”
    '''
    def __init__(self, text_desc="0 empty"):
        '''Initialzes a classroom. By default it has id 0 and is a "empty" room with no inventory or exits.'''
        description = text_desc.split()

        self.id = int(description[0])
        self.course = description[1]

        # Initialize a dictionary of potential exits as empty
        self.exits = {}

        # Initialize a "backpack" of items as empty list
        self.backpack = []
        
        #ADD YOUR CODE HERE
        while True:         #creating an original loop.
            if len(description)>2: 
                for item in description[2:]:
                    
                    if item[0] in 'UDLR':   # after splitting if item is not from UDLR
                        self.exits[item[0]]= int(item[1:])
                    
                    else:
                        
                        self.backpack.append(item)  # appending to the empty backpack list.
            
            break
                
                
#                if item[0] not in description:
#                    self.backpack.append(item)
#                else:
#                    self.exits[item[0]]= int(item[1:])
        

            

    def __repr__(self):
        '''Returns a string representation of the classroom.'''
        classroom_repr = '''Classroom("''' + repr(self.id) + " " + self.course

        for direction in self.exits:
            classroom_repr += " {}".format(direction) + repr(self.exits[direction])

        for item in self.backpack:
            classroom_repr += " " + item

        classroom_repr += '''")'''

        return classroom_repr

    def __str__(self):
        '''Returns a string representing the room in a nice conversational style.'''

        # Basic classroom description
        classroom_str = "You see a " + self.course + " classroom."

        # List the things in the classroom
        if len(self.backpack) == 1:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + "."
        if len(self.backpack) == 2:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + \
                             " and a " + self.backpack[1] + "."
        elif len(self.backpack) > 2:
            classroom_str += " On the desk you see "
            for item in self.backpack[:-1]:
                classroom_str += "a " + item + ", "
            classroom_str += "and a " + self.backpack[-1] + "."

        # List the exits
        if len(self.exits) == 0:
            classroom_str += " Run through the classroom grab what you need (if possible). Exit and run to the exam!"
        elif len(self.exits) == 1:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + "."
        elif len(self.exits) == 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + " or " + MAP[list(self.exits.keys())[1]] + "."
        elif len(self.exits) > 2:
            classroom_str += " Run through the classroom grab what you need (if possible). Now, run into the hallway and go "
            for direction in list(self.exits.keys())[:-1]:
                classroom_str += MAP[direction] + ", "
            classroom_str += "or " + MAP[list(self.exits.keys())[-1]] + "."

        return classroom_str
    
    def __eq__( self, C ):
        '''
        : Returns True if Classroom id, course, exits and backpack are equal
        to the id, course, exits and backpack of C. Otherwise, returns False.
        '''
        if self.id==C.id and self.course==C.course and self.exits==C.exits and self.backpack==C.backpack: 
            #equating the self values to students values.
            
            return True
        else:
            
            return False
    
    def add_item(self, item):
        '''
        Adds an item to the classroom's inventory, its "backpack" 
        '''
        self.backpack.append(item)      #appending the values.


    def remove_item(self, item):
        '''
        Removes an item from the room's inventory, "backpack", if
        it is there
        '''
        if item in self.backpack:
            self.backpack.remove(item)
            return True
        else:    
            print("Failure to find the item in the classroom.")
        

    def get_room(self, direction):
        '''
            Returns the room id in the given direction, or False if
            there is no such room. The direction must be a valid key into self.exits,
            i.e. U, D, R, L;
            returns False, if not valid.
        '''
        
        for key , m in self.exits.items():  # iteratig through the exits dictionary.
            if direction in key:
                return m

        return False    # if m is not returned then we return False.
        
    

        

class Rush(object):
    '''
    This is the class that governs the escapade itself. It is responsible for 
    interactions between the user, the character, and the rooms
    '''

    def __init__(self, filename="rushing.txt"):
        '''Initializes the student rushing to class.  The student starts in the classroom with the lowest id.'''

        # First make a student start with an empty inventory
        self.student = Student()

        # Create classrooms are an empty dictionary
        self.classrooms = {}
        
        # Now read the file to get the classroom lines
        
        #ADD YOUR CODE HERE
        
        fp=open(filename, "r")
        
        for line in fp:
            #key will be id and value is classroom line
            
            classroom= Classroom(line)
            
            classroom_id =classroom.id
            
            self.classrooms.update({classroom_id:classroom})
            
        
    
        # Place the student in the room with lowest id
        self.student.place(min(self.classrooms.keys()))
        

    def __repr__(self):
        '''Returns a string representation.'''

        return self.__str__()   #string.

    def __str__(self):
        '''Returns a string representing the journey to the class, simply giving the number of rooms.'''
        search_str = "You are searched in "
        if len(self.classrooms) == 0:
            search_str += "no classrooms at all, you are in the hallway. You are late run in a random class and get items from the desks."
        elif len(self.classrooms) == 1:
            search_str += "a classroom."
        else:
            search_str += "a set of " + str(len(self.classrooms)) + \
                          " classrooms."

        return search_str

    def intro(self):
        '''Prints an introduction to the search for items because you are late
        This prompt includes the commands.'''
        print("\nAHHHH! I'm late for class\n")
        print("*runs out the house to catch the bus with an empty backpack*")

        print("\nYou're popular and have friends in many classes. Find and collect any items you find useful for your exam.")
        print("You are already late, and have a CSE231 Final Exam in 10 mins.\n")
        self.print_help()


    def print_help(self):
        '''Prints the valid commands.'''
        print("Use your instincts: ")
        print("*thinks*.. *thinks*.. what to do?!?!?!?!")
        print("*running*")
        print("S or search -- prints a description of the classroom you ran into")
        print("B or backpack - prints a list of items in your backpack")
        print("P pencil or pickup pencil - *mental* instruction to pick up an item called pencil")
        print("DR pencil or drop pencil - *mental* instruction to drop off an item called pencil")
        print("U or up - *mental* instruction to up the hallway to find another classroom")
        print("D or down - *mental* instruction to down the hallway to find another classroom")
        print("R or right - *mental* instruction to right in the hallway to find another classroom")
        print("L or left - *mental* instruction to left in the hallway to find another classroom")
        print("G or giveup - I have no more time, I need to get to class!!!")
        print("H or help - prints this list of options again")
        print()
        print("Remember that uppercase and lowercase SHOULD NOT matter. ")
        print("JUST GRAB WHAT YOU NEED AND GET TO CLASS TO START YOUR FINAL EXAM!!! HURRYYYY!!!")
        print()

    def prompt(self):
        '''Prompts for input and handles it, whether by error message or handling a valid command.
        Returns True as long as the user has not chosen to quit, False if they have.'''

        print("In room {} with course {}".format(self.student.classroom_id,self.classrooms[self.student.classroom_id].course))
        print(self.student)
        user_input = input("Enter a command (H for help): ")
        print()

        # Handle input: split for pickup/drop, capitalization unimportant for commands
        input_list = user_input.split()

        if len(input_list) == 0:
            user_input = "?"  # No command is not a valid command
            return False
        else:
            try:
                command = input_list[0].upper()  # The command
                if len(input_list) > 1:
                    item = input_list[1]
                if command == 'S':
                    self.search()
                elif command == 'B':
                    self.backpack()
                elif command == 'P':
                    self.pickup(item)
                elif command == 'DR':
                    self.drop(item)
                elif command in "UDLR":
                    self.move(command)
                elif command == 'G':
                    print("I have no more time, I need to get to class!!!")
                    return False
                elif command == 'H':
                     self.print_help() 
                else:
                    print("Unfortunately, that's not a valid option.")
                    return False
            except:
                print("Problem with the option or the item.")
                return False
        if self.win():
            return "win"
        return True

    def search(self):
        '''Prints the description of the current room.'''
        current_classroom = self.classrooms[self.student.classroom_id]
        print(current_classroom)

    def backpack(self):
        '''
          This method prints the student’s inventory in their backpack, using the
          method you wrote for Student. 
        '''
        print(self.student.backpack)    #printing the backpack value.
        

    def pickup(self, item):
        '''
             This method coordinates the student with their current classroom to
             remove the item from the classroom and add it to the student’s backpack
        '''
        a=self.classrooms[self.student.classroom_id].backpack
        if item in a:
            # iterating through classrooms.backpack
            
            self.student.add_item(item)
        
        self.classrooms[self.student.classroom_id].remove_item(item)    #removing the item.
  
        
        
            
    
    def drop(self, item):
        '''
        This method coordinates the student with their current classroom and
        removes the item from the student’s backpack and places it in the classroom
        '''
        b=self.student.backpack
        if item in b:
            
            self.classrooms[self.student.classroom_id].add_item(item)   #adding item.
        
        self.student.remove_item(item)
        
    
    def move(self, direction):
        '''
        This method moves the student in the specified direction if the
        current classroom has that direction in its attributes. If not, the move fails, 
        and this method will print an error message 
        '''
    
        while True:     #creating an original while loop.
            j = self.classrooms[self.student.classroom_id].get_room(direction)
            
            if j:       # essentially an if True statement.
                
                self.student.place(j)
                
                print("You went " + MAP[direction] + " and found a new classroom.")
            
            else:   # if the earlier condition is not met.
                
                errMsg = "Unfortunately, you went " + MAP[direction] + " and there was no classroom."
                 
                print(errMsg)

            break
        
        
    def win(self):
        '''
        This method checks that the student has entered the CSE231 classroom and has
        in their backpack the cheatsheet, eraser, paper, and pencil. If so, it returns True
        '''
        
        winning_backpack = ['cheatsheet', 'eraser', 'paper', 'pencil']
        
        present_classroom=self.classrooms[self.student.classroom_id]    
        
        if present_classroom.course == 'CSE231':    # according to pdf.
            
            if set(winning_backpack) == set(self.student.backpack):
                
                return True
        elif True:
            
            return False    # returning falsse if earlier conditions aren't met.
        
        
#        if winning_backpack in sorted(self.student.backpack):
#            return True
#        else:
#            return False
#        
    
def main():
    '''
    Prompts the user for a file, then plays that file until the user chooses to give up.
    Does not check formatting of input file.
    '''

    while True:
        try:
            filename = input("Enter a text filename: ")
            escapade = Rush(filename)
            break
        except IOError:
            print("Cannot open file:{}. Please try again.".format(filename))
            continue
    
    escapade.intro()
    escapade.__str__()
    escapade.search()
    
    keep_going = True
    while keep_going:
        keep_going = escapade.prompt()
        if keep_going == 'win':
            break
    if keep_going == 'win':
        print("You succeeded!")
    else:
        print("Thank you for playing")

if __name__ == "__main__":    
    main()