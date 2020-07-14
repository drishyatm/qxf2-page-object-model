
"""
This class models the main login  page.
URL: 
The page consists of login
"""
from .Base_Page import Base_Page
import conf.base_url_conf
from utils.Wrapit import Wrapit


class Login_page(Base_Page):

    "Page Object for the Login  page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = conf.base_url
        self.open(url)
