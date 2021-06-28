import requests
import json

## This Class is to Call Get API of Terello
class GetTerelloAPICaller:

    @staticmethod
    def __getAllBoardsJson__(key, token):
        url = "https://api.trello.com/1/members/me/boards"
        headers = {
            "Accept": "application/json"
        }

        query = {
            'key': key,
            'token': token,
            'name': '{name}'
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query

        )

        boardsjson = json.loads(response.text)
        return boardsjson

    @staticmethod
    def __getBoardLabelsJson__(key, token, boardid):
        url = f"https://api.trello.com/1/boards/{boardid}/labels"

        query = {
            'key': key,
            'token': token
        }

        response = requests.request(
            "GET",
            url,
            params=query
        )

        labelsjson = json.loads(response.text)
        return labelsjson

    @staticmethod
    def __getBoardListsJson__(key, token, boardId):
        url = f"https://api.trello.com/1/boards/{boardId}/lists"
        query = {
            'key': key,
            'token': token
        }

        response = requests.request(
            "GET",
             url,
            params=query
        )

        listsjson = json.loads(response.text)
        return listsjson
