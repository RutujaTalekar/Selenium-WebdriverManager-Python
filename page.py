from locator import *
from element import BasePageElement
#from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import glob,os
from pathlib import Path

class SearchTextElement(BasePageElement):
	locator = "sequence_input"
#To access each web page, contains more of selenium code


#base class for all of the pages, we need to pass it a driver
class BasePage(object):			#@inheritance object is optional
	def __init__(self,driver):	#constructor that will help initialize driver for all the child pages
		self.driver = driver

class MainPage(BasePage):

	#attribute
	search_text_element = SearchTextElement()		#Creating a descriptor (to hide the functionality of underlying module/specific attribute)
	#every time we access the variable search_text_element (set/get) it will use the methods 
	#from element.py
	#MainPage is passed to the set method as obj, a value with it.   



	def is_title_matches(self):
		return "GLYCAM" in self.driver.title

	def click_submit_button(self):
		element = self.driver.find_element(*MainPageLocator.submit_btn)	#defined in locator.py
		#* stands for unpacking tuple, to separate into objects
		element.click()
	
	def check_gg(self):
		element = self.driver.find_element(*MainPageLocator.gg)	#defined in locator.py
		element.click()
		time.sleep(1)

	def check_gt(self):
		element = self.driver.find_element(*MainPageLocator.gt)	#defined in locator.py
		element.click()
		time.sleep(1)

	def check_tg(self):
		element = self.driver.find_element(*MainPageLocator.tg)	#defined in locator.py
		element.click()
		time.sleep(1)

	def check_structure_count(self):
		element = self.driver.find_element(*MainPageLocator.structure_count)
		count = element.text
		flag = True
		if int(count) > 64 :
			print("The structure count on options page for give sequence exceeded 64 ")
			flag = False
		return flag

	def click_generate_default_structures(self):
		element = self.driver.find_element(*MainPageLocator.generate_selected_structures_btn)
		element.click()

	def check_all_conformer_files_ready(self):
		time.sleep(2)		#The locator doesnt get the ids if this sleep time is removed, why? Ids are constant.
		element = self.driver.find_elements(*MainPageLocator.list_of_substructure_buttons)
		#print(element)
		for e in element:
			if  e.get_attribute("href").endswith('(0)'):
				#print(e.get_attribute("href"))
				time.sleep(1)
			else:	
				#print(e.get_attribute("href"))
				print(e.get_attribute("id"),"button is ready")
		pass
	def find_downloaded_file(self, dir):
		#zip_name = "some"
		for i in os.listdir(dir):
			try:
				if i.endswith(".zip"):
					#print("Files with extension .zip are:",i)
					return i
			except FileNotFoundError as e:
				print(e)

	def find_downloaded_file(self, dir):
		#zip_name = "some"
		for i in os.listdir(dir):
			try:
				if i.endswith(".zip"):
					print("Files with extension .zip are:",i)
					return i
			except FileNotFoundError as e:
				print(e)
		
	
	def click_download_all(self):
		element = self.driver.find_element(*MainPageLocator.download_all)
		counter = 1
		cur_dir = os.getcwd()
		#print(cur_dir)
		#project_zip = cur_dir + "/downloads/project.zip"
		dwnld_dir = cur_dir + "/downloads/"
		#print("Iam here")
		while counter <= 10:
			time.sleep(1)
			counter +=1
			#if element.get_attribute("href").endswith('\#'):
			if len(element.get_attribute("href")) > 31:
				time.sleep(2)
				#print(element.get_attribute("href"))
				element.click()
				time.sleep(1)
				downloaded_zip = self.find_downloaded_file(dwnld_dir)
				print("................"+ downloaded_zip + " file downloaded successfully................")
				zip_path = dwnld_dir + downloaded_zip
				#print(zip_path)
				file_size = os.stat(zip_path)
				print("Size of file :", file_size.st_size, "bytes")
				print("Downloaded file has been deleted successfully, bye!")
				return True
		return False

		
class SearchResultPage(BasePage):
	def is_result_found(self):
		return "No results found" not in self.driver.page_source	
		