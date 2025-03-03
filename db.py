import pyodbc  

class NotesDB():
    def __init__(self, *args, **kwargs):
        self.cnxn = pyodbc.connect('Driver={SQL Server};' 
                     'Server=SUSHMITHA;' 
                     'Database=DEVDB;' 
                     'Trusted_Connection=yes;')
        self.cursor = self.cnxn.cursor()

    def __exit__(self, *args):
        if self.cnxn:
            self.cnxn.close()
            self.cnxn = None

    def create_user_in_db(self, firstName, secondName, email, password):
        try:

            SQL = ''' INSERT INTO DEVDB.dbo.susmitha_users_table(firstName, lastName, email, password)VALUES( ?,?,?,?);'''
            cursor = self.cursor.execute(SQL, (firstName, secondName, email, password))
            cursor.commit()
        except Exception as e :
            print("Exception occured on saving the database--",e)
            return False
        return True
    
    def validate_user(self, email, password):
        try: 
            SQL = ''' SELECT *  From  DEVDB.dbo.susmitha_users_table where email in ( ?);'''
            cursor = self.cursor.execute(SQL, (email),)
            rows = self.cursor.fetchall()
        except Exception as e :
            print("Exception occured on Logging into admin",e)
            return (False,e)
        return (True, rows)
    
    def get_notes_of_user(self,id):
        SQL = '''SELECT * from DEVDB.dbo.susmitha_notes_table where userId in ( ?)'''
        cursor = self.cursor.execute(SQL, id)
        rows = self. cursor.fetchall()
        
        return rows
    
    def save_notes_of_user(self,id, notes):
        try:

            SQL = ''' INSERT INTO DEVDB.dbo.susmitha_notes_table(userId, notes)VALUES( ?,? );'''
            cursor = self.cursor.execute(SQL, (id, notes))
            cursor.commit()
        except Exception as e :
            print("Exception occured on saving the database--",e)
            return False
        return True
    
    def delete_notes_of_user(self,id):
        try:

            SQL = ''' DELETE FROM DEVDB.dbo.susmitha_notes_table Where id = ( ?);'''
            cursor = self.cursor.execute(SQL, id)
            cursor.commit()
        except Exception as e :
            print("Exception occured on saving the database--",e)
            return False
        return True
    
    
