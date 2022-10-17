todoList=[]
todo = input("Ajouter une tâche ou taper 'ok' s'il n'y a rien à ajouter");
while todo!="ok":
    todoList.append(todo)
    todo = input("Ajouter une tâche ou taper 'ok' s'il n'y a rien à ajouter");
if todo == "ok":
    print("Voici votre liste de tâches:")
    print(todoList)

doneIndex=input("Pour marquer une tâche comme finie, tapez 0.")
while todoList!=[]:
   del todoList[int(doneIndex)]
   print(todoList)
   if todoList!=[]:
     doneIndex = input("Pour marquer une tâche comme finie, tapez 0.")
if todoList==[]:
    print("Félicitations, vous avez accompli toutes vos tâches.")

