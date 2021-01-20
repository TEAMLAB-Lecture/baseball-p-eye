# -*- coding: utf-8 -*-

import random

def get_random_number():
    return random.randrange(100, 1000)

def is_digit(user_input_number):
    return user_input_number.isdigit()

def is_between_100_and_999(user_input_number):
    return int(user_input_number) > 99 and int(user_input_number) < 1000

def is_duplicated_number(three_digit):
    return len(set(three_digit)) != len(three_digit)

def is_validated_number(user_input_number):
    return is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number)

def get_not_duplicated_three_digit_number():
    while True:
        num = get_random_number()
        if is_validated_number(str(num)):
            return num

def get_strikes_or_ball(user_input_number, random_number):
    result = [0, 0]
    for i, num1 in enumerate(user_input_number):
        for j, num2 in enumerate(random_number):
            if i == j and num1 == num2:
                result[0] += 1
            elif num1 == num2:
                result[1] += 1
    return result

def is_yes(one_more_input):
    if one_more_input.lower() == "y" or one_more_input.lower() == "yes":
        return True
    return False

def is_no(one_more_input):
    if one_more_input.lower() == "n" or one_more_input.lower() == "no":
        return True
    return False

def main():
    print("Play Baseball")
    play = True
    while play:
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        user_input = 999
        while user_input != random_number:
            user_input = input("Input guess number : ")
            if user_input == "0":
                play = False
                break
            if not is_validated_number(user_input):
                print("Wrong Input, Input again")
            else:
                strike, ball = get_strikes_or_ball(user_input, random_number)
                print(f"Strikes : {strike} , Balls : {ball}")
                if strike == 3:
                    while True:
                        more = input("You win, one more(Y/N) ?")
                        if not is_no(more) and not is_yes(more):
                            print("Wrong Input, Input again")
                        else:
                            break
        if is_no(more):
            play = False
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
