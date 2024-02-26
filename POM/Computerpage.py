class ComputerPage:

    def __init__(self,driver):
        self.driver=driver

    def destop_link(self):
        self.driver.find_element("xpath","(//a[@href='/desktops'])[4]").click()