# encoding=utf8
import sys, re, csv, time
reload(sys)
sys.setdefaultencoding('utf8')

from bs4 import BeautifulSoup
import urllib, time, random, pprint

def clean(text):
    cleantext = text.replace('\n', '')
    return cleantext

def dblspace(text):
    cleantext = re.sub(ur'  +', '' , text, re.UNICODE)
    return cleantext

def numdupl(mylist):
    return [v + str(mylist[:i].count(v) + 1) if mylist.count(v) > 1 else v for i, v in enumerate(mylist)]

# Based on https://stackoverflow.com/questions/48280586/catching-an-error-in-python-using-function/48280722#48280722
def get_attribute(obj, attr, href=None, func=None,recur=None):
    try:
        if  href== True:
            return getattr(obj, attr)['href']
        if  recur!= None:
            return getattr(obj, attr)(*[func],**{'recursive': recur})
        if  func!= None:
            temp2 = getattr(obj, attr)(func)
            return [clean(one.text) for one in temp2]
        else:
            return getattr(obj, attr)
    except AttributeError:
        return 'N/A'

targets = []

with open('wstargets1.csv') as f:
    reader = csv.reader(f)

    for i in range(0,700):
        next(reader)

    for i in range(700,791):
        currenttarget = next(reader)
        pagedict = {}
        r = urllib.urlopen('http://www.iwm.org.uk/memorials/item/memorial/'+currenttarget[0]).read()
        soup = BeautifulSoup(r, "html.parser")

        pagedict['target_name'] = currenttarget[1]

        pagedict['target_rn'] = currenttarget[0]

        pagedict['pagetitle'] = clean(soup.find('div', attrs={'class': 'page-title'}).text)

        pagedict['gglurl'] =  get_attribute(soup.find('div', attrs={'class': 'wmamap_link'}), 'a', href=True)

        if pagedict['pagetitle'] == 'Search UK War Memorials':
            print "Dead page ;("
        else:
            reg21 = get_attribute(get_attribute(soup.find('div', attrs={'id': 'memorials-region2'}),'dl'),'find_all',func='dt')

            reg21 = [u'reg2_' + dblspace(each).lower().replace(' ','_') for each in reg21 if reg21 != u'N/A']

            reg22 = get_attribute(get_attribute(soup.find('div', attrs={'id': 'memorials-region2'}),'dl'),'find_all',func='dd')

            reg22 = [dblspace(each) for each in reg22  if reg22 != u'N/A']

            pagedict.update({k: v for k, v in zip(reg21, reg22)})

            try:
                subper = reg21.index('reg2_subject/period')
                wars1 = getattr(get_attribute(soup.find('div', attrs={'id': 'memorials-region2'}),'dl'),'find_all')('dd')[subper]
                wars2 = getattr(wars1,'find_all')('li')
                pagedict.update({'reg2_subject/period_' + str(k+1): v for k, v in enumerate([dblspace(clean(each.text)) for each in wars2 ])})
            except ValueError:
                pass

            try:
                creat = reg21.index('reg2_creator')
                crt1 = getattr(get_attribute(soup.find('div', attrs={'id': 'memorials-region2'}),'dl'),'find_all')('dd')[creat]
                crt2 = getattr(crt1,'find_all')('li')
                pagedict.update({'reg2_creator_' + str(k+1): v for k, v in enumerate([dblspace(clean(each.text)) for each in crt2 ])})
            except ValueError:
                pass

            reg31 = get_attribute(soup.find('div', attrs={'id': 'memorials-region3'}),'find_all',func='h5')

            reg31 = numdupl([u'reg3_' + dblspace(each).lower().replace(' ','_') for each in reg31 if reg31 != u'N/A'])

            reg32 = get_attribute(soup.find('div', attrs={'id': 'memorials-region3'}),'find_all', func='div', recur=False)

            reg32 = [dblspace(clean(get_attribute(get_attribute(each,'div'),'text'))) for each in reg32 if reg32 != u'N/A' ]

            pagedict.update({k: v for k, v in zip(reg31, reg32)})

            pprint.pprint(pagedict)

        targets.append(pagedict)

        rt1 = random.randint(20,30)

        print "sleeping for %i seconds" % rt1
        print "done loop --> #" + str(i)

        time.sleep(rt1)

    with open('data3-wsonly-700.csv', 'w') as csvfile:
        fieldnames = sorted(set([k for d in targets for k in d.keys()]))
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,restval='N/A')
        writer.writeheader()
        for eachitem in targets:
            writer.writerow(eachitem)

print "current task completed"
