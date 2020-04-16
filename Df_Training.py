import csv
import json
import trainingjsonfile

# Define The folder name
csvfile = "TrainingCSV/symptomtriagefallback.csv"

# Define the Folder name where you want to create all the JSON file.
importFolder="Intent/"

with open(csvfile, 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        trainingjsonfile.userSays(row)
        print(trainingjsonfile.userSays(row))
        if row[21]:
            with open(importFolder+row[0]+".json",'w') as f:
                json.dump(trainingjsonfile.defaultcontext(row), f, indent=2)
        else:
            with open(importFolder+row[0]+"_usersays_en.json", 'w') as f:
                json.dump(trainingjsonfile.userSays(row), f, indent=2)
            if row[3] and row[4]:
                trainingjsonfile.outputOutputContext(row)
                print(trainingjsonfile.outputOutputContext(row))
                with open(importFolder+row[0]+".json", 'w') as f:
                    json.dump(trainingjsonfile.outputOutputContext(row), f, indent=2)
            elif row[3]:
                trainingjsonfile.inputContext(row)
                print(trainingjsonfile.inputContext(row))
                with open(importFolder+row[0]+".json", 'w') as f:
                    json.dump(trainingjsonfile.inputContext(row), f, indent=2)
            elif row[4]:
                trainingjsonfile.outputContext(row)
                print(trainingjsonfile.outputContext(row))
                with open(importFolder+row[0]+".json", 'w') as f:
                    json.dump(trainingjsonfile.outputContext(row), f, indent=2)
            else:
                trainingjsonfile.noFollowup(row)
                with open(importFolder+row[0]+".json", 'w') as f:
                    json.dump(trainingjsonfile.noFollowup(row), f, indent=2)
