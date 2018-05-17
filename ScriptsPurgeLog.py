#!/bin/python3

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

if(os.path.isfile(file_name) == True):              # проверяем есть ли в файле что-то
    log_file_size = os.stat(file_name).st_size      # указываем размер файла в байтах
    log_file_size = log_file_size / 1024            # переводим байты в килобайты

    if(log_file_size >= limit_size):
        if(logs_number > 0):
            for current_file_num in range(logs_number, 1, -1):
                source = file_name + "_" + str(current_file_num - 1)
                distance = file_name + "_" + str(current_file_num)
                if(os.path.isfile(source) == True):
                    shutil.copyfile(source, distance)
                    print("скопирован {1} to {2}".format(source, distance))

            shutil.copyfile(file_name, file_name + "_1")
            print("скопирован {1} to {2}_1".format(file_name, file_name))
        my_file = open(file_name, "w")
        my_file.close()

