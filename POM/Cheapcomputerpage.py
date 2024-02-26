class CheapComPage:

    def __init__(self,driver):
        self.driver=driver

    def add_cart(self):
        self.driver.find_element("xpath","//input[@id='add-to-cart-button-72']").click()

    def shopping_cart(self):
        self.driver.find_element("xpath","//span[.='Shopping cart']").click()
