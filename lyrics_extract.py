import requests, json

song = input("Enter song name: ")
artist = input("Enter artist name: ")

#construct url
url = 'https://api.lyrics.ovh/v1/'+artist+'/'+song

#get content from url and convert to JSON format
response = requests.get(url)
json_data = json.loads(response.text)

#convert JSON format data to readable text
with open ("lyrics.txt","w") as f:
    f.write(json_data['lyrics'])

#exit program
input("press Enter to exit")
