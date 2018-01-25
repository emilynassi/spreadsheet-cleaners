#import dependencies
import pandas as pd
from pandas import ExcelWriter
import numpy as np
import os

#import file
cole_file1 = os.path.join('LittleSilver.csv')

#read csv
cn = pd.read_csv(cole_file)

#change cell rows to object to display phone number correctly
pd.options.display.float_format = '{:.0f}'.format

#create Dataframe for people with home phone, email and cell phone
both_df = pd.DataFrame(cn, columns = ["First Name", "Last Name", "Address 1", "City", "ST", "ZIP",
                                      "Home Phone", "Cell Phone", "Email Address"])

#make emails lower case
both_df["Email Address"] = both_df['Email Address']

#Drop rows with missing cell phone or email to create dataframe of both
both_df = both_df.dropna()

#create Dataframe for people with emails
emails_df = pd.DataFrame(cn, columns = ["First Name", "Last Name", "Address 1", "City", "ST", "ZIP", "Email Address"])

#make emails lower case
emails_df["Email Address"] = emails_df['Email Address']

#Drop rows with missing email to create dataframe of people with emails
emails_df = emails_df.dropna()

#create Dataframe for people with cell phones
cell_df = pd.DataFrame(cn, columns = ["First Name", "Last Name", "Address 1", "City", "ST", "ZIP", "Cell Phone"])

#Drop rows with missing cell phone or to create dataframe of people with cell phones
cell_df = cell_df.dropna()

#create Dataframe for people with cell phones
home_df = pd.DataFrame(cn, columns = ["First Name", "Last Name", "Address 1", "City", "ST", "ZIP", "Home Phone"])

#Drop rows with missing cell phone or to create dataframe of people with cell phones
home_df = home_df.dropna()

#write to excel and move index to first name
writer = ExcelWriter('LittleSilver.xlsx')
both_df.to_excel(writer,'Email, Cell and Home Phone', index=False)
home_df.to_excel(writer,'Home Phone', index=False)
emails_df.to_excel(writer,'Emails', index=False)
cell_df.to_excel(writer,'Cell Phone', index=False)

#save file
writer.save()