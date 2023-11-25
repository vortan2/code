import random
card_list = []
def card():
    number = random.randint(1000000000000000, 9999999999999999)
    while number in card_list:
        number = random.randint(1000000000000000, 9999999999999999)
        if not number in card_list:
            card_list.append(number)

card()

# rweqrqwrqwrqwr wwergwregwqaegqaw3g