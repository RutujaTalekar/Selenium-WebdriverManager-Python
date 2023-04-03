#Test written to check if cb app generates output for following sequences - 

#1. Test with DManpa1-OH, because it is quick, and people tend to test with that first, 
#so it can be a test for reusing previous builds, which is important. It also should skip 
#the options page and go straight to downloads. If it takes time while it minimizes, 
#test it again to verify that reusing previous builds happens fast.


#2. Test with DManpa1-6DManpa1-6DManpa1-OH because it provides rotamer options, 
#meaning you will reach the options page. Also tends to be previously built. 
#If in a rush, select down to 2 builds. If being thorough, do more.

#NOTE- following test will only work on chrome

import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import page
import sys
import os
from pathlib import Path


#This class contains the test cases that needs to be performed
#You can create multiple of such classes, but one class should be able to handle one app
class GLYCAM_cb_testSuit(unittest.TestCase):
	cur_dir = os.getcwd()
	downloads = cur_dir + "/downloads"
	try:
		#ip = sys.argv[0]
		browser = sys.argv[1]
	except:
		print("----------------------------\nPlease provide the choice of browser. \nExample: python3 main.py chrome \n----------------------------\nCurrently we only support the following choices for browser - chrome, firefox")
		quit()
	
	
	def readIp(self):
		cur_dir = os.getcwd()
		p = Path(cur_dir)
		proxy = p.parent.parent.parent.parent.parent.parent
		#print(proxy)
		env = str(proxy) + "/Proxy/env.txt"
		#print(env)
		with open(env,'r') as f:
			lines = f.read()
		lines.replace('\n'," ")
		self.ip = lines
		#print(lines)
		#print(type(self.ip))
#this is like init method, whatever you will need in the program later can be 
#added in this method. This method is called before every test method executes, each time.
	#@classmethod
	#def setUpClass(self):
	def setUp(self):
		print("\n")
		print("************************************************************************")
		print("Setting up the driver")		
		
		if self.browser == "chrome":
			options = webdriver.ChromeOptions()
			prefs = {"download.default_directory" : self.downloads}
			options.add_experimental_option("prefs",prefs)
			self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
			
	#Change downloads directory, test
		elif self.browser == "firefox":
			#profile = webdriver.FirefoxProfile()
			options = Options()
			options.set_preference("browser.download.folderList", 2)
			options.set_preference("browser.download.manager.showWhenStarting", False)
			options.set_preference("browser.download.dir", self.downloads)
			options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
			self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)

			

		else:
			print("Enter a valid browser")
		self.readIp()
		self.driver.maximize_window()
		self.ip = '''http://'''+self.ip + '''/txt/'''
		self.driver.get(self.ip)
		print("\n")


#any method which starts with "test" keyword, will be treated as test

#demo test
	def demo_test_title(self):
		print("Reached:Does title matches")
		mainPage = page.MainPage(self.driver)
		assert mainPage.is_title_matches()

#The following test checks if cb app generates all the files successfully, skips options page. 
	def test_check_cb_flow1(self):
		print("Reached:CB app test1 | Building with text - DManpa1-OH | goodluck :)")
		mainPage = page.MainPage(self.driver)	
		mainPage.search_text_element = "DManpa1-OH"
		print("Reached:CB app test1 | Setting sequence name")
		mainPage.click_submit_button()
		print("Reached:CB app test1 | Downloads page")
		mainPage.check_all_conformer_files_ready()
		file_download_check = mainPage.click_download_all()
		#print("Reached:CB app test2 | All structures are minimized, downloaded file is above -- MB")
		time.sleep(1)
		assert file_download_check

#The following test checks if cb app hits options page and then generates all the files successfully.
	def test_check_cb_flow2(self):
		print("Reached:CB app test2 | Building with text - DManpa1-6DManpa1-6DManpa1-OH | goodluck :)")
		mainPage = page.MainPage(self.driver)	
		mainPage.search_text_element = "DManpa1-6DManpa1-6DManpa1-OH"
		print("Reached:CB app test2 | Setting sequence name")
		mainPage.click_submit_button()
		print("Reached:CB app test2 | Options page, choose all available rotamersclick on generate seq")
		mainPage.check_gg()
		mainPage.check_gt()
		mainPage.check_tg()
		print("Reached:CB app test2 | Options page, check if structure count exceeds 64")
		flag = mainPage.check_structure_count()
		#print(flag)
		if flag == False:
			assert True		#The test stops if the structure count exceeds 64
		else:
			print("Reached:CB app test2 | Options page, click on generate structures")
			mainPage.click_generate_default_structures()
			print("Reached:CB app test2 | Downloads page")
			mainPage.check_all_conformer_files_ready()
			file_download_check = mainPage.click_download_all()
			#print("Reached:CB app test2 | All structures are minimized, downloaded file is above -- MB")
			time.sleep(1)
			assert file_download_check


#this is cleanup method, Just like setUp, it runs after each test case.
	#@classmethod
	#def tearDownClass(self):
	def tearDown(self):
		for f in Path(self.downloads).glob('*.zip'):
			try:
				f.unlink()
			except OSError as e:
				print("Error: %s : %s" % (f, e.strerror))
		self.driver.quit()


if __name__ == "__main__":
	if len(sys.argv) > 0:
		GLYCAM_cb_testSuit.browser = sys.argv.pop()
		#GLYCAM_cb_testSuit.ip = sys.argv.pop()
	unittest.main()
