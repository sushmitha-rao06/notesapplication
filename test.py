
   
# ///////////////////reportss////////////////////////////////////

# ///////////////////////////////////////////////////////////////


  def save_notes_of_user(self,id, notes):
        try:

            SQL = ''' INSERT INTO DEVDB.dbo.susmitha_notes_table(userId, notes)VALUES( ?,? );'''
            cursor = self.cursor.execute(SQL, (id, notes))
            cursor.commit()
        except Exception as e :
            print("Exception occured on saving the database--",e)
            return False
        return True
    