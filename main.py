from Code.Helper.ConsolePrintHelper import ConsolePrintHelper


def InteractWithUser():

    try:
        inputVar = "y"
        while (inputVar.__contains__('y') or inputVar.__contains__('Y')):
            consolePrintHelper = ConsolePrintHelper()
            consolePrintHelper.__GetKeyAndTokenOption__()
            isSuccessfull = consolePrintHelper.__CollectBoardInformationToDisplay__()
            if isSuccessfull:
                consolePrintHelper.__displayCollectedBoards__()
                consolePrintHelper.__getBoardToWorkWith__()
                consolePrintHelper.__displayCollectedList__()
                consolePrintHelper.__getListToWorkWith__()
                consolePrintHelper.__getCommentToadd__()
                consolePrintHelper.__displayCollectedLabels__()
                consolePrintHelper.__getlabelToAdd__()
                iscardAdded = consolePrintHelper.__addCardWithCommentAndLabel__()
                if iscardAdded:
                    inputVar = input("press 'Y' if you want to continue")
                else:
                    inputVar = '0'
            else:
                inputVar = '0'
    except Exception as ex:
        print("error has occurred")
        print(f"The exception thrown is {ex}")


if __name__ == "__main__":
    InteractWithUser()
