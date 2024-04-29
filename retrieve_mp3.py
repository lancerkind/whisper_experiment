import ssl 
from urllib import request

url = "https://mcdn.podbean.com/mf/web/rcuqsg/CON_LA_240325_-_SN_VSM_4_-_Podcast-v1bbkvn.mp3" 

# The below is to work around an SSL certificat issue. See https://support.chainstack.com/hc/en-us/articles/9117198436249-Common-SSL-Issues-on-Python-and-How-to-Fix-it
context = ssl._create_unverified_context()

response = request.urlopen(url, context=context)
#check for error here.
