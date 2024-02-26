
class RegisterPage:

    def __init__(self,driver):
        self.driver = driver
    def gender_male(self):
        self.driver.find_element("id","gender-male").click()
    def first_name(self,data):
        self.driver.find_element("id","FirstName").send_keys(data)
    def last_name(self,data):
        self.driver.find_element("id","LastName").send_keys(data)
    def email(self,data):
        self.driver.find_element("id","Email").send_keys(data)
    def password(self,data):
        self.driver.find_element("id","Password").send_keys(data)
    def confirm_password(self,data):
        self.driver.find_element("id","ConfirmPassword").send_keys(data)
    def register_button(self):
        self.driver.find_element("xpath","(//input[@type='submit'])[2]").click()
