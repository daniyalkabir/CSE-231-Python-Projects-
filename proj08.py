# -*- coding: utf-8 -*-
''' ###############################################################################
#                                                                             # 
#This assignment focuses on the usagae of dictionaries,lists and tuples to 
derive datat from the files and it also tests the knowlege about.csv reader. 
It is based on videogames. '''

import csv
import pylab
from operator import itemgetter


def open_file():    #open file function using the utf 8 encode
    while True:
        filename = input("Enter filename: ")
        try:
            fp = open(filename, encoding='utf - 8')
            return fp;
            break;
        except FileNotFoundError:
            print("File not found! Please try again!")




def read_file(fp):
    '''This function takes into account the file pointer and then
    returns the three dictionaries that are required for processing the
    file further.'''
    c = csv.reader(fp)
    i = 0
    D1 = {}
    D2 = {}
    D3 = {}
    for line in c:
        i = i + 1   
        if i > 1:   # creating a false statement
            name = line[0].lower().strip()  #according to instructions.
            platform = line[1].lower().strip()
            try:
                year = int(line[2])
                na_sales = float(line[5]) * 1000000
                europe_sales = float(line[6]) * 1000000 # according to need
                japan_sales = float(line[7]) * 1000000
                other_sales = float(line[8]) * 1000000
            except:
                continue
            genre = line[3].lower().strip()
            publisher = line[4].lower().strip()

            global_sales = na_sales + europe_sales + japan_sales + other_sales
            tup1 = (name, platform, year, genre, publisher, global_sales)
            if name not in D1:
                D1[name] = [tup1]
            else:
                D1[name].append(tup1)
            tup2 = (genre, year, na_sales, europe_sales, japan_sales, other_sales, global_sales)
            if genre not in D2:
                D2[genre] = [tup2]
            else:
                D2[genre].append(tup2)
            tup3 = (publisher, name, year, na_sales, europe_sales, japan_sales, other_sales, global_sales)
            if publisher not in D3:
                D3[publisher] = [tup3]
            else:
                D3[publisher].append(tup3)
    Z2 = {}
    Z3 = {}
    Z1 = {}



    for key in sorted(D1):      # sorting values according to the requirment
        Z1[ key ] = sorted(D1[ key ], key=itemgetter(5),reverse=True)
    for key in sorted(D2):
        Z2[ key ] = sorted(D2[ key ], key=itemgetter(6),reverse=True)
    for key in sorted(D3):
        Z3[ key ] = sorted(D3[ key ], key=itemgetter(7),reverse=True)

    return Z1,Z2,Z3


def get_data_by_column(D1, indicator, c_value):
    '''This function goes t through the dictionary D1 and analyzes the data
    inferred and returns the value of the global value sales in the form of 
    tuples.'''
    
    if not c_value or c_value == '':
        return []

    l1 = []
    if indicator == 'year':
        for key in D1:
            # l1 = []
            for val in D1[key]:
                if val[2] == int(c_value):
                    l1.append(val) # appending the values

        l2 = sorted(l1, key=itemgetter(5), reverse=True)
        l3 = sorted(l2, key=itemgetter(1))
        #print(l3)
        return l3#returning the values

    if indicator == 'platform':
        for key in D1:
            # l1 = []
            for val in D1[key]:
                if val[1] == c_value:
                    l1.append(val)
        l2 = sorted(l1, key=itemgetter(5), reverse=True)
        l3 = sorted(l2, key=itemgetter(2))
   # print(l3)
    return l3 # return appropriate values.



def get_publisher_data(D3, publisher):
    '''This function shall go through d3 and get the values we need in this 
    function it happens to be list of tuples'''
    l1 = []
    for key in D3:  #using dictionary to ectract key from d3
        # l1 = []
        for val in D3[key]:
            if val[0] == publisher:
                l1.append(val)
    l1.sort(key=itemgetter(1))
    l1.sort(key=itemgetter(7),reverse=True)
    return l1




