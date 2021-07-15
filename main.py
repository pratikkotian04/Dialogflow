import csv
import json
import trainingjsonfile
import os

# Define The folder name
csvfile = "TrainingCSV\English Template - English Template.csv"
# /home/karthika/karthika/IDES/June 7/Dialogflow/TrainingCSV/25-06-2021 Template - Sheet1.csv
# Define the Folder name where you want to create all the JSON file.
importFolder = "Intent/"


def chip(row):
    chip = []
    for i in row.split("/"):
        chip.append({"text": i[:25]})
    return chip


def chipgoogle(row):
    chipgoogle = []
    for i in row.split("/"):
        chipgoogle.append({"title": i[:25]})
    return chipgoogle


with open(csvfile, 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        # trainingjsonfile.userSays(row)
        # print(trainingjsonfile.userSays(row))

        if row[5]:
            if(os.path.exists(importFolder+row[0]+".json")):
                with open(importFolder+row[0]+".json", encoding="utf8") as f:
                    data = json.load(f)
                message = {
                    "type": 0,
                    "lang": row[10] or "en",
                    "condition": "",
                    "speech": row[1]
                }
                data['responses'][0]['messages'].append(message)
                data['responses'][0]['messages'].append(
                    {
                        "type": 14,
                        "platform": "telephony",
                        "title": "",
                        "textToSpeech": "",
                        "lang": row[10] or "en",
                        "text": row[2],
                        "condition": ""
                    })
                with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                    json.dump(trainingjsonfile.defaultcontext(
                        row), f, indent=2, ensure_ascii=False)
        else:
            if(row[10]):
                with open(importFolder+row[0]+"_usersays_"+row[10]+".json", 'w', encoding='utf-8') as f:
                    json.dump(trainingjsonfile.userSays(row),
                              f, indent=2, ensure_ascii=False)
            else:
                with open(importFolder+row[0]+"_usersays_en.json", 'w', encoding='utf-8') as f:
                    json.dump(trainingjsonfile.userSays(row),
                              f, indent=2, ensure_ascii=False)

            if row[3] and row[4] or row[3]:
                if(os.path.exists(importFolder+row[0]+".json")):
                    with open(importFolder+row[0]+".json", encoding="utf8") as f:
                        data = json.load(f)
                    payload_data = row[6]
                    if payload_data:
                        data['responses'][0]['messages'].append(
                            {
                                "type": 0,
                                "lang": row[10] or "en",
                                "condition": "",
                                "speech": row[1]
                            })
                        data['responses'][0]['messages'].append(
                            {
                                "type": 4,
                                "lang": row[10] or "en",
                                "condition": "",
                                "payload": json.loads(row[6])
                            }

                        )
                        data['responses'][0]['messages'].append(
                            {
                                "type": 14,
                                "platform": "telephony",
                                "title": "",
                                "textToSpeech": "",
                                "lang": row[10] or "en",
                                "text": row[2],
                                "condition": ""
                            })
                    else:
                        message = {
                            "type": 0,
                            "lang": row[10] or "en",
                            "condition": "",
                            "speech": row[1]
                        }
                        data['responses'][0]['messages'].append(message)
                        data['responses'][0]['messages'].append(
                            {
                                "type": 14,
                                "platform": "telephony",
                                "title": "",
                                "textToSpeech": "",
                                "lang": row[10] or "en",
                                "text": row[2],
                                "condition": ""
                            })
                    with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    trainingjsonfile.outputOutputContext(row)
                    print(trainingjsonfile.outputOutputContext(row))
                    with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                        json.dump(trainingjsonfile.outputOutputContext(
                            row), f, indent=2, ensure_ascii=False)
            elif row[4]:
                if(os.path.exists(importFolder+row[0]+".json")):
                    with open(importFolder+row[0]+".json", encoding="utf8") as f:
                        data = json.load(f)
                    #payload_data = chip(row[6])[0].get("text", "")
                    payload_data = row[6]
                    if payload_data:
                        data['responses'][0]['messages'].append(
                            {
                                "type": 0,
                                "lang": row[10] or "en",
                                "condition": "",
                                "speech": row[1]
                            })
                        data['responses'][0]['messages'].append(
                            {
                                "type": 4,
                                "lang": row[10] or "en",
                                "condition": "",
                                "payload": json.loads(row[6])
                            }

                        )
                        data['responses'][0]['messages'].append(
                            {
                                "type": 14,
                                "platform": "telephony",
                                "title": "",
                                "textToSpeech": "",
                                "lang": row[10] or "en",
                                "text": row[2],
                                "condition": ""
                            })
                    else:
                        message = {
                            "type": 0,
                            "lang": row[10] or "en",
                            "condition": "",
                            "speech": row[1]
                        }
                        data['responses'][0]['messages'].append(message)
                        data['responses'][0]['messages'].append(
                            {
                                "type": 14,
                                "platform": "telephony",
                                "title": "",
                                "textToSpeech": "",
                                "lang": row[10] or "en",
                                "text": row[2],
                                "condition": ""
                            })
                    with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    trainingjsonfile.outputContext(row)
                    print(trainingjsonfile.outputContext(row))
                    with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                        json.dump(trainingjsonfile.outputContext(
                            row), f, indent=2, ensure_ascii=False)
            else:
                # If the .json file is present it will append the message for different language in the same file.
                if(os.path.exists(importFolder+row[0]+".json")):
                    with open(importFolder+row[0]+".json", encoding="utf8") as f:
                        data = json.load(f)
                    #payload_data = chip(row[6])[0].get("text", "")
                    payload_data = row[6]
                    if payload_data:
                        data['responses'][0]['messages'].append(
                            {
                                "type": 0,
                                "lang": row[10] or "en",
                                "condition": "",
                                "speech": row[1]
                            })
                        data['responses'][0]['messages'].append(
                            {
                                "type": 4,
                                "lang": row[10] or "en",
                                "condition": "",
                                "payload": json.loads(row[6])
                            }

                        )
                        data['responses'][0]['messages'].append(
                            {
                                "type": 14,
                                "platform": "telephony",
                                "title": "",
                                "textToSpeech": "",
                                "lang": row[10] or "en",
                                "text": row[2],
                                "condition": ""
                            })
                    else:
                        message = {
                            "type": 0,
                            "lang": row[10] or "en",
                            "condition": "",
                            "speech": row[1]
                        }
                        data['responses'][0]['messages'].append(message)
                        data['responses'][0]['messages'].append(
                            {
                                "type": 14,
                                "platform": "telephony",
                                "title": "",
                                "textToSpeech": "",
                                "lang": row[10] or "en",
                                "text": row[2],
                                "condition": ""
                            })
                    with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2, ensure_ascii=False)
                else:
                    trainingjsonfile.noFollowup(row)
                    with open(importFolder+row[0]+".json", 'w', encoding='utf-8') as f:
                        json.dump(trainingjsonfile.noFollowup(row),
                                  f, indent=2, ensure_ascii=False)
