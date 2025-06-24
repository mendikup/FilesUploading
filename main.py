# 1
from pdb import line_prefix

with open("my_text.txt" ,"w") as flehandlr:
    flehandlr.write("helo world\n")

    flehandlr.write("it's the first exercise in I/O\n")

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



# 3
with open("my_text.txt" ,"r") as flehandlr:
    count_even_lines=0
    for  line in flehandlr:
        line_length=len(line.strip())
        if line_length%2==0:
            count_even_lines+=1
    print(count_even_lines)


    #count words (without numbers)in the txt file
    flehandlr.seek(0)
    words_counter=0
    for line in flehandlr:
        words_in_line=line.strip().split()
        for word in words_in_line:
            if not word.isdigit():
                words_counter+=1
    print(words_counter)








