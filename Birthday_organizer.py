import gspread
import pandas as pd
import re
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name('Sheet_access.json', scope)
client = gspread.authorize(cred)
sheet = client.open("Birthday_list")
worksheet = sheet.worksheet('Sheet1')
# lambda is an instance function
# usually used when needing to pass a function to another function
# defs is the keyword used to make a function
def bday_sort(bday_series):
    bday_series.apply(bday_datetime) #alternative is using: lambda entry:datetime.strptime(entry,"%m/%d"))
    print("this is the output of bday series")
    print(bday_series)
    return sorted(bday_series)
def bday_datetime(entry):
    datetime_entry = (datetime.strptime(entry,"%m/%d"))
    return datetime_entry

df = pd.DataFrame(worksheet.get_all_records())

while True:
    print(df)
    response = input("Here is the current list, is there more names that need to be added? (yes/no): ").lower()
    if response == 'no':
        break
        print("no additional data added")
    elif response == 'yes':

        name = input("enter name of the person ")
        birthday = input("enter the birthday date (MM/DD) ")
        month,day = birthday.split('/')
        entry_date = f"{int(month):02d}/{int(day):02d}"
        # entry_datetime = datetime.strptime(entry_date, "%m/%d") # returns a bunch of date objects and can sort those objects
        # entry_new_row = pd.Series(data=[name, entry_datetime], index=df.columns)
        df.loc[len(df)] = [name, entry_date]

    else:
        print("invalid input, type in yes or no")


print(df.sort_values(by='Birthday', key=bday_sort))