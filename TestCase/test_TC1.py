from Generic.verifytitle import *
from POM.registerpage import *
from POM.welcomepage import *

def test_TC1(launch):
    driver=launch
    verify_title(driver,"Demo Web Shop")
    w1=WelcomePage(driver)
    w1.register_link()
    verify_title(driver,"Demo Web Shop. Register")
    r=RegisterPage(driver)
    r.gender_male()
    r.first_name("selhiren")
    r.last_name("motion")
    r.email("gandhi123@gmail.com")
    r.password("selen@123")
    r.confirm_password("selen@123")
    r.register_button()
    verify_title(driver,"Demo Web Shop. Register")
    b=WelcomePage(driver)
    b.register_btn()
    w=WelcomePage(driver)
    w.logout_link()
    verify_title(driver,"Demo Web Shop")