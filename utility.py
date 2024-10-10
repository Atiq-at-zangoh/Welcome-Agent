import pandas as pd
from csv import writer
import os


## Create a new visitors.csv if not available

def create_csv():

    if not os.path.exists("visitors.csv"):

        visitor_details_table = pd.DataFrame(columns=["Name", "Contact", "Email", "Company", "Designation"])

        visitor_details_table.to_csv("visitors.csv")

def update_csv(new_visitor: list):

    with open('visitors.csv', 'a') as f:
 
        writer_object = writer(f)
 
        writer_object.writerow(new_visitor)
 
        f.close()


