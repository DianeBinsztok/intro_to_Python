todoList=[]
# 1 - Ajouter des tâches à la liste
todo = input("Ajouter une tâche ou taper 'ok' s'il n'y a rien à ajouter");
while todo!="ok":
    todoList.append(todo)
    todo = input("Ajouter une tâche ou taper 'ok' s'il n'y a rien à ajouter");
if todo == "ok":
    print("Voici votre liste de tâches:")
    print(todoList)

# 2 - Supprimer des tâches de la liste
done=input("Pour marquer une tâche comme finie, tapez son numero.")
doneIndex = int(done)
while todoList!=[]:
    if doneIndex < len(todoList):
        del todoList[doneIndex]
        print(todoList)
        if todoList!=[]:
            done = input("Pour marquer une tâche comme finie, tapez son numero.")
            doneIndex = int(done)
    else:
        print("Vous n'avez pas autant de tâches dans votre liste")
        if todoList != []:
            done = input("Pour marquer une tâche comme finie, tapez son numero.")
            doneIndex = int(done)
else:
    print("Félicitations, vous avez accompli toutes vos tâches.")

