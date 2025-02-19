import gspread
from google.oauth2.service_account import Credentials
SERVICE_ACCOUNT_FILE = '/Users/abdussami/Desktop/repo/Repo@2/transitioning/ignore_files/chaya-445400-c43c889bec6f.json' 
SCOPES = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(credentials)

#-------*--*---------------*-----*--------------*--------------**-----------*--------------------#

def order_values(spreadsheet_name,worksheet_name):
    spreadsheet = client.open(spreadsheet_name)
    worksheet = spreadsheet.worksheet(worksheet_name)
    data = worksheet.get_all_values()
    ##MOST IMPORTANT LINE OF CODE:
    nested_ = [[n[(c_)-2],n[(c_)-1], [data.index(n),c_]]    
        for n in data for c_,i in enumerate(n) if i == '-']
    return nested_


