#!/usr/bin/env python3
import os, sys, time

def mine_block():
    print("let's mine a new block!")
    os.system("ls -la r")
    try:
        print("what's the current blkno?")
        blkno = int(open('.blkno').read())
    except:
        print("no blkno, assuming 0")
        blkno = 0
    os.system("echo 0123456789abcdef >r/.nce")
    os.system("cat r/* r/.nce | openssl ripemd160 >r/.~id")
    new_id = open('r/.~id').read()
    print("success!  moving %s" % new_id)
    os.system("mkdir -p         b/%s/%s"%(blkno, new_id))
    os.system("mv r/.[A-~]* r/* b/%s/%s"%(blkno, new_id))
    print("let's increment the blkno for next time")
    with open('.blkno','w') as f: f.write(str(blkno+1))

def main():
    print("let's start mining!")
    while 1:
        print(repr(os.listdir('r')))
        if os.listdir('r'):  mine_block()
        else:  print("No data! Lets wait...")
        time.sleep(4)

if __name__=='__main__': main()
