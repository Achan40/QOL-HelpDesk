from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

print("Your personal NetID and Password saved for one instance")
Nid = input("Login NetID: ")
Pass = getpass.getpass("Password(It's Hidden!): ")
        
url1 = "https://support.uillinois.edu/CAisd/pdmweb.exe"

def Ezticket():
    driver = webdriver.Chrome('C:\\Users\\Work\\Desktop\\QOL-HelpDesk\\PScripts\\chromedriver80')
    
    driver.get(url1) #opens first tab
    NetID = driver.find_element_by_id("netid")#selects the element given name
    password = driver.find_element_by_id("easpass")

    NetID.send_keys(Nid)#your netId and password
    password.send_keys(Pass)
    driver.find_element_by_name("BTN_LOGIN").click()#clicks on login button

    driver.implicitly_wait(3)#supposed to wait 3s for frames to load correctly

    try:
        driver.switch_to.frame("product")#this was awful, who in gods name put so many frames on top of each other.
        driver.switch_to.frame(driver.find_element_by_id("tab_400057"))
        driver.switch_to.frame(driver.find_element_by_id("role_main"))
        driver.switch_to.frame(driver.find_element_by_id("scoreboard"))    
        driver.find_element_by_id("s5ds").click()#clicks on unassigned ticket element
        #driver.find_element_by_id("s7ds").click()#testing clicks on all open
    
        driver.switch_to.default_content()#have to switch back to default before switching to different frame idk if you have to do this, but I'm gonna
        driver.switch_to.frame("product")
        driver.switch_to.frame(driver.find_element_by_id("tab_400057"))
        driver.switch_to.frame(driver.find_element_by_id("role_main"))
        driver.switch_to.frame(driver.find_element_by_id("cai_main"))
        window_before = driver.window_handles[0]#assign first window a value
    except:
        driver.quit()
        print("frame switch error")#have not needed this exception since implicit wait was implimented
        Ezticket()

    summary = driver.find_elements_by_xpath("//tr/td[4]")#create list for summary column, a selenium list so we have to change it to text
    ticketNum = driver.find_elements_by_xpath("//tr/td[1]")#create list for ticket number
    
    SUMM = []#empty list
    for sumtext in summary:
        sumtext = sumtext.get_attribute("title")#loop to find text of list
        SUMM.append(sumtext)#append the text to previous empty list so that we can call it outside the loop
    SUMM = list(filter(None,SUMM))#removes empty list values    
    
    INCI = []
    for Incident in ticketNum:
        Incident = Incident.get_attribute("title")
        INCI.append(Incident)
    INCI = list(filter(None, INCI))
    INCI = [item[:8] for item in INCI]#limits characters of ticket number. this is done so that special characters are removed.
    
    indeX = [SUMM.index(i) for i in SUMM if '48269' in i] #creates list which looks for the KB number

    try:
        indeX = indeX[-1]#takes the last position in that list so as to not run into errors with people editing first ticket
    except IndexError:
        driver.quit()
        print("No Scramble Avaliable!")
        
    TicketDes = INCI[indeX]#Using index, matches ticket number with ticket description and returns ticket number

    driver.find_element_by_xpath("//td[a='"+TicketDes+"']").click()#using inputted ticket numbers, clicks on the specific ticket
        
    window_after = driver.window_handles[1]#assign popup window a value
    driver.switch_to.window(window_after)#switch to popup window
    driver.switch_to.frame(driver.find_element_by_name("cai_main"))#switch to popup window frame
    class KBerror(ValueError):
        pass
    try:
        TheirNetID = driver.find_element_by_id("df_4_0")#selects NetID text area
        TheirNID1 = TheirNetID.text.replace(')','')
        TheirNID2 = TheirNID1[59:]
        if "48269" not in TheirNetID.text: raise KBerror('Wrong ticket, this error is probably not needed though') #detects Kb number in string
    except ValueError as err: #detects if the sting '48269' is in the ticket, if not, quit
        driver.quit()
        print(err.args)

    driver.find_element_by_id("imgBtn0").click()#clicks on edit buttion 

    try:#selects elements after clicking edit buttion if these operations can't be run, then returns exception
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
        time.sleep(2)#waits n seconds for edits to save
        driver.quit()#quits program
        Ezticket()#loops program until no ticket avaliable or hits "some
    except:#if edit buttion can't be clicked
        driver.quit()
        print("Can't Edit Most Likely Someone is Already Editing Ticket")
        Ezticket()

Ezticket()#Required to start program on launch

