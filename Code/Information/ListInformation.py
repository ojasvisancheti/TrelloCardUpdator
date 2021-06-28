## encapsule list data in the form of object
## each list object has its own card tracker
class ListInformation:
    def __init__(self, name, id, numberAssign, cardTracker):
        self.__nameValue__ = name
        self.__id__ = id
        self.__numberAssign__ = numberAssign
        self.__cardTracker__ = cardTracker