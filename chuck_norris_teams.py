import requests
import json
from config import access_token, roomId


def get_joke(): #function that pulls a random Chuck Norris joke
    url = "http://api.icndb.com/jokes/random?firstName=John&amp;lastName=Doe"
    payload={'Accept':'text/plain'}
    headers = {'Cookie': '__cfduid=d9eb69b11b962f8f8f8ac2483f964b5df1615221088'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response_data = json.loads(response.text)
    joke = response_data.get('value',{}).get('joke')
    return joke


def post_message(): #function to post in Webex Teams
    joke_message = get_joke()
    print (joke_message)
    apiUrl = 'https://webexapis.com/v1/messages'

    httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    body = { 'roomId': roomId, 'text': joke_message }

    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )

    print( response.status_code )
    print( response.text )


post_message() #executes the post_message function
