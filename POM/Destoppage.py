class DestopPage:

    def __init__(self,driver):
        self.driver=driver

    def cheap_computer(self):
        self.driver.find_element("xpath","(//a[@href='/build-your-cheap-own-computer'])[4]").click()
