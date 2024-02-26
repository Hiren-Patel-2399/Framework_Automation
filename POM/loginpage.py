class LoginPage:

    def __init__(self,driver):
        self.driver = driver
    def email(self,data):
        self.driver.find_element("id","Email").send_keys(data)
    def password(self,data):
        self.driver.find_element("id","Password").send_keys(data)
    def login_buuton(self):
        self.driver.find_element("xpath","//input[@value='Log in']").click()
