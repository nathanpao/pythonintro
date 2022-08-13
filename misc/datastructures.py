students = {'Bear':['Python', 'DJango', 'DRF'], 'Dog':['Java', 'Spring'], 'Cat':['JS', 'Node', 'React']}
keys = students.keys()
for eachKey in keys:
    print("Courses taken by", eachKey, "are:")
    for eachCourse in students[eachKey]:
        print(eachCourse)