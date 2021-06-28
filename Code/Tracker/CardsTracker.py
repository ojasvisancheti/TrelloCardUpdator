from Code.Information.CardInformation import CardInformation
from Code.APICaller.AddTerelloAPICaller import AddTerelloAPICaller

## This class manages and track all card information with respect to particular board and list
class CardsTracker:

    def __init__(self, key, token, boardId, listId):
        self.key = key
        self.token = token
        self.boardId = boardId
        self.listId = listId
        self.__isSuccessFull__ = True

   ## adds a called by calling Add API
    def __addANewCard__(self, labels =[]):
        try:
            self.cardJson = AddTerelloAPICaller.__addCardToLisWithLablels__(self.key, self.token, self.listId, labels)
            self.newCard = CardInformation(self.cardJson['id'], "", labels)
            return self.newCard
            self.__isSuccessFull__ = True
        except Exception as ex :
            print(f"Something went wrong while creating a card")
            print(f"The exception is {ex}")
            self.__isSuccessFull__ = False

    ## adds a comment to card by calling API
    def __addACommentToCard__(self, cardId, comment):
        try:
            self.cardJson = AddTerelloAPICaller.__AddCommentToCard__(self.key, self.token, cardId, comment)
            self.__isSuccessFull__ = True
        except Exception as ex:
            print(f"Something went wrong while adding comment to card")
            print(f"The exception is {ex}")
            self.__isSuccessFull__ = False






