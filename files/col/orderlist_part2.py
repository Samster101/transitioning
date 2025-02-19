from orderlist_ import order_values, client, credentials
from extract_digits import extract_digits
sheet_= "CHAYA ATTEMPT 1"
worksheet_= "sheet_without"
worksheet_2 = "sheet_with #"
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def get_cell_position(sheet_,worksheet_):
    list_ = order_values(sheet_,worksheet_)
    lwst = [n[2] for n in list_]
    cell_list = [letters[n[1]] + str((n[0]+1)) for n in lwst]
    stock_amount_list = [c[1] for c in list_]
    return cell_list,stock_amount_list,list_ 



def try_zoom_func(n,data):
    try:
        a__ = data[n][0]
        return data[n][0][0]
    except:
        return None


def get_numbers(x,y,cell_list):
    spreadsheet = client.open(x)
    worksheet = spreadsheet.worksheet(y)
    data_ = worksheet.batch_get(cell_list)
    return data_


def combine_list(list__,data_,sst):
    lst = extract_digits([try_zoom_func(n,data=data_) for n,c in enumerate(data_)])
    sst_ = extract_digits([n for n in sst])
    get_numbs = [[list__[n][0],sst_[n],lst[n]] for n in range(len(list__))]
    return get_numbs


def stock_sheet_entry(): 
    function_list =  get_cell_position(sheet_=sheet_,worksheet_=worksheet_)
    stock_cell_data = get_numbers(x=sheet_, y=worksheet_2,cell_list=function_list[0])
    return (combine_list(function_list[2],stock_cell_data,function_list[1]))


    


