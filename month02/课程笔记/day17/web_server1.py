import re
from socket import *
from select import select


class HTTPServer:
    def __init__(self, host="0.0.0.0", port=8000, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 创建套接字和地址绑定
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setblocking(False)
        self.rlist.append(self.sockfd)

    def bind(self):
        self.address = (self.host, self.port)
        self.sockfd.bind(self.address)

    def start(self):
        self.sockfd.listen(3)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    c.setblocking(False)
                    self.rlist.append(c)
                else:
                    self.handle(r)

    # 对每个客户端进行请求处理
    def handle(self, connfd):
        request = connfd.recv(1024).decode()
        print(request)
        pattern = r"[A-Z]+\s+(/\S*)"
        try:
            info = re.match(pattern, request).group(1)  # 只取子组内容
        except:
            self.rlist.remove(connfd)
            connfd.close()
            return
        else:
            self.get_html(connfd, info)

    def get_html(self, connfd, info):
        # info :  /     /xxxxx.html
        if info == '/':
            filename = self.html + '/index.html'
        else:
            filename = self.html + info

        # 打开网页
        try:
            f = open(filename, 'rb')
        except:
            # 考虑请求的网页可能不存在
            response_headers = "HTTP/1.1 404 NOT FOUND\r\n"
            response_headers += "Content-Type:text/html\r\n"
            response_headers += "\r\n"
            response_content = "<h1>Sorry......</h1>"
            response = (response_headers + response_content).encode()
        else:
            # 请求的网页存在
            response_content = f.read()
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers += "Content-Type:text/html\r\n"
            response_headers += "Content-Length:%d\r\n" % len(response_content)
            response_headers += "\r\n"
            response = response_headers.encode() + response_content
            f.close()
        finally:
            # 将http响应发送给浏览器
            connfd.send(response)


if __name__ == '__main__':
    "通过类快速搭建服务，为了展示这组网页"
    host = "0.0.0.0"
    port = 8000
    html = "./static"
    # 实例化对象
    httpd = HTTPServer(host=host,port=8000,html=html)
    # 调用方法
    httpd.start()
