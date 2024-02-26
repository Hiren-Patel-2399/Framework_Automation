class WelcomePage:
    def __init__(self,driver):
        self.driver= driver
    def register_link(self):
        self.driver.find_element("xpath","//a[.='Register']").click()

    def register_btn(self):
        self.driver.find_element("xpath","(//input[@type='button'])[2]").click()
    def login_link(self):
        self.driver.find_element("xpath","//a[.='Log in']").click()
    def logout_link(self):
        self.driver.find_element("xpath","//a[.='Log out']").click()

    def computer_link(self):
        self.driver.find_element("xpath","(//a[@href='/computers'])[1]").click()

    def Apparel_shoes(self):
        self.driver.find_element("xpath","(//a[contains(.,'Apparel & Shoes')])[1]").click()