import random
import time
import requests

#A list of tech-centric quotes
#quotes = [
#    'Embrace The Journey',
#    'Seek Always A New Horizon',
#    'Code like there\'s no tomorrow',
#    #add more quotes
#]


#functionto get a random quote
def get_random_quote():
#    return random.choice(quotes)
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            json_data = response.json()
            quote = json_data["content"]
            author = json_data["author"]
            return f'"{quote}" -{author}'
        else:
            return "Error while getting a quote"
    except Exception as e:
        return f"Something went wrong: {e}"  
# display a new quote every 5 seconds
while True:
    print(get_random_quote())
    time.sleep(5)      

#if __name__=="__main__":
#    random_quote = get_random_quote()
#    print(get_random_quote())
    



