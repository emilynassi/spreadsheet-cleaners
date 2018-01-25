#import dependencies
import pandas as pd
from pandas import ExcelWriter
import os
import numpy as np

#import file
past_sales = os.path.join('jamessmith.csv')

#read csv
past_sales_read = pd.read_csv(past_sales, usecols=[4,7,14,21,31,37,39,40, 41, 42, 43, 44, 45, 46, 47])

#create Dataframe of relevant columns
ps_df = pd.DataFrame(past_sales_read)

#replace nans with blanks and name variations if necessary 
ps_df = ps_df.replace(np.nan, '', regex=True)
ps_df = ps_df.replace("James M Smith", "James Smith")

#Concatenate Street and drop old columns
ps_df['Address'] = ps_df['House Number'].astype(str) + " " + ps_df['Dir.'].astype(str) + " " + ps_df['Street Name'] + " " + ps_df['NO_COMMON_NAME.1'].astype(str) + " " + ps_df['Street Suffix'] + " " + ps_df['Postal City'] + " " + ps_df['State'] + " " + "0" + ps_df['Zip Code'].astype(str)

#Create new column for buy or sell side
ps_df['Represented'] = " "

#Use if statement to find out if on sell or buy side
ps_df['Represented'] = np.where(ps_df['Listing Agent' or 'Co-Listing Agent'] == "Patricia Caruso", 'Sell', 'Buy')

ps_df.drop(ps_df.columns[[0, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1, inplace=True)
ps_df = ps_df.replace('', np.nan, regex=True)
ps_df['Sold Price'] = ps_df['Sold Price'].apply('${:,.2f}'.format)
ps_df.dropna(how='any') 

#write to excel and move index to first name
writer = ExcelWriter('JamesSmithPastSales.xlsx')
ps_df.to_excel(writer,'Past Sales', index=False)
writer.save()

#write to csv
ps_df.to_csv('JamesSmithPastSales.csv', encoding='utf-8')