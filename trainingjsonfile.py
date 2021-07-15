import json
from uuid import uuid4


def userSays(row):
    userSays = []
    for i in row[12:]:
        if(i):
            userSays.append({"id": "", "data": [{"text": i, "userDefined": False}],
                            "isTemplate": False, "count": 0, "lang": row[10] or "en", "updated": 0})
    return userSays


def noFollowup(row):
    def webhook(row):
        if(row == "" or row.lower() == "false"):
            return False
        else:
            return True
    noFollowup = {
        "id": str(uuid4()),
        "name": row[0],
        "auto": True,
        "contexts": [],
        "responses": [
            {
                "resetContexts": False,
                "affectedContexts": [],
                "parameters": [],
                "messages": [
                    {
                        "type": 0,
                        "lang": row[10] or "en",
                        "condition": "",
                        "speech": row[1]
                    },
                    {
                        "type": 14,
                        "platform": "telephony",
                        "title": "",
                        "textToSpeech": "",
                        "lang": row[10] or "en",
                        "text": row[2],
                        "condition": ""
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": webhook(row[8]),
        "webhookForSlotFilling": False,
        "fallbackIntent": False,
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return noFollowup


def inputContext(row):
    def webhook(row):
        if(row == "" or row.lower() == "false"):
            return False
        else:
            return True
    inputContext = {
        "id": "",
        "name": row[0],
        "auto": True,
        "contexts": [],
        "responses": [
            {
                "resetContexts": False,
                "affectedContexts": [
                    {
                        "name": row[3],
                        "parameters": {},
                        "lifespan": 2
                    }
                ],
                "parameters": [],
                "messages": [
                    {
                        "type": 0,
                        "lang": row[10] or "en",
                        "condition": "",
                        "speech": row[1]
                    },
                    {
                        "type": 14,
                        "platform": "telephony",
                        "title": "",
                        "textToSpeech": "",
                        "lang": row[10] or "en",
                        "text": row[2],
                        "condition": ""
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": webhook(row[8]),
        "webhookForSlotFilling": False,
        "fallbackIntent": False,
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return inputContext


def outputContext(row):
    def webhook(row):
        if(row == "" or row.lower() == "false"):
            return False
        else:
            return True
    outputContext = {
        "id": row[7] or "",
        "name": row[0],
        "auto": True,
        "contexts": [
            row[4]
        ],
        "responses": [
            {
                "resetContexts": False,
                "affectedContexts": [],
                "parameters": [],
                "messages": [
                    {
                        "type": 0,
                        "lang": row[10] or "en",
                        "condition": "",
                        "speech": row[1]
                    },
                    {
                        "type": 14,
                        "platform": "telephony",
                        "title": "",
                        "textToSpeech": "",
                        "lang": row[10] or "en",
                        "text": row[2],
                        "condition": ""
                    }
                ],
                "defaultResponsePlatforms": {},
                "speech": []
            }
        ],
        "priority": 500000,
        "webhookUsed": webhook(row[8]),
        "webhookForSlotFilling": False,
        "fallbackIntent": False,
        "events": [],
        "conditionalResponses": [],
        "condition": "",
        "conditionalFollowupEvents": []
    }
    return outputContext


def outputOutputContext(row):
    def webhook(row):
        if(row == "" or row.lower() == "false"):
            return False
        else:
            return True

    def chip(row):
        chip = []
        for i in row.split("/"):
            chip.append({"text": i})
        return chip

    def chipgoogle(row):
        chipgoogle = []
        for i in row.split("/"):
            chipgoogle.append({"title": i})
        return chipgoogle

    def outputnewcontext(row):
        outputcontextadd = []
        for i in row.split("/"):
            outputcontextadd.append(
                {"name": i.split("=")[0], "parameters": {}, "lifespan": i.split("=")[1]})
        return outputcontextadd

    def inputnewcontext(row):
        inputnewcontext = []
        for i in row.split("/"):
            inputnewcontext.append(i)
        return inputnewcontext

    #data = chip(row[6])[0].get("text", "")
    data = row[6]

    if data:
        outputOutputContext = {
            "id": row[7] or "",
            "name": row[0],
            "auto": True,
            "contexts": inputnewcontext(row[4]),
            "responses": [
                {
                    "resetContexts": False,
                    "affectedContexts": outputnewcontext(row[3]),
                    "parameters": [],
                    "messages": [
                        {
                            "type": 14,
                            "platform": "telephony",
                            "title": "",
                            "textToSpeech": "",
                            "lang": row[10] or "en",
                            "text": row[2],
                            "condition": ""
                        },
                        {
                            "type": 0,
                            "lang": row[10] or "en",
                            "condition": "",
                            "speech": row[1]
                        },
                        {
                            "type": 4,
                            "lang": row[10] or "en",
                            "condition": "",
                            "payload": json.loads(row[6])
                        }

                    ],
                    "defaultResponsePlatforms": {
                        "google": True
                    },
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": webhook(row[8]),
            "webhookForSlotFilling": False,
            "fallbackIntent": False,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
    else:
        outputOutputContext = {
            "id": row[7] or "",
            "name": row[0],
            "auto": True,
            "contexts": inputnewcontext(row[4]),
            "responses": [
                {
                    "resetContexts": False,
                    "affectedContexts": outputnewcontext(row[3]),
                    "parameters": [],
                    "messages": [
                        {
                            "type": 0,
                            "lang": row[10] or "en",
                            "condition": "",
                            "speech": row[1]
                        },
                        {
                            "type": 14,
                            "platform": "telephony",
                            "title": "",
                            "textToSpeech": "",
                            "lang": row[10] or "en",
                            "text": row[2],
                            "condition": ""
                        }

                    ],
                    "defaultResponsePlatforms": {
                        "google": True
                    },
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": webhook(row[8]),
            "webhookForSlotFilling": False,
            "fallbackIntent": False,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }

    return outputOutputContext


def defaultcontext(row):
    def webhook(row):
        if(row == "" or row.lower() == False):
            return False
        else:
            return True

    def chip(row):
        chip = []
        for i in row.split("/"):
            chip.append({"text": i})
        return chip

    def chipgoogle(row):
        chipgoogle = []
        for i in row.split("/"):
            chipgoogle.append({"title": i})
        return chipgoogle

    def inputnewcontext(row):
        inputnewcontext = []
        for i in row.split("/"):
            inputnewcontext.append(i)
        return inputnewcontext

    if row[0] == "Default Fallback Intent":
        defaultcontext = {
            "id": row[7].split("||")[0] or "",
            "name": row[0],
            "auto": False,
            "contexts": inputnewcontext(row[4]),
            "responses": [
                {
                    "resetContexts": False,
                    "action": "",
                    "affectedContexts": [],
                    "parameters": [],
                    "messages": [
                        # {
                        #     "type": "suggestion_chips",
                        #     "platform": "google",
                        #     "lang": row[10] or "en",
                        #     "condition": "",
                        #     "suggestions": chipgoogle(row[6])
                        # },
                        {
                            "type": 0,
                            "lang": row[10] or "en",
                            "condition": "",
                            "speech": row[1]
                        },
                        {
                            "type": 14,
                            "platform": "telephony",
                            "title": "",
                            "textToSpeech": "",
                            "lang": row[10] or "en",
                            "text": row[2],
                            "condition": ""
                        }
                        # {
                        #     "type": 4,
                        #     "lang": row[10] or "en",
                        #     "condition": "",
                        #     "payload": {
                        #         "richContent": [
                        #             [
                        #                 {
                        #                     "type": "chips",
                        #                     "options": chip(row[6])
                        #                 }
                        #             ]
                        #         ]
                        #     }
                        # }
                    ],
                    "defaultResponsePlatforms": {
                        "google": True
                    },
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": webhook(row[8]),
            "webhookForSlotFilling": False,
            "fallbackIntent": True,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
    else:
        defaultcontext = {
            "id": row[7].split("||")[0] or "",
            "parentId": row[7].split("||")[1] or "",
            "rootParentId": row[7].split("||")[1] or "",
            "name": row[0],
            "auto": False,
            "contexts": inputnewcontext(row[4]),
            "responses": [
                {
                    "resetContexts": False,
                    "action": "",
                    "affectedContexts": [],
                    "parameters": [],
                    "messages": [
                        # {
                        #     "type": "suggestion_chips",
                        #     "platform": "google",
                        #     "lang": row[10] or "en",
                        #     "condition": "",
                        #     "suggestions": chipgoogle(row[6])
                        # },
                        {
                            "type": 0,
                            "lang": row[10] or "en",
                            "condition": "",
                            "speech": row[1]
                        },
                        {
                            "type": 14,
                            "platform": "telephony",
                            "title": "",
                            "textToSpeech": "",
                            "lang": row[10] or "en",
                            "text": row[2],
                            "condition": ""
                        }
                        # {
                        #     "type": 4,
                        #     "lang": row[10] or "en",
                        #     "condition": "",
                        #     "payload": {
                        #         "richContent": [
                        #             [
                        #                 {
                        #                     "type": "chips",
                        #                     "options": chip(row[6])
                        #                 }
                        #             ]
                        #         ]
                        #     }
                        # }
                    ],
                    "defaultResponsePlatforms": {
                        "google": True
                    },
                    "speech": []
                }
            ],
            "priority": 500000,
            "webhookUsed": webhook(row[8]),
            "webhookForSlotFilling": False,
            "fallbackIntent": True,
            "events": [],
            "conditionalResponses": [],
            "condition": "",
            "conditionalFollowupEvents": []
        }
    return defaultcontext
