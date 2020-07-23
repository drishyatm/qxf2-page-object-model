"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. Zero page
2. Tutorial Main page
3. Codecademy_Home_Page
4. Codecademy Catalog_Page
5. Codecademy_SQL_Course_Page
6. Codecademy_Enroll_SQL_Course_Page
"""


import conf.base_url_conf
from page_objects.zero_page import Zero_Page
from page_objects.codecademy_login_page import Codecademy_Login_Page
from page_objects.codecademy_home_page import Codecademy_Home_Page
from page_objects.codecademy_catalog_page import Codecademy_Catalog_Page
from page_objects.codecademy_sql_course_page import Codecademy_SQL_Course_Page
from page_objects.codecademy_enroll_sql_course_page import Codecademy_Enroll_SQL_Course_Page


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name, base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["zero", "zero page", "agent zero"]:
            test_obj = Zero_Page(base_url=base_url)
        elif page_name == "main page":
            test_obj = Codecademy_Login_Page(base_url=base_url)
        elif page_name == "home page":
            test_obj = Codecademy_Home_Page(base_url=base_url)
        elif page_name == "catalog page":
            test_obj = Codecademy_Catalog_Page(base_url=base_url)
        elif page_name == "sql course page":
            test_obj = Codecademy_SQL_Course_Page(base_url=base_url)
        elif page_name == "learn sql course page":
            test_obj = Codecademy_Enroll_SQL_Course_Page(base_url=base_url)
            
        else:
            print("not working AAA")

        return test_obj

    get_page_object = staticmethod(get_page_object)
