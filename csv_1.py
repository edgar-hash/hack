import csv
import os

def csvChecker(dining_hall, food_item):
    folder_path = 'csvfolder'

    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    dictary = []

    if dining_hall.lower() == "Carillo":
        csvacsess = csv_files[:3]
    elif dining_hall.lower() == "DLG":
        csvacsess = csv_files[3:7]
    else:
        csvacsess = csv_files[-4:]


    # Get a list of all CSV files in the folder

    for csv_file in csvacsess:
    # Construct the full path to the CSV file
        file_path = os.path.join(folder_path, csv_file)
        data_dict = {}

        # Open the CSV file and read its contents as a dictionary
        with open(file_path, 'r') as csvfile:
        # Create a CSV DictReader object
            csv_reader = csv.DictReader(csvfile)

        # Iterate through each row in the CSV file
            for row in csv_reader:
        # Add the data to the dictionary
        # Assuming the first column is 'key' and the second column is 'value'
                key = row['name']  # Replace 'column1' with the actual header of the first column
                value = row['station']  # Replace 'column2' with the actual header of the second column
                data_dict[key.lower()] = (value.lower())
                
        dictary.append(data_dict)

    options=[]
    duplicatechecker = []
    for menui in dictary:
        for menuitem in menui:
            if food_item in menuitem:
                if menuitem not in duplicatechecker:
                    options.append((menuitem,menui[menuitem]))
                    duplicatechecker.append(menuitem)

    return options
