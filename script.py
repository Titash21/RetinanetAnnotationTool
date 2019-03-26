import os
import glob


txt_file = open("../Labels/001/cat-1.txt", "r")
lines = txt_file.read().split('\n')
print(lines)

if(not os.path.isdir("../Labels/002/")) or (not os.path.exists("../Labels/002/")):
    os.mkdir("Labels_test",0o777)