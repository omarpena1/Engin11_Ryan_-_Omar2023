import sys
import random
import time

start_time = int(time.time())
run_time = int(sys.argv[1])

file_name = "randomdata.csv"
if (len(sys.argv) > 2):
        file_name = sys.argv[2] + file_name
f = open(file_name, "w")

        

metadata = ["time", "value"]

for entry in metadata:
    f.write(entry + ",")
    
f.write("\n")

while time.time() < (start_time + run_time):
        f.write(str(int(time.time())) + ",")
        f.write(str(random.random()) + ",")
        f.write("\n")
        time.sleep(2)
