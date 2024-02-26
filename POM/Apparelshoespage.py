class ApparelshoesPage:

    def __init__(self,driver):
        self.driver=driver

    def blue_sneaker(self):
        self.driver.find_element("xpath","(//a[@href='/blue-and-green-sneaker'])[2]").click()
