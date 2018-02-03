import sys
import re
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys

class ScreenshotDownloader:
	# Default values for attributes
	horizontal_screenshot_resolution = 1366
	vertical_screenshot_resolution = 768
	chromedriver_path = "../resources/chromedriver"
	site_load_timeout = "7"
	options = webdriver.ChromeOptions()

	def __init__(self):
		super(ScreenshotDownloader, self).__init__()
		# self.arg = arg
		self.setOptions()

	def setScreenshotResolution(self,horizontal_resolution,vertical_resolution):
		self.horizontal_screenshot_resolution = horizontal_resolution
		self.vertical_screenshot_resolution = vertical_resolution
		# print("Resolution = ",self.horizontal_resolution,"x",self.vertical_resolution)

	def setChromedriverPath(self,path):
		self.chromedriver_path=path

	def setSiteLoadTimeout(self,timeout):
		self.site_load_timeout=timeout
		
	def setOptions(self):
		self.options.add_argument('--headless')
		self.options.add_argument('--disable-gpu')
		self.options.add_argument('--ignore-certificate-errors')
		self.options.add_argument('--allow-running-insecure-content')
		self.options.add_argument('--process-per-site')
		self.options.add_argument('--disable-plugins')
		self.options.add_argument('--hide-scrollbars')
		self.options.add_argument('--log-level=3');
		self.options.add_argument('--silent');

	def setProperties(self,driver):
		driver.set_window_size(self.horizontal_screenshot_resolution, self.vertical_screenshot_resolution)
		driver.set_page_load_timeout(self.site_load_timeout)

	def takeScreenshot(self,URL,PATH):
		driver = webdriver.Chrome(self.chromedriver_path,chrome_options=self.options)
		self.setProperties(driver)
		err = 0
		save_path = PATH+URL.replace('/','').replace(':','_')+".png"
		try:
			driver.get(URL)
		except:
			print("Error getting ",URL,"!")
			driver.quit()
			return 1
		try:
			context.driver.switch_to.alert.dismiss()
			screenshot = driver.get_screenshot_as_file(save_path)
			print("[",err,"]  Saved screenshot on : ",save_path,sep='',file=sys.stderr)
			driver.close()
			driver.quit()
			return 0
		except:	
			screenshot = driver.get_screenshot_as_file(save_path)
			err = 1
			print("[",err,"]  Saved screenshot on : ",save_path,sep='',file=sys.stderr)
			driver.close()
			driver.quit()
			return 0
		return 0