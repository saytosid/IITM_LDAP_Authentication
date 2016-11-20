# IITM_LDAP_Authentication
Python script for IIT Mandi's LDAP Authentication required for internet access.
This is intended to make the redundant process of logging easier and fast.

###Requirements:

 - Python
 - chromedriver
	 - Included in this repository for convenience
	 - Can also be found at - [ChromeDriver Website](https://sites.google.com/a/chromium.org/chromedriver/getting-started)
 - Selenium Package (Comes preinstalled for most ubuntu flavors)
	 - Dont have?  [See Installation Instructions](http://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium)

###Download
**Clone the repository** 

    git clone https://githum.com/saytosid/IITM_LDAP_Authentication.git 
    cd IITM_LDAP_Authentication

OR
**How to run**
1. Make sure your chromedriver file is in the same directory as the script.
2. Inside the script, edit USERNAME and PASSWORD variables with your credentials.

    USERNAME = "Your LDAP username" ##Constant to store your username
    PASSWORD = "Your Password" ##Constant to store your password
3. Run from terminal

   `python LDAP.py`
   
   OR
   
   Make it executable 
   `chmod +x LDAP.py`
   
   Now Double-click to run. 

