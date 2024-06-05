# where BFS algo goes + other functions used in this program
from data import types
def greet():
    """greet message to user"""
    pass

def user_input():
    """Gathers user input for the autocomplete()"""
    return input("Type the first few letters of the genre you would like to be reccomended to you: ")

def pattern_search(user_input, target):
    if user_input in target:
        return True
    return False

def auto_complete():
    """Uses input function to get user input and checks if the begging part of genre equals input
    
       return: output(string): the result of matchs of user input
    """
    user = user_input()
    output = []
    
    for genre in types:
        if pattern_search(user, genre):
            output.append(genre)
    
    if len(output) == 0:
        print("\nLooks like we don't have what you're looking for please try a diffrent genre.\n")
        auto_complete()

    if len(output) > 1:
        print("\nLooks like you have a few options, please select one of the options given:\n {}\n".format(output))
        auto_complete()
    else:
        return output[0]



    



def goodbye():
    """goodbye message to user"""
    pass


def reccomendation_main():
    """This function acts as the main function to call all needed functions"""
    greet()

    auto_complete()

    goodbye()

