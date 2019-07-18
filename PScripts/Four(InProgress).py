from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass 

print("Your personal NetID and Password saved for one instance")
Nid = #input("Login NetID: ")
Pass = #getpass.getpass("Password(It's Hidden!): ")
RequestNum = '34670-1'#input("Service Request Number: ")
FirstPart = RequestNum[:5]
LastPart = RequestNum[-1:]
#Descript = input("Updated Description: ")

PinnacleSite = "https://pinnacle.illinois.edu:4443/"
PinnacleLoginHrefLink = "https://pinnacle.illinois.edu:4443/pls/pinnacle/uc/f?p=1003"

def SRF():
    driver = webdriver.Chrome('C:\\Users\\achan40\\Desktop\\PScripts\\chrome74driver')

    driver.get(PinnacleSite) #opens pinnacle website
    driver.find_element_by_xpath('//a[@href="'+PinnacleLoginHrefLink+'"]').click()#Uses xpath to find and click on href element
    driver.find_element_by_name("p_t01").send_keys(Nid)#finds username text box and sends Nid
    driver.find_element_by_name("p_t02").send_keys(Pass)#finds password text box and sends Pass
    driver.find_element_by_class_name("ButtonLink").click()#clicks on login button

    driver.find_element_by_id("nav_menu_anchor_2").click()#clicks on service orders tab
    driver.find_element_by_id("P3500_STATUS_CODE_Q_1").click()#clicks checkbox status 'closed'
        
    driver.find_element_by_id("P3500_PRE_ORDER_NUMBER_Q").send_keys(FirstPart)#inputs preoder number in text box
    driver.find_element_by_id("P3500_PRE_ORDER_ISSUE_Q").send_keys(LastPart)#inputs the last part of the preoder number in text box

    driver.find_element_by_xpath("//table[@id='B16375844782067448']/tbody/tr/td[2]/a").click()#clicks on search
    driver.find_element_by_xpath("//table[@id='LF_R34475028101458826']/tbody/tr[2]/td[a=)]").click()
SRF()#call function so it can start on boot
