"""
This class models the redirect page of the Selenium tutorial
URL: selenium-tutorial-redirect
The page consists of a header, footer and some text
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Codecademy_SQL_Course_Page(Base_Page):
    "Page Object for the Catalog page"

    # locators
    heading_course_sql = locators.heading_course_sql
    sql_course_path = locators.sql_course_path
    recommended_path_sql = locators.recommended_path_sql
    recommeded_course_sql_path = locators.recommeded_course_sql_path
    redirect_title_course = "Learn SQL"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'catalog/language/sql'
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading_course_sql)
        self.conditional_write(result_flag,
                               positive='Correct heading present on SQL Course page',
                               negative='Heading on SQL Course Page is INCORRECT!!',
                               level='debug')

        return result_flag
      

    @Wrapit._exceptionHandler
    def check_recommended(self):
        " Click the SQL course in catalog page"
        result_flag = self.check_element_present(self.recommended_path_sql)
        self.conditional_write(result_flag,
                               positive='Verified the Recommended course in SQL',
                               negative='Could not verify the Recommeded course in SQL ',
                               level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sql_course(self):
        " Click the SQL course in SQL Course page"
        result_flag = self.click_element(self.recommeded_course_sql_path)
        self.conditional_write(result_flag,
                               positive='Clicked on the SQL in the SQL course page ',
                               negative='Could not click on the SQL course in SQL course page',
                               level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def check_redirect(self):
        "Check if we have been redirected to the learn SQL course page"
        result_flag = False
        print(self.driver.title)
        if self.redirect_title_course in self.driver.title:
            result_flag = True
            self.switch_page("Learn SQL course page")

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_course_sql(self):
        "Selecting the course"
        result_flag = self.check_heading()
        result_flag &= self.check_recommended()
        result_flag &= self.click_sql_course()
        result_flag &= self.check_redirect()

        return result_flag
