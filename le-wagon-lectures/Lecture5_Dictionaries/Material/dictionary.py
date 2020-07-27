# -*- coding: utf-8 -*-

# Dictionary

# Unlike lists, which are indexed by a range of numbers, dictionaries are 
# indexed by keys.
# Stores key-value pairs
# Keys are always unique !!

people = { "pm": "Antonio Costa", "president": "Marcelo" }


len(people)
# 2

type(people)
# dict

# CRUD on Dictionaries

# READ
print(people["pm"])
#print(people.get("abc", 0))

# CREATE
people["em"] = "Centeno"
#print(people)

# UPDATE
people["pm"] = "Swen"
#print(people)

# DELETE
del(people["em"])
#print(people)


students = { "students": [{ "name": "joao" }, { "name": "ana" }] }

#print(students["students"][0]["name"])


# ITERATE

# iterating people dict
for key, value in people.items():
    print(f"Our {key} is {value}")

# iterating students dict
for key, values in students.items():
    print(f"Our {key}: ")
    for elem in values:
        student_name = elem["name"]
        print(f"Name: {student_name}")




























