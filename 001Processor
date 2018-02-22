import os
import datetime
from dateutil import parser

print("Aggregation initializing")

save = ""
count = 1
for x in range(7,13):
    for z in range (1,16):
        if os.path.exists("C:/Users/Nics Faller/Documents/G12/STRess/Data/Dec 4-8/G"+str(x)+"/G"+str(x)+"-"+str(z)):
            for file in os.listdir("C:/Users/Nics Faller/Documents/G12/STRess/Data/Dec 4-8/G"+str(x)+"/G"+str(x)+"-"+str(z)):
                if file.endswith(".txt"):
                    #print(file)
                    print("File #: ")
                    print(count)

                    with open("C:/Users/Nics Faller/Documents/G12/STRess/Data/Dec 4-8/G"+str(x)+"/G"+str(x)+"-"+str(z)+"/"+file) as f:
                        data = [line.split() for line in f.readlines()]
                        #print(data)

                    def is_number(s):
                        try:
                                float(s)
                                return True
                        except ValueError:
                                return False
            
                    for line in data:
                            if len(line) == 3 and is_number(line[1]):
                                    save += line[0] + " " + line[1] + " " + line[2] + "\n"
                    count+=1

                    savefile = open("data.txt", "w")
                    savefile.write(save)
                    savefile.close()


print("Aggregation finished.")
