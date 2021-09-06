#..........................................................
# webscraping => control browser with selenium
#..........................................................
# control browser with selenium for automated testing
# download file from the internet
# subtitle and add on your movies [many modules]
# get quotes from websites
# get gold and currencies rate
# get news from websites
#..........................................................
# import selenium
# from selenium import __package__
# print(dir(__package__))



from selenium import webdriver   
from webdriver_manager.chrome import ChromeDriverManager
# when you import module => you import as an object with lowercase letter ,
#  to make loop on it to extract its function , but the object connect to it must,
#  but the object connect with it must be upper case to determine that is module like Chrome 
driver = webdriver.Chrome(ChromeDriverManager().install()) 
# driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe") 
driver.get("https://elzero.org")

# between the URL browser and page of the sit you will find : chrome is being controlled by 
# automated test software
driver.find_element_by_css_selector("#search").send_keys("Front-End Developer")
# id search is the value of class search which manage search ,
# put in it send_keys
driver.implicitly_wait(2) # wait 2 second to adapt the speed of the lower internet speed now
driver.find_element_by_css_selector(".search-submit").click()
driver.find_element_by_css_selector(".search-result .result-box:first-of-type h3 a").click()
driver.quit()
