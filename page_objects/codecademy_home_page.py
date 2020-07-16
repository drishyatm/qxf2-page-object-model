"""
This class models the redirect page of the Selenium tutorial
URL: selenium-tutorial-redirect
The page consists of a header, footer and some text
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Codecademy_Home_Page(Base_Page):
    "Page Object for the Codecademy Home page"

    # locators
    heading = locators.heading
    
    catalog_path = locators.catalog_path
    redirect_title_catalog = "All Courses & Tutorials"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'learn'
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading_home(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading)
        self.conditional_write(result_flag,
                               positive='Correct heading present on Home page',
                               negative='Heading on Home page is INCORRECT!!',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_catalog(self):
        " Click the catalog in home page"
        result_flag = self.click_element(self.catalog_path)
        self.conditional_write(result_flag,
                               positive='Clicked on the catalog on home page',
                               negative='Could not click on the catalog on home page',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect_catalog(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False
        print(self.driver.title)
        if self.redirect_title_catalog in self.driver.title:
            result_flag = True
            self.switch_page("Catalog page")
        
        
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def go_to_catalog(self):
        "Click  the Catalog page"
        result_flag = self.check_heading_home()
        result_flag &= self.click_catalog()
        result_flag &= self.check_redirect_catalog()
        print("gotocatalog",result_flag)
        return result_flag
