from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


#this file will represent one element on the page like a search bar, or input element
class BasePageElement(object):
	def __set__(self,obj,value):
		driver = obj.driver
		try:
			#print("pssssss setting the obj")
			WebDriverWait(driver,5).until(
				lambda driver:driver.find_element(By.ID, self.locator))		#lamda- anonymous function
			driver.find_element(By.ID,self.locator).clear()					#empty the field so no garbage value is inserted
			driver.find_element(By.ID,self.locator).send_keys(value)
		except:
			print("I timed out in __set__")


	#any new element that we want to access, we wont have to wait for it separately,
	#set method will implement that functionality
	#Similarly get method gets us the element, we will not have to implement these functionalities
	#again, we can use the basePageElement class

	def __get__(self,obj):
		driver = obj.driver
		try:
			WebDriverWait(driver,5).until(
				lambda driver:driver.find_element(By.ID,self.locator))
			element = driver.find_element(By.ID, self.locator)
			return element.getAttribute("value")		#get the attribute from html template of "value" and return it
		except:
			print("I timed out in __get__")
		#these will be used for every object

	

	#Search_text_element = "DManpa1-3[DManpa1-2DManpa1-6DManpa1-6]DManpb1-4DGlcpNAcb1-4DGlcpNAcb1-OH"


