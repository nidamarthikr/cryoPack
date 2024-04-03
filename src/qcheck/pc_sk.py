import sys
import h5py
import mrcfile
import warnings
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import *
from skimage import morphology
import matplotlib.pyplot as plt

def list_g(f):
    dlist=[]
    def print_grp_name(grp_name, object):
        try:
           n_subgroups = len(object.keys())
        except:
           n_subgroups = 0
           dlist.append (object.name)
    f.visititems(print_grp_name)
    return(dlist)


def my_func(a):
    a = a[a!=0]
    if len(a) == 0:
       PC = np.nan
    elif len(a) <10:
       PC = np.nan   
    else:
       spect = np.fft.fft(a)
       spect = spect/abs(spect)
       angles = np.arctan2(spect.imag, spect.real)
       PC = np.sqrt((np.sum(np.cos(angles)))**2 + (np.sum(np.sin(angles)))**2) / np.shape(angles)[0]
    return(PC)


def extract(a,x):
    #a1 = a.copy() #earlier versions
    a1 = a[:]      #new versions
    binarized = np.where(a1>x, 1, 0)
    processed = morphology.remove_small_objects(binarized.astype(bool), min_size=50,connectivity=2).astype(int)
    mask = np.where(processed == 0)
    a1[mask] = 0
    return a1


def cal_mom(data,con):
    aa = extract(data,con)
    xs,ys,zs = np.where(aa!=0)
    a1 = aa[min(xs):max(xs)+1,min(ys):max(ys)+1,min(zs):max(zs)+1]
    warnings.filterwarnings('ignore')
    p_1 = np.apply_along_axis(my_func, 0, a1)
    p_1 = p_1[~np.isnan(p_1)]
    p_1 = (p_1 - np.nanmin(p_1))/(np.nanmax(p_1)-np.nanmin(p_1))
    p3 = np.percentile(p_1, 75)
    p_2 = p_1[p_1 > np.percentile(p_1, 75)]
    s1 = skewtest(p_2)[0]
    k1 = kurtosistest(p_2)[0]
    all = np.array([p3,s1,k1])
    return(all)
    

def skplot(x,y,z):
    inp = np.array([x,y])
    mv = np.abs(np.max(inp)) + 5
    ex = [mv*-1,mv, mv*-1,mv]
    arr = np.array([[1,0],[0,1]])
    fig, ax = plt.subplots(1,1)
    ax.scatter(x,y, marker='s', s=10, c='r', edgecolors='red', lw=1)
    #ax.scatter(x2,y2, marker='s', s=30, c='none', edgecolors='red', lw=1)
    ax.imshow(arr, extent=ex, cmap=plt.cm.Greys, interpolation='none', alpha=.1)
    ax.axhline(0, color='red')
    ax.axvline(0, color='grey')
    ax.axhspan(0, min(ex), facecolor='red', alpha=0.2)
    ax.grid(which = "major", alpha = 0.7)
    ax.grid(which = "minor", alpha = 0.2)
    #ax.grid(which ="both")
    ax.minorticks_on()
    plt.title("Scatter plot of Z-scores")
    plt.xlabel("Z-score of Skew Test")
    plt.ylabel("Z-score of Kurtosis Test")
    textstr = '\n'.join((
        r'$High-PC=%.2f$' % (z, ),
        r'$Z-skew=%.2f$' % (x, ),
        r'$Z-kurtosis=%.2f$' % (y, )))
    props = dict(boxstyle='round', facecolor='white', alpha=0.5)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=8,
        verticalalignment='top', bbox=props)
    plt.show()

def main():
    script_name = sys.argv[0]
    a = sys.argv[1]
    con = float(sys.argv[2])
    val1=[]
    fmt = sys.argv[1].split(".")[1]
    if(fmt =="mrc" or fmt =="map"):
       m = mrcfile.open(a)
       data = m.data
       val = cal_mom(data,con)
       val1.extend(val)
    elif(fmt == "hdf"):
       f = h5py.File(a,'r')
       dl = list_g(f)
       for i in dl: 
        #data = f.get(i).value    #for python2.7
           data = f[i]            #for python3.7
           val = cal_mom(data,con)
           val1.extend(val)
    print('Input Map:%s' %(sys.argv[1]))
    print('Input contour value:%5f'%(con))
    print('High PC value:%5f'%(val1[0]))
    print('Z-score of Skew Test:%5f'%(val1[1]))
    print('Z-score of Kurtosis Test:%5f'%(val1[2]))
    skplot(val1[1],val1[2],val1[0])

if __name__ == '__main__':
     main()
