import json
from nss_handler import status
from repository import db_get_single, db_get_all, db_delete, db_update, db_create

class OrdersView() :
    def get(self, handler, pk):
        parsed_url = handler.parse_url(handler.path)
        if pk != 0:
            expand_params = parsed_url['query_params'].get('_expand')
            if expand_params:
                # need to make new SELECT that gets everything
                sql="""
SELECT
             o.id,
                    o.metalId,
                    o.styleId,
                    o.sizeId,
                    o.timestamp,
                    m.id AS metal_id,
                    m.metal,
                    m.price as metal_price,
                    s.id AS size_id,
                    s.carets,
                    s.price as size_price,
                    st.id AS style_id,
                    st.style,
                    st.price as style_price
                    FROM Orders o
                    LEFT JOIN Metals m ON o.metalId = m.id
                    LEFT JOIN Sizes s ON o.sizeId = s.id
                    LEFT JOIN Styles st ON o.styleId = st.id
                    WHERE o.id = ?"""
                

                query_results = db_get_single(sql, pk)

                order_data = {
                    "id": query_results['id'],
                    "timestamp": query_results['timestamp'],
                    "metal_id": query_results['metal_id'],
                    "style_id": query_results['style_id'],
                    "size_id": query_results['size_id']
                }

                if 'metal' in expand_params:
                    order_data["metal"] = {
                        "id": query_results['metal_id'],
                        "metal": query_results['metal'],
                        "price": query_results['metal_price']
                    }
                if 'style' in expand_params:
                    order_data["style"] = {
                        "id": query_results['style_id'],
                        "style": query_results['style'],
                        "price": query_results['style_price']
                    }
                if 'size' in expand_params:
                    order_data["size"] = {
                        "id": query_results['size_id'],
                        "carets": query_results['carets'],
                        "price": query_results['size_price']
                    }
                serialized_orders = json.dumps(dict(order_data))
            
            else:
                # needs to match original order table
                sql = "SELECT o.id, o.metalId, o.styleId, o.sizeId, o.timestamp FROM Orders o WHERE o.id = ?"
                query_results = db_get_single(sql, pk)
                serialized_orders = json.dumps(dict(query_results))
            return handler.response(serialized_orders, status.HTTP_200_SUCCESS.value)
          
        else:
            # needs to be single line when created
            sql = """
                SELECT 
                id,
                styleId,
                metalId,
                sizeId,
                timestamp
                FROM orders;
                """
            query_results = db_get_all(sql)
            order = [dict(row) for row in query_results]
            serialized_order = json.dumps(order)

        return handler.response(serialized_order, status.HTTP_200_SUCCESS.value)
        
    def add(self, handler, order_data):
        sql= """
        INSERT INTO orders (styleId, metalId, sizeId) VALUES (?,?,?);
        """
        number_of_rows_created = db_create(
            sql, (order_data['styleId'], order_data['metalId'], order_data['sizeId'])
        )
        response_sql = """
        SELECT id, styleId, metalId, sizeId,timestamp FROM orders;
            """
        query_response = db_get_all(response_sql)
        row_orders = [dict(row) for row in query_response]
        response_orders = json.dumps(row_orders)
        if number_of_rows_created > 0:
            return handler.response(response_orders, status.HTTP_201_SUCCESS_CREATED.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND)
        
    def delete(self, handler, pk):
        number_of_rows_deleted = db_delete("DELETE FROM orders WHERE id = ?", pk)

        if number_of_rows_deleted > 0:
            return handler.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
        else:
            return handler.response("", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
        
    def update(self, handler, pk, order_data):
        return handler.response("", status.HTTP_405_UNSUPPORTED_METHOD.value)
