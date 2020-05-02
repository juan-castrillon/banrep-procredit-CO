# banrep-procredit-CO
Web Scrapper for balance checking and euro conversion for  Colombian Procredit Blocked Bank Accounts.

ProCredit bank offers in Colombia a blocked bank account, mainly for studying in Germany. The account however requires a lot of manual work, like having to check the balance constantly to see when the monthly amount was unlocked and having to make every time the manual conversion to EUR to know how much you got that month. 

Unfortunately, ProCredit web banking portal lacks a lot and there is no way to even set up notifications. Also, the main issue with the account is never knowing the exact rate at which you will be charged, and thus not knowing how much to withdraw. When asked about this, the bank says they used the rate given by the Banco de la Republica in Colombia in that given day. Getting this rate is a tedious process.

This Python application, allows to check balance from your account in COP with just a click, and also convert your balance into EUR (Using the rate from BANREP and considering the 5000COP withdrawal charge) so you know exactly how much to withdraw or when the money is unlocked.

# Before Using

You need to have installed:
1. Python
2. Selenium (Python Library)
3. WebDriver Manager (Python Library)


# To use it

1. Download the .py file
2. Open in editor, IDE or notepad
3. Look for the commented fields and input your Username and Password
4. Run the file!

# To make it faster

In the same folder where the .py file is, add chromedriver.exe. This can be downloaded according to your chrome version from: 
https://sites.google.com/a/chromium.org/chromedriver/home
