print ("I will ask u what u want to add to your todo-iist, when you're done just type <end> ")
task = input("what do u wanna do next?")
end = "end"
i=1

tasks = []
tasks.append(task)

if task != end and i != 1000000:
    while i != 1000000 and task != end:
        task=input("anything else?")
        if task != end:
            tasks.append(task)
            i = i + 1

        else:
            print("Allright that's your todo list;", tasks)
else:
    tasks.remove("end")
    print("Your list is empty mate!", tasks)


