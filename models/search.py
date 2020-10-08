from models.dbConnection import DBConnector
from datetime import datetime 

class Search(DBConnector):
    
    def __init__(self):
        self.connection=super(Search,self).__init__()

    def post_search_data(self,user_id,keyword):
        sql_cursor = self.connection.cursor()
        query="Insert into searches Values('{}', '{}', '{}')".format(user_id, keyword, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        sql_cursor.execute(query)
        self.connection.commit()

    def fetch_search_data(self,user_id, keyword):
        sql_cursor = self.connection.cursor()
        query="Select * from searches where user_id = '{}' and keyword like '%".format(user_id) + keyword + "%'"
        sql_cursor.execute(query)
        results = sql_cursor.fetchall()
        return results
