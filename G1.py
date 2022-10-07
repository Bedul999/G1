import random
import sys
import time
def mengetik(s):
    for c in s + '/n':
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.3)

mengetik('tata cara tata kata tata makna bedul999/nberkarya/nsemangat.')
