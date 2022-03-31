from DTPySide import *

def get_current_ip():

    try:
        ip = json.loads(requests.get('https://api.ipify.org/?format=json',timeout=1).text)['ip']    
    except:
        ip = "Failed"
    
    # print("Checking IP =", ip)

    return ip