from Generic.takescreenshot import *
def verify_text(driver,etext):
    try:
        assert etext in driver.page_source
    except:
        screenshot(driver)
        raise Exception