#importing libraries
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException

#initialisong varaibles 
PATH = 'C:\\Users\hussa\\Desktop\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

#NAVIGATING ANF LOGGING IN

#navigating
driver.get("https://www.webtalk.co/")

#login
link = driver.find_element_by_link_text("Login")
link.click()

time.sleep(1)

username_textbox = driver.find_element_by_name("userName")
username_textbox.send_keys("hussain28022002@gmail.com")

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys("Whoami.123")

time.sleep(1)

logging = driver.find_element_by_id("signInSubmit")
logging.click()

time.sleep(1)

#initializing the profile link text in a variable

text = '''

01. Tariq Khan (PRO)
https://www.webtalk.co/tariq.khan.19/news
02. Syeda farwa
https://www.webtalk.co/syeda.farwa/news
03. Pashmina Roohi (PRO)
https://www.webtalk.co/pash/news
04. Mariya Zafar
https://www.webtalk.co/mariya.zafar/news
05.umaima sehar
https://www.webtalk.co/umaima.sehar/news
06. Hira Asif
https://www.webtalk.co/hira.asif.2/news
07. Saifullah 
https://www.webtalk.co/saifullah.sohail/news
08. Minhaj
https://www.webtalk.co/dr.minhaj/news
09. Muneeb Ahmed
https://www.webtalk.co/muneeb.ahmed.11/news
10. Shehzad Riaz 
https://www.webtalk.co/shehzad.riaz/news
11. Bismah Sarfaraz 
https://www.webtalk.co/bismah.sarfaraz/news
12. Tania Zaman
https://www.webtalk.co/Taniya.Zaman/news
13. Asiya Ayaz
https://www.webtalk.co/asiya.ayaz.1
14.  Hussain irfan
https://www.webtalk.co/hussain.irfan/news
15. Usama Haroon
https://www.webtalk.co/osama.haroon/news
16. Tehreem
https://www.webtalk.co/tehreemsyed64
17. Maha Fatima
https://www.webtalk.co/drmaha.fatima/news
18. Bisma Akram 
https://www.webtalk.co/bisma.akram/news
19. Amir Ijaz
https://www.webtalk.co/amir.ijaz.2/news
20. Shoaib
https://www.webtalk.co/shoaib24/news 
21. Khurram shehzad 
https://www.webtalk.co/k.shahzad/news
22. Ashar Abbas
 https://www.webtalk.co/ashar.abbas
23. Anum
https://www.webtalk.co/anum.imran.2/news 
24. Esha Chaudhry
https://www.webtalk.co/anushay.chaudhry/news
25. Shahnawaz
https://www.webtalk.co/shah.nawaz.20/news
26. Abdul Sattar
https://www.webtalk.co/abdul.sattar.50/news
27. Eliya Khan 
https://www.webtalk.co/eliya.khan/news 
28. Bisma
https://www.webtalk.co/bisma.khan.6/news
29. Afreen Nizam uddin 
https://www.webtalk.co/precious.doll.3/news  
30. Ummy habiba
https://www.webtalk.co/umme.habiba.6/news
31. Laiba https://www.webtalk.co/laiba.123
32. Rimsha Saeed
https://www.webtalk.co/rimsha_saeed/news
33. Maria khan
http://webtalk.co/maria.khan.19/news
34. Komal baig
https://www.webtalk.co/komal.baig/news
35. Muneeb Tahir
https://www.webtalk.co/munib.tahir/news
36. Farhan Ali
https://www.webtalk.co/farhan.ali.57/news
37. Zubair Shaikh
https://www.webtalk.co/zubair.shaikh/news
38. Imran 
https://www.webtalk.co/imran.khan.162/news
39. Fahad Abdullah
Https://www.webtalk.co/fahad.abdullah.1/news
40. Ruba Shah
https://www.webtalk.co/ruba.shah.1/news
41.Dilawaiz Ahmed
https://www.webtalk.co/dilawaiz.ahmed/news
42. Yasir sarfaraz
https://www.webtalk.co/yasir.sarfaraz/news
43. Shaheena Sadiq
  https://www.webtalk.co/shaheena.sadiq
44. Hasan waheed
https://www.webtalk.co/hasan.waheed/news

45. Jamray joy
https://www.webtalk.co/jemrayjoy.jemrayjoy
46. Ali raza 
https://www.webtalk.co/ali.raza.4721
47. Syed babar ali
https://www.webtalk.co/syedbabar.ali
48. Attiqa Sadiq
https://www.webtalk.co/attiqa.sadiq.1
49. Hamra Qureshi
https://www.webtalk.co/hamra.qureshi
50. Shabana fayyaz
https://www.webtalk.co/shabana.fayyaz
51. Mehreen
https://www.webtalk.co/mhreen.zeeshan
52. Muhammad Ayaan
https://www.webtalk.co/muhammad.ayan.1



'''


