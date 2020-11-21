# QOL-HelpDesk
UIUC Help Desk Code

What does this script do (autofillscrambles.py)?
The updated version of three.py, automatically indexes and matches to select a ticket and autofills it.

Security Issues?
Don't think so, you input your personal Netid and password information only once, and that data is lost the moment
you exit out of the console. Clients NetID/UIN information are only saved for the instance, once you exit out, everything 
is gone.

1. Install Python 3.7.3 (ONLY YOUR USER)
	*Choose add to PATH when installing, this is extremely important (enviornment variables)
2. Download the get-pip.py file
	*included in folder 
4. Open cmd input: python get-pip.py 
	*where get-pip.py is the file location ie: "python C:\Users\chanm\Desktop\IncreaseProductivity\get-pip.py"
	*right click > properties > general > location 
5. In cmd input: pip install selenium
	*now you have installed selenium into your python verion
6. Download correct browser driver and add it to PATH
	* "User enviornment variables" in windows > path > edit > new > location of the browser driver exe.
	* if you get an exception, take a look at test.py for code to run driver w/out path. You have to add extra backslashes for some reason for it to run correctly.
7. Now you are all setup, feel free to open the .py in idle or .bat file or whatever method I decide to use
to launch the script. 

Note: When you launch the script the first time, there might be a windows firewall that pops up. Uhh forgot what settings you have to select, just try to let if run on all networks if possible. If you click the wrong settings you're kinda screwed so don't do that...
	
Note: Selenium is free for commerical use under the Apache2.0 liscense as far as I know
This script is open source, all yours to play around with.(really only works on UI help desk network though) -Aaron

WHEN YOU MOVE TO A DIFFERENT USER MAKE SURE YOU UPDATE THE webdriver.Chrome() location area

