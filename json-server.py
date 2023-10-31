import json
from http.server import HTTPServer
from nss_handler import HandleRequests, status


# Add your imports below this line
from views import SizesView, StylesView, MetalsView, OrdersView



class JSONServer(HandleRequests):

    def do_GET(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        try:
            view.get(self, url["pk"])
        except AttributeError:
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_PUT(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        try:
            view.update(self, self.get_request_body(), url["pk"])
        except AttributeError:
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)

    def do_POST(self):
        # Parse the URL
        url = self.parse_url(self.path)
        # Determine the correct view needed to handle the requests
        view = self.determine_view(url)
        # Get the request body
        disallowed_methods = {
            "metals" : "No additions allowed for this item",
            "styles" : "No additions allowed for this item",
            "sizes" : "No additions allowed for this item"
        }

        requested_resource = url["requested_resource"]

        if requested_resource in disallowed_methods:
            return self.response(disallowed_methods[requested_resource], status.HTTP_405_UNSUPPORTED_METHOD.value)
        try:
            # don't need request body because there isn't one
            # evaluates request body first because of empty ()
            view.add(self, self.get_request_body())
            # view.add(self)
            # as ex shows stack trace in terminal
        except AttributeError as ex: 
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
        # Invoke the correct method on the view

        # Make sure you handle the AttributeError in case the client requested a route that you don't support

        # Once you implement this method, delete the following line of code

    def do_DELETE(self):
        url = self.parse_url(self.path)
        view = self.determine_view(url)

        try:
            view.delete(self, url["pk"])
        except AttributeError:
            return self.response("No view for that route", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
        





    def determine_view(self, url):
        """Lookup the correct view class to handle the requested route

        Args:
            url (dict): The URL dictionary

        Returns:
            Any: An instance of the matching view class
        """
        try:
            routes = {
                "sizes": SizesView,
                "styles": StylesView,
                "metals": MetalsView,
                "orders": OrdersView
            }

            matching_class = routes[url["requested_resource"]]
            return matching_class()
        except KeyError:
            return status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value








#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ''
    port = 8000
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()