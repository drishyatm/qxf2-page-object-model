"""
This class models the codecademy login page.
URL: login

"""

from .Base_Page import Base_Page
from .codecademy_login_page_objects import Codecademy_Login_Page_Objects



class Codecademy_Login_Page(Base_Page, Codecademy_Login_Page_Objects):
    "Page Object for the Codecademy Login page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'login'
        print("launching the page")
        self.open(url)
