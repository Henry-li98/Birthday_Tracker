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

#sometimes when calling the subfunction of the class itll edit the class and other times it'll jsut spit out a raw value look at documentation on which of these 2 event occurs in the case of line 21 it can change the underlying value but it doesnt
df = pd.DataFrame(worksheet.get_all_records())
def bday_datetime(entry):
    datetime_entry = datetime.strptime(str(entry), "%m/%d")
    return datetime_entry
def bday_sort(bday_series):
    bday_output = bday_series.map(bday_datetime) #alternative is using: lambda entry:datetime.strptime(entry,"%m/%d"))
    # print(f"This is a {bday_output=}")
    return bday_output

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
        df.loc[len(df)] = [name, entry_date]
        # figure out how exactly above actually made an entry to last index
    else:
        print("invalid input, type in yes or no")

df_sorted = df.sort_values(by='Birthday', key=bday_sort)

print(df_sorted)

worksheet.clear()
worksheet.update([df_sorted.columns.values.tolist()] + df_sorted.values.tolist())
# print(f"{[df_sorted.columns.values.tolist()]=}")
# print(f"{df_sorted.values.tolist()=}")
# print(f"{([df_sorted.columns.values.tolist()] + df_sorted.values.tolist())=}")

now = datetime.now()
# print(df_sorted.Birthday)
# print("this is the start of the test loop")
# df_sorted_dict = df_sorted.to_dict()
# df_names = df_sorted_dict['Name']
# df_birthdays = df_sorted_dict['Birthday']
# print(f"{df_sorted.to_dict(orient='split')}")
# print(f"{df_names=}")
# print(f"{df_birthdays=}")
df_sorted_dict = df_sorted.to_dict(orient='split')
paired_info = df_sorted_dict['data']
for pair in paired_info:
    cur_name = pair[0]
    cur_date = pair[1]

    strptime_date_string = cur_date + "/" + str(now.year)
    strptime_format = f"%m/%d/%Y"
    datetime_birthday = datetime.strptime(strptime_date_string, strptime_format)

    if now <= datetime_birthday:
        days_left = datetime_birthday - now
        print(f"In {days_left.days} days, {cur_name} has a birthday happening on {cur_date}")
        break

# after the last birthday, the next birthday function wont work until next year, fix this

# look into how would you might delete or search for a specific person within the list or give everyone within this month

#look into key value pairs and dictionaries




# in order to sort may have to split off the month and day in order to begin sorting


#list comprehension read into it

# for i in x:              ==========  z = [i+1 for i in x]
#     y.append(i + 1)

