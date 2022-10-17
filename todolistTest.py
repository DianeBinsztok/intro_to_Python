todoList=[]
todo = input("Ajouter une tâche ou taper 'ok' s'il n'y a rien à ajouter");
while todo!="ok":
    todoList.append(todo)
    todo = input("Ajouter une tâche ou taper 'ok' s'il n'y a rien à ajouter");
if todo=="ok":
    print("Voici votre liste de tâches:")
    print(todoList)
