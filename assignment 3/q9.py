#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
marks = []
for i in range(5):   #range(5) - 0,1,2,3,4
    mark = int(input("enter mark:"))
    total = sum(marks)
    if total >= 450:
        print(f"first class:")
    else:
        print(f"second class:")