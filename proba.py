import pandas as pd
import csv
import os
import string

path = input("If you want to show the path of yours CSV source file, write it down. If you want to use default source file, click ENTER")

if path== "":
    path='/home/ewelina/Documents/Python/vscode/ludnosc.csv'

#source file
csvfile = pd.read_csv(path, sep=',', encoding='utf-8')

if os.path.isfile(path):
    #list of lower alphabet letters
    alphabet= set(string.ascii_letters.lower())

    # new column with 1st letter
    source_cols = csvfile.columns[0]
    new_cols = ["letter"]

    csvfile[new_cols] = csvfile[source_cols].str.lower()

    source_cols = csvfile.columns[4]
    new_cols = ["first_letter"]
    csvfile[new_cols] = csvfile[source_cols].str[0]

    #group by letter and sum all columns
    county_group=csvfile.groupby("first_letter").sum()

    print("SUMMARY of all numbers group by first letter of the 'name column':")
    print(county_group)

    #summary of all missing letters 
    #convert index into column
    new_summary = county_group.reset_index()
    #create a set of all found letters
    set_letters=set(new_summary["first_letter"])

    missing=alphabet.difference(set_letters)
    
    print("COMMENTS:")
    for item in missing:
        print(item, "wasn't a first letter in source file.")
else:
    print ('Source file is not exist.')