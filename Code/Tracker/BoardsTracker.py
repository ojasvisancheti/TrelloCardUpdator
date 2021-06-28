from Code.APICaller.GetTerelloAPICaller import GetTerelloAPICaller
from Code.Information.BoardInformation import  BoardInformation
from Code.Information.LabelInformation import LabelInformation
from Code.Tracker.ListsTracker import ListsTracker


## This class manages and track allboard information
class BoardsTracker:
    boardsInfo = []
    def __init__(self, key, token):
        self.key = key
        self.token = token
        self.boardsInfo = []
        self.__isSuccessFull__ = True
        self.collectBoardInformation()

    def __getBoards__(self):
        return self.boardsInfo

   # Call API to get Borad Information
    def collectBoardInformation(self):
        try:
            boardsjson = GetTerelloAPICaller.__getAllBoardsJson__(self.key, self.token)
            defaultAssignNumber = 1
            for boardjson in boardsjson:
                self.createListOfBoardInformationFromJson(boardjson, defaultAssignNumber)
                defaultAssignNumber = defaultAssignNumber +1
            self. __isSuccessFull__ = True
        except Exception as ex:
            print("something went wrong while collecting board information")
            print(f"The exception is {ex}")
            self.__isSuccessFull__ = False

   # Collect json information in the form of python object
    def createListOfBoardInformationFromJson(self, boardjson, assignNumber):
        self.labels = self.getBoardLabels(boardjson['id'])
        boardListTracker = ListsTracker(self.key, self.token, boardjson['id'])
        boardObject = BoardInformation(boardjson['name'], boardjson['id'], assignNumber, boardListTracker, self.labels)
        self.boardsInfo.append(boardObject)

   # Get Label available with respect to particular board by calling API
    def getBoardLabels(self, boardid):
        labelsjson = GetTerelloAPICaller.__getBoardLabelsJson__(self.key, self.token, boardid)
        labelsCollected = self.getBoardLabelListFromJson(labelsjson)
        return labelsCollected;

   # Collect lable avilable in the form of python object
    def getBoardLabelListFromJson(self, labelsjson):
        labels = []
        defaultAssignNumber = 1
        for labeljson in labelsjson:
            labelInfo = LabelInformation(labeljson['color'], labeljson['id'], defaultAssignNumber)
            labels.append(labelInfo)
            defaultAssignNumber = defaultAssignNumber + 1
        return labels







