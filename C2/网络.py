import socket
def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        ts=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        ts.connect(('8.8.8.8',80))
        ip=ts.getsockname()[0]
    finally:
        ts.close()
    return ip


s = socket.socket()
host = socket.gethostname()
ip=get_host_ip()
print(host,ip)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind((ip, 1234))
while True:
    s.sendto(b'hello',('192.168.43.146',1234))