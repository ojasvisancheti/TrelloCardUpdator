from Code.Tracker.ListsTracker import ListsTracker

## encapsule board data in the form of object
## each board object has its own list tracker
class BoardInformation:
    def __init__(self, name, id,numberAssign, boardlistTracker, lables =[]):
        self.__nameValue__ = name
        self.__id__ = id
        self.__boardlistTracker__ = boardlistTracker
        self.__numberAssign__ = numberAssign
        self.__lables__ = lables



