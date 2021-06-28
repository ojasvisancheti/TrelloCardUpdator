A. Information Needed to work with the Application
    1. If you want to work with your own board get Key and Token from https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/
    2. This application assume you atleast have 1 board or 1 list per board.
    3. While adding card the application will ask you for comment and label( select from list shown) to add 
    4. its reccomded to have different names for board and list as it will improve your UI exprince.
    5. This code will require requests and json  python libraries to work

Running Instruction:

Go to Command Prompt activate your virtual environment, go to the path of the 'TerelloCode' folder and Run main.py File

1. press 1 or add key and token otherwise it will work with default board
2. Once you added, a list of board will be displayed you need to select a board number you want to work with
3. Once you selected board, a list of boardlist will be displayed you need to select the board list you want to work with
4. once you selected the list the application will ask you for comment to add
5. Once you added the comment, the application will display the tags available to add for selected board
6. Select the tag numbers in comma seprated format
7. The card will get added 
8. The application will ask you for continue, press 'Y' if you want to continue otherwise any other string input will stop the application


B. Code Structure as real objects
BordsTracker will track and manage all board information
ListsTracker will track and manage  all list information with respect to particular board.
CardsTracker will track and manage all cards information with respect to particular list and board.
each boardInformation object will have information about its list tracker
and ecah listinformation will have information about its card tracker.

API classes will only responsible to call TerelloAPI.(Separation of concerns)
ConsolePrinterHelper will only track input and output to console application.



C. Future Improvements:
This is a small application only to add card with comment and tags.
At present only BoardTracker , ListTracker and CardTRacker is present with some Collect and Add  methods we can  extent it to AddBoard, AddList methods as well
I have made compulsory to add comment and tags in this application,  we can also make it flexible as all methods are properly seprated.

This is the console application we can create a good Visual UI for the User to increase there UI exprince
 







	