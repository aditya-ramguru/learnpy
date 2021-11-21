from game_data import data
import random
import art

print(art.logo)


def details(index):
    a_name = data[index]['name']
    a_occupation = data[index]['description']
    a_country = data[index]['country']
    return f"{a_name}, a {a_occupation}, from {a_country}."


score = 0
correct_answer = True
ind1 = random.randint(0, 49)
A = details(ind1)
a_followers = data[ind1]['follower_count']

while correct_answer:

    ind2 = random.randint(0, 49)
    while ind2 == ind1:
        ind2 = random.randint(0, 49)
    B = details(ind2)
    b_followers = data[ind2]['follower_count']
    print(f"Compare A: {A}")
    print(art.vs)
    print(f"Against B: {B}")
    A_B = input("Who has more followers? Type 'A' or 'B': ").lower()

    if A_B == 'a' and a_followers > b_followers:
        score += 1
        print(f"Your right! Current score: {score}")
        A = B

    elif A_B == 'a' and b_followers > a_followers:
        print(f"Sorry that's wrong. Final score: {score}")
        correct_answer = False

    elif A_B == 'b' and b_followers > a_followers:
        score += 1
        print(f"Your right! Current score: {score}")
        A = B

    else:
        print(f"Sorry that's wrong. Final score: {score}")
        correct_answer = False




