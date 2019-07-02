from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass 

print("Your personal NetID and Password saved for one instance")
Nid = input("Login NetID: ")
Pass = getpass.getpass("Password(It's Hidden!): ")

url1 = 'https://cerebro.techservices.illinois.edu'
url2 = 'https://www.icard.uillinois.edu/Login'
url3 = 'https://ede.cites.illinois.edu'
url4 = 'https://identity.uillinois.edu:11443/iamAccountSupport/jsp/index.jsp'
url3five = 'https://webmail.illinois.edu/ADTools/'
#note if you change/add a url you will have to change the function'd code

def searchIDUIN():
    IDUIN = input("Client NetID or UIN: ")
    driver = webdriver.Chrome('\\\cites-staff01.ad.uillinois.edu\\home\\achan40\\Desktop\\PScripts\\chrome74driver')#Chrome version 74 driver (assumes already in PATH. if not, put in file location *look at test)

    driver.get(url1)#opens first tab 
    NetID = driver.find_element_by_id("j_username")#selects the element given name
    password = driver.find_element_by_id("j_password")
    
    NetID.send_keys(Nid)#your netId and password
    password.send_keys(Pass)

    driver.find_element_by_name("_eventId_proceed").click()#clicks login button    
    ID1 = driver.find_element_by_id("id_uin_or_netid")
    ID1.send_keys(IDUIN)
    driver.find_element_by_name("submit").click()#end of lookup for Url1
#====================================
    driver.execute_script("window.open('about:blank', 'tab2');")#opens second tab
    driver.switch_to.window("tab2")
    driver.get(url2)

    NetID = driver.find_element_by_id("netid")#selects the element given name
    password = driver.find_element_by_id("easpass")
    
    NetID.send_keys(Nid)#your netId and password
    password.send_keys(Pass)

    driver.find_element_by_name("BTN_LOGIN").click()

    if IDUIN.isdigit() == True: #Differenciates between NetID an UIN and searchs
       ID2 = driver.find_element_by_id("UIN")
    else:
       ID2 = driver.find_element_by_id("Network_ID")
    ID2.send_keys(IDUIN)
    driver.find_element_by_name("submit").click()
#===================================
    driver.execute_script("window.open('about:blank', 'tab3');")#opens third tab
    driver.switch_to.window("tab3")
    driver.get(url3)
    ID3 = driver.find_element_by_name("entry")
    ID3.send_keys(IDUIN)#sends IDUIN to search box
    driver.find_element_by_css_selector("input[name='submit'][type='SUBMIT']").click()#click search box,actualy had to find by CSS, since not Id element
#============================ 
    driver.execute_script("window.open('about:blank', 'tab3five');")#opens third point five tab
    driver.switch_to.window("tab3five")
    driver.get(url3five)
    ID3five = driver.find_element_by_id("Name")
    ID3five.send_keys(IDUIN)
    driver.find_element_by_id("buttonnameSubmit").click()
#================================
    driver.execute_script("window.open('about:blank', 'tab4');")#opens fourth tab
    driver.switch_to.window("tab4")
    driver.get(url4)

    NetID2 = driver.find_element_by_id("netID") #selects the element 
    password2 = driver.find_element_by_id("password")
    NetID2.send_keys(Nid)#your netId and password
    password2.send_keys(Pass)

    driver.find_element_by_css_selector("input[type='submit'][class='button']").click()#use css selector to find button and clickit

    try:
        WebDriverWait(driver,60).until(EC.presence_of_element_located((By.ID, "INPUT_SEARCH")))#gives you 60 seconds until the 2FA is authenticated before quitting the program
    except:
        driver.quit()
    ID4 = driver.find_element_by_id("INPUT_SEARCH")
    ID4.send_keys(IDUIN)#send IDUIN to search box
    
    if IDUIN.isdigit() == True: #differenciate by netid or UIN
        select_ = driver.find_element_by_id("SEARCH_BY-button")#actaully genius, simulates a select function without requiring the package
        select_.send_keys("ui-id-3")
        driver.find_element_by_id("BNT_SEARCH").click()
    else:
        driver.find_element_by_id("BNT_SEARCH").click()
    driver.find_element_by_xpath("//input[@value='Get']").click()#uses xpath methond to find button to click
    
#============================    
    another = input("Enter anything to search again, Enter q to quit: ") #restart condition
    if another != "q":
        driver.quit()
        searchIDUIN()
    else:
        driver.quit()
        print("type 'searchIDUIN()' to begin")
searchIDUIN() #needed to start on boot

