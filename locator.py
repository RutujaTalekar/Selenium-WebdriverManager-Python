#centralized location for all css locator

from selenium.webdriver.common.by import By


#this class will define all the locators for mainpage
class MainPageLocator(object):
	submit_btn = (By.ID,"txt_submit")
	generate_selected_structures_btn = (By.ID, "request-files-btn")
	download_all = (By.ID, "bulk-download")
	gg = (By.ID, "select_all_omg_gg")
	gt = (By.ID, "select_all_omg_gt")
	tg = (By.ID, "select_all_omg_tg")
	structure_count = []
	structure_count = (By.ID, "structureCount")
	list_of_substructure_buttons = (By.XPATH,"//*[starts-with(@id,'download-all-')]");  
class SearchResultsPageLocators(object):
	pass
	#will add stuff in it later as per documentation