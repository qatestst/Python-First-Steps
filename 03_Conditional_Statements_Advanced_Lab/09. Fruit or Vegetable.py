fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetables = ["tomato", "cucumber", "pepper", "carrot"]

user_input = input()

if user_input in fruits:
    print('fruit')
elif user_input in vegetables:
    print('vegetable')
else:
    print('unknown')