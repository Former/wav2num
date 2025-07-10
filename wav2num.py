# Copyright © 2025 Alexei Bezborodov. Contacts: <AlexeiBv+wav2nim@narod.ru>
# License: Public domain: http://unlicense.org/


from scipy.io.wavfile import read
import numpy as np

def wav2num(file_name):
    arr = read(file_name)
    arr = np.array(arr[1],dtype=int)

    print('Process file... ' + file_name)
    print(arr)

    id = 0
    l = open(file_name + "_num.txt", "w")
    for i in arr:
        l.write(str(arr[id]))
        l.write('\n')
        id += 1
        if id%100 == 0:
	        print(f"{id/len(arr)}%\r")

    l.close()
    print('Finish file... ' + file_name)

import sys

files_to_work = []

if __name__ == "__main__":
    for i in range(len(sys.argv)):
        param = sys.argv[i]
        if i > 0:
            files_to_work.append(param)

for f in files_to_work:
    wav2num(f)
