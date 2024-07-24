import mysql.connector
import sys 

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host = "localhost", 
                user="root", 
                password = "", 
                database = "hit-db-demo")
            self.mycursor = self.conn.cursor() #communicate with DB
        except:
            print("Some error occured. Could not connect to database")
            sys.exit(0)
        else:
            print("Connected to DB")


    def register(self, name, email, password):

        try:
            self.mycursor.execute("""INSERT INTO `users` (`id`, `Name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}');""".format(name, email, password))

            self.conn.commit() #important
        except:
            return -1
        else:
            return 1
        
    def search(self, email, password):
        
        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}' ORDER BY `id` ASC""".format(email, password))
        
        data = self.mycursor.fetchall()
        return data
        
        
    