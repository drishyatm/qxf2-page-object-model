"""
This class models the redirect page of the Selenium tutorial
URL: selenium-tutorial-redirect
The page consists of a header, footer and some text
"""
from utils.Wrapit import Wrapit
from .Base_Page import Base_Page
import conf.locators_conf as locators
import conf.catalog_page_conf as courses

class Codecademy_Catalog_Page(Base_Page):
    "Page Object for the Catalog page"

    # locators
    heading_catalog = locators.heading_catalog
    sql_course_path = locators.sql_course_path
    course_name = courses.course_name
    redirect_title_course = courses.redirect_title_course

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'catalog/all'
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading_catalog)
        self.conditional_write(result_flag,
                               positive='Correct heading present on Catalog page',
                               negative='Heading on Catalog page is INCORRECT!!',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sql_course(self):
        " Click the SQL course in catalog page"
        result_flag = self.click_element(self.sql_course_path%self.course_name)
        self.conditional_write(result_flag,
                               positive='Clicked on the SQL course ',
                               negative='Could not click on the SQL course',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect(self):
        "Check if we have been redirected to the course page"
        result_flag = False
        print(self.driver.title)
        if self.redirect_title_course in self.driver.title:
            result_flag = True
            self.switch_page("SQL course page")

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_course(self):
        "Selecting the course"
        result_flag = self.check_heading()
        result_flag &= self.click_sql_course()
        result_flag &= self.check_redirect()

        return result_flag
