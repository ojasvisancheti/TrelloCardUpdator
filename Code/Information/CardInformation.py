
# Encapsule card information in the form of object
# we can add comment or label tracker if we want to extent the application
class CardInformation:
    def __init__(self, id, comment, lables =[]):
        self.__id__ = id
        self.__comment__ = comment
        self.__lables__ = lables



