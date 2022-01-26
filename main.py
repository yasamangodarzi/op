import requests
import pymongo
myclient = pymongo.MongoClient()

mydb = myclient["Music_bot"]
mycol = mydb["songs"]
m={"name":"مهتاب تر از باران ","address":"https://webahang.ir/single-tracks/alireza-ghorbani-mahtab-tar-az-baran/"}
mycol.insert_one(m)
def find(input):
 response = requests.get("http://api.codebazan.ir/music/?type=search&query={}&page=1".format(input)).json()
 Title=response["Result"]
 answer=""
 answer2=""

 lid=[]
 for  x in Title:
     y=x["Title"]
     yg=x["Link"]
     mydict = {"name": str(y), "address": str(yg)}
     print(mydict)
    # answer=answer+y+"\n"+yg+"\n"
     syu=y+"\n"+yg+"\n"
     lid.append(syu)
     mycol.insert_one(mydict)
 for x in range(3):

         answer=answer+lid[x]



 print(answer)

find("اسمان")

