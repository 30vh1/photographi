import sys
import re
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Firefox, FirefoxProfile

class ScreenshotDownloader:
	# Default values for attributes
	horizontal_screenshot_resolution = 1366
	vertical_screenshot_resolution = 768
	driver_path = "../resources/chromedriver"
	site_load_timeout = "7"
	browser = "Chrome"
	options = webdriver.ChromeOptions()
	capabilities = DesiredCapabilities.CHROME.copy()
	profile = FirefoxProfile()

	def __init__(self):
		super(ScreenshotDownloader, self).__init__()
		# self.arg = arg
		# self.setOptions()

	def setScreenshotResolution(self,horizontal_resolution,vertical_resolution):
		self.horizontal_screenshot_resolution = horizontal_resolution
		self.vertical_screenshot_resolution = vertical_resolution

	def setDriverPath(self,path):
		self.driver_path=path

	def setSiteLoadTimeout(self,timeout):
		self.site_load_timeout=timeout

	def setBrowser(self,browser):
		self.browser=browser
		self.setOptions()
		
	def setOptions(self):
		if self.browser == "Chrome":
			# self.options.add_argument('--headless')
			self.options.add_argument('--disable-gpu')
			self.options.add_argument('--ignore-certificate-errors')
			self.options.add_argument('--allow-running-insecure-content')
			self.options.add_argument('--process-per-site')
			self.options.add_argument('--disable-plugins')
			self.options.add_argument('--hide-scrollbars')
			self.options.add_argument('--log-level=3');
			self.options.add_argument('--silent');
		elif self.browser == "Firefox":
			self.capabilities = DesiredCapabilities.FIREFOX.copy()
			self.capabilities['platform'] = "WINDOWS"
			print(self.capabilities)
			self.options = Options()
			profile = FirefoxProfile()
			profile.set_preference('security.insecure_field_warning.contextual.enabled', False)
			profile.set_preference('security.insecure_password.ui.enabled', False)
			profile.set_preference('dom.ipc.processCount', 1)
			profile.set_preference('browser.tabs.remote.autostart.2',False)
			self.options.add_argument("-headless")
			self.options.add_argument("-new-tab")
			# self.options.add_argument("-browser")
			self.options.add_argument("-no-remote")
			self.options.add_argument("-no-first-run")
			self.options.add_argument("-app")


	def setProperties(self,driver):
		driver.set_window_size(self.horizontal_screenshot_resolution, self.vertical_screenshot_resolution)
		driver.set_page_load_timeout(self.site_load_timeout)

	def createWebdriver(self):
		if self.browser == "Firefox":
			# print(self.capabilities["moz:firefoxOptions"])	
			driver = webdriver.Firefox(firefox_profile=self.profile,firefox_options=self.options,executable_path=self.driver_path,capabilities=self.capabilities)
		elif self.browser == "Chrome":
			driver = webdriver.Chrome(self.driver_path,chrome_options=self.options)
		return driver

	def takeScreenshot(self,URL,PATH):
		driver = self.createWebdriver()
		self.setProperties(driver)
		err = 0
		save_path = PATH+URL.replace('/','').replace(':','_')+".png"
		try:
			driver.get(URL)
		except:
			print("Error getting ",URL,"!",sep="",file=sys.stderr)
			driver.quit()
			return 1
		try:
			context.driver.switch_to.alert.dismiss()
			screenshot = driver.get_screenshot_as_file(save_path)
			print("[",err,"]  Saved screenshot on : ",save_path,sep='',file=sys.stderr)
			driver.close()
			driver.quit()
			# return 0
		except:	
			screenshot = driver.get_screenshot_as_file(save_path)
			err = 1
			print("[",err,"]  Saved screenshot on : ",save_path,sep='',file=sys.stderr)
			driver.close()
			# if driver != null:
			# 	driver.quit()
			return 0
		return 0