import random

while True:
    print("it's ya fucking calculator boi")
    print("the fuck you wanna calculate?")

    print("a. i wanna add sum shit")
    print("b. i wanna subtract sum shit")
    print("c. i wanna have sex")
    print("d. i'm finna break shit into pieces")

    invalid_input_insults = [
        "u high bro? can't you read???",
        "bruh, for real?",
        "come on man, it ain't that hard",
        "you're adopted",
        "beaching your eyes is bad for your health, but i don't care",
        "you've earned a gold medal in disappointing people",
        "world literacy rate just wen't down by a magnitude",
        "please hand me over to your mom",
        "i expected nothing but you still managed to disappoint me",
    ]

    has_fucked_up_at_least_once = False

    valid_operations = ["a", "b", "c", "d"]
    operation = input(":")
    while operation not in valid_operations:
        has_fucked_up_at_least_once = True
        print(random.choice(invalid_input_insults))
        operation = input(":")

    while True:
        try:
            a = int(input("a: "))
            b = int(input("b: "))

            break
        except ValueError:
            has_fucked_up_at_least_once = True
            print(random.choice(invalid_input_insults))

    answer_message = "your answer is"
    if has_fucked_up_at_least_once:
        answer_message = "here you go bitch, it's"

    match operation:
        case "a":
            print(answer_message, a + b)
        case "b":
            print(answer_message, a - b)
        case "c":
            print(answer_message, a * b)
        case "d":
            try:
                print(answer_message, a / b)
            except ZeroDivisionError:
                print("you can't give a fuck if you have no fucks to give you dumbass")
