# qns 2
import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750


def split_bill(friends, total):
    return total / len(friends)


def pick_lucky(friends):
    return random.choice(friends)


def final_summary(friends, total):

    share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)

    print("Bill Summary")
    print("-" * 30)

    for friend in friends:
        print(f"{friend}: NPR {share:.2f}")

    lucky_total = share + 50

    print(f"\nLucky Person: {lucky_person}")
    print(f"{lucky_person} pays NPR {lucky_total:.2f}")


final_summary(friends, total_bill)
