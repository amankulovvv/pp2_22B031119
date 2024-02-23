import json

with open('sample-data.json') as a:
    data = json.load(a)

print("Interface Status")
print("="*100)
print("{:<50}{:<25}{:<8}{}".format("DN", "Description", "Speed", "MTU"))
print("-"*100)

for interface in data["imdata"]:
    dn = interface["l1PhysIf"]["attributes"]["dn"]
    description = interface["l1PhysIf"]["attributes"]["descr"]
    speed = interface["l1PhysIf"]["attributes"]["speed"]
    mtu = interface["l1PhysIf"]["attributes"]["mtu"]
    print("{:<50}{:<25}{:<8}{}".format(dn, description, speed, mtu))