import requests, json

song = input("Enter song name: ")
artist = input("Enter artist name: ")

#construct url
url = 'https://api.lyrics.ovh/v1/'+artist+'/'+song

# get content from url
response = requests.get(url)
json_data = json.loads(response.text)

#create file and write lyrics
with open ("lyrics.txt","w") as f:
    f.write(json_data['lyrics'])

#exit program
input("press Enter to exit")
