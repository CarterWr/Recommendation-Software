# where BFS algo goes + other functions used in this program
from data import types, game_data
from Tree_struct import TreeNode
from collections import deque




def greet():
    """greet message to user"""
    print("\n\n=================================================")

    print("Welcome to Carter's game reccomendation software")

    print("=================================================\n\n")

def user_input():
    """Gathers user input for the autocomplete()"""
    return input("\nType the first few letters of the genre you would like to be recommended to you: ").strip()

def pattern_search(user_input, target):
    """Check if user input is in target"""
    if user_input in target:
        return True
    return False

def auto_complete_check(output):
    """Dooble checks if user wants to do selected option
    
       params: output(str): the option the user selected origonally
    """
    user = input("\nDo you wish to select '{}' y/n: ".format(output)).strip()
    if user == "y":
        return True
    elif user == "n":
        return False
    else:
        print("\nInput was invalid please try again.")
        auto_complete_check(output)

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
        return auto_complete()

    if len(output) > 1:
        print("\nLooks like you have a few options, please select one of the options given:\n {}\n".format(output))
        return auto_complete()
    
    if len(output) == 1:
        if auto_complete_check(output[0]):
            return output[0]
        else:
            return auto_complete()

def initalize_tree():
    root = TreeNode("Root")
    for data in game_data:
        temp = TreeNode(data)
        root.add_child(temp)

    return root

    
def budget_bfs(root_node, target_value):
    """Breadth first search but the tree is only 1 level deep so no need to search the children of children
       
       Params: root_node(node): The root node of a basic tree data struct
               target_value(string): The value we returened from our autocomplete function
    
       Returns: result(arr): a list of all values of all target nodes found
    """
    result = []
    for child in root_node.children:
        if child.value[0] == target_value:
            result.append(child.value[1:])
    
    return result


def format_results(bfs_result):
    """
       Takes in the result list from bfs and prints to the user the reccomendations formatted
    
       params: bfs_result(arr): a arr of results from the budget_bfs algo function
       
       returns: None: just formats and prints results to the console to look nice
       """
    
    print("\n\n\n\n\n\nBelow are the games recommended for you: \n\n")

    for game in bfs_result:
        print("\n\n----------------------------------\n")
        print("Name: {}".format(game[0]))
        print("Maturity Rating: {}".format(game[1]))
        print("Player Rating: {}".format(game[2]))
        print("Price: {}".format(game[3]))
        print("Where to buy: {}\n".format(', '.join(game[4])))
        print("----------------------------------\n\n")
        

def get_check_input():
    """tracks the users input if y recursive calls reccomendation main if n ends program else loops this function"""
    user = input("Would you like to see diffrent genre reccomendations? y/n: ").strip()
    if user == "y":
        return True
    if user == "n":
        return False
    else:
        return get_check_input()

def goodbye():
    """goodbye message to user"""
    print("\n\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    print("Thank you for using Carter's game reccomendation software")

    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")


def reccomendation_main(firstIteration=True, root=None):
    """This function acts as the main function to call all needed functions"""
    if firstIteration:
        greet()
        root = initalize_tree()
        
    bfs_result = budget_bfs(root, auto_complete())
    format_results(bfs_result)


    
    if get_check_input():
        firstIteration = False
        return reccomendation_main(firstIteration, root)
    else:
        goodbye()


