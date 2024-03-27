# find a module or library that can read nad write off of google sheets for the birthdays and names
# create array to hold the birthday date and name (figure out the proper name of what it is
# use some algorithm that will organize the array by date
# later use this algo to compare to the current date to determine the next birthday
# find a module that interacts with windows notification, use it to display the next upcoming birthday thats coming when its within X days

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


#provides access to the Google sheets and drive in order to be able to interact and manipulate data
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# 'https://www.googleapis.com/auth/spreadsheets.readonly' , https://spreadsheets.google.com/feeds
cred = ServiceAccountCredentials.from_json_keyfile_name('Sheet_access.json', scope)

client = gspread.authorize(cred)

sheet = client.open("Birthday_list")

worksheet = sheet.worksheet('Sheet1')

df = pd.DataFrame(worksheet.get_all_records())

print(df)
while True:
    response = input("Here is the current list, is there more names that need to be added? (yes/no): ").lower()
    if response == 'no':
        break
        print("no additional data added")
    elif response == 'yes':
        name = input("enter name of the person ")
        date = input("enter the birthday date (MM/DD) ")
        new_row = {name, date}
        df.loc[len(df)] = new_row
        df = df.append(new_row, ignore_index=True)
    else:
        print("invalid input, type in yes or no")

print(user_input)
print(user_input2)
df = pd.DataFrame(worksheet.get_all_records())
# creating user input as an option to add more names and dates


# figure out how to add to the data frames and link both name and date together so when they get changed its moved together
# learn how to use bubblesort to organize the cells that are attached via names and dates and order them sequentially


# test adding then sorting the names
# find a module that can access the windows OS notifications feature


































#first error was forgetting to go into the google sheets itself and give it editor powers to service account