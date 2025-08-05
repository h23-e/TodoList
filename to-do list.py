tasks = input("""

 ____    ____           _________   ___        ______      ___     __   _        _    
|_   \  /   _|         |  _   _  |.'   `.     |_   _ `.  .'   `.  [  | (_)      / |_  
  |   \/   |   _   __  |_/ | | \_/  .-.  \______| | `. \/  .-.  \  | | __  .--.`| |-' 
  | |\  /| |  [ \ [  ]     | |   | |   | |______| |  | || |   | |  | |[  |( (`\]| |   
 _| |_\/_| |_  \ '/ /     _| |_  \  `-'  /     _| |_.' /\  `-'  /  | | | | `'.'.| |,  
|_____||_____[\_:  /     |_____|  `.___.'     |______.'  `.___.'  [___|___|\__) )__/  
              \__.'                                                          
 Enter your to do list sperated by comma📝 :  """).split(", ")
done_tasks = []
ongoing_tasks = []


for task in tasks:
  print(f"\n🔘 {task}\n")
  answer = input(f"have you finished {task} yet? (yes/no) : ")

  if answer == "yes":
    print("nice job✅")
    done_tasks.append(task)
    print("--------")

  else :
    print("try not to put it off❌ ")
    ongoing_tasks.append(task)
    print("--------")


see_progress = input("""
do you want to see today's progress✏️? (yes/no) : """)
if see_progress == "yes" :
  print("""
  ********** 🟢✅ done tasks ✅🟢 **********""")
  print(done_tasks)
  print("""
  ********* 🔃 ongoing tasks 🔃 *********""")
  print(ongoing_tasks)

else :
  input("""

--------
press enter to exit....""")

input("""

--------
press enter to exit....""")