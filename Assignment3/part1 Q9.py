#9.Write a function to take user’s score as argument and determine if they pass or fail (pass if score is above 60, otherwise fails.)
users_score=int(input("Enter the score :"))
def funct(users_score):
    if users_score>60:
        return "Pass"
    else:
        return "fail"
result=funct(users_score)
print(result)

