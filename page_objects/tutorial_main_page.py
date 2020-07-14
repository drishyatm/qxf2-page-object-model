"""
This class models the codecademy login page.
URL: login

"""
from utils.Wrapit import Wrapit
from .Base_Page import Base_Page
"""
from .form_object import Form_Object
from .header_object import Header_Object
from .table_object import Table_Object
from .footer_object import Footer_Object

"""


class Tutorial_Main_Page(Base_Page):
    "Page Object for the tutorial's main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'login'
        print("launching the page")
        self.open(url)
