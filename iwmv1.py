# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


from bs4 import BeautifulSoup
import urllib, time, random

def clean(text):
    cleantext = text.replace('\n', '')
    return cleantext

filename = "data.txt"
f = open(filename, 'a')
# headers = "order\treg2refnum\tpagetitle\tgglurl\treg2memtype\treg2lost\treg2town\treg2county\treg2district\treg2subper\treg2creat\treg2cer\treg3curloc\treg3descr\treg3inscr\treg3inscr_leg\treg3names\treg3names_url\treg3subj1\treg3subj2\treg3compt\treg3cer1\treg3cer2\treg3hist\treg3cost\treg3trust\treg3spons\treg3resp\treg3ref\n"
# f.write(headers)

for i in range(162,200):

    r = urllib.urlopen('http://www.iwm.org.uk/memorials/item/memorial/'+str(i)).read()
    soup = BeautifulSoup(r, "html.parser")

    pagetitle = clean(soup.find('div', attrs={'class': 'page-title'}).text)
    try:
        gglurl =  soup.find('div', attrs={'class': 'wmamap_link'}).a['href']
    except AttributeError:
        gglurl = pagetitle = 'N/A'

    try:
        reg2list = soup.find('div', attrs={'id': 'memorials-region2'}).dl.find_all("dd")

        try:
            reg2refnum = clean(reg2list[0].text.replace(' ', ''))
        except (AttributeError, IndexError, TypeError):
            reg2refnum = 'N/A'
        try:
            reg2memtype = clean(reg2list[1].text)
        except (AttributeError, IndexError, TypeError):
            reg2memtype = 'N/A'
        try:
            reg2lost = clean(reg2list[2].text.replace(' ', ''))
        except (AttributeError, IndexError, TypeError):
            reg2lost = 'N/A'
        try:
            reg2town = clean(reg2list[3].text)
        except (AttributeError, IndexError, TypeError):
            reg2town = 'N/A'
        try:
            reg2county = clean(reg2list[4].text)
        except (AttributeError, IndexError, TypeError):
            reg2county = 'N/A'
        try:
            reg2district = clean(reg2list[5].text)
        except (AttributeError, IndexError, TypeError):
            reg2district = 'N/A'
        try:
            reg2subper = clean(reg2list[6].text)
        except (AttributeError, IndexError, TypeError):
            reg2subper = 'N/A'
        try:
            reg2creat = clean(reg2list[7].text)
        except (AttributeError, IndexError, TypeError):
            reg2creat = 'N/A'
        try:
            reg2cer = clean(reg2list[8].text.replace('    ', ''))
        except (AttributeError, IndexError, TypeError):
            reg2cer = 'N/A'
    except AttributeError:
        reg2refnum = reg2memtype = reg2lost = reg2town = reg2county = reg2district = reg2subper = reg2creat = reg2cer = 'N/A'


    try:
        reg3list = soup.find('div', attrs={'id': 'memorials-region3'}).find_all('div',recursive=False)

        try:
            reg3curloc = clean(reg3list[0].div.text.replace('    ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3curloc = 'N/A'
        try:
            reg3descr = clean(reg3list[1].div.text)
        except (AttributeError, IndexError, TypeError):
            reg3descr = 'N/A'
        try:
            reg3inscr = clean(reg3list[2].div.text)
        except (AttributeError, IndexError, TypeError):
            reg3inscr = 'N/A'
        try:
            reg3inscr_leg = clean(reg3list[3].div.text)
        except (AttributeError, IndexError, TypeError):
            reg3inscr_leg = 'N/A'
        try:
            reg3names = clean(reg3list[4].div.text.replace('    ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3names = 'N/A'
        try:
            reg3names_url = reg3list[4].div.a['href']
        except (AttributeError, IndexError, TypeError):
            reg3names_url = 'N/A'
        try:
            reg3subj1 = clean(reg3list[5].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3subj1 = 'N/A'
        try:
            reg3subj2 = clean(reg3list[6].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3subj2 = 'N/A'
        try:
            reg3compt = clean(reg3list[7].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3compt = 'N/A'
        try:
            reg3cer1 = clean(reg3list[8].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3cer1 = 'N/A'
        try:
            reg3cer2 = clean(reg3list[9].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3cer2 = 'N/A'
        try:
            reg3hist = clean(reg3list[10].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3hist = 'N/A'
        try:
            reg3cost = clean(reg3list[11].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3cost = 'N/A'
        try:
            reg3trust = clean(reg3list[12].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3trust = 'N/A'
        try:
            reg3spons = clean(reg3list[13].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3spons = 'N/A'
        try:
            reg3resp = clean(reg3list[14].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3resp = 'N/A'
        try:
            reg3ref = clean(reg3list[15].div.text.replace('     ', ''))
        except (AttributeError, IndexError, TypeError):
            reg3ref = 'N/A'
    except AttributeError:
        reg3curloc = reg3descr = reg3inscr = reg3inscr_leg = reg3names = reg3names_url = reg3subj1 = reg3subj2 = reg3compt = reg3cer1 = reg3cer2 = reg3hist = reg3cost = reg3trust = reg3spons = reg3resp = reg3ref = 'N/A'

    f.write(str(i) + '\t' + reg2refnum + '\t' + pagetitle + '\t' + gglurl + '\t' + reg2memtype + '\t' + reg2lost + '\t' + reg2town + '\t' + reg2town + '\t' + reg2county + '\t' + reg2district + '\t' + reg2subper + '\t' + reg2creat + '\t' + reg2cer + '\t' + reg3curloc + '\t' + reg3descr + '\t' + reg3inscr + '\t' + reg3inscr_leg + '\t' + reg3names + '\t' + reg3names_url + '\t' + reg3subj1 + '\t' + reg3subj2 + '\t' + reg3compt + '\t' + reg3cer1 + '\t' + reg3cer2 + '\t' + reg3hist + '\t' + reg3cost + '\t' + reg3trust + '\t' + reg3spons + '\t' + reg3resp + '\t' + reg3ref + "\n")
    print "writing row #" + str(i)

    rt1 = random.randint(15,30)
    print "sleeping for %i seconds" % rt1
    time.sleep(rt1)

f.close()
print "current task completed"
