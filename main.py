# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, jsonify, request
import yaml
import ast
import random

app = Flask(__name__)

def registeredTrips():
    trips = []
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        trips = list(con["TRIPS"].keys())
    return trips
def registeredEmailIds():
    email_ids = []
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        email_ids = list(con["USERS"].keys())
    return email_ids

Registered_EmailIds = registeredEmailIds()
Registered_Trips = registeredTrips()


@app.route("/")
def hello_w():
    return "Hello"

@app.route("/createfile")
def create_a_file():
    file_path = r"C:\Users\Jayprakash\Desktop\AppDB\newfile" + str(random.randint(10000,1000000)) + r".txt"
    with open(file_path,'w') as file:
        file.write("uwejsddddddddddddd"*1000)

@app.route("/details")
def getDetails():
    d = {"name":"Harry", "email":"harry@gmail.com"}
    return (d, 200, {'Content-Type':'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
# Press the green button in the gutter to run the script.
@app.route("/login", methods=['POST'])
def getLoginDetails():
    req_data = request.get_data()
    req_data = ast.literal_eval(req_data.decode())
    result = {'data': {}, 'authorized': False}
    with open('user_data.yaml', 'r') as file:
        con = yaml.safe_load(file)
        req_email = req_data.get('email', None)
        if req_email in list(con["USERS"].keys()):
            password = req_data.get('password', None)
            if con["USERS"][req_email]['Password']==password:
                result['authorized'] = True
                result['data'] = con["USERS"][req_email]
    result['data'].pop("Password")
    response = (result, 200, {'Content-Type':'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

@app.route("/userdetails", methods=["POST"])
def getUserDetails():
    req_data = request.get_data()
    req_data = ast.literal_eval(req_data.decode())
    userEmail = req_data["Email"]
    result = {"data":{}}
    with open('user_data.yaml', 'r') as file:
        con = yaml.safe_load(file)
        result["data"] = con["USERS"][userEmail]
    result['data'].pop("Password")
    response = (result, 200, {'Content-Type': 'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

@app.route("/signup", methods=["POST"])
def writeSignUpDetails():
    data_to_write = {}
    req_data = request.get_data()
    req_data = ast.literal_eval(req_data.decode())
    with open('user_data.yaml', 'r') as file:
        cont = yaml.safe_load(file)
        data_to_write = cont

    email_id = req_data.get("email", "")
    user_data = {"Name":req_data.get("name", ""), "Email":email_id, "Password":req_data.get("password", ""), "Trips":[],"Polls":[], "Friends":{"Ids":[], "Request Sent":[], "Request Received":[]}}


    data_to_write["USERS"][email_id] = user_data
    # print(data_to_write)
    if not email_id in Registered_EmailIds:
        with open('user_data.yaml', 'w') as file:
            yaml.dump(data_to_write, file)
        result = {'data':{'message':'Sign Up Successful!'}}
    else:
        result = {'data':{'error':'Email Already Registered!'}}
    response = (result, 200, {'Content-Type':'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

@app.route("/searchfriends", methods=["POST"])
def searchFriends():
    req_data = request.get_data()

    req_data = ast.literal_eval(req_data.decode())
    userEmail = req_data["userEmail"]
    result = {'matchedIds':[], 'updatedUserFriends':{}}
    matchValue = req_data.get("matchValue", "")
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        userFriends = con["USERS"][userEmail]["Friends"]["Ids"]
    if matchValue:
        for email_id in Registered_EmailIds:
            if matchValue in email_id and email_id!=userEmail and email_id not in userFriends:
                result["matchedIds"].append(email_id)
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        result['updatedUserFriends'] = con["USERS"][userEmail]["Friends"]
    response = (result, 200, {'Content-Type':'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

@app.route("/addfriend", methods=["POST"])
def addFriend():
    req_data = request.get_data()
    req_data = ast.literal_eval(req_data.decode())
    data_to_write = {}
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        data_to_write = con
    if req_data["receiver"] not in data_to_write["USERS"][req_data["sender"]]["Friends"]["Request Sent"]:
        data_to_write["USERS"][req_data["sender"]]["Friends"]["Request Sent"].append(req_data["receiver"])
    if req_data["sender"] not in data_to_write["USERS"][req_data["receiver"]]["Friends"]["Request Received"]:
        data_to_write["USERS"][req_data["receiver"]]["Friends"]["Request Received"].append(req_data["sender"])
    print(req_data)
    result = {"updatedUserFriends":{}}
    with open("user_data.yaml", 'w') as file:
        yaml.dump(data_to_write, file)
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        result["updatedUserFriends"] = con["USERS"][req_data["sender"]]["Friends"]
    response = (result, 200, {'Content-Type':'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

@app.route("/getfriends", methods=["POST"])
def getFriends():
    req_data = request.get_data()
    req_data = ast.literal_eval(req_data.decode())
    result = {"userFriends":{}}
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        userFriendsDetails = con["USERS"][req_data]["Friends"]
        result["userFriends"]["Request Received"] = userFriendsDetails["Request Received"]
        result["userFriends"]["Request Sent"] = userFriendsDetails["Request Sent"]
        result["userFriends"]["NamesIds"] = []
        for friend_id in userFriendsDetails["Ids"]:
            if con["USERS"].get(friend_id, None):
                friend_name = con["USERS"][friend_id]["Name"]
                result["userFriends"]["NamesIds"].append({friend_id:friend_name})
            else:
                result["userFriends"]["NamesIds"].append({friend_id:"Fake"})

    # result["userFriends"] = con["USERS"][req_data]["Friends"]
    response = (result, 200, {'Content-Type':'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

@app.route("/acceptrequest", methods=["POST"])
def acceptFriendRequest():
    req_data = request.get_data()
    req_data = ast.literal_eval(req_data.decode())
    result = {"updatedUserFriends":{}}
    data_to_write = {}
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        data_to_write = con

    if req_data["Acceptor"] and req_data["FriendToBe"]:
        data_to_write["USERS"][req_data["Acceptor"]]["Friends"]["Ids"].append(req_data["FriendToBe"])
        data_to_write["USERS"][req_data["Acceptor"]]["Friends"]["Request Received"].remove(req_data["FriendToBe"])
        data_to_write["USERS"][req_data["FriendToBe"]]["Friends"]["Ids"].append(req_data["Acceptor"])
        data_to_write["USERS"][req_data["FriendToBe"]]["Friends"]["Request Sent"].remove(req_data["Acceptor"])
        result["updatedUserFriends"] = data_to_write["USERS"][req_data["Acceptor"]]["Friends"]

    with open("user_data.yaml", 'w') as file:
        yaml.dump(data_to_write, file)

    response = (result, 200, {'Content-Type': 'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

@app.route("/trips", methods=["POST"])
def getTripsDetails():
    req_data = request.get_data()
    req_data = ast.literal_eval(req_data.decode())
    print(req_data)
    tripIds = req_data.get("trips",[]) if type(req_data)=='dict' else list(req_data)
    result = {'data': []}
    with open('user_data.yaml', 'r') as file:
        con = yaml.safe_load(file)
        registered_trips = Registered_Trips
        for tripId in tripIds:
            if tripId in registered_trips:
                result["data"].append(con["TRIPS"][tripId])

    response = (result, 200, {'Content-Type':'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

@app.route("/addtrip", methods=["POST"])
def AddTripToDatabase():
    req_data = request.get_data()
    req_data = ast.literal_eval(req_data.decode())
    print(req_data)
    result = {}
    data_to_write = {}
    with open("user_data.yaml", 'r') as file:
        con = yaml.safe_load(file)
        data_to_write = con
    users_included = [req_data.get("TripAdmin", None)]
    polls_in_trip = []
    for key,val in req_data["PollDetails"].items():
        polls_in_trip.append(key)
        data_to_write["POLLS"][key] = val
    if req_data["Friends"]:
        users_included.extend(req_data["Friends"])


    data_to_write["TRIPS"][req_data["TripId"]] = {}
    data_to_write["TRIPS"][req_data["TripId"]]["Name"] = req_data["Name"]
    data_to_write["TRIPS"][req_data["TripId"]]["Users"] = users_included
    data_to_write["TRIPS"][req_data["TripId"]]["Polls"] = polls_in_trip
    data_to_write["TRIPS"][req_data["TripId"]]["TripId"] = req_data["TripId"]

    for user in users_included:
        data_to_write["USERS"][user]["Trips"].append(req_data["TripId"])
        data_to_write["USERS"][user]["Polls"].extend(polls_in_trip)
    print(data_to_write["TRIPS"][req_data["TripId"]])
    print(data_to_write["POLLS"])
    with open("user_data.yaml", 'w') as file:
        yaml.dump(data_to_write, file)
        result["Success"] = True
    # print()
    response = (result, 200, {'Content-Type': 'text/json', 'Access-Control-Allow-Origin': 'http://localhost:3000'})
    return response

if __name__ == '__main__':
    app.run(debug=True)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
