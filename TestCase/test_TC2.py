from Generic.verifytitle import *
from POM.loginpage import *
from POM.welcomepage import *
from POM.Computerpage import *
from POM.Destoppage import *
from POM.Cheapcomputerpage import *


def test_TC2(launch):
    driver=launch
    verify_title(driver,"Demo Web Shop")
    w=WelcomePage(driver)
    w.login_link()
    verify_title(driver,"Demo Web Shop. Login")

    l=LoginPage(driver)
    l.email("sren@gmail.com")
    l.password("selen@123")
    l.login_buuton()
    verify_title(driver,"Demo Web Shop")

    h=WelcomePage(driver)
    h.computer_link()
    verify_title(driver,"Demo Web Shop. Computers")

    d=ComputerPage(driver)
    d.destop_link()
    verify_title(driver,"Demo Web Shop. Desktops")

    click=DestopPage(driver)
    click.cheap_computer()
    verify_title(driver,"Demo Web Shop. Build your own cheap computer")

    ac=CheapComPage(driver)
    ac.add_cart()

    sh=CheapComPage(driver)
    sh.shopping_cart()
    verify_title(driver,"Demo Web Shop. Shopping Cart")

    l=WelcomePage(driver)
    l.logout_link()
    verify_title(driver,"Demo Web Shop")





