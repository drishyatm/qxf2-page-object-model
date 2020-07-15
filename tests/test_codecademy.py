"""
This test file will help you get started in writing a new test using our framework
"""

import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import conf.login_page_conf as conf
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser

@pytest.mark.GUI
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

        #  Get the test details from the conf file
        user_name = conf.user_name
        code_password = conf.password

        #  Set username  in login
        result_flag = test_obj.set_user_name(user_name)
        test_obj.log_result(result_flag,
                            positive="Username was successfully set to: %s\n" % user_name,
                            negative="Failed to set name: %s \nOn url: %s\n" % (user_name, test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time()-start_time)))

        # Set passowrd in login
        result_flag = test_obj.set_password(code_password)
        test_obj.log_result(result_flag,
                            positive="Password was successfully set to: %s\n" % code_password,
                            negative="Failed to set Password: %s \nOn url: %s\n" % (code_password, test_obj.get_current_url()))
        test_obj.write('Script duration: %d seconds\n' %
                       (int(time.time() - start_time)))

        # Set and log in to Codecademy
        result_flag = test_obj.submit_form(user_name, code_password)
        test_obj.log_result(result_flag,
                            positive="Successfully submitted the form\n",
                            negative="Failed to submit the form \nOn url: %s" % test_obj.get_current_url(),
                            level="critical")

        # 13. Print out the result
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
        print(option_obj.print_usage())
