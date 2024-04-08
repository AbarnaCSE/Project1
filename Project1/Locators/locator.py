from selenium.webdriver.common.by import By  
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

class WebLocators:

   def __init__(self):
       self.usernameLocator = "username"
       self.passwordLocator = "password"
       self.FirstNameLocator = "firstName"
       self.LastNameLocator = "lastName"
       self.DriversLicenseNumberLocator = "input.oxd-input.oxd-input--active[fdprocessedid='wyvrfe']"
       self.buttonlocator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
       self.PIMlocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
       self.Addlocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
       self.Savelocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
       self.EmployeeIdLocator = "input[data-v-1f99f73c].oxd-input.oxd-input--active"  
       self.EmployeeNameLocator = "input[data-v-75e744cd]"
       self.searchlocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'   
       self.editlocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]'
       self.savelocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
       self.deletelocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]' 
       self.selectlocator ='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]' 
   def enterText(self, driver, value, textValue):
       element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, value)))
       element.send_keys(textValue)
   def clickButton(self,driver, value):
       element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))
       element.click()
   def EmployeeText(self, driver, value, textValue):
       element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
       element.send_keys(textValue)
   def editButton(self,driver, value):
       element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
       element.click()    
    





    
   

    

       

