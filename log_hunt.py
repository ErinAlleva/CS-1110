# Alex Hicks (awh4kc)

import re

list_one = []
list_two = []

datafile = open("access.log", "r")

url = re.compile(r"https://[a-z0-9.\/]+")

ip_address = re.compile(r"172.[0-9]{2}.[0-9]{2}.[0-9]{2,3}")

#results_url = []
#results_ip = []
list = []

for line in datafile:
    #results_url = url.match(line)
    results_ip = ip_address.match(line)
    results_ip = results_ip.group()
    #print(results_url)
    list.append(results_ip)

# ip_address_cavalier = re.compile(r"172.25.[0-9]{2}.[0-9]{2,3}")
# ip_address_wahoo = re.compile(r"172.27.[0-9]{2}.[0-9]{2,3}")



ip_add_cav = 0
ip_add_wah = 0
for item in list:
    if '172.25' in item:
        ip_add_cav += 1
    elif '172.27' in item:
        ip_add_wah += 1
if ip_add_cav > ip_add_wah:
    print("Cavalier has more traffic")

else:
    print("Wahoo has more traffic")

