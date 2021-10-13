import requests
from config import *
import json

def list_boards():
    url = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"

    query = {'key': KEY_API_TRELLO, 'token': TOKEN_API_TRELLO}

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )

    lists = json.loads(response.text)

    for list in lists:
        print(f"List: {list['name']} ID: {list['id']}")

def create_card(name, list_id):
    url = f"https://api.trello.com/1/cards"

    query = {'name': name, 'idList': list_id, 'key': KEY_API_TRELLO, 'token': TOKEN_API_TRELLO}

    requests.request("POST", url, params=query).json()

def main():
    tasks_file = open("tasks.txt", "r")
    for task in tasks_file:
        if len(task) > 0:
            create_card(task, LIST_ID)

    tasks_file.close()

if __name__ == "__main__":
    main()