def display_global_sales_data(L, indicator):
    
    
    c = 0


    if indicator=='year':
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Platform', 'Genre', 'Publisher', 'Global Sales'))
        for v in L:
            c += v[5]
            n=v[0][0:25]    #slicing the values according to hintsd
            p=v[1]
            g=v[3][0:15]
            pu=v[4][0:25]

            print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format(n,p,g,pu,v[5]))

        print('\n')
        print("{:90s}{:<12,.02f}".format('Total Sales',c))
    else:
        print("{:30s}{:10s}{:20s}{:30s}{:12s}".format('Name', 'Year', 'Genre', 'Publisher', 'Global Sales'))
        for v in L:
            c += v[5]
            n=v[0][0:25]# sorting according to the slicing
            g=v[3][0:25]
            pu=v[4][0:25]

            print("{:30s}{:<10}{:20s}{:30s}{:<12,.02f}".format(n,v[2], g, pu,v[5]))

        print('\n')
        print("{:90s}{:<12,.02f}".format('Total Sales', c))


def get_genre_data(D2, year):
    D = {}
    for k in D2.keys():
        for e in D2[k]:
            if e[1] == year:
                if not e[0] in D:

                    tup = (e[0], 1, e[2],e[3],e[4],e[5],e[6])
                    D[e[0]] = tup

                else:
                    tup = D[e[0]]
                    tup = (tup[0], int(tup[1]) + 1, tup[2] + e[2], tup[3] + e[3] ,tup[4] + e[4] , tup[5] + e[5] , tup[6] + e[6])
                    D[e[0]] = tup
    l1=[]
    for k in D.values():
        l1.append(k)
    l1.sort()  # sorting according to the genre
    l1.sort(key=itemgetter(-1), reverse=True)
    return l1




def display_genre_data(genre_list):
    '''
    This function prints a table and evaluates data from of all data based on genre
    '''
    header=('Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global')
    e = 0
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(header[0],header[1],header[2],header[3],header[4],header[5]))

    for v in genre_list:
            genre = v[0][0:15]
            na = v[2]
            eur = v[3]
            jpn = v[4]
            other = v[5]
            glob = v[6]
            e += v[6]
            print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(\
                  genre, na, eur, jpn, other, glob))
    print("\n{:90s}{:<15,.02f}".format('Total Sales', e))

def display_publisher_data(pub_list):
    '''
        This table gives us a data of all regional sales per year based on the genre   '''

    header=('Title', 'North America', 'Europe', 'Japan', 'Other', 'Global')
    e = 0
    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(header[0],header[1],header[2],header[3],header[4],header[5]))

    for v in pub_list:
        title = v[1][0:25]#slicing the appropriate values.
        na = v[3]
        eur = v[4]
        jpn = v[5]
        other = v[6]
        glob = v[7]
        e += v[7]
        print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}".format(title, na, eur, jpn, other, glob))

    #printing the values according to the rquired format
    
    print("\n{:90s}{:<15,.02f}".format("Total Sales", e))



def get_totals(L, indicator):
    '''This function has to taake the list from data_ column and then by
    by processing we get a list of tuples and the indicator '''


    l1 =[]      # creating empty values.
    l2 = []
    dict1={}
    if indicator == 'year':
        for e in L:
            if e[1] not in dict1:
                dict1[e[1]]=e[5]
            else:
                dict1[e[1]]+=e[5]
        l1 = sorted(dict1)
        for k in l1:
            l2.append(dict1[k])
        return l1, l2
    elif indicator == 'platform':
        for year in L:
            if year[2] not in dict1:
                dict1[year[2]] = year[5]
            else:
                dict1[year[2]] += year[5]
        l1 = sorted(dict1)
        for k in l1:
            l2.append(dict1[k])
        return l1, l2

def prepare_pie(genres_list):
    '''
     This function take slist adn genres_list from a function and then returns
     new lists based on the genre and global sale   
    '''
    L = []
    for genre in genres_list:
        L.append((genre[0], genre[6]))

    L.sort(key = itemgetter(1), reverse = True)
    # appending values to list
    List_A = []
    List_B = []
    for v in L:
        List_A.append(v[0])
        List_B.append(v[1])

    return List_A , List_B



def plot_global_sales(x, y, indicator, value):
    '''
        This function plots the global sales per year or platform.

        parameters:
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)

        Returns: None
    '''
    if indicator == 'year':
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")

    pylab.ylabel("Total copies sold (millions)")

    pylab.bar(x, y)
    pylab.show()


