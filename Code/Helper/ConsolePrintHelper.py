from Code.Tracker.BoardsTracker import BoardsTracker

## This file is helper to take input and output from console
class ConsolePrintHelper:
    def __init__(self):
        DefaultKey = "b484f79254e071d549508f428c840c0c"
        DefaultToken = "bd9e92fb3671f13e3dd5eb3e85c2184392437c407f354545e6c78181b137ef20"
        self.key = DefaultKey
        self.token = DefaultToken
        self.labelsToadd = []

    def __GetKeyAndTokenOption__(self):
        print("Hello Welcome to Add card Application")
        print("Do you want to work with default board or want to enter new key and token")
        print("press 1 to enter new key and token or press any integer to go with default board")
        boardSelected = int(input())
        if (boardSelected == 1):
            print("enter key")
            self.key = input()
            print("enter Token")
            self.token = input()


    def __displayCollectedBoards__(self):
        numberofBoards = len(self.boardTracker.__getBoards__())

        ### select default board#######
        selectedBoard = self.boardTracker.__getBoards__()[0]
        if (numberofBoards > 1):
            print("Terello site has more than 1 board  select board number you want to add card to")
            for board in self.boardTracker.__getBoards__():
                print(f"{board.__numberAssign__}   {board.__nameValue__}")


    def __getBoardToWorkWith__(self):
        self.selectedBoard = self.boardTracker.__getBoards__()[0]
        boardNumberSelected = int(input("Enter board number"))
        for board in self.boardTracker.__getBoards__():
            if (board.__numberAssign__ == boardNumberSelected):
                self.selectedBoard = board
                break
        print(f"The board selected to add card to is {self.selectedBoard.__nameValue__}")
        print()


    def __displayCollectedList__(self):
        numberofLists = len(self.selectedBoard.__boardlistTracker__.boardLists)
        self.selectedlist = self.selectedBoard.__boardlistTracker__.boardLists[0]

        if (numberofLists > 1):
            print("Select number of list you want to add card to")
            for boardlist in self.selectedBoard.__boardlistTracker__.boardLists:
                print(f"{boardlist.__numberAssign__}   {boardlist.__nameValue__}")

    def __getListToWorkWith__(self):
        self.selectedlist = self.selectedBoard.__boardlistTracker__.__GetList__()[0]
        listNumberSelected = int(input("select list number"))
        for boardlist in self.selectedBoard.__boardlistTracker__.__GetList__():
            if boardlist.__numberAssign__ == listNumberSelected:
                self.selectedlist = boardlist
                break
        print(
            f"The  Board and List selected to add card to is {self.selectedBoard.__nameValue__} and {self.selectedlist.__nameValue__}")
        print()

    def __displayCollectedLabels__(self):
        print("Select a labels to add  to card in a comma separated format, for wrong input no label will get added")
        for labels in self.selectedBoard.__lables__:
            print(f"{labels.__numberAssign__}   {labels.__color__}")

    def __getlabelToAdd__(self):
        label = (input("Select Label in comma separated form"))
        labellist = label.split(',')

        for label in self.selectedBoard.__lables__:
            if (labellist.__contains__(str(label.__numberAssign__))):
                self.labelsToadd.append(label.__id__)

    def __getCommentToadd__(self):
        self.comment = input("Add Comment To add to new card")


    def __CollectBoardInformationToDisplay__(self):
        self.boardTracker = BoardsTracker(self.key, self.token)
        if self.boardTracker.__isSuccessFull__:
            print("Terello Information collected successfully")
            return True
        else:
            return False

    def __addCardWithCommentAndLabel__(self):
        newcard = self.selectedlist.__cardTracker__.__addANewCard__(self.labelsToadd)
        self.selectedlist.__cardTracker__.__addACommentToCard__(newcard.__id__, self.comment)
        if self.selectedlist.__cardTracker__.__isSuccessFull__:
            print("Card Successfully added")
            return True
        else:
            return False


