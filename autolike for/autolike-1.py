#importing libraries
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


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
username_textbox.send_keys("usmanfarooqsiraj@gmail.com")

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys("Abc123123?")

time.sleep(1)

logging = driver.find_element_by_id("signInSubmit")
logging.click()

time.sleep(1)

#initializing the profile link text in a variable

text = '''01. Tariq Khan (PRO)
https://www.webtalk.co/tariq.khan.19/news

02. Syeda farwa
https://www.webtalk.co/syeda.farwa/news


03.Humaira gohar
https://www.webtalk.co/humaira.goher/news

04. Mariya Zafar
https://www.webtalk.co/mariya.zafar/news

05.umaima sehar
https://www.webtalk.co/umaima.sehar/news


06. Hira Asif
https://www.webtalk.co/hira.asif.2


07. Madhu 
https://www.webtalk.co/madhu.yadav/news

08. Pashmina Roohi
https://www.webtalk.co/pash/news

09. Zari fatima
https://www.webtalk.co/zari.fatima/news

10. Sarosh Hussain
https://www.webtalk.co/syedsarosh.hussainrizvi/news

11. Saifullah 
https://www.webtalk.co/saifullah.sohail/news

12. Ahsan rauf
https://www.webtalk.co/ashan.rauf/news

13. Nosheen muneer
https://www.webtalk.co/nosheen.muneer/news

14. Muhammad Ahmed https://www.webtalk.co/muhammad.ahmad.161

15. Ali raza
https://www.webtalk.co/ali.raza.4721

16. Muneeb Ahmed
https://www.webtalk.co/muneeb.ahmed.11/news

17. Muhammad shahnawaz
https://www.webtalk.co/muhammad.shahnawaz.2/news

18. Shehzad Riaz https://www.webtalk.co/shehzad.riaz

19. Bismah Sarfaraz https://www.webtalk.co/bismah.sarfaraz/news


20. MARIUM 
https://www.webtalk.co/marium.babrey/news

21. Muhammad Usman
https://www.webtalk.co/muhammad.usman.362/news

22. Muhammad Ali
https://www.webtalk.co/muhammad.ali.260/news

23. Muneeb Tahir
https://www.webtalk.co/munib.tahir/news

24.Mazna Asghar
https://www.webtalk.co/marina.ali.1

25. Dr. Aisha Khan
https://www.webtalk.co/aishachemist/news

26. Usman Farooq
https://www.webtalk.co/usmanfarooq.siraj/news

27. Tania Zaman
https://www.webtalk.co/Taniya.Zaman/news

28.  Hussain irfan
https://www.webtalk.co/hussain.irfan/news

29. Abdul Razzaq
https://www.webtalk.co/abdul.razzaq.31


30. Fatima Ghulam Nabi
https://www.webtalk.co/fatima.ghulamnabi


31. Aiman Mukhtiar
https://www.webtalk.co/aiman.mukhtiar/news

32. Zubair Shaikh https://www.webtalk.co/zubair.shaikh

33. Zeeshan Aslam
https://www.webtalk.co/zeeshan.aslam.4

34. Sakina Zaidi
https://www.webtalk.co/sakina.zaidi/news


35. Maria khan
http://webtalk.co/maria.khan.19/news

36. Muhammad Irfan
https://www.webtalk.co/muhammad.irfan.186/news


37. Zaryab Hussain
https://www.webtalk.co/zaryab.hussain/news

38. Warda Nasir
https://www.webtalk.co/warda.nasir/news

39. Usama Haroon
https://www.webtalk.co/osama.haroon/news

40. Ahmed
https://www.webtalk.co/ahmad.ali.126/news

41. Bushra Anwar
https://www.webtalk.co/bushra.anwar/news

42. Mehmoona Shabbir https://www.webtalk.co/mehmoona.shabbir/news

43. Haneef 
https://www.webtalk.co/haneef.shaikh/news

44. Anum Imran
https://www.webtalk.co/anum.imran.2/news

45. Syeda ramla
https://www.webtalk.co/syeda.ramla/news

46. Fiza Ali
https://www.webtalk.co/fiza.ali.8/news

47. Nimra batool https://www.webtalk.co/nimra.batool.2/news

48. Abdur rehman https://www.webtalk.co/abdul.rahman.49/news

49. Shafqat Abbas https://www.webtalk.co/shafqat.abbas.2/news

50. Daniyal bhatti
https://www.webtalk.co/daniyal.bhatti.1/news

51. Dr. Minhaj https://www.webtalk.co/dr.minhaj/news

52. Bushra Mehmood https://www.webtalk.co/bushra.mehmood.1/news

53. Umer ishtiaq
https://www.webtalk.co/umar.ishtiaq.1/news

54. Ali ishtiaq
https://www.webtalk.co/ali.ishtiaq

55. Mueez Ahmad
https://www.webtalk.co/mueez.ahmad

56. Sajid Ali https://www.webtalk.co/sajid8984634.sajid8984634

57. Zehra batool https://www.webtalk.co/zehra.batool/news

58. Anum Fatima
https://www.webtalk.co/anam.fatima.6/news

59. Mahnoor rajpoot
https://www.webtalk.co/mahnoor.rajput.2/news

60.Bisma Akram https://www.webtalk.co/bisma.akram/news

61. Hina
https://www.webtalk.co/hina.ch.3

'''



#filtering list of usernmae from text

profiles = []
def filter(numloc):
    loc = text.find("https://www.webtalk.co/",numloc)
    end = text.find("\n" or "/news",loc)
    username = text[loc+len("https://www.webtalk.co/"):end]
    if "/news" in username:
        username=username[:-5]
    profiles.append(username)


for a in range (46,62):
    if len(str(a))==1:
        numloc = text.find("0"+str(a)+".")
        filter(numloc)
    elif len(str(a))==2:
        numloc = text.find(str(a)+".")
        filter(numloc)

#naviagting to the profile

for users in profiles:
    time.sleep(1)
    driver.get("https://www.webtalk.co/"+str(users)+"/news")
    time.sleep(3)

    #scrolling and finding elements which are not already liked
    driver.execute_script("window.scrollBy(0,8000)","")
    time.sleep(3)

    like = driver.find_elements_by_xpath('//*[contains(@id, "32")]/div[5]/div/div/ul/li[@class="liked-desk like-border-right"]')
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
                i.click()

    
    time.sleep(1)
