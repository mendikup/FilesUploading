# 1
with open("my_text.txt" ,"w") as flehandlr:
    flehandlr.write("helo world\n")

    flehandlr.write("my_text.txt")

    flehandlr.write("That mean it is number 1\n")

    flehandlr.write("Not 2\n")

    flehandlr.write("Not three\n")

    flehandlr.write("it is exciting\n")

    flehandlr.write("And i am all 4 it")


# 2
with open("my_text.txt" ,"r") as flehandlr:
    for line in flehandlr:
         if any(char.isdigit() for char in line):
            print(line.strip())





