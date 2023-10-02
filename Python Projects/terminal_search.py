import requests
import json
from requests.models import PreparedRequest
#Programmable Search Engine Key
engine_key="YOUR_SEARCH_ENGINE_KEY"
cx="YOUR_SEARCH_ENGINE_IDENTIFIER"
URL = "https://www.googleapis.com/customsearch/v1"
#Function for fetching the search results from Google Programmable Search Engine
def gSearch(query):
    params = {
        "key":engine_key,
        "cx": cx,
        "gl": "IN",
        "q": query,
    }
    req = PreparedRequest()
    req.prepare_url(URL, params)

    response = requests.get(req.url)

    resDict = json.loads(response.text)['items']
    pairedResult=[]
    links=[]
    for i in resDict:
        #Storing the raw response in a structured list-tupple format
        pairedResult.append((i['title'],i['snippet'],i['link']))
        
    return pairedResult
def displayResult(arr):
    res=''
    print('\n')
    for i in range(0,len(arr)):
        #Preparing the final result to print, using text decorations
        res = res+str(i+1)+'. '+'\033[1m'+arr[i][0]+'\033[0m'+'\n'+'\033[91m'+arr[i][1]+'\033[0m'+'\n'+ '\x1B[3m'+'Link: '+'\033[94m'+arr[i][2]+'\033[0m'+'\x1B[0m\n\n'
    print(res)

def main():
    print("Welcome  to terminal search, a conceptual terminal search engine powered by python which demostrates the power of Google's Programmable Search Engine!!!")
    while(True):
        query=input("Enter something to search\n")
        res = gSearch(query)
        displayResult(res)
        choice=input("DO you want to search again???\n \x1B[3mPress 1 for Yes and 0 for No\x1B[0m\n")
        if(choice=='0'):
            break
    print("Thanks for using this programmable search engine!")

if __name__=="__main__":
    main()