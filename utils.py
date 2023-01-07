from DTPySide import *
import urllib3
from pythonping import ping

def get_current_info(key):
    try:
        url='https://ipinfo.io/json'
        pool=urllib3.connection_from_url(url,timeout=1)
        r=pool.urlopen("GET","/")
        text=r.data.decode("utf-8")
        res = json.loads(text)
        if key=="all":
            value=res
        else:
            value=res[key]
    except:
        value="Failed"
    return value

def ping_ip(ip, count, timeout):
    try:
        res=ping(ip, count=count, timeout=timeout/1000)

        if res.stats_success_ratio:
            true_rtt_avg = (res.rtt_avg_ms*res.stats_packets_sent-res.stats_packets_lost*timeout)/res.stats_packets_returned
        else:
            true_rtt_avg = "inf"
    
        return true_rtt_avg, res.stats_success_ratio
    except:
        return "inf", -1
