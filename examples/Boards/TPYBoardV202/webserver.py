try:
    import usocket as socket
except:
    import socket
import network

login_html = """
<html>
    <html>
    <head>
        <title>TPYBoard v202-WebServer</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
    </head>
    <body>
        <center>
        <h2>TPYBoard v202-WebServer</h2>
            <form action="/" method="get" accept-charset="utf-8">
                <p>UserName:&nbsp;<input type="text" name="name"  /></p>  
                <p>Password:&nbsp;&nbsp;<input type="password" name="pwd"  /></p>
                <input type="Submit" value="Login"  />         
                
            </form>
        </center>
    </body>
</html>
"""
html="""
<html>
    <html>
    <head>
        <title>TPYBoard v202-WebServer</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style type="text/css">
            h2
            {
                margin-top:4%;
                margin-bottom:40px;
            }
        </style>
    </head>
    <body>
        <center>
        <h2>Hello TPYBoard v202</h2>
        </center>
    </body>
</html>
"""
def CreatNetwork(ssid,pwd):
    ap_if = network.WLAN(network.AP_IF)#AP 模式
    ap_if.active(True)
    ap_if.config(essid=ssid,password=pwd)
    return ap_if.ifconfig()[0]
def main(ip):
    s = socket.socket()
    ai = socket.getaddrinfo(ip, 80)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://",ip,":80/")
    #默认的登录用户
    username='v202'
    userpwd='123456'
    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        req =client_s.readline()
        while True:
            h = client_s.readline()
            if h == b"" or h == b"\r\n":
                break
            req+=(h.decode('utf-8').lower())
        print("Request:")
        s_data=login_html#默认页面为登录页面
        req=req.decode('utf-8').lower().split('\r\n')
        #http header 解析
        req_data=req[0].lstrip().rstrip().replace(' ','')
        print(req_data)
        if req_data.find('favicon.ico')>-1:
            client_s.send(s_data)
            client_s.close()
            continue
        else:
            if len(req_data)>12:
                req_data=req_data.replace('get/?','').replace('http/1.1','')
                _name=req_data.find('name')
                _pwd=req_data.find('pwd')
                if _name>-1 and _pwd>-1:
                    #判断是否是用户登录
                    if req_data.find(username)>-1 and req_data.find(userpwd)>-1:
                        s_data=html
                        print('Login Success!')
            client_s.send(s_data)
            client_s.close()
        
myip=CreatNetwork('TPYBoard v202','tpyboard')#建立一个AP
main(myip)#搭建web服务器