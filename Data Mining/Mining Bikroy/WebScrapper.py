import urllib3

from bs4 import BeautifulSoup


## http = urllib3.PoolManager()

## request = http.request('GET', 'http://en.akinator.com/personnages/')

def requestify(link):
    '''
    Give link string as parameter and return request object. 
    '''
    http = urllib3.PoolManager()
    return(http.request('GET', link))


def soupify(req):
    '''
    Give request object as parameter and return soup object. 
    '''
    soup = BeautifulSoup(req.data, 'lxml')
    return(soup)


def soupified_request(link):
    return (soupify(requestify(link)))


## print(soupified_request('www.google.com'))