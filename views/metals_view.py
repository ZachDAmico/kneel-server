import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class MetalsView() :
    def get(self, handler, pk):
        if pk != 0:
            sql = "SELECT metals.id, metals.metal, metals.price FROM metals WHERE metals.id = ?"
            query_results = db_get_single(sql, pk)
            serialized_metal = json.dumps(dict(query_results))

            return handler.response(serialized_metal, status.HTTP_200_SUCCESS.value)
        
        else: 
            sql = "SELECT metals.id, metals.metal, metals.price FROM metals"
            query_results = db_get_all(sql)
            metal = [dict(row) for row in query_results]
            serialized_metal = json.dumps(metal)

            return handler.response(serialized_metal, status.HTTP_200_SUCCESS.value)
        
    def add(self, handler):
        
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def update(self, handler):
    
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    
    def delete(self, handler):

        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
    