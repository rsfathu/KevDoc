import pandas
from sqlalchemy import create_engine
import sqlite3
import random as r
import numpy
import pprint
from sqlite3.dbapi2 import SQLITE_SELECT

database = sqlite3.connect('KevDocPanda.db')
cursor = database.cursor()
def initiateprogram():
    #Using Pandas to get the latest data from google sheets table with songs
    sheet_id = "1jLsb5_ShOcPxoCxansGiiw2JseUP4RdxRvTP-mecBo8"
    #df stands for datafile
    df = pandas.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    #retrieve relevant columns specifically
    idcolumn = df[["Subject", "Modal", "Verb", "Adverbial"
                   ]]
    engine = create_engine('sqlite:///KevDocPanda.db', echo=True)
    sqlite_connection = engine.connect()
    #Creating the table with headers
    idcolumn.to_sql("KevDoc_information", sqlite_connection, if_exists="replace")

#created a function or class called 'retreive' to retrieve info
#whatyoulookingfor is a variable in which you put in the column data that you want from the excel
def retrieve(whatyoulookingfor):
    executedcode = " SELECT {} FROM 'KevDoc_information' ".format(str(whatyoulookingfor))
    cursor.execute(executedcode)
    getdata = cursor.fetchall()
    return getdata

initiateprogram()        

#below are lists of the respective columns
subjectlst = retrieve("Subject")
modallst = retrieve("Modal")
verblst = retrieve("Verb")
adverbiallst = retrieve("Adverbial")