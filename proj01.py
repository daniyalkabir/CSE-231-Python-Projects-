PROMPT = '''\nWould you like to continue (Y/N)? '''


in_str = input(PROMPT)
    


code = input("\nCustomer code (BDW): ")
odo_str=input("Odometer reading at the start: ")
odo_int = int(odo_str)
odo_str2= input("Odometer reading at the end:   ")
odo_int2= int(odo_str2)
mile = odo_int2- odo_int
day_str= input("\nNumber of days: ")
day=int(day_str)

while in_str == 'Y' :
   
    if code == 'B':
        amountdue==40*day + 0.25*mile
         print (amount due : , 'amountdue')
    if code == 'D' :
        if mile< 100*day 
            amountdue== 60*day
            print (amount due : , 'amountdue')
        if mile >100:
            amountdue== 60*day + 0.25(mile-100)
             print (amount due : , 'amountdue')
     if code == 'W' 
                   
             
   

    
    
    
    
    
    
   
    
    
    
    
    
     
    
    in_str = input(PROMPT)
    