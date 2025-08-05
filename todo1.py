


tasks = []


while True: 
 user_input = input("""
            📝My To-Do List📝
             1. Enter a new task
             2. Remove a task
             3. Show my list
             4. Quit
             🟢choose an option🟢: """)

 
 if user_input == "1":
    new_task = input("Enter your new task: ").strip() #strip makes it cleaner so it get rid of any not wanted spaces,etc
    if new_task:
       tasks.append(new_task)
       print(f"task '{new_task}' added!")
    else:
       print("Task cannot be empty.")

 elif user_input == "2":
    if tasks:
       print("\nCurrent tasks:")
       for i, task in enumerate(tasks, start=1): #enumerate is used to iterate through a list (tasks) while also keeping track of an index (i) for each item in the list.and The start=1 argument means the index starts at 1 instead of the default 0. This makes it more user-friendly
        print(f"{i}. {task}")
       try:
          task_number = int(input("Enter the number of task you wangt to remove: "))
          if 1 <= task_number <= len(tasks):
             removed_task = tasks.pop(task_number - 1)
             print(f"Task '{removed_task}' removed!")
          else:
             print("Invalid task number.")
       except ValueError:
          print("Please enter a valid number.")
    else:
       print("No tasks to remove.")              
          
 elif user_input == "3":
    if tasks:
       print("Your To-Do List:")
       for i, task in enumerate(tasks, start=1):
         print(f"{i}. {task}")
    else:
       print("Your To-Do List is empty!")   


 elif user_input == "4":
    print("Closing the program...")
    break
 
 else:
    print("Invalid option. Please choose 1, 2, 3, or 4.")
        









    
    
