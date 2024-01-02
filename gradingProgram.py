student_scores = {
    "Billy": 81,
    "Jimmy": 78,
    "Timmy": 99,
    "Ram": 74,
    "Sam": 62,
}
#empty dicionary
student_grades = {}

# changes score into grades
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Eceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades) 

#Nesting Dictionary in a Dictionary
travel_log = {
    "Panama":{"cities_visited" : ["Panama","Santiago","Chiriqui","Darien","Bocas Del Toro"],"total_visits": 10},
    "Puerto Rico":{"cities_visited":["Bayamon","Caguas","Yauco","Ponce","Rincon"],"total_visits": 0}
}

print(travel_log["Panama"]) 

#Nesting Dictionary in a List
travel_log = [
    {"country": "Panama",
     "cities_visited" : ["Panama","Santiago","Chiriqui","Darien","Bocas Del Toro"],
     "total_visits": 10},
    {"country": "Puerto  Rico",
     "cities_visited":["Bayamon","Caguas","Yauco","Ponce","Rincon"],
     "total_visits": 0},
]         