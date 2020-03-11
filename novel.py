"""
This program takes the database novel.db and give the users options to either
display all the novel names in the database, add a novel to the database,
or exit the program.
---Program template courtesy of Ms. Richardson---
---Program written by Son Nguyen---
"""

import sqlite3 as sq

# identify location of database
con = sq.connect("/Users/imperium/Documents/GitHub/novel-console-application-TheLordInquisitor/novel.db")
c = con.cursor()

#Getting data from the database
def get_data(column):
    if column == 'novelName':
        sql = c.execute("SELECT Name FROM Novels")
    elif column == 'authorName':
        sql = c.execute("SELECT Name FROM Authors")
    elif column == 'authorID':
        sql = c.execute("SELECT AuthorID FROM Authors")
    elif column == 'novelID':
        sql = c.execute("SELECT NovelID FROM Novels")
    data = c.fetchall()
    return data


#Inserting the novel into the database
def insert_novels(novelName, novelQuantity, novelID, authorID):
    insertion = ('INSERT INTO Novels (Name, Quantity, NovelID, AuthorID) Values ("' + str(novelName) + '", ' + str(novelQuantity) + ', ' + str(novelID) + ', ' + str(authorID) + ')');
    sql = c.execute(insertion)
    con.commit()


#Create the menu
def render_menu():
    print("\n----------------\n")
    print("1. Display Novels\n")
    print("2. Add Novels\n")
    print("3. Exit\n")
    print("----------------\n")
    choice = int(input("Choose an option (1/2/3): "))

    #Move on to the next phase based on the choice
    if choice == 1:
        display('novels')
    elif choice == 2:
        add_novels()
    elif choice == 3:
        end_program()
        return False;

    return True;



def end_program():
    print("\nQuitting now. Thank you for using this application\n")
    con.close()


def display(table):
    #Select which data to display based on the parameter
    if table == 'novels':
        table = get_data('novelName')
    elif table == 'authors':
        table = get_data('authorName')

    #Code from Ms. Richardson - This display the list in a neat way
    tbl = "|---------------------------\n\n"
    for eName in table:
        for field in eName:
            tbl += str(field)
        tbl += "\n\n"

    tbl += "---------------------------|"

    print("\n\nList: \n\n" + tbl)
    

def add_novels():

    #Get data
    display('authors')

    #Get data from database
    authorList = get_data('authorName')
    idListAuthor = get_data('authorID')
    idListNovel = get_data('novelID')

    #Check if the name is correct and match the author ID from the id List with that author using indexes
    authorUnknown = True
    numAuthor = len(get_data('authorID'))
    while authorUnknown: 
        author = input("Please input the author's name exactly as put above: ")
        for i in range(0, numAuthor):
            if author == authorList[i][0]:
                authorUnknown = False
        if authorUnknown:
            print("You need to enter the author's name correctly")
    authorID = idListAuthor[i][0]
    print(authorID)


    #Get the name and the quantity from the user   
    novelName = input("Enter novel name: ")
    novelQuantity = int(input("Enter amount: "))

    #Get the new ID and check if it's taken or not
    needID = True
    while needID:
        novelID = int(input("Enter novel ID: "))
        needID = False
        for ID in idListNovel:
            if novelID == ID[0]:
                needID = True
                print("The ID you've entered is already taken.")

    #Final check
    check_and_enter_selection(novelName, novelQuantity, novelID, authorID)
    

#Code from Ms. Richardson
def check_and_enter_selection(name, quantity, selfID, foreignID):
    try:
        insert_novels(name, quantity, selfID, foreignID)
        print("Success", "Your novel has been added")

    except:
        print("Error- Try again. Perhaps your novel ID is taken")
        return


#The menu
while(render_menu()):
    print("\n\nWelcome to our library system")

