
import re
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#joining connection
browser = webdriver.Chrome("/home/oxygen_/Documents/chromedriver")
browser.get('https://www.instagram.com')

#clicking the login button
login_elem = browser.find_element(By.XPATH,'//a[text()="Log in"]')
login_elem.click()

#find forms inputs and enter data
inputs = browser.find_elements_by_xpath('//input')



ActionChains(browser).move_to_element(inputs[0]).click()\
					 .send_keys('poetofnights')\
					 .move_to_element(inputs[1]).click()\
					 .send_keys('username')\
					 .perform()

login_button = browser.find_elements_by_xpath(
				'//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/span/button')

ActionChains(browser)\
			.move_to_element(login_button[0])\
			.click().perform()
time.sleep(5)

search_but = browser.find_elements_by_xpath(
	'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'
	)

ActionChains(browser)\
	.move_to_element(search_but[0]).click()\
	.send_keys('poets')\
	.send_keys(Keys.ENTER).perform()

time.sleep(5)


accn = browser.find_elements_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div/span')



ActionChains(browser)\
	.move_to_element(accn[0]).click().perform();

time.sleep(5)

xPathLink = "//a[contains(@href,'followers')]"

followers_count = browser.find_elements_by_xpath(xPathLink)

ActionChains(browser).move_to_element(followers_count[0]).click().perform()
time.sleep(5)

eles = browser.find_elements_by_class_name('_6e4x5')
for ele in eles :
	x = ele.find_element_by_tag_name('a') 
	zz = x.get_attribute("href")
	print(zz)

'''for _ in range(3) :
	body_elem_2.send_keys(Keys.END)
	time.sleep(5)
	body_elem_2.send_keys(Keys.HOME)
	time.sleep(5)
'''

time.sleep(5000000)
