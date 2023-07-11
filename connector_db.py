import json
import pymysql

json_data=open("D:\Escritorio\FurryFriends2daParte2\FuryFriendsFinal-main\productos.json").read()
json_obj=json.loads(json_data)
con=pymysql.connect(host="localhost",user="root",password="",db="json")

cursor=con.cursor()

for item in json_obj:
    id=item.get("id")
    precio=item.get("precio")
    title=item.get("title")
    thumbnailUrl=item.get("thumbnailUrl")
    cursor.execute("insert into json_file(id,precio,title,thumbnailUrl) value(%s,%s,%s,%s)",(id,precio,title,thumbnailUrl))
con.commit()
con.close()
