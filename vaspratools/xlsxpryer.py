"""
Created by Doug Lawrence - Github: Vaspra

Shortcuts for getting data out of spreadsheets, utilising openpyxl.
"""


def get_column(ws, col_index:str, last_row, return_cells=False):
    """
    Returns a list containing the values in the column of an openpyxl ws.
    
    Use return_cells=True for a list of cell references instead.
    """
    
    # Cast to int
    last_row = str(int(last_row))
    
    # Get the cells
    cell_ts = ws[col_index + '1' : col_index + last_row]
    cells = []
    for cell_t in cell_ts:
        cells.append(cell_t[0])
        
    # If only cells are needed, return them as a list
    if return_cells:
        return cells
    
    # Else, return the values in the cells as a list
    else:
        vals = []
        for cell in cells:
            vals.append(cell.value)
        return vals
    
    
def format_list_to_commastring(ls):
    """
    Converts and returns a list into a string, comma separated format.
    """
    
    string = ''
    for item in ls:
        string += str(item) + ','
    string = string.strip(',')
    
    return string


def fill_col_with_data_dict(ws, key_col, insert_col, data_dict,
                       exact_match=False, insert_col_name=''):
    """
    For each entry in 'data_dict', this function will look for the entry's
    key in all the cells of the column 'key_col'. If 'in' one of these cells
    (or '==' if given 'exact_match=True'), the entry's value will be inserted
    into the row's 'insert_col' cell.
    
    Forces a lower case comparison (tEsT == test == TEST), if not using
    'exact_match=True'
    
    If an 'insert_col_name' argument is provided, the column header will be
    set to this value.
    """
    
    assert key_col.isalpha,\
        '\'key_col\' (%s) argument must be alphabetic' % key_col
        
    assert insert_col.isalpha,\
        '\'insert_col\' (%s) argument must be alphabetic' % insert_col
    
    empties = 0
    inserts = 0
    unmatched = 0
    
    for row in range(1, len(ws[key_col]) + 1):           
        r = str(row)
        success = False 
        for key, value in data_dict.items():
            
            if not ws[key_col + r].value:
                print('Empty cell [%s]: %s'\
                      % (key_col + r, ws[key_col + r].value))
                empties += 1
                break
            
            if not exact_match:
                if key.lower().strip() in ws[key_col + r].value\
                                          .lower().strip():
                    ws[insert_col + r].value = value
                    inserts += 1
                    success = True
                    break
            else:
                if key == ws[key_col + r].value:
                    ws[insert_col + r].value = value
                    inserts += 1
                    success = True
                    break
        
        if ws[key_col + r].value and not success:          
            print('Unmatched cell [%s]: %s'\
                  % (key_col + r, ws[key_col + r].value))
            unmatched += 1
                
    if insert_col_name:
        ws[insert_col + '1'].value = insert_col_name
                
    print('\nInserted %d / %d data entries from dictionary into column: \'%s\''\
          % (inserts, len(ws[key_col]), insert_col))
    print('%d empty cells, %d unmatched cells'\
          % (empties, unmatched))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
                
                
                
                
                
                
                