from Code.Information.ListInformation import ListInformation
from Code.APICaller.GetTerelloAPICaller import GetTerelloAPICaller
from Code.Tracker.CardsTracker import CardsTracker

## This class manages and track all list information with respect to particular board
class ListsTracker:

    def __init__(self, key, token, boardId):
        self.key = key
        self.token = token
        self.boardId = boardId
        self.boardLists = []
        self.collectListInformation()

        # returns a collected lists

    def __GetList__(self):
        return self.boardLists

    # Call API to get Borad Information
    def collectListInformation(self):
        listsjson = GetTerelloAPICaller.__getBoardListsJson__(self.key, self.token, self.boardId)
        defaultAssignNumber= 1
        for listjson in listsjson:
            self.collectListInformationListFromJson(listjson, defaultAssignNumber)
            defaultAssignNumber = defaultAssignNumber + 1

    # Collect json list information in the form of python object
    def collectListInformationListFromJson(self, boardlistjson, defaultAssignNumber):
        cardTracker = CardsTracker(self.key, self.token, self.boardId, boardlistjson['id'])
        listObject = ListInformation(boardlistjson['name'], boardlistjson['id'], defaultAssignNumber, cardTracker)
        self.boardLists.append(listObject)


