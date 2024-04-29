import ssl 
from urllib import request
import shutil

def download_file(url, local_path):
    """
    Downloads a file from the given URL and saves it to the specified local path.
    """
    # The context is to work around an SSL certificat issue. See https://support.chainstack.com/hc/en-us/articles/9117198436249-Common-SSL-Issues-on-Python-and-How-to-Fix-it
    context = ssl._create_unverified_context()

    with request.urlopen(url, context=context) as response:
        with open(local_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

url = "https://mcdn.podbean.com/mf/web/rcuqsg/CON_LA_240325_-_SN_VSM_4_-_Podcast-v1bbkvn.mp3" 
local_path = './temp.mp3'

download_file(url, local_path)