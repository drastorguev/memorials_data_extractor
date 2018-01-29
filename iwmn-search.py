# encoding=utf8
import sys, time, urllib, re
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf8')

try:
    with open('Sutton+Coldfield-targets.txt', 'w') as f:
        for i in range(5):
            r = urllib.urlopen('https://www.iwm.org.uk/memorials/search?query=Sutton+Coldfield&page='+str(i)).read()
            soup = BeautifulSoup(r, "html.parser")
            targets = soup.find_all('h6', attrs={'class': 'teaser__title'})
            for each in targets:
                f.write((str(each.text)+'\t'+str(each.a['href'])+'\t'+str(each.a['href'].split('/memorial/')[-1])+'\n'))
            print 'loop done #' +str(i)
            time.sleep(10)
except:
    f.close()
