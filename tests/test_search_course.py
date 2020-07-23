"""
This is for end to end scenario for searching course . 
Logging in to the codecademy
Home page click the search icon 
Type the search course name 
verify the search page with title 
Click on search icon again 
click on any of the popular search course ( selected html)
"""
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Option_Parser import Option_Parser
from page_objects.PageFactory import PageFactory
import conf.login_page_conf as conf
import conf.home_page_conf as home_page_conf

def test_codecademy(test_obj):
    "Run the test"
    try:
    
        # Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        # Set start_time with current time
        start_time = int(time.time())

        # This is the test object, you can change it to the desired page with relevance to the page factory
        test_obj = PageFactory.get_page_object("Main page")

        # Turn on the highlighting feature
        test_obj.turn_on_highlight()

        #  Get the login details from the conf file for login page
        user_name = conf.user_name
        code_password = conf.password
        
        #  Get the  details from the conf file for home page
        search_text_course = home_page_conf.search_text_course
     
        # Set and log in to Codecademy
        result_flag = test_obj.submit_form(user_name, code_password)
        test_obj.log_result(result_flag,
                            positive="Successfully submitted the form\n",
                            negative="Failed to submit the form \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")

        # Selecting course from catalog
        result_flag = test_obj.search_course(search_text_course)
        test_obj.log_result(result_flag,
                            positive="Course in search bar was successful\n",
                            negative="Search looks wrong.%s" % test_obj.get_current_url(),
                            level="critical")
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))
        
        
        #  Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception when trying to run test: %s" % __file__)
        print("Python says:%s" % str(e))

    assert expected_pass == actual_pass, "Test failed: %s" % __file__


# ---START OF SCRIPT
if __name__ == '__main__':
    print("Start of %s" % __file__)
    # Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()

    # Run the test only if the options provided are valid
    if options_obj.check_options(options):
        test_obj = PageFactory.get_page_object("Zero", base_url=options.url)

        # Setup and register a driver
        test_obj.register_driver(options.remote_flag, options.os_name, options.os_version, options.browser,
                                 options.browser_version, options.remote_project_name, options.remote_build_name)

        test_codecademy(test_obj)

        # teardowm
        test_obj.wait(3)
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(options_obj.print_usage())
