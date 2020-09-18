###############################################################################
#              Computer Project # for CSE231                                                                                                 #
#               Algorithm                                                                                                                     #
#                                                                                                                                             #
# This project requires us to write a  program that will compute and display
# information for MSU Tuition fee calculator. #
###############################################################################
PROMPT = 'Resident (yes/no) :'
in_str= input (PROMPT)
level = 'Level-freshman, sophomore, junior, senior:'
lev = input(level)
cred = 'Credits:'
credit = input(cred)



while in_str == 'yes':
    
    if lev == 'freshman':
        eng=input('Are you admitted to the College of Engineering (yes/no)')
        
        if eng == 'yes' :
            
            if cred>=12 and cred<=18: