import threading
import os


ip_list = ["8.8.8.8", "192.168.1.1", "10.0.0.1"]

def ping(ip):
    output = os.system(f"ping -c 1 {ip}>/dev/null 2>&1")
    if output == 0:
        print(f"{ip} is up")
    else:
        print(f"{ip} is down")


for ip in ip_list:
    ping(ip)


threads = []
for ip in ip_list:
    t = threading.Thread(target=ping, args=(ip,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("ping scan completed")