
from utils.Wrapit import Wrapit
import conf.locators_conf as locators
from .Base_Page import Base_Page


"""
This class models the Codecademy page of the Enrolling the course 
URL: learn/learn-sql
Verify the heading, click on start button of the course and verify the redirect
"""


class Codecademy_Enroll_SQL_Course_Page(Base_Page):
    "Page Object for the Enroll Course Page page"

    # locators
    heading_learn_sql = locators.heading_learn_sql
    enroll_course_button = locators.enroll_course_button
    redirect_title_course = ""

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'learn/learn-sql'
        self.open(url)

    @Wrapit._exceptionHandler
    def check_heading(self):
        "Check if the heading exists"
        result_flag = self.check_element_present(self.heading_learn_sql)
        self.conditional_write(result_flag,
                               positive='Correct heading present on SQL Course page',
                               negative='Heading on SQL Course Page is INCORRECT!!',
                               level='debug')

        return result_flag

   
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_start_course(self):
        " Click the Start button in Learn SQL Course page"
        result_flag = self.click_element(self.enroll_course_button)
        self.conditional_write(result_flag,
                               positive='Clicked on the Start button  in the Learn SQL course page ',
                               negative='Could not click on the Start button Learn SQL course page',
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
            #self.switch_page("Learn SQL course page")

        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_enroll_course_sql(self):
        "Selecting the course"
        result_flag = self.check_heading()
        result_flag &= self.click_start_course()
        #result_flag &= self.check_redirect()

        return result_flag
