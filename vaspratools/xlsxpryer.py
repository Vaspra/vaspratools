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