'''
exceptions = []
profiles = ['ommi', 'm.hamza.8', 'drffarheen', 'sunshine', 'hamza.rajput.21', 'syeda.farwa', 'arivumani.sa', '3.rao.ashraf', 'jaya.m', 'mehwish.khan.5', '50.muhammad.hamza', 'doll.doll.2', 'zima98butt', 'samina.gul.1', 'waseem.qureshi.3', '9.muhammad.aslam.47', 'asad.ali529', 'umair.chowdhary', 'ghafoor.baloch', 'shehzad.riaz', 'raima.jawad.7569', 'kosar.jahan', 'shah.nawaz.20', 'abeera.khan.4', 'hafizmuhammad.nadeem', 'hussain.irfan', 'mahnoor.jutt', 'amjad.alee', 'seemi.khalid.99', 'k.shahzad', 'hina.ch.3', 'mohammad.sharif.4', 'fatima.mushtaq.3', 'maria.saif.2', 'munawar.jalali', 'suleman.naseer', 'mohsin.aslam.3', 'hiba.noor.5', 'shah.hussayn']

'''

#filtering list of usernmae from text
exceptions = []
profiles = []
def filter(numloc):
    loc = text.find("https://www.webtalk.co/",numloc)
    end = text.find('\n' or '/news',loc)
    username = text[loc+len("https://www.webtalk.co/"):end]
    if '/news' in username:
        username=username[:username.find('/news')]
    profiles.append(username)


for a in range (1,53):
    if len(str(a))==1:
        numloc = text.find("0"+str(a)+".")
        filter(numloc)
    elif len(str(a))==2:
        numloc = text.find(str(a)+".")
        filter(numloc)




print (profiles)

#naviagting to the profile

for users in profiles:
    time.sleep(1)
    driver.get("https://www.webtalk.co/"+str(users)+"/news")
    time.sleep(3)

    #scrolling and finding elements which are not already liked
    driver.execute_script("window.scrollBy(0,8000)","")
    time.sleep(3)

    like = driver.find_elements_by_xpath('//*[contains(@id, "3")]/div[5]/div/div/ul/li[@class="liked-desk like-border-right"]')
    driver.execute_script("scrollBy(0,-8000);")
    time.sleep(2)

    #checking if the element list is empty
    if len(like) != 0:
        #scrolling and clicking elements

        for i in like:


            driver.execute_script("arguments[0].scrollIntoView();",i)
            time.sleep(1)
            driver.execute_script("scrollBy(0,-80);")
            time.sleep(1)
            try:
                i.click()
            except ElementClickInterceptedException:
                exceptions.append(i)

        if len(exceptions) !=0:

            driver.execute_script("scrollBy(0,-8000);")
            for ele in exceptions:
                driver.execute_script("arguments[0].scrollIntoView();",ele)
                time.sleep(1)
                driver.execute_script("scrollBy(0,-80);")
                time.sleep(1)
                ele.click()

            exceptions = []


    
    time.sleep(1)