def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.

        parameters:
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order
            year: the year of the genre data (int)

        Returns: None
    '''

    pylab.pie(values, labels=genre, autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()


def main():
    ''' This function makes use of all the other functions. '''
    
    fp = open_file()
    D1, D2, D3 = read_file(fp)
    # Menu options for the program
    MENU = '''Menu options
    
    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit
    
    Enter choice: '''
    start = ''
    
    while start != '5':
        
        #continue the loop till option is not eqyual to 5
        
        choice = input(MENU)
        
        #Option 1: Display all platforms for a single year
        if choice=="1": 

            try:

               year=input("Enter year: ") 

                #if the list of platforms for a single year is empty, show an error message    

               data=get_data_by_column(D1,'year',int(year))
               if len(data)==0:
                   print("The selected year was not found in the data.")

               elif True:
                   print("\n{:^80s}".format("Video Game Sales in {}".format(year)))
                   
                   display_global_sales_data(data,'year')
                   
                   plot=input("Do you want to plot (y/n)? ")
                   
                   if plot=="y":
                       x,y = get_totals(data, "year")
                       plot_global_sales(x,y,"year", year)
            except TypeError:
                print("Invalid year.")
                    
        #Option 2: Display all year for a single platform
        elif choice == '2':
            try:
                global_sales_input = str(input("Enter platform: ")) # setting basics
                getdata = get_data_by_column(D1, 'platform', global_sales_input)
                if len(getdata) == 0:
                    print("The selected platform was not found in the data.")
                elif True:
                    print("\n{:^80s}".format("Video Game Sales for {}".format(global_sales_input)))
                    
                    display_global_sales_data(getdata, 'platform')
                    plot_input = input("Do you want to plot (y/n)? ")
                    if plot_input == 'y':
                        #incase user opts y
                        getdata1 , getdata2 = get_totals(getdata, 'platform')
                        plot_global_sales(getdata1, getdata2, 'platform', global_sales_input)
                    else:
                        continue    
            except ValueError:
                    print("Invalid platform.")
                    
        #Option 3: Display the regional sales for all video game genres
        elif choice == '3':
            try:
                genre_s = int(input("Enter year: ")) 
                
                genre_l = get_genre_data(D2, genre_s)
                
                if len(genre_l) ==0 :
                    print("The selected year was not found in the data.")
                elif True:
                    
                    print("\nRegional Video Games Sales per Genre")
                    display_genre_data(genre_l)
                    plot_input = input("Do you want to plot (y/n)? ")
                    if plot_input == 'y':
                        alpha , beta = prepare_pie(genre_l)
                        plot_genre_pie(alpha, beta, genre_s)
                    else:
                        continue  
            
            except ValueError:
                    print("Invalid year")
                    
        #Option 4: Display publisher data
        elif choice == '4':
            # Enter keyword for the publisher name
            pub = input("Enter keyword for publisher: ")
            
            # search all publisher with the keyword
            empty = []
            index_list = []
            for k, v in D3.items(): # enemurating the values
                if pub in k:
                    
                    empty.append(D3[k]) # according to pdf
            if len(empty) > 0:    
                print("There are {} publisher(s) with the requested keyword!".format(len(empty)))
                
                
                for alpha,beta in enumerate(empty):
                    
                    index_list.append((alpha,beta [0][0]))#appending the required alpha and beta
                    
                    
                    print("{:<4d}{}".format(alpha, beta[0][0]))
               
                index = int(input("Select the index for the publisher to use: "))
                
                for value in index_list:
                    if index == value[0]:
                        publisher_name = value[1]
                        pub_list = get_publisher_data(D3, publisher_name)
                        
                        print("\nVideo Games Sales for {}".format(publisher_name))
                        
                        display_publisher_data(pub_list)
                
            
            else:
                print('No publisher name containing "{}" was found!'.format(pub))
                continue
                
#        
        elif choice == '5':
            print("\nThanks for using the program!")
            print("I'll leave you with this: \"All your base are belong to us!\"")
            break           #to reloop the values
        
        else:
            print("Invalid option. Please Try Again!")
        
if __name__ == "__main__":      # running the main function.
    main()

