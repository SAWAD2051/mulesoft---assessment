import sqlite3
def createtable():
    con=sqlite3.connect('movie.db')
    c=con.cursor()
    c.execute("""CREATE TABLE Movies(
    mname text,
    actor text,
    director text,
    year_of_release integer)""")
    con.commit()
    con.close()
def add_many(a,b,c,d):
    con=sqlite3.connect('movie.db')
    c=con.cursor()
    c.execute("INSERT INTO Movies VALUES (?,?,?,?)",(a,b,c,d))
    con.commit()
    con.close()
def display():
    con=sqlite3.connect('movie.db')
    c=con.cursor()
    c.execute("SELECT rowid,* FROM Movies")
    items=c.fetchall()
    for i in items:
        print(i)
    con.commit()
    con.close()
def movie_lookup(actor):
    con=sqlite3.connect('movie.db')
    c=con.cursor()
    c.execute("SELECT mname from Movies WHERE actor=(?)",(actor,))
    movies=c.fetchall()
    for actor in movies:
        print(actor)
    con.commit()
    con.close()
while True:
    choice=int(input("""ENTER 1 TO CREATE TABLE Movies
    ENTER 2 TO INSERT DETAILS
    ENTER 3 TO DISPLAY THE RECORD
    ENTER 4 TO FIND THE MOVIES PLAYED BY AN ACTOR
    ENTER 5 TO EXIT"""))
    if(choice==1):
        createtable()
        print("table created")
        pass
    elif(choice==2):
        list=[]
        n=int(input("Enter the number of records to be added to table"))
        for i in range(n):
            a=input("Enter name of the movie"+str(i))
            b=input("Enter name of the actor"+str(i))
            c=input("Enter name of the actoress"+str(i))
            d=input("Enter year of the movie released"+str(i))
            list.appe
        add_many(list)
        pass
    elif(choice==3):
        display()
        pass
    elif(choice==4):
        nam=input("Enter the name of the actor to be searched")
        movie_lookup(nam)
        pass
    elif(choice==5):
        exit
    else:
        print("Enter a proper number")
        pass
    

    


     






