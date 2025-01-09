import sys    
from time import sleep    

def skrivUt(ord):
    for char in ord:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()