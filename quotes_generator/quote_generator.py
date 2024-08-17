import random

#A list of tech-centric quotes
quotes = [
    'Embrace The Journey',
    'Seek Always A New Horizon',
    'Code like there\'s no tomorrow',
    #add more quotes
]

def get_random_quote():
    return random.choice(quotes)

if __name__=="__main__":
    random_quote = get_random_quote()
    print(get_random_quote())
    



