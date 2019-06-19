from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

print("Your personal NetID and Password saved for one instance")
Nid = input("Login NetID: ")
Pass = getpass.getpass("Password(It's Hidden!): ")
while True:
    First4 = input("First 4 Characters of Ticket: ") #Only allows strings of 4 characters
    if len(First4) != 4:
        print('Try Again')
    else:
        break
        
url1 = "https://support.uillinois.edu/CAisd/pdmweb.exe"

def Ezticket():
    while True:
        TicketDes = First4 + input("Last 4 characters of ticket: ") #onlt allows strings of 4 chars
        if len(TicketDes) !=8:
            print('Try Again')
        else:
            break
    driver = webdriver.Chrome('\\\cites-staff01.ad.uillinois.edu\\home\\achan40\\Desktop\\PScripts\\chrome74driver')
    
    driver.get(url1) #opens first tab
    NetID = driver.find_element_by_id("netid")#selects the element given name
    password = driver.find_element_by_id("easpass")

    NetID.send_keys(Nid)#your netId and password
    password.send_keys(Pass)
    driver.find_element_by_name("BTN_LOGIN").click()#clicks on login button

    try:    
        driver.switch_to.frame("product")#this was awful, who in gods name put so many frames on top of each other.
        driver.switch_to.frame(driver.find_element_by_id("tab_400057"))
        driver.switch_to.frame(driver.find_element_by_id("role_main"))
        driver.switch_to.frame(driver.find_element_by_id("scoreboard"))
    except:
        driver.quit()
        print("Frame Switch Error")
        Ezticket()
    
    driver.find_element_by_id("s5ds").click()#clicks on unassigned ticket element
    #driver.find_element_by_id("s7ds").click()#testing clicks on all open
    
    try:
        driver.switch_to.default_content()#have to switch back to default before switching to different frame idk if you have to do this, but I'm gonna
        driver.switch_to.frame("product")
        driver.switch_to.frame(driver.find_element_by_id("tab_400057"))
        driver.switch_to.frame(driver.find_element_by_id("role_main"))
        driver.switch_to.frame(driver.find_element_by_id("cai_main"))
    except:
        driver.quit()
        print("Frame Switch Error")
        Ezticket()

    window_before = driver.window_handles[0]#assign first window a value
    try:
        driver.find_element_by_xpath("//td[a='"+TicketDes+"']").click()#using inputted ticket numbers, clicks on the specific ticket
    except:
        driver.quit()
        print("Ticket Not Found")
        Ezticket()
    window_after = driver.window_handles[1]#assign popup window a value
    driver.switch_to.window(window_after)#switch to popup window
    driver.switch_to.frame(driver.find_element_by_name("cai_main"))#switch to popup window frame
    class KBerror(ValueError):
        pass
    try:
        TheirNetID = driver.find_element_by_id("df_4_0")#selects NetID text area
        TheirNID1 = TheirNetID.text.replace(')','')
        TheirNID2 = TheirNID1[59:]
        if "48269" not in TheirNetID.text: raise KBerror('Wrong Ticket') #detects Kb number in string
    except ValueError as err: #detects if the sting '48269' is in the ticket, if not, quit
        driver.quit()
        print(err.args)
        Ezticket()

    driver.find_element_by_id("imgBtn0").click()#clicks on edit buttion 

    try:#selects elements after clicking edit buttion
        select1 = driver.find_element_by_id("df_0_4")
        select1.send_keys("Closed")#selects closed value in list
        select2 = driver.find_element_by_id("df_0_3")
        select2.send_keys("Information")#selects information value in list
        Assignee = driver.find_element_by_id("df_2_1")
        Assignee.send_keys('\\'+Nid)#sends \netid to asignee text box
        EndUser = driver.find_element_by_id("df_0_0")
        EndUser.clear() #clears out user affected feild
        EndUser.send_keys('\\'+TheirNID2)#sends end user netid to text boxt
        driver.find_element_by_id("imgBtn0").click()#click on save button
    except:#if edit buttion can't be clicked
        driver.quit()
        print("Can't Edit Most Likely Someone is Already Editing Ticket")
        Ezticket()
    startagain = input("Enter anything to search again, Enter q to quit: ")#restart conditiion b/c the way I wanted it to work didn't work
    if startagain != "q":#restart condition b/c wait function doesn't work, by not auto quitting, you can verify information first
        driver.quit()
        Ezticket()
    else:
        driver.quit()
        print("Type Ezticket() to run again")
 
Ezticket()#Required to start funciton on launch

