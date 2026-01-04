# first of all lets load the json file
import json

# read the json file
with open("users.json","r") as f:
    data = json.load(f) # since we know that json.load() reads the json file and returns a list of dictionaries

# now we will clean the data
def cleanData(data):
    for item in data:
        # make ids integers
        item["simpleID"] = int(item["simpleID"])
        # make sure first name and last name is correct that is no whitespaces and capitalized
        item["firstname"] = item["firstname"].strip().capitalize() # whitespaces from fron and back will be removed and
        # first letter of firstname will be capitalized
        # make sure last name is correct that is no whitespaces and capitalized
        item["lastname"]  = item["lastname"].strip().capitalize()
        # make sure username should be in lower case and no whitespaces
        item["username"] = item["username"].strip().lower()
        #take care of password weather it has more than 1 and less than 16 characters or not
        if len(item["password"]) >1 and len(item["password"]) <16 and " " not in item["password"]:
            item["password"] = item["password"]
        else:
            item.pop("password") # remove the password key if it does not satisfy the condition
        # make sure email is in lower case and no whitespaces and should contain @ if not contain @ or no email 
        # then remove the email key
        if "@" in item["email"] and item["email"].strip() != "":
            item["email"] = item["email"].strip().lower()
        else:
            item.pop("email")
        # make sure birthdate is in the correct format (YYYY.MM.DD) if not then remove the birthdate key

        parts = item["birthDay"].split(".") # ["1990","05","23",""]  it will give 4 as a valid date is in form :- year.month.day.
        if len(parts) == 4 and item["birthDay"].strip() != "":   
            
             item["birthDay"] = item["birthDay"].replace("."," ").strip() # strings immutable so it return a new string
             item["birthDay"] = f"{item['birthDay'].split()[0]} year, {item['birthDay'].split()[1]} month, {item['birthDay'].split()[2]} day"
             item["birthDay"] = str(item["birthDay"])
        else:   
            # if no of "." is not 3 means atleast one thing is missing or empty string 
            item.pop("birthDay")
        # make sure married is either "yes" or "no" if any other answer or bank remove it
        if item["married"].strip().lower() == "yes":
            item["married"] = "Yes"
        elif item["married"].strip().lower() == "no":
            item["married"] = "No"
        else:
            item.pop("married")
        # from the list of favorite movies remove duplicates and make sure each movie name is capitalized and no whitespaces
            # to remove the duplicates we can convert the list to a set and then back to a list but our order will not be 
            #maintained so we will use another method that is dictionary as in dictionary keys are unique
        unique_movies = dict()
        for movie in item["favmovies"]:
            if len(item["favmovies"]) == 0:
                item["favmovies"] = ["No favorite movies listed"]
            elif movie.strip() != "":
                movieName = movie.strip().capitalize()
                unique_movies[movieName] = movieName
            else:
                item["favmovies"].remove(movie) # remove empty strings from the list
        item["favmovies"] = list(unique_movies.keys())

        if item["haskids"].strip().lower() == "yes":
            item["haskids"] = "Yes"
        elif item["haskids"].strip().lower() == "no":
            item["haskids"] = "No"
        else:
            item.pop("haskids")
        hairs = ["black","brown","blonde","red","gray","white","bald"]
        if item["haircolor"].strip().lower() in hairs:
            item["haircolor"] = item["haircolor"].strip().capitalize() # remove leaading and trailing whitespaces and capitalize
        else:
            item.pop("haircolor")
        if item["country"].strip() == "" or item["country"].strip().lower() == "n/a" or item["country"].strip().lower() == "none":
            item.pop("country")
        else:
            item["country"] = item["country"].strip().capitalize()
    return data

cleaned_data = cleanData(data)
with open("corrected_data.json","w") as f:
    json.dump(cleaned_data,f,indent=4)
