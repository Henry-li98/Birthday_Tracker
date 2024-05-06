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
# within the def() the () is an argument
# use functions to streamline and conceptualizes the code
def bday_datetime(entry):
    datetime_entry = datetime.strptime(str(entry), "%m/%d")
    return datetime_entry
def bday_sort(bday_series):
    bday_output = bday_series.map(bday_datetime) #alternative is using: lambda entry:datetime.strptime(entry,"%m/%d"))
    print(f"This is a {bday_output=}")
    return bday_output
#sometimes when calling the subfunction of the class itll edit the class and other times it'll jsut spit out a raw value look at documentation on which of these 2 event occurs in the case of line 21 it can change the underlying value but it doesnt
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

df_sorted = df.sort_values(by='Birthday', key=bday_sort)
print(df_sorted)

worksheet.clear()
worksheet.update([df_sorted.columns.values.tolist()] + df_sorted.values.tolist())
print(f"{[df_sorted.columns.values.tolist()]=}")
print(f"{df_sorted.values.tolist()=}")
print(f"{([df_sorted.columns.values.tolist()] + df_sorted.values.tolist())=}")

#how would you might delete or search for a specific person within the list or give everyone within this month

#look into key value pairs and dictionaries