from DTPySide import *

def get_current_ip():
    return get_current_info("ip")

def get_current_info(key):
    try:
        res = json.loads(requests.get('http://ipinfo.io/json',timeout=1).text)
        if key=="all":
            value=res
        else:
            value=res[key]
    except:
        value="Failed"

    return value