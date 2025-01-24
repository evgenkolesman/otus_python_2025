import ast

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

list = input()
raws = input()
#rowsNeeded = input()
try:
    list = ast.literal_eval(list)
    raws = int(raws)
    rowIndex = None
    for row  in list:
        freeSeats = 0
        for seat in row:
            if (seat == 0):
                freeSeats += 1
                if freeSeats >= raws:
                    rowIndex = list.index(row) + 1
                    break
            else:
                freeSeats = 0
        if(rowIndex != None):
            print(rowIndex)
            break
    if(rowIndex == None):
        print("Cannot find free sets in raw as you wish")
except ValueError:
    print("False")