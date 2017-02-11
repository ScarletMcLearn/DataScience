####import urllib.request
##
####from urllib import request
##
###import error
##
##try:
##    from urllib.request  import urlopen
##except ImportError:
##    from urllib2 import urlopen
##
##    
##import re
##
##
##url = "http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/"
##
##
##request = urllib.request.Request(url)
##
##
####request = urllib2.request(url) - custom 
##
##
####response = urllib.request.urlopen(request)
##
##
####response = urllib2.urlopen(request)
##
##response = urlopen(request)
##
##responseData = response.read()
##
##















import re



try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

html = urlopen(#"http://www.google.com/")
"https://pythonprogramming.net/parse-website-using-regular-expressions-urllib/?completed=/regular-expressions-regex-tutorial-python-3/")

html_data = (html.read())


paragraphs = re.findall(r'<p>(.*?)</p>',str(html_data))



for eachP in paragraphs:
    print(eachP)

##print(paragraphs)

##print(html_data)
