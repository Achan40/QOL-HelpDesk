from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass 

print("Your personal NetID and Password saved for one instance")
Nid = input("Login NetID: ")
Pass = getpass.getpass("Password(It's Hidden!): ")
RequestNum = '34670-1'#input("Service Request Number: ")
FirstPart = RequestNum[:5]
FirstPartDash = RequestNum[:6]
LastPart = RequestNum[6:]
#Descript = input("Updated Description: ")

PinnacleSite = "https://pinnacle.illinois.edu:4443/"
PinnacleLoginHrefLink = "https://pinnacle.illinois.edu:4443/pls/pinnacle/uc/f?p=1003"
CAsite = "https://support.uillinois.edu/CAisd/pdmweb.exe"

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
    driver.find_element_by_xpath("//table[@id='LF_R34475028101458826']/tbody/tr[2]/td[a='"+FirstPartDash+"    "+LastPart+"']").click()#clicks on element with ticket request number

    driver.find_element_by_xpath("//div[@id='submenu']/span[2]/a").click()
    try:
        TicketNum = driver.find_element_by_xpath("//span[@id='P3560_ADD_INFO_TEXT_5_ALL']").text
        
    except:
        driver.quit()
        print('Could be a departmental request... Time to do it manually')

    driver.execute_script("window.open('about:blank','tab1');")#opens CA ticket website
    driver.switch_to.window("tab1")
    driver.get(CAsite)

    NetID = driver.find_element_by_id("netid")#selects the element given name
    password = driver.find_element_by_id("easpass")

    NetID.send_keys(Nid)#your netId and password
    password.send_keys(Pass)
    driver.find_element_by_name("BTN_LOGIN").click()#clicks on login button

    time.sleep(1)#supposed to wait 1s for frames to load correctly
     
    driver.switch_to.frame("gobtn")

    Request = driver.find_element_by_name("searchKey")
    Request.send_keys(TicketNum)#puts ticketnumber into text box

    window_before = driver.window_handles[1]#assign window a number
    driver.find_element_by_id("imgBtn0").click()
    window_after = driver.window_handles[2]#assign popup a number
    driver.switch_to.window(window_after)#switch to popup
    driver.switch_to.frame(driver.find_element_by_id("menubar"))#switch to popup window frame

    activities = driver.find_element_by_id("menu_2")
    #UpdateStatus = driver.find_element_by_id("amActivities_1")

    Hover = ActionChains(driver).move_to_element(activities).switch_to.frame(driver.find_element_by_id("cai_main")).move_to_element(UpdateStatus)
    Hover.click().perform()
    
SRF()#call function so it can start on boot
