from datetime import datetime

def screenshot(driver):
    d= datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    driver.save_screenshot(f"../Screenshot/{d}.png")