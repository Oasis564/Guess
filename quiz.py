# Hello! Welcome to Quiz
# Are you ready to play the Quiz:(y/n) y
# 1. What is the most famous programming language ?Python
# Correct
# 2. What is 13*5 ?75
# Incorrect
# 3. What is the capital of India ?Delhi
# Correct
# Thank you for playing, your total right answers were:  2
# Marks:  20.0 % 
# Try again. 
# Good Luck.

print("Hello! Welcome to Quiz")
yn = input("Are you ready to play the Quiz:(y/n)")
points = 0
total = 30
if yn == "y" or yn == "yes" or yn == "Y" or yn == "Yes":
    print("==================================")
    q1 = input("1. What is the most famous programming language ? ")
    if q1 == "Python" or q1 == "python":
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q1, " was not the correct answer!")
    print("==================================")
    q2 = int(input("What is 13*5 ? "))
    if q2 == 65:
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q2, " was not the correct answer!")
    print("==================================")
    q3 = input("What is the capital of Russia ? ")
    if q3 == "Moscow" or q3 == "moscow" :
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q3, " was not the correct answer!")
    print("==================================")
    
    
    
    print("==================================")
    q4 = input("What is the largest continetent ? ")
    if q4 == "Asia" or q4 == "asia" :
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q4, " was not the correct answer!")
    print("==================================")
    
    
    
    print("==================================")
    q5 = input("What animal is considered the fastest on land ? ")
    if q5 == "Cheetah" or q5 == "cheetah" :
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q5, " was not the correct answer!")
    print("==================================")
    
    
    
    
    
    print("==================================")
    q6 = input("What sky based animal is associated with America ? ")
    if q6 == "Eagle" or q6 == "eagle" or q6 == "Bald Eagle" or q6 == "bald Eagle" or q6 == "Bald eagle"  :
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q6, " was not the correct answer!")
    print("==================================")
    
    
    
    
    print("==================================")
    q7 = input("Which country has the most immigrants ? ")
    if q7 == "USA" or q7 == "usa" or q7 == "America" or q7 == "america" :
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q7, " was not the correct answer!")
    print("==================================")
    
    
    
    
    print("==================================")
    q8 = input("Which galaxy is the closest to us ? ")
    if q8 == "Andromeda" or q8 == "androma" or q8 == "The Andromeda Galaxy" or q8 == "The andromeda galaxy" or q8 == "the Andromeda galaxy" or q8 == "the andromeda Galaxy" :
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q8, " was not the correct answer!")
    print("==================================")

    
    
    
    
    print("==================================")
    q9 = input("What is the name of the bomb that destroyed Hiroshima in WW2? ")
    if q9 == "Little Boy" or q9 == "little boy" or q9 == "Little boy" or q9 == "little Boy" :
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q9, " was not the correct answer!")
    print("==================================")
    
    
    
    
    print("==================================")
    q10 = input("What is the largest blackhole in the known universe ? ")
    if q10 == "TON 618" or q10 == "Ton 618" or q10 == "ton 618" :
        print("Correct! You got 10 points")
        points = points + 10
    else:
        print("Incorrect! ", q10, " was not the correct answer!")
    print("==================================")
    
    percentage = (points/total) * 100
    print("Marks: ",percentage, "%")

else:
    print("Game has been cancelled.")