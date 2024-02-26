from Generic.verifytitle import *
from POM.loginpage import *
from POM.welcomepage import *
from POM.Apparelshoespage import *
from POM.Sneakershoespage import *


def test_TC3(launch):
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

    apsh=WelcomePage(driver)
    apsh.Apparel_shoes()
    verify_title(driver,"Demo Web Shop. Apparel & Shoes")

    shoes=ApparelshoesPage(driver)
    shoes.blue_sneaker()
    verify_title(driver,"Demo Web Shop. Blue and green Sneaker")

    spge=SneakerShoesPage(driver)
    spge.add_wishlist()
    # verify_text(driver,"The product has been added to your")

    wishlist=SneakerShoesPage(driver)
    wishlist.wishlist()
    verify_title(driver,"Demo Web Shop. Wishlist")

    l=WelcomePage(driver)
    l.logout_link()
    verify_title(driver,"Demo Web Shop")




