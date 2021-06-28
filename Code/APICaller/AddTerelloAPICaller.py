import requests
import json

## This Class is to Call Add API of Terello
class AddTerelloAPICaller:

    @staticmethod
    def __addCardToList__(key, token, listId):

        url = f"https://api.trello.com/1/cards"

        query = {
            'key': key,
            'token': token,
            'idList': listId,
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )

        return json.loads(response.text)

    @staticmethod
    def __addCardToLisWithLablels__(key, token, listId, labels =[]):
        url = f"https://api.trello.com/1/cards"

        query = {
            'key': key,
            'token': token,
            'idList': listId,
            'idLabels': labels
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )

        return json.loads(response.text)

    @staticmethod
    def __AddCommentToCard__(key, token, cardId, comment):
        url = f"https://api.trello.com/1/cards/{cardId}/actions/comments"
        query = {
            'key': key,
            'token': token,
            'text': comment
        }

        response = requests.request(
            "POST",
            url,
            params=query
        )

        return json.loads(response.text)

