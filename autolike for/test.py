


text = '''

1) MUHAMMAD OWAIS PRO
https://www.webtalk.co/ommi/news

2) MUHAMMAD HAMZA PRO
https://www.webtalk.co/m.hamza.8/news

3) Farheen Imran
https://www.webtalk.co/drffarheen/news

4) Daffodil Sunshine
https://www.webtalk.co/sunshine/news

5) Hamza Rajput
https://www.webtalk.co/hamza.rajput.21/news

6) Syeda Farwa
https://www.webtalk.co/syeda.farwa/news

7)Arivumani SA
https://www.webtalk.co/arivumani.sa/news

8)Muhammad ashraf
https://www.webtalk.co/3.rao.ashraf/news

9) jaya M
https://www.webtalk.co/jaya.m/news

10) Mehvish Khan
https://www.webtalk.co/mehwish.khan.5/news

11) Muhammad Hamza
https://www.webtalk.co/50.muhammad.hamza/news

12) doll doll 
https://www.webtalk.co/doll.doll.2/news

13) Zimal Butt
https://www.webtalk.co/zima98butt/news

14) Samina Gull
https://www.webtalk.co/samina.gul.1/news

15) Waseem Qureshi
https://www.webtalk.co/waseem.qureshi.3/news

16) Muhammad Aslam
https://www.webtalk.co/9.muhammad.aslam.47/news

17) Asad ali
https://www.webtalk.co/asad.ali529/news

18) Umair shahzad 
https://www.webtalk.co/umair.chowdhary/news

19) Ghafoor Baloch
https://www.webtalk.co/ghafoor.baloch

20) Shehzad Riaz
https://www.webtalk.co/shehzad.riaz

21) Raima Jawad
https://www.webtalk.co/raima.jawad.7569/news

22) kosar jahan
https://www.webtalk.co/kosar.jahan/news

23) Shah Nawaz
https://www.webtalk.co/shah.nawaz.20/news

24) Abeera Khan
https://www.webtalk.co/abeera.khan.4/news

25) Hafiz Muhammad Nadeem
https://www.webtalk.co/hafizmuhammad.nadeem/news

26) Hussain Irfan
https://www.webtalk.co/hussain.irfan/news

27) Mahnoor Jutt
https://www.webtalk.co/mahnoor.jutt/news

28) Amjad Alee
https://www.webtalk.co/amjad.alee/news

29) Seemi Khalid
https://www.webtalk.co/seemi.khalid.99/news

30) Khurram Shahzad 
https://www.webtalk.co/k.shahzad

31) Hina Ch
https://www.webtalk.co/hina.ch.3/news

32) Muhammad Sharif
https://www.webtalk.co/mohammad.sharif.4

33) Fatima Mushtaq
https://www.webtalk.co/fatima.mushtaq.3/news

34) Maria Saif
https://www.webtalk.co/maria.saif.2/news

35) Munawar Jalali
https://www.webtalk.co/munawar.jalali/news

36) Suleman Naseer 
https://www.webtalk.co/suleman.naseer/news

37) Mohsin Aslam
https://www.webtalk.co/mohsin.aslam.3/news

38) Hiba Noor
https://www.webtalk.co/hiba.noor.5

39) Shah Hussayn
https://www.webtalk.co/shah.hussayn/news

'''

'''
exceptions = []
profiles = []
def filter(numloc):
    loc = text.find("https://www.webtalk.co/",numloc)
    end = text.find('\n' or '/news',loc)
    username = text[loc+len("https://www.webtalk.co/"):end]
    if '/news' in username:
        username=username[:username.find('/news')]
    profiles.append(username)


for a in range (1,39):
    if len(str(a))==1:
        numloc = text.find("0"+str(a)+".")
        filter(numloc)
    elif len(str(a))==2:
        numloc = text.find(str(a)+".")
        filter(numloc)


'''

profiles = []
def filter(numloc):
    loc = text.find("https://www.webtalk.co/",numloc)
    end = text.find("\n" or "/news",loc)
    username = text[loc+len("https://www.webtalk.co/"):end]
    if "/news" in username:
        username=username[:username.find('/news')]
    profiles.append(username)


for a in range (1,40):
    numloc = text.find(str(a)+")")
    filter(numloc)
        




























