from scipy.signal import cheby1
N = 4
rp = 1
Wn = 0.4
btype = 'low'
analog = False
output = 'ba'
cheby1(N, rp=rp, Wn=Wn, btype=btype, analog=analog, output=output, fs=None)