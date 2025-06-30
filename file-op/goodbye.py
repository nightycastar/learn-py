with open("msg.txt","r") as file:
  data = file.read()
  print(data)

with open("msg.txt","w") as file:
  file.write("Hello, World!")