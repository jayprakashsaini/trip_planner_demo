import yaml
# d = {}
# user2 = dict()
# user2["Name"] = "Naman Nahar"
# user2["Email"] = 'namannahar@gmail.com'
# user2["Password"] = 0000
# user2["Trips"] = [26729, 78902]
# user2["Polls"] = [35267]
# with open('user_data2.yaml', 'r') as yaml_file:
#     cont = yaml.safe_load(yaml_file)
#     # cont = yaml.load(yaml_file, Loader=yaml.FullLoader)
#     d = cont
#     # cont = {"USERS":{}}
#     # print("11111", cont)
#
#     d["USERS"]['namannahar@gmail.com'] = user2
#     print("222222", d)
#
# print(d)
# with open('user_data2.yaml', 'w') as file:
#     yaml.dump(d, file)
#     # print(str(cont))
#     # print(bytes(str(cont), 'utf-8'))
#     # b = bytes(str(cont), 'utf-8')
#     # cont =
#     # file.write(b)
#     # yaml.dump(data_to_write, yaml_file, default_flow_style=False)
with open("user_data.yaml", 'r') as file:
    d = yaml.safe_load(file)
    print(d["USERS"]["jayprakashsaini549@gmail.com"]["Polls"])
    print(type(d["USERS"]["jayprakashsaini549@gmail.com"]["Polls"]))
    print(d["USERS"]["jayprakashsaini549@gmail.com"]["Trips"])

