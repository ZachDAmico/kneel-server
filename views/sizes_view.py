import sqlite3
import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class SizesView():

    def add(self, handler):
        
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
        
# get method usually handles HTTP GET request
# takes 3 parameters here, self(object itself), handler(HTTP request handler), and primary key)
    def get(self, handler, pk):
        if pk != 0:
            sql = "SELECT sizes.id, sizes.carets, sizes.price FROM sizes WHERE sizes.id = ?"
            query_results = db_get_single(sql, pk)
            serialized_size = json.dumps(dict(query_results))

            return handler.response(serialized_size, status.HTTP_200_SUCCESS.value)
        else:

            sql = "SELECT sizes.id, sizes.carets, sizes.price FROM sizes"
            query_results = db_get_all(sql)
            size = [dict(row) for row in query_results]
            serialized_size = json.dumps(size)

            return handler.response(serialized_size, status.HTTP_200_SUCCESS.value)
        

    def delete(self, handler, pk):

        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)

    def update(self, handler, pk):
    
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)