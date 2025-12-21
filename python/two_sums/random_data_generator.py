import random

def main(generate_this_many, target):
    to_submit = []
    for i in range(generate_this_many):
        random_integer = random.randint(1, 10)
        to_submit.append(random_integer)

    print(to_submit)



if __name__ == "__main__":
    generate_this_many = 100000
    target = 90
    main(generate_this_many, target)
