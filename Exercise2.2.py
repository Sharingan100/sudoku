'''
Exercise2.2: implement eliminate()

Now, let's finish the code for the function eliminate(), which will take as input a puzzle in dictionary form. 
The function will iterate over all the boxes in the puzzle that only have one value assigned to them, 
and it will remove this value from every one of its peers.

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
            

#2. function.py ----------------------------
# 2.1 implement eliminate(values)
# from utils import *
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
#    
    def update_rows_cols(dat):
        const = []
        elem = {}
        rows_cols = rows + cols
        print(rows_cols)
            
        for char in dat:
    #        const = [value for key, value in values.items() if char in key and len()]
            for key, value in values.items():
                if char in key and len(value) == 1:
                  
                    const.append(value)
                
                if char in key and len(value) != 1:
                    elem[key] = value
    #        for item in const:
            for x in const:
                elem = {key:value.replace(x,'') for key, value in elem.items() }
            values.update(elem)
            print('===================const')
            print(const)
            print('===================elem')
            print(elem)
            print('===================values')
            print(values)
            const = []
            elem = {}
        return values
    values.update(update_rows_cols(rows))
    values.update(update_rows_cols(cols))
    
    const = []
    elem = {}
    for square in square_units:
        print('========================square')
        print(square)
        
        for x in square:
            print('========================value[x]')
            print(values[x])
            if (len(values[x]) == 1):
              const.append(values[x])  
            else:
                elem[x] = values[x]
        print('========================elem')
        print(elem)
        print('========================const')
        print(const)
        
        for x in const:
            elem = { key:value.replace(x, '') for key, value in elem.items() }
#            for key, value in elem:
#                values[key] = value.replace(x, '')
        values.update(elem)
        print('================values')        
        print(values)        
        const = []
        elem = {}
#                tmp = set(values[x])
#                intersection.add(tmp)
#        print('================intersection')
#        print(intersection)
    
    return values


    
            
            
    

#3. Test utils.py ----------------------------  
values = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
print("The original Sudoku board is **********************************************")
display(values)

#4. Test function.py ----------------------------  
eliminate(values)
print("\n")
print("After implement eliminate(values) method **********************************")
display(values)