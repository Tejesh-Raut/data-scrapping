from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.expedia.co.in/Activities")
assert "Activities" in driver.title
elem1 = driver.find_element_by_id("activity-destination")
place = input("Enter the destination: ")


elem2 = driver.find_element_by_id("activity-start")
d1 = input("Enter the start date(dd/mm/yyyy): ")

elem3 = driver.find_element_by_id("activity-end")
d2 = input("Enter the end date(dd/mm/yyyy): ")

elem1.send_keys(place)
elem2.send_keys(d1)
elem3.send_keys(d2)
elem1.send_keys(Keys.RETURN)

assert "Sorry, we're unable to find things to do" not in driver.page_source
scheight = .1
while scheight < 9.9:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
    scheight += .01
all_spans = driver.find_elements_by_class_name("activity-tile")
i=0
elem4 = driver.find_elements_by_class_name("tile-name")
elem5 = driver.find_elements_by_class_name("tile-activity-duration")

elem7 = driver.find_elements_by_class_name("activityFromPrice")

for span in all_spans:
	print("Details: "+elem4[i].text)
	print("Activity "+elem5[i].text)
	elem6 = driver.find_element_by_class_name("tile-free-cancel")
	print(elem6.text)
	
	print("Price: "+elem7[i].text)
	i = i+1
	print('')
	print('')
driver.close()