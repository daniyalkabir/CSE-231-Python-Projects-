###############################################################################
#              Computer Project # for CSE231                                                                                                 #
#               Algorithm                                                                                                                     #
#                                                                                                                                             #
# This project requires us to write a  program that will compute and display
# information for MSU Tuition fee calculator. #
###############################################################################
print("2019 MSU Undergraduate Tuition Calculator.\n")



james="none"
eng = "none"

PROMPT = 'Resident (yes/no): '#Input if internationational student or resident
while True:
    
    in_str= input(PROMPT)
    in_str=in_str.lower()
    
    if in_str !='yes':
        inter=('International (yes/no): ')
        inter=input(inter)
    
    
    lev=input("Level—freshman, sophomore, junior, senior: ").lower() #converting all values to lowercase for uniformity in code
    
    
    while lev not in ("freshman", "sophomore", "junior", "senior"):
            print("Invalid input. Try again.")
            lev = input("Level—freshman, sophomore, junior, senior: ").lower()
            continue                                        #Reiterates the loop when wrong input is entered
    if lev in ("freshman", "sophomore", "junior", "senior"):
        if lev== 'freshman' or lev=='sophomore':
            eng = input('Are you admitted to the College of Engineering (yes/no): ').lower()
            if eng!= 'yes':
                james=input('Are you in the James Madison College (yes/no): ')
            
    if lev=='junior' or lev=='senior':
        college = input('Enter college as business, engineering, health, sciences, or none: ')
        cmse=input('Is your major CMSE (“Computational Mathematics and Engineering”) (yes/no): ') 
                
        if college not in ("business", "engineering", "health", "sciences"):
            james = input("Are you in the James Madison College (yes/no): ")
         
      
    
    cred = (input('Credits: '))
    while True:
        if cred.isdigit() and  (cred != "0"):
            cred = int(cred)
            break
        else:
            print("Invalid input. Try again.")
            cred = (input('Credits: '))
            

    
    asmsu=21
    asmsu=int(asmsu)     #constants defined for ease in code
    fm=3
    fmu=int(fm)
    news= 5
    news=int(news)
    
    
    
    
    
    extra_cred = cred - 18
    extra_cred = int(extra_cred)
    while in_str == 'yes':      #calculations amde for residents.
            
        
            if lev == 'freshman' :
               
                
                
                if eng == 'yes' :
                    
                    if cred >= 12 and cred <= 18:
                        tue= 7230+asmsu+fm+ 670+news
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*482)+asmsu+fm+news+670+news
                    elif cred<6:
                        tue= (cred*482)+asmsu+fm+670
                    elif cred<=4:
                        tue= (cred*482)+asmsu+fm+402
                    elif cred>18:
                        tue= 7230+(cred*482)+670+news
                    print ('Tuition is ${:,.2f}.'.format(tue))
                    break
                    
                        
                if eng!= 'yes':
                    if cred >= 12 and cred <= 18:
                        tue = 7230+asmsu+fm+news
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*482)+asmsu+fm+news
                    elif cred<6:
                        tue= (cred*482)+asmsu+fm+670
                    elif cred<=4:
                        tue= (cred*482)+asmsu+fm+402    
                    elif cred>18:
                        tue= 7230+(cred*482)
                    print ('Tuition is ${:,.2f}.'.format(tue))
                    break
                
                if james=='yes':
                    if cred >= 12 and cred <= 18:
                        tue= 7410+asmsu+fm+news+7.50 
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*494)+asmsu+fm+news+7.50
                    elif cred<6:
                        tue= asmsu+fm+(cred*494)+7.50 
                    elif cred<=4:
                        tue= (cred*494)+asmsu+fm+7.50    
                    elif cred>18:
                        tue= 7410+(cred*494)+asmsu+fm+news+7.50        
                    print ('Tuition is ${:,.2f}.'.format(tue))
                        
            if lev== 'sophomore':
    
                if eng == 'yes' :
                    
               
                    if cred >= 12 and cred <= 18:
                        tue= 7410+asmsu+fm+ 670+news
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*494)+asmsu+fm+news+670
                    elif cred<6:
                        tue= (cred*494)+asmsu+fm+670
                    elif cred<=4:
                        tue= (cred*494)+7410+asmsu+fm+402     
                    elif cred>18:
                        tue= 7410+(cred*494)+670+asmsu+fm+news
                    print ('Tuition is ${:,.2f}.'.format(tue))    
                        
                if eng!= 'yes' :
                    
                    
                    if cred >= 12 and cred <= 18:
                        tue= 7410+asmsu+fm+news 
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*494)+asmsu+fm+news
                    elif cred<6:
                        tue= asmsu+fm+(cred*494) 
                    elif cred<=4:
                        tue= (cred*494)+asmsu+fm    
                    elif cred>18:
                        tue= 7410+(cred*494)+asmsu+fm+news
                    print ('Tuition is ${:,.2f}.'.format(tue))    
                if james=='yes':
                    if cred >= 12 and cred <= 18:
                        tue= 7410+asmsu+fm+news+7.50 
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*494)+asmsu+fm+news+7.50
                    elif cred<6:
                        tue= asmsu+fm+(cred*494)+7.50 
                    elif cred<=4:
                        tue= (cred*494)+asmsu+fm+7.50    
                    elif cred>18:
                        tue= 7410+(cred*494)+asmsu+fm+news+7.50
                    print ('Tuition is ${:,.2f}.'.format(tue))
                
            if lev == "junior":
                
               if eng == 'yes' or cmse == "yes": 
                
                   if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+ 670
                   elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+670
                   elif cred<6:
                        tue= asmsu+fm+(cred*555)+670
                   elif cred<=4:
                       tue=  asmsu+fm+(cred*555)+402
                   elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+670
                   print ('Tuition is ${:,.2f}.'.format(tue)) 
               if james =='yes':
                    if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+news+7.50 
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+7.50
                    elif cred<6:
                        tue= asmsu+fm+(cred*555)+7.50 
                    elif cred<=4:
                        tue= (cred*555)+asmsu+fm+7.50    
                    elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+7.50
                    print ('Tuition is ${:,.2f}.'.format(tue))
                
               if college == 'business':
                    
                    if cred >= 12 and cred <= 18:
                        tue= 8595+asmsu+fm+ 226 + news
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+226
                    elif cred<6:
                        tue= asmsu+fm+(cred*555)+226
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*555)+113
                    elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+226
                    print ('Tuition is ${:,.2f}.'.format(tue))  
                        
               if college == 'health':
                    
                    if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+100
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+100
                    elif cred<6:
                        tue= asmsu+fm+(cred*555)+100
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*555)+50
                    elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+100
                    print ('Tuition is ${:,.2f}.'.format(tue))    
                
               if college ==  'sciences':
                    if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+100
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+100
                    elif cred<6:
                        tue= asmsu+fm+(cred*555)+100
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*555)+50
                    elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+100
                    print ('Tuition is ${:,.2f}.'.format(tue))
                    
            if lev == "senior":
               
               if college == "engineering": 
                    
                   if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+ 670
                   elif cred<= 12 and cred>=6 :
                        tue= (cred*555)+asmsu+fm+news+670
                   elif cred < 6:
                        tue= asmsu+fm+(cred*573)+670
                        
                   elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+670
                        
                   print ('Tuition is ${:,.2f}.'.format(tue))
                   break
               
               if james=='yes':
                    if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+news+7.50 
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+7.50
                    elif cred<6:
                        tue= asmsu+fm+(cred*555)+7.50 
                    elif cred<=4:
                        tue= (cred*555)+asmsu+fm+7.50    
                    elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+7.50
                    print ('Tuition is ${:,.2f}.'.format(tue))
                
               if college == 'business':
                    
                    if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+ 226
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+226
                    elif cred<6:
                        tue= asmsu+fm+(cred*555)+226
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*555)+113
                    elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+226
                    print ('Tuition is ${:,.2f}.'.format(tue))  
                        
               if college == 'health':
                    
                    if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+100
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+100
                    elif cred<6:
                        tue= asmsu+fm+(cred*555)+100
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*555)+50
                    elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+100
                    print ('Tuition is ${:,.2f}.'.format(tue))    
                
               if college ==  'sciences':
                    if cred >= 12 and cred <= 18:
                        tue= 8325+asmsu+fm+100
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*555)+asmsu+fm+news+100
                    elif cred<6:
                        tue= asmsu+fm+(cred*555)+100
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*555)+50
                    elif cred>18:
                        tue= 8325+(cred*555)+asmsu+fm+news+100
                    print ('Tuition is ${:,.2f}.'.format(tue))        
            break
                        
                        
                        
    while in_str != 'yes':      #calculations in while loop for non residents
            
                        
            if lev == 'freshman' or lev=='sophomore' :
               
                
                if eng == 'yes' :
                    
                    if cred >= 12 and cred <= 18:
                        tue= 19883+asmsu+fm+ 670+news+750
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*1325.50)+asmsu+fm+news+670+news+750
                    elif cred<6:
                        tue= (cred*1325.50)+asmsu+fm+670+750
                    elif cred<=4:
                        tue= (cred*1325.50)+asmsu+fm+402+375
                    elif cred>18:
                        tue= 19883 +(extra_cred*1325.50)+670+news+750 +asmsu + fm
                    print ('Tuition is ${:,.2f}.'.format(tue))
                    break
                        
                if eng!= 'yes':
                    if cred >= 12 and cred <= 18:
                        tue = 19883+asmsu+fm+news+750
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*1325.50)+asmsu+fm+news+750
                    elif cred<6:
                        tue= (cred*1325.50)+asmsu+fm+750
                    elif cred<=4:
                        tue= (cred*1325.50)+asmsu+fm+402 +375   
                    elif cred>18:
                        tue= 19883+(cred*1325.50)+750
                    print ('Tuition is ${:,.2f}.'.format(tue))
                
                if james=='yes':
                    if cred >= 12 and cred <= 18:
                        tue= 19883+asmsu+fm+news+7.50+750 
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*1325.50)+asmsu+fm+news+7.50+750
                    elif cred<6:
                        tue= asmsu+fm+(cred*1325.50)+7.50 +750
                    elif cred<=4:
                        tue= (cred*1325.50)+asmsu+fm+7.50+375    
                    elif cred>18:
                        tue= 19883+(cred*1325.50)+asmsu+fm+news+7.50+750        
                    print ('Tuition is ${:,.2f}.'.format(tue))
                        
            
        
                
            if lev=='senior'or lev=='junior':
               
                
               if college =='engineering':
                  
                
                   if cred >= 12 and cred <= 18:
                        tue= 20786+asmsu+fm+ 670+750
                   elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*1366.75)+asmsu+fm+news+670+750
                   elif cred <6:
                        tue= asmsu + fm +(cred*1385.75) + 670 + 750
                   
                   elif cred>18:
                        tue= 20786+(cred*1385.75)+asmsu+fm+news+670
                        
                   print ('Tuition is ${:,.2f}.'.format(tue))
                   break 
                
               if james=='yes':
                    if cred >= 12 and cred <= 18:
                        tue= 20501+asmsu+fm+news+7.50 +750
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*1366.75)+asmsu+fm+news+7.50+750
                    elif cred<6:
                        tue= asmsu+fm+(cred*1366.75)+7.50 +750
                    elif cred<=4:
                        tue= (cred*1366.75)+asmsu+fm+7.50+375    
                    elif cred>18:
                        tue= 20501+(cred*1366.75)+asmsu+fm+news+7.50+750
                    print ('Tuition is ${:,.2f}.'.format(tue)) 
                
               if college == 'business':
                    
                    if cred >= 12 and cred <= 18:
                        tue= 20786+asmsu+fm+ 226+750
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*1385.75)+asmsu+fm+news+226+750
                    elif cred<6:
                        tue= asmsu+fm+(cred*1385.75)+226+750
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*1385.75)+113+375
                    elif cred>18:
                        tue= 20786+(cred*1385.75)+asmsu+fm+news+226+750
                    print ('Tuition is ${:,.2f}.'.format(tue))    
                        
               if college == 'health':
                    
                    if cred >= 12 and cred <= 18:
                        tue= 20501+asmsu+fm+100+750
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*1366.75)+asmsu+fm+news+100+750
                    elif cred<6:
                        tue= asmsu+fm+(cred*1366.75)+100+750
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*1366.75)+50+375
                    elif cred>18:
                        tue= 20501+(cred*1366.75)+asmsu+fm+news+100+750
                    print ('Tuition is ${:,.2f}.'.format(tue))    
                        
                
               if college ==  'sciences':
                    if cred >= 12 and cred <= 18:
                        tue= 20501+asmsu+fm+100+750
                    elif cred<= 12 and cred>=6 :
                        
                        tue= (cred*1366.75)+asmsu+fm+news+100+750
                    elif cred<6:
                        tue= asmsu+fm+(cred*1366.75)+100+750
                    elif cred<=4:
                       tue=  asmsu+fm+(cred*1366.75)+50+375
                    elif cred>18:
                        tue= 8325+(cred*1366.75)+asmsu+fm+news+100+750
                    print ('Tuition is ${:,.2f}.'.format(tue))    
                        
                        
    calc=input('Do you want to do another calculation (yes/no): ').lower()
    if calc != "yes":
        break
    
    
