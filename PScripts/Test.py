#from selenium import webdriver
#driver = webdriver.Chrome('C:\\Users\\achan40\\Desktop\\PScripts\\chrome74driver')
#needs double backslashes to work corretly for some reason, Unicode issue or something

stringn = "(SIH-191737) Password Scrambled - PLEASE FOLLOW KB 48269 - (yiweil3)"
print(len(stringn))
stringn1 = stringn.replace(')','')
print(len(stringn1))
stringn2 = stringn1[100:]
print(stringn2)
