from bs4 import BeautifulSoup
import urllib.request

for i in range (0,1000, 12):
    print(i)
    link_1 = "https://librarycatalog.bilkent.edu.tr/client/tr_TR/default/search/results?rw="
    link_2 = "&isd=true"

    tam_link = link_1 + str(i) + link_2
    #print(tam_link)

    webSayfasi = urllib.request.urlopen(tam_link).read()
    soup = BeautifulSoup(webSayfasi ,features="html.parser")

    kitap_listesi = soup.find_all("div", "results_bio")

    for link in kitap_listesi:
        #
        print(link.a.string)
        linkString = ""
        linkString =link

    #print(linkString)

