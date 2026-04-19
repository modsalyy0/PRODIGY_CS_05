import socket

print("Packet Analyzer Started...\n")

host = socket.gethostbyname(socket.gethostname())

print("Your IP:", host)
print("Listening for packets...\n")

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((host, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

for i in range(5):
    packet = s.recvfrom(65565)
    print("Packet:", packet[0][:40])

s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)