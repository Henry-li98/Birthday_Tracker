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
cred = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

client = gspread.authorize(cred)

sheet = client.open("Birthday_list")

worksheet = sheet.worksheet(0)

df = pd.DataFrame(worksheet.get_all_records())

print (df)
