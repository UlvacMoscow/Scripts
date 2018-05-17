import os
import sys
import shutil



# ScriptsPurgeLog.py log.txt 12 4

if len((sys.argv) < 4):
    print("неправильно введена команда, пример: script.py 12 4")
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_number = int(sys.argv[3])



