import os, sys, peer2peer

def save_pub(branch, path, data):
    print('mkdir -p ' + branch)
    os.system('mkdir -p ' + branch)
    with open(path, 'w') as f: f.write(data)

def read_pub(ws):
    msg1 = ws.receive()
    msg2 = ws.receive()
    msg3 = ws.receive()
    fname = msg1.split()[-1]
    print('fname is', repr(fname))
    if fname == '0':
        print("ignore this")
        return
    branch = os.path.join(*os.path.split(fname)[:-1])
    print(2,repr(branch))
    save_pub(branch, fname, msg3)

def sub(ch):
    ws = peer2peer.conn(sys.argv[1])
    channel_list = [str(id(ws)), "0", ch]
    msg = "sub "+' '.join(channel_list)
    ws.send(msg)
    while 1:
        read_pub(ws)

if __name__=='__main__': sub(sys.argv[2])
