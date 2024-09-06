#!/usr/bin/env python3

import json
import csv
import time
import os
from tkinter import messagebox
import tkinter as tk


def showMessage(type, message):
    # Initialize tk
    root = tk.Tk()
    # Hide the main tk window
    root.withdraw() 
    # Show message
    messagebox.showinfo(type, message)
    # Destroy tk window
    root.destroy()

def main():
    try:
        # Open file data.json
        with open('./data.json') as file:
            data = json.load(file)

        # Name output file
        filename = time.strftime("%Y%m%d.csv")
        print(filename)

        # Create and open csv file
        csv_file = open(filename, 'w+', newline='')
        
        # Initialize csv writer for output file
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

        # Include header in file
        header = ["name", "creditcard"]
        csv_writer.writerow(header)

        # For each entry in data.json only include "name" and "creditcard"
        for line in data:
            # Only include not null values
            if (line["name"] and line["creditcard"]):
                csv_writer.writerow([line["name"], line["creditcard"]])
        
        # Close output file
        csv_file.close()

        # Show file path
        showMessage("Info", f"""File created in path: {os.getcwd()}""")
        

        print(f"""File created in path: {os.getcwd()}""")

    except FileNotFoundError:
        # Show file path
        showMessage("Error",f"""Sorry, could not find data.json in path: {os.getcwd()}""")
        print(f"""Sorry, could not find data.json. Make sure the file is located in your current working directory (CWDs)""")
        print(f"""CWD: {os.getcwd()}""")

    except Exception as e:
        showMessage("Error", f"""Sorry, an error ocurred: {e}""")
        print(f"""Sorry, an error ocurred: {e}""")
        


if __name__ == "__main__":
    main()