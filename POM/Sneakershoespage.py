class SneakerShoesPage:

    def __init__(self,driver):
        self.driver= driver

    def add_wishlist(self):
        self.driver.find_element("xpath","//input[@id='add-to-wishlist-button-28']").click()

    def wishlist(self):
        self.driver.find_element("xpath","//a[.='Wishlist']").click()
