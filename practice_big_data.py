import yaml
# from pprint import pprint
d = {"Friends": {"Ids": [[1, 2, 3], [3, 4, 5], []], "Request Received": [], "Request Sent": []}, "Trips": [], "Polls": [], "Email": "abc@def.com", "Password": "qwerty"}
dtr = {}
# for i in range(10):
#     key = "user" + str(i)
#     dtr[key] = d
#     print(key)
#     dtr[key] = key
#
# pprint(dtr)
# with open("user_data3.yaml", 'r') as file:
#     con = yaml.safe_load(file)
#     dtr = con
#     print(con["user34543"])
#
# dtr["user34543"]["Name"] = "Name Changed"
# dtr["user34543"]["Friends"]["Ids"].append("friend1")
# with open("user_data3.yaml", 'w') as file:
#     yaml.dump(dtr, file)

with open("user_data3.yaml", 'w') as file:
    yaml.dump(d, file)
    # con = yaml.safe_load(file)
    # print(con["user34543"])
# with open("user_data3.yaml", 'w') as file:
#     yaml.dump(dtr, file)