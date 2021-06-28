from Code.Tracker.CardsTracker import CardsTracker
from Code.Tracker.ListsTracker import ListsTracker
from Code.Tracker.BoardsTracker import BoardsTracker

DefaultKey = "b484f79254e071d549508f428c840c0c"
DefaultToken = "bd9e92fb3671f13e3dd5eb3e85c2184392437c407f354545e6c78181b137ef20"
url = "https://api.trello.com/1/members/me/boards"

def CollectBoardInformationCountTest():
    boardTracker = BoardsTracker(DefaultKey, DefaultToken)
    numberofboards = 2
    boards = boardTracker.__getBoards__()
    assert len(boards) == numberofboards,"test failed"

def CollectBoardInformationNameTest():
    boardTracker = BoardsTracker(DefaultKey, DefaultToken)
    boards = boardTracker.__getBoards__()
    boardsName =["TrelloBoard", "TerelloBoard1"]
    for board in boards:
        assert boardsName.__contains__(board.__nameValue__),"test failed"
        lists = board.__boardlistTracker__.__GetList__()
        for list in lists:
            print(list.__nameValue__)


def CollectBoardList1InformationCountTest():
    boradtrack = ListsTracker(DefaultKey, DefaultToken, '60a52146bbe74c4fcae74e6f')
    numberoflists = 2
    lists = boradtrack.__GetList__()
    assert len(lists) == numberoflists, "test failed"


def CollectBoard1ListInformationNameTest():
    boradtrack= ListsTracker(DefaultKey, DefaultToken, '60a52146bbe74c4fcae74e6f')
    lists = boradtrack.__GetList__()
    listsName = ["List1", "List2"]
    for list in lists:
        assert listsName.__contains__(list.__nameValue__), "test failed"

def AddaNewCardTest():
    cardtracker =  CardsTracker(DefaultKey, DefaultToken, '60a52146bbe74c4fcae74e6f', '60a52152e2b96d57518b140a')
    newCard = cardtracker.__addANewCard__()

def AddaNewCardWithLabelTest():
    cardtracker =  CardsTracker(DefaultKey, DefaultToken, '60a52146bbe74c4fcae74e6f', '60a52152e2b96d57518b140a')
    newCard = cardtracker.__addANewCard__(['60a52146c824613830e649c7'])


def AddCommentToNewCard():
        cardtracker = CardsTracker(DefaultKey, DefaultToken, '60a52146bbe74c4fcae74e6f', '60a52152e2b96d57518b140a')
        newCard = cardtracker.__addANewCard__()
        cardtracker.__addACommentToCard__(newCard.__id__, "Hello")



CollectBoardInformationCountTest()
CollectBoardInformationNameTest()
CollectBoardList1InformationCountTest()
CollectBoard1ListInformationNameTest()
AddaNewCardWithLabelTest()
