import os
import sys
import shutil
import subprocess


def makefile(num):   
    if not os.path.exists(path+num):
        os.mkdir(path+num)

        for i in abc:
            f_path = path+num+i
            shutil.copyfile('template.py',f_path)
    


if __name__ == '__main__':
    abc = ['/a.py','/b.py','/c.py','/d.py']
    # abc = [f'/{str(i)}.py' for i in range(1,101)]
    num = (sys.argv[1])

    if sys.argv[2] == 'v':
        path = '/Users/yamashitayoh/Documents/ac_code/virtual/'
    else:
        path = '/Users/yamashitayoh/Documents/ac_code/abc'

    makefile(str(num))
    if sys.argv[2] == 'v':
        subprocess.run(f"cd virtual/{num} && $SHELL", shell=True)
    else:
        subprocess.run(f"cd abc{num} && $SHELL", shell=True)
    
    