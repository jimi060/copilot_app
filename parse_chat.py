import json

with open("chat_2025-05-21.json", encoding="utf-8") as file:
    data = json.load(file)

new_document = {}

new_document["requests"] = []

for request in data["requests"]:
    new_document["requests"].append(
        {
            "message": {
                "text": request["message"]["text"]
            },
            "response": [
                {
                    "content":{
                        "value": response["content"]["value"]
                    }
                }
                for response in request["response"]
            ]
        }
    )

with open("chat_2025-05-21_requests.json", "w", encoding="utf-8") as file:
    json.dump(new_document, file, ensure_ascii=False, indent=4)