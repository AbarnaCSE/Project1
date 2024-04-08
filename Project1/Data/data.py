class WebData:
   
   def __init__(self):
       self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
       self.input_data = [
           {"username": "Admin", "password": "admin"},
           {"username": "Admin", "password": "admin123"}
           ] 
       self.firstName = "Gowri"
       self.lastName = "mano"
       self.EmployeeId = "243"
       self.DriversLicenseNumber = "458"
       self.EmployeeName = "Gowri"
       self.loginPageTitle = "Login"
       self.dashboardURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
   def get_credentials(self):
       for data in self.input_data:
           yield data["username"], data["password"] 
