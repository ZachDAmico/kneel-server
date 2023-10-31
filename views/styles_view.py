import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class StylesView():
    def get(self, handler, pk):
        if pk != 0:
            sql = "SELECT styles.id, styles.style, styles.price FROM styles WHERE styles.id = ?"
            query_results = db_get_single(sql, pk)
            serialized_style = json.dumps(dict(query_results))

            return handler.response(serialized_style, status.HTTP_200_SUCCESS.value)
        
        else: 
            sql = "SELECT styles.id,styles.style,styles.price FROM styles"
            query_results = db_get_all(sql)
            style = [dict(row) for row in query_results]
            serialized_style = json.dumps(style)

            return handler.response(serialized_style, status.HTTP_200_SUCCESS.value)

    def add(self, handler):
        
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)

    def update(self, handler, pk):
    
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def delete(self, handler, pk):

        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)