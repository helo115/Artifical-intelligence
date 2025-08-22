#4.	Write a code to get first and second best scores from the list:
#Scores_list = [40, 89, 90, 89, 23, 90, 50]


Scores_list = [40, 89, 90, 89, 23, 90, 50]
Scores_list.sort(reverse=True)
print(Scores_list)
print(f" {Scores_list[0]} is first best score")
print(f" {Scores_list[2]} is second  best score")

