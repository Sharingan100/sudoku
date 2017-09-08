
'''
Exercise6.1: Coding the Solution

Time to code the final solution! Finish the code in the function search, 
which will create a tree of possibilities and traverse it using DFS until it finds a solution for the sudoku puzzle.
'''
#1. utils.py ----------------------------
#1.1 define rows: 
rows = 'ABCDEFGHI'

#1.2 define cols:
cols = '123456789'

#1.3 cross(a,b) helper function to create boxes, row_units, column_units, square_units, unitlist
def cross(a, b):
    return [s+t for s in a for t in b]

#1.4 create boxes
boxes = cross(rows, cols)

#1.5 create row_units
row_units = [cross(r, cols) for r in rows]

#1.6 create column_units
column_units = [cross(rows, c) for c in cols]

#1.7 create square_units for 9x9 squares
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]

#1.8 create unitlist for all units
unitlist = row_units + column_units + square_units

#1.9 create peers of a unit from all units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

#1.10 display function receiving "values" as a dictionary and display a 9x9 suduku board
def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    
    ''' Your solution here 
    .........
    .........
    .........
    .........
    .........
    .........
    '''
    
    values = {}
    count_row = 0
    for i in range(0, len(grid), 3):
        word = grid[i : i + 3] #..3
        for j in range(len(word)):

            key = rows[count_row] + cols[( i + j ) % 9]
            
            
            values[key] = cols if (word[j] == '.') else word[j]
            
        if (i % 9 == 6 and i != 0 ):
            count_row += 1

    return values


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    
    ''' Your solution here 
    .........
    .........
    .........
    .........
    .........
    .........
    '''
    
    def eliminate0(dat):
        const = []
        elem = {}
        for value in dat:
            
            for x in value:
                if (len(values[x]) == 1):
                    const.append(values[x])
                else:
                    elem[x] = values[x]
            
            for x in const:
                elem = { key:value.replace(x, '') for key, value in elem.items() }
            
            const2 = []
            for x in value:
                if len(values[x]) == 1:
                    if values[x] in const2:
                        elem.update({x: ''})
                    const2.append(values[x])
                
            values.update(elem)
            const = []
            elem = {}
            
#        print(values)
        return values
        
    values.update(eliminate0(row_units))
    values.update(eliminate0(column_units))
    values.update(eliminate0(square_units))
    
    return values


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    
    ''' Your solution here 
    .........
    .........
    .........
    .........
    .........
    .........
    '''

    for square in square_units:
        elem = []
        checker = set()
        unit = {}
        
#        keep value inside dict which len != 1
        for key in square:
            
#            convert str to set
#            convet set to list
#            print('=============values[key]')
#            print(values[key])
    
            if len(values[key]) != 1:
#            append every lists together
                unit.update({key:values[key]})
                value = set(values[key])
                checker = checker.union(value)
                elem += list(value)
         
        for x in checker:
#            find value occurs once
            if (elem.count(x) == 1):
#                find that value occurs inside unit dict
                for key2, value2 in unit.items():
                    if (value2.find(x) != -1):
#                        update values dict to x
                        values.update({key2 : x})
                
        
        
    return values
    
    
def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    
    ''' Your solution here 
    .........
    .........
    .........
    .........
    .........
    .........
    '''
    
#    count = 0
    compare_values = {}
    compare_values.update(values)
    processing_values = {}
    
    processing = True
    while processing:
        processing_values.update(eliminate(compare_values))
        processing_values.update(only_choice(processing_values))
#        print('======================processing_values')
#        print(processing_values)
#        print('======================compare_values')
#        print(compare_values)
        
        if (compare_values == processing_values):
            processing = False
        compare_values.update(processing_values)
#        count += 1
#        print(count)
    values.update(compare_values)
    return values  

#2. function.py ----------------------------
# 2.1 implement search() using Depth First Search Algorithm
#from utils import *
def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    # Search and Choose one of the unfilled squares with the fewest possibilities
    # Now use recursion to solve each one of the resulting sudokus, 
    # and if one returns a value (not False), return that answer!
    
    ''' Your solution here 
    .........
    .........
    .........
    .........
    .........
    .........
    '''

    final_ans = {}
    
    def dfs(current_key, count):
        if (current_key > 80):
            return False

        choices = values[boxes[current_key]]
        back_up = {}
        back_up.update(values)
#        display(values)
#        x = input()
        for choice in choices:
            
            values[boxes[current_key]] = choice
            values.update(reduce_puzzle(values))
            if dfs(current_key + 1, count +1):
                return True
            values.update(back_up)
            
        if count == 80:
            final_ans.update(values)
            return True

    dfs(0, 0)
    return final_ans
    
    

    
#3. Test utils.py ----------------------------  
grid_easy = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
grid_hard = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values = grid_values(grid_hard)
#values = grid_values(grid_easy)
print("The original Sudoku board is **********************************************")
display(values)

#4. Test function.py ----------------------------  
new_values = search(values)
print("\n")
print("After applying Depth First Search Algorithm *****************")
display(new_values)