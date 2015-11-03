from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


#driver = webdriver.Firefox()
#driver.get("https://www.expedia.co.in/Activities")
#assert "Activities" in driver.title
#elem1 = driver.find_element_by_id("activity-destination")
place = input("Enter the destination: ")


#elem2 = driver.find_element_by_id("activity-start")
d1 = input("Enter the start date(dd/mm/yyyy): ")

#elem3 = driver.find_element_by_id("activity-end")
d2 = input("Enter the end date(dd/mm/yyyy): ")

#elem1.send_keys(place)
#elem2.send_keys(d1)
#elem3.send_keys(d2)
#elem1.send_keys(Keys.RETURN)



## get the Firefox profile object
firefoxProfile = FirefoxProfile()
## Disable CSS
firefoxProfile.set_preference('permissions.default.stylesheet', 2)
## Disable images
firefoxProfile.set_preference('permissions.default.image', 2)
## Disable Flash
firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so',
                              'false')
## Set the modified profile while creating the browser object 
driver= webdriver.Firefox(firefoxProfile)

driver.get("https://www.expedia.co.in/things-to-do/?location="+place+"&startDate="+d1+"&endDate="+d2)

assert "Sorry, we're unable to find things to do" not in driver.page_source
#scheight = .1
#while scheight < 9.9:
#    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
#    scheight += .01
all_spans = driver.find_elements_by_class_name("activity-tile")
i=0
elem4 = driver.find_elements_by_class_name("tile-name")
elem5 = driver.find_elements_by_class_name("tile-activity-duration")
elem6 = driver.find_elements_by_class_name("tile-duration")
elem7 = driver.find_elements_by_class_name("activityFromPrice")

for span in all_spans:
	print("Details: "+elem4[i].text)
	print("Activity "+elem5[i].text)
	if(len(elem6[i].find_elements_by_class_name("tile-freeCancellation")) > 0):
		print ("Free cancellation")
	else:
		print ("No Free cancellation")
	print("Price: "+elem7[i].text)
	i = i+1
	print('')
	print('')

driver.close()