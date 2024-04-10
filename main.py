# find a module or library that can read nad write off of google sheets for the birthdays and names
# create array to hold the birthday date and name (figure out the proper name of what it is
# use some algorithm that will organize the array by date
# later use this algo to compare to the current date to determine the next birthday
# find a module that interacts with windows notification, use it to display the next upcoming birthday thats coming when its within X days

import gspread
import pandas as pd
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime


#provides access to the Google sheets and drive in order to be able to interact and manipulate data
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name('Sheet_access.json', scope)

client = gspread.authorize(cred)

sheet = client.open("Birthday_list")

worksheet = sheet.worksheet('Sheet1')


df = pd.DataFrame(worksheet.get_all_records())
# changes entire list into a dictionary list that is now sorted and in a list that can be edited

# used to test if the listed items within the excel sheet actually become a dictionary list to be edited
# for i in range(len(birthday_list)):
#     print(birthday_list[i])

print(df)

while True:
    response = input("Here is the current list, is there more names that need to be added? (yes/no): ").lower()
    if response == 'no':
        break
        print("no additional data added")
    elif response == 'yes':
        Name = input("enter name of the person ")
        Birthday = input("enter the birthday date (MM/DD) ")
        month,day = Birthday.split('/')
        # birthday_list = df.to_dict(orient='records')
        print(month)
        print(day)
        # append a constant year to the new ones
        year = 2020
        adding_year = f"{month}/{day}/{year}"
        complete_birthday = datetime.strptime(adding_year, "%m/%d/%Y")
        bday = complete_birthday.date()
        # # print("name added: " + (Name) + " birthday added: " + (Birthday))
        print(complete_birthday)   #prints 2020-02-22 00:00:00
        print(bday)                #prints 2020-02-22

        new_row = Name, adding_year
        last_index =df.index[-1]
        worksheet.append_row(new_row)
        print(df)
    else:
        print("invalid input, type in yes or no")

print("sorting months by alphabetical order")
for i in index , i++
    #learn to use bubble sort for this
# figure out how to add to the data frames and link both name and date together so when they get changed its moved together
# learn how to use bubblesort to organize the cells that are attached via names and dates and order them sequentially


# test adding then sorting the names
# find a module that can access the windows OS notifications feature
























#list of problems that lasted way too much time

#forgetting to go into the google sheets itself and give it editor powers to service account
#