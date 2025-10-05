grades_input = input("Enter grades with spaces in between: ")
grades = [int(x) for x in grades_input.split()]

excellent = []
good = []
pass_list = []
fail = []

for g in grades:
    if g >= 90:
        excellent.append(g)
    elif g >= 70:
        good.append(g)
    elif g >= 50:
        pass_list.append(g)
    else:
        fail.append(g)

print("excellent:", excellent)
print("good:", good)
print("pass:", pass_list)
print("fail:", fail)
