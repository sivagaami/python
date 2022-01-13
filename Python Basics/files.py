fname = input('Enter file name:')
fh = open(fname)
count = 0
num = 0.0
for lx in fh:
    line = lx.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        fnd = lx.find('0')
        snd = lx[fnd:]
        fsnd = float(snd)
        num = num + fsnd
        count = count +1
print('Average spam confidence:',num/count)
