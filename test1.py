import requests
import msgpack
import time
def Get(url):
    r = requests.get(url, headers={'Expect': 'application/msgpack'}, stream=True, timeout=5)
    return (r.status_code, msgpack.unpackb(r.content, use_list=False, raw=False))

host = 'http://192.168.4.1:80'
urls= ['/Time/Time',
       '/Time/SystemStartTime',
       '/Time/SystemUptime',
       '/Runtime/LastIgnition',
       '/Runtime/StateUptime',
       '/Runtime/State',
       '/Errors/Lockout',
       '/Errors/LastErrorTime',
       '/Errors/LastError',
       '/Errors/LastLockoutReleseTime',
       '/Errors/ErrorList',
       '/Properties/ID',
       '/Properties/Firmware',
       '/Properties/Hardware',
       '/Properties/LastChange',
       '/Properties/Changes',
       '/Properties/Log',
       '/Properties/PermLog',
       '/Properties/Settings',
       '/Properties/Settings',
       '/Properties/UART1',
       '/Properties/UART2',
       '/Properties/APIversion',
       '/Querry/Interval',
       '/Modbus/Address',
       '/Modbus/GatewayTimeoutChange',
       '/ISM010_all',
       '/ISM010_available',
       '/FileList']
def go():
    for prop in urls:
        url = host+prop
        time.sleep(5)
        print (url)
        result=Get(url)
        print (prop,Get(url))
