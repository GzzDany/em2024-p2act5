def sol_calculate_price():
    ### BEGIN SOLUTION
    prices = {"chilaquiles":100, "tacos":50, "molletes":85, "huevos rancheros":80}
    print("The products and prices are:")
    print(prices)
    total = 0
    while True:
        product = input("Input the product name. Type 'stop' to stop. ")
        if product == "stop":
            break
        if product not in prices.keys():
            print("Invalid product name. Try again.")
            continue
        total += prices[product]
    print("Your total price is: " + str(total))
    return

def input_calculate_price(num_tests=30):
    from random import choices, choice
    options = ["chilaquiles", "tacos", "molletes", "huevos rancheros", "bad_input", "another_bad_input"]
    input_values = [choices(options, k=choice([1, 4, 3, 5])) for i in range(num_tests)]
    for l in range(num_tests):
        input_values[l].append("stop")
    args = [{} for i in range(num_tests)]
    return input_values, args   

def sol_count_items(my_list):
    ### BEGIN SOLUTION
    counts = {}
    for item in my_list:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    return counts
    ### END SOLUTION

def input_count_items(num_tests=30):
    from random import choices, choice
    options = [i for i in range(10)]
    args = [{"my_list":choices(options, k=choice([4, 10, 8, 15]))} for i in range(num_tests)]
    input_values = [[] for i in range(num_tests)]
    return input_values, args

def sol_rock_paper_scissors_lizard_spock(player1, player2):
    winner_loser = {"scissors":['paper', 'lizard'],
                           "paper":["rock", "spock"], 
                           "rock":["scissors", "lizard"], 
                           "lizard":["spock", "paper"], 
                           "spock":["scissors", "rock"]}
    ### BEGIN SOLUTION
    if player1 == player2:
        print("It's a tie!")
        return
    elif player2 in winner_loser[player1]:
        print("Player 1 wins!")
        return
    else:
        print("Player 2 wins!")
        return
    ### END SOLUTION

def input_rock_paper_scissors_lizard_spock(num_tests=30):
    input_values = [[] for i in range(num_tests)]
    from random import choice
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    args = [{"player1":choice(options), "player2":choice(options)} for i in range(num_tests)]
    return input_values, args

def sol_convert_grade(grade):
    grade_cutoffs= {"A":90, "B":80, "C":70, "D":60}
    ### BEGIN SOLUTION
    for letter, cutoff in grade_cutoffs.items():
        if grade >= cutoff:
            return letter
    return "F"
    ### END SOLUTION

def input_convert_grade(num_tests=30):
    from random import choice
    options = [i for i in range(30, 100, 4)]
    args = [{"grade":choice(options)} for i in range(num_tests)]
    input_values = [[] for i in range(num_tests)]
    return input_values, args
