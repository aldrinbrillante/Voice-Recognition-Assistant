#this is code versions of different parts of my project progress

# this is the function that acts when user responds to being 'male' onto terminal
def male():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return friday("Good morning sir!")
    elif hour>= 12 and hour < 18:
        return friday("Good afternoon sir!")
    else:
        return friday("Good evening sir!")
# this is the function that acts when user responds to being 'female' onto terminal
def female():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        return friday("Good morning madam!")
    elif hour>= 12 and hour < 18:
        return friday("Good afternoon madam!")
    else:
        return friday("Good evening madam!")

