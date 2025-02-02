#name = input("имя: ")
#print(name)
#name1 = "Vova"
#print(name == name1)
###############-----условные конструкции------################
name = input( "имя: ")
login = "Vova"

if name == login:
  print("Hello", name)
elif len(name) < 3:
  print("недопустимая длина имени")
elif name == "Lyba":
  print("здравствуйте Любовь")
else: print("отказанно в доступе")

print("The end")