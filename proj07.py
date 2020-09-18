''' Your header goes here '''
import csv
from operator import itemgetter



def open_file():
    '''This functions accepts no input but helps us to open the file and return
    the file pointer that can be used in teh enxt function'''
    while True:  # we create a loop which will use try except
        file = input('Enter filename: ')  # taking the input

        try:
            fp = open(file)

            break

        except:
            FileNotFoundError
            print("File not found! Please try again!")  # print error message
        continue  # reloop if the input is not correct.

    return fp


def calc_multipliers():
    ''' Docstring goes here '''
    mult = []
    for n in range(2, 61):
        mult.append(1 / ((n * (n - 1)) ** 0.5))

    return mult


def calc_priorities(s, p, m):
    ''' Docstring goes here '''
    mult = []
    for z in range(len(m)):
        mult.append((int(m[z] * p), s))

        mult.sort(reverse=True)
    return mult


def read_file_make_priorities(fp, multipliers):
    ''' Docstring goes here '''
    reader = csv.reader(fp)
    next(reader)
    list1 = []
    list2 = []
    state_reps = []
    priorities = []

    for line in reader:
        s = line[1].strip().strip('"')
        p = line[2]
        if s == 'District of Columbia' or s == 'Puerto Rico':
            continue
        list1.append([s,1])
        list2+=calc_priorities(s,int(line[2]),multipliers)


    list1.sort()
    res = sorted(list2, key=itemgetter(0),reverse=True)
    return list1,res[:386]


def add_to_state(state, states):
    ''' Docstring goes here '''
    for item in states:
        if item[0] == state:
            item[1] = int(item[1])+1


def display(states):
    ''' Docstring goes here '''
    print("State          Representatives")
    for item in states:
        print("{:<15s}{:>4d}".format(item[0],item[1]))


def main():
    ''' Docstring goes here '''
    fp=open_file()
    multipliers=calc_multipliers()
    state_reps,priorities=read_file_make_priorities(fp, multipliers)


    for item in priorities:
       add_to_state(item[1], state_reps)

    display(state_reps)






if __name__ == "__main__":
    main()