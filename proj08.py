''' Your header goes here '''

import csv
# import pylab
from operator import itemgetter
import collections

def open_file():
    while True:
        filename = input("Enter filename: ")
        try:
            fp = open(filename, encoding='utf - 8')
            return fp;
            break;
        except FileNotFoundError:
            print("File not found! Please try again!")
            open_file()

pass


def read_file(fp):
    c = csv.reader(fp)
    i = 0
    D1 = {}
    D2 = {}
    D3 = {}
    for line in c:
        i = i + 1
        if i > 1:
            name = line[0].lower().strip()
            platform = line[1]
            try:
                year = int(line[2])
                na_sales = float(line[5]) * 1000000
                europe_sales = float(line[6]) * 1000000
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

    D4 = {}
    D5 = {}
    D6 = {}
    D7 = {}
    D8 = {}
    D9 = {}

    for key in sorted(D1.keys()):
        D4[key] = D1[key]

    for key in D4:
        l1 = []
        for val in D4[key]:
            l1.append(val)
        l1.sort(reverse=True)
        D5[key] = l1

    # print(D5)

    for key in sorted(D2.keys()):
        D6[key] = D2[key]

    for key in D6:
        l1 = []
        for val in D6[key]:
            l1.append(val)
        l1.sort(reverse=True)
        D7[key] = l1

    # print(D7)

    for key in sorted(D3.keys()):
        D8[key] = D3[key]

    for key in D8:
        l1 = []
        for val in D8[key]:
            l1.append(val)
        l1.sort(reverse=True)
        D9[key] = l1

    # print(D9)

    return D5,D7,D9

pass


def get_data_by_column(D1, indicator, c_value):

    if not c_value or c_value == '':
        return []

    l1 = []
    if indicator == 'year':
        for key in D1:
            # l1 = []
            for val in D1[key]:
                if val[2] == int(c_value):
                    l1.append(val)

        l2 = sorted(l1, key=lambda x: int(x[5]), reverse=True)
        l3 = sorted(l2, key=lambda x: int(x[1]))
        # print(l3)
        return l3

    if indicator == 'platform':
        for key in D1:
            # l1 = []
            for val in D1[key]:
                if val[1] == int(c_value):
                    l1.append(val)
        l2 = sorted(l1, key=lambda x: int(x[5]), reverse=True)
        l3 = sorted(l2, key=lambda x: int(x[2]))
    return l3



def get_publisher_data(D3, publisher):
    l1 = []
    for key in D3:
        # l1 = []
        for val in D3[key]:
            if val[0] == publisher:
                l1.append(val)

    return l1


def display_global_sales_data(L, indicator):

    # if indicator == 'year':
    #     for e in L:
    #         if e[2] ==


    header1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
    header2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']

    pass


def get_genre_data(D2, year):
    D = {}
    for k in D2.keys():
        for e in D2[k]:
            if e[1] == year:
                if not e[1] in D:

                    tup = (e[0], 1, e[2],e[3],e[4],e[5],e[6])
                    D[e[0]] = {tup}

                else:
                    tup = D[e[0]]
                    tup = (tup[0], tup[1] + 1, tup[2] + e[2], tup[3] + e[3] + tup[4] + e[4] + tup[5] + e[5] + tup[6] + e[6])
                    D[e[0]] = tup

    # print(D);
    return D

    pass


