import time
from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

class LoginPage:

   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(10)

   def quit(self):
       self.driver.quit()

   def login(self):

    try:
        self.boot()
        credentials_generator = data.WebData().get_credentials()
        for username, password in credentials_generator:
            locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, username)
            locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, password)
            locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonlocator)
            time.sleep(5)
            if self.driver.current_url == data.WebData().dashboardURL:
                print("Successfully LoggedIn")
                time.sleep(5)
            else:
                 print("Invalid credentials")
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().PIMlocator)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().Addlocator)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().FirstNameLocator, data.WebData().firstName)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().LastNameLocator, data.WebData().lastName)
        locator.WebLocators().EmployeeText(self.driver, locator.WebLocators().EmployeeIdLocator, data.WebData().EmployeeId)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().Savelocator)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().PIMlocator)
        locator.WebLocators().EmployeeText(self.driver, locator.WebLocators().EmployeeNameLocator, data.WebData().EmployeeName)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().searchlocator)
        time.sleep(5)  
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().editlocator)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().FirstNameLocator, data.WebData().firstName)
        locator.WebLocators().enterText(self.driver, locator.WebLocators().LastNameLocator, data.WebData().lastName)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().savelocator)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().PIMlocator)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().deletelocator)
        locator.WebLocators().clickButton(self.driver, locator.WebLocators().selectlocator)
        time.sleep(5)
    except NoSuchElementException as e:
        print("Error!")
            
    finally:
        self.quit()         
obj = LoginPage()
obj.login()