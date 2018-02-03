import sys
import re
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from customip import customIP

PROTOCOLS_TO_MATCH=['http','https','http-proxy']

DRIVER = '../resources/chromedriver.exe'

def setOptions():
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--allow-running-insecure-content')
	options.add_argument('--process-per-site')
	options.add_argument('--disable-plugins')
	options.add_argument('--hide-scrollbars')
	options.add_argument('--log-level=3');
	options.add_argument('--silent');
	return options

def setProperties(driver):
	driver.set_window_size(1920,1080)
	driver.set_page_load_timeout(20)

def takeScreenshotIP(IP,PATH):
	driver = webdriver.Chrome(DRIVER)
	setProperties(driver)
	index = int(0)
	for actualPROTOCOL in IP.get_protocols():
		actualPROTOCOL.replace('?','')
		if(actualPROTOCOL=="ssl/http" or actualPROTOCOL=="ssl/https" or actualPROTOCOL=="ssl"):
			actualPROTOCOL="https"
		if actualPROTOCOL in PROTOCOLS_TO_MATCH:
			driver.get(actualPROTOCOL+"://"+IP.get_address()+":"+IP.get_ports()[index])
			try:
				context.driver.switch_to.alert.dismiss()
			except:	
				screenshot = driver.save_screenshot(PATH+IP.get_address()+"_"+IP.get_ports()[index]+"_"+actualPROTOCOL+".png")
			else:
				screenshot = driver.save_screenshot(PATH+IP.get_address()+"_"+IP.get_ports()[index]+"_"+actualPROTOCOL+".png")	
			print("Saved screenshot: "+PATH+IP.get_address()+"_"+IP.get_ports()[index]+"_"+actualPROTOCOL)
		index+=1
	driver.quit()
	return 0

def takeScreenshotFullURL(URL,PATH):
	options = setOptions()
	driver = webdriver.Chrome(DRIVER,chrome_options=options)
	setProperties(driver)
	err = 0
	save_path = PATH+URL.replace('/','').replace(':','_')+".png"
	try:
		driver.get(URL)
	except:
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