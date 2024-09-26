import sys
import random
import os
#usage: python main.py dim directory 
if isinstance(int(sys.argv[2]), int) == False:
    print("Improper dimesion")
    exit(1)
dim = int(sys.argv[2])

entries = os.listdir(sys.argv[3])

for entry in entries:
  i = random.randrange(dim)
  os.rename(entry, str(i)+'_'+entry)
