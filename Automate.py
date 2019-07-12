##...........performs basic functionality completely..............##
##........Function : Runs all test cases in folder MDS ONLINE and stores ouput of 'DEV_POS' folder in output.txt file.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


##.........This is script to automate work on T3 web application using Google Chrome web browser............##


##...........Variables...............................................................##
path = 'C:\\Users\\e086441\\Downloads\\chromedriver'
t3_link = 'https://ech-10-157-136-229:8443/index.html'
username_id = 'textfield-4159-inputEl'
username = 'ASMITAC'
password_id = 'textfield-4160-inputEl'
password = 'asmitac'
login_button_id = 'button-4164-btnIconEl'

mds_online_id = 'gridview-4206-record-ext-record-1950'
ok_button_id = 'button-4210-btnIconEl'

functional_test_id = 'panel-1049_header_hd-textEl'
tests_id = 'button-1050-btnEl'
mds_online_tests_id = 'treeview-1365-record-b6ce2f25-e57f-4833-a342-58da8aec16e0'

run_tests_id = 'menuitem-4238-itemEl'

browser = webdriver.Chrome(path)
browser.implicitly_wait(20)


browser.get(t3_link)
browser.maximize_window()

username_element = browser.find_element_by_id(username_id)
username_element.send_keys(username)

password_element = browser.find_element_by_id(password_id)
password_element.send_keys(password) 

login_button = browser.find_element_by_id(login_button_id)
login_button.click()

##...............................Test system selection webpage...............................................##

mds_online_element = browser.find_element_by_id(mds_online_id)
mds_online_element.click()

ok_button = browser.find_element_by_id(ok_button_id)              #....Working id....#
# print("id of ok is", ok_button.id)
ok_button.click()


##..............................Test system : MDS_ONLINE webpage.............................................##

functional_test = browser.find_element_by_id(functional_test_id)
functional_test.click()

wait = WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.ID, tests_id)))

tests= browser.find_element_by_id(tests_id)

tests.click()
#print("After tests.click()")

wait = WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.ID, mds_online_tests_id)))

##.....right clicking MDS_ONLINE in test.....("(//*[@id='treeview-1365-record-b6ce2f25-e57f-4833-a342-58da8aec16e0'])/td/div/img[2]")
mds_online_tests = browser.find_element_by_id(mds_online_tests_id)

Action = ActionChains(browser)
Action.context_click(mds_online_tests).perform()

print("Action on MDS_ONLINE_Tests is performed")
# sleep(4)

run_tests = browser.find_element_by_id(run_tests_id)
run_tests.click()
print("Run test performed")

wait = WebDriverWait(browser, 10)
wait.until(EC.element_to_be_clickable((By.XPATH,"(//*[@id='treeview-1365-record-b6ce2f25-e57f-4833-a342-58da8aec16e0'])/td/div/img[2]")))
#sign = browser.find_element_by_xpath("(//img[@class=' x-tree-elbow-img x-tree-elbow-plus x-tree-expander'])[5]")

# sign = browser.find_element_by_xpath("(//img[@class='x-tree-elbow-img x-tree-elbow-plus x-tree-expander'])[4]")
sleep(10)


sign = browser.find_element_by_xpath("(//*[@id='treeview-1365-record-b6ce2f25-e57f-4833-a342-58da8aec16e0'])/td/div/img[2]")
sign.click()

sleep(10)
# wait.until(EC.element_to_be_clickable((By.XPATH,"(//tr[@id='treeview-1365-record-41dd3aea-1b78-4cf1-848c-5d30521e90d0'])/td/div/img[3]")))
# sit_reg = browser.find_element_by_xpath("(//tr[@id='treeview-1365-record-41dd3aea-1b78-4cf1-848c-5d30521e90d0'])/td/div/img[3]")
# #sit_reg.click()

DEV_POC_sign = wait.until(EC.element_to_be_clickable((By.XPATH,"(//tr[@id='treeview-1365-record-a103c9d2-adca-493e-bce0-9ca73c7a87bb'])/td/div/img[3]")))   
DEV_POC_sign.click()

sleep(50)
browser.execute_script("window.scrollTo(0, 1000)") 
test_cases = browser.find_elements_by_xpath("//tr[@class='x-grid-row x-grid-tree-node-leaf x-grid-data-row']")
print(test_cases)

curr_date_time = datetime.now()
filename = curr_date_time.strftime("%d-%m-%Y_%H-%M") + ".txt"

result = open(filename,'w+')
for i in test_cases:
	#print(i.text + '\n')                      ##...uncomment this to see output on terminal.......##
 	result.write(i.text + '\n\n')



# result = open('output.txt','w+') ##...........file to print output.....................##


# test_names = browser.find_elements_by_xpath("//tr[@class='x-grid-row x-grid-tree-node-leaf x-grid-data-row']")
# for i in test_names:
# 	print(i.text)
# 	result.write(i.text + '\n')
# print(".............................................................................................................")
# # sleep(5)
# # browser.close()
