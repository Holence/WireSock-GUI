from DTPySide import *
import urllib3

def get_current_info(key):
    try:
        url='https://ipinfo.io/json'
        pool=urllib3.connection_from_url(url,timeout=1)
        r=pool.urlopen("GET",url)
        text=r.data.decode("utf-8")
        res = json.loads(text)
        if key=="all":
            value=res
        else:
            value=res[key]
    except:
        value="Failed"

    return value