def display_genre_data(genre_list):


    header = ['Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    print(header)
    for e in genre_list:
        print(e[0], e[2],e[3],e[4],e[5],e[6])

    pass


def display_publisher_data(pub_list):
    '''
        WRITE DOCSTRING HERE!
    '''
    pub = pub_list[0][0]
    header = ['Title', 'North America', 'Europe', 'Japan', 'Other', 'Global']

    pass


def get_totals(L, indicator):
    l1 =[]
    l2 = []
    if indicator == 'year':
        for e in L:
            l1.append(e[1])
            l2.append(e[5])
            return l1,l2
    elif indicator == 'platform':
        for e in L:
            l1.append(e[2])
            l2.append(e[5])
            return l1,l2


def prepare_pie(genres_list):
    l1=[]
    l2=[]
    for e in genres_list:
        l1.append(genres_list[0])
        l2.append(genres_list[6])

    return l1,l2


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

    # if indicator == 'year':
    #     pylab.title("Video Game Global Sales in {}".format(value))
    #     pylab.xlabel("Platform")
    # elif indicator == 'platform':
    #     pylab.title("Video Game Global Sales for {}".format(value))
    #     pylab.xlabel("Year")
    #
    # pylab.ylabel("Total copies sold (millions)")
    #
    # pylab.bar(x, y)
    # pylab.show()


def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.

        parameters:
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order
            year: the year of the genre data (int)

        Returns: None
    '''

    # pylab.pie(values, labels=genre, autopct='%1.1f%%')
    # pylab.title("Video Games Sales per Genre in {}".format(year))
    # pylab.show()


def main():
    # Menu options for the program
    MENU = '''Menu options

    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit

    Enter choice: '''

    fp = open_file()
    (D1, D2, D3) = read_file(fp)

    choice = input(MENU)
    # print(choice)
    # if choice == '1':
    #     print("c 1")
    #     fp = open_file()
    #     (D1, D2, D3) = read_file(fp)
    #     l1 = get_data_by_column(D1, 'year', 1980)
    #     print("l1 is : ")
    #     print(l1)

    while choice != '5':

        # Option 1: Display all platforms for a single year
        if choice == '1':
            try:
                year = input('Enter year: ')
                if not isinstance(int(year), int):
                    raise ValueError
                print(get_data_by_column(D1, 'year', year))
                get_genre_data(D2, 1980)
                p = input('Do you want to plot (y/n)? ')
                if p == 'y':
                    plot_global_sales()
                else:
                    choice = input(MENU)
                # if the list of platforms for a single year is empty, show an error message

            except ValueError:
                print("Invalid year.")

        if choice == '2':
            try:
                platform = input('Enter platform: ')
                if isinstance(platform, int):
                    raise ValueError
                print(get_data_by_column(D1, 'platform', platform))
                p = input('Do you want to plot (y/n)? ')
                if p == 'y':
                    l = get_totals()
                    plot_global_sales()
                else:
                    choice = input(MENU)
                # if the list of platforms for a single year is empty, show an error message
                pass

            except ValueError:
                print("Invalid plaform.")

        if choice == '3':
            try:
                year = input('Enter year: ')
                if not isinstance(int(year), int):
                    raise ValueError
                print(get_genre_data(D2, year))
                p = input('Do you want to plot (y/n)? ')
                if p == 'y':
                    plot_genre_pie()
                # if the list of platforms for a single year is empty, show an error message
                else:
                    choice = input(MENU)

            except ValueError:
                print("Invalid year.")

        if choice == '4':
            try:
                year = input('Enter year: ')
                if not isinstance(year, int):
                    raise ValueError
                print(get_data_by_column(D1, 'year', year))
                p = input('Do you want to plot (y/n)? ')
                if p == 'y':
                    plot_global_sales()
                # if the list of platforms for a single year is empty, show an error message
                else:
                    choice = input(MENU)

            except ValueError:
                print("Invalid year.")

            # Option 4: Display publisher data

            # Enter keyword for the publisher name

            # search all publisher with the keyword
            # match = []
            #
            # # print the number of matches found with the keywords
            # if len(match) > 1:
            #     print("There are {} publisher(s) with the requested keyword!".format(len(match)))
            #     for i, t in enumerate(match):
            #         print("{:<4d}{}".format(i, t[0]))
            #
            #     # PROMPT USER FOR INDEX
            #
            # else:
            #     index = 0



    print("\nThanks for using the program!")
    print("I'll leave you with this: \"All your base are belong to us!\"")


if __name__ == "__main__":
    main()