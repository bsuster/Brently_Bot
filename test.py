from pathlib import Path

myFile = Path("Brently_Bot-master/info.txt")
if myFile.is_file():
    with open("Brently_bot-master/info.txt","r+") as file_info:
        print("File exists!")
        token = str(file_info.readline())
        token = token[7:66]
        print("Token: " + token + " soup") 
        server_id = str(file_info.readline())
        server_id = server_id[11:]
        print("Server ID: " + server_id)


elif not myFile.is_file(): 
    with open("Brently_bot-master/info.txt", "w+") as file_info:
        print("Creating info.txt...")
        file_info.write("Token: \n")
        file_info.write("Server ID: ")
