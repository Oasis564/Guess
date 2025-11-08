print("Hello! Welcome to Quiz")
yn = input("Are you ready to play the Quiz:(y/n) ")
points = 0
total = 100 

if yn.lower() in ["y", "yes"]:
    print("==================================")

    print("1. What is the most famous programming language?")
    print("1. Java")
    print("2. Python")
    print("3. C++")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "2":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("2. What is 13 * 5?")
    print("1. 60")
    print("2. 70")
    print("3. 65")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "3":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("3. What is the capital of Russia?")
    print("1. Saint Petersburg")
    print("2. Moscow")
    print("3. Sochi")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "2":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("4. What is the largest continent?")
    print("1. Asia")
    print("2. Europe")
    print("3. Africa")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "1":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("5. What animal is considered the fastest on land?")
    print("1. Cheetah")
    print("2. Lion")
    print("3. Tiger")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "1":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("6. What sky-based animal is associated with America?")
    print("1. Falcon")
    print("2. Bald Eagle")
    print("3. Hawk")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "2":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("7. Which country has the most immigrants?")
    print("1. Canada")
    print("2. USA")
    print("3. Australia")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "2":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("8. Which galaxy is the closest to us?")
    print("1. Andromeda")
    print("2. Milky Way")
    print("3. Whirlpool")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "1":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("9. What is the name of the bomb that destroyed Hiroshima in WW2?")
    print("1. Fat Man")
    print("2. Little Boy")
    print("3. Big Boy")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "2":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    print("10. What is the largest blackhole in the known universe?")
    print("1. TON 618")
    print("2. M87*")
    print("3. Sagittarius A*")
    print("Answer in numeric 1, 2 or 3")
    ans = input()
    if ans == "1":
        print("Correct! You got 10 points")
        points += 10
    else:
        print("Incorrect!")

    print("==================================")
    percentage = (points / total) * 100
    print("Marks:", percentage, "%")

else:
    print("Game has been cancelled.")
