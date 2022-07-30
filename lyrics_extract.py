import requests, json
song = input("Enter song name: ")
artist = input("Enter artist name: ")
url = 'https://api.lyrics.ovh/v1/'+artist+'/'+song
response = requests.get(url)
json_data = json.loads(response.text)
with open ("lyrics.txt","w") as f:
    f.write(json_data['lyrics'])
#print(json_data['lyrics'])
input("press Enter to exit")
