import re
import sys
import mrcfile
import h5py
import argparse
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from skimage.measure import *
from skimage.util import img_as_float
from sklearn.decomposition import PCA
from scipy.spatial import distance
from argparse import RawTextHelpFormatter

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

def sorted_nicely( l ):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

#lccc is a measure of Lin's concordance correlation coefficient, which is measure
#of agreement between two variables (this is nearly identical to other inter-class
#correlations, such as pearson's).
def lccc(y_true,y_pred):
    cor=np.corrcoef(y_true,y_pred)[0][1]
    mean_true=np.mean(y_true)
    mean_pred=np.mean(y_pred)
    var_true=np.var(y_true)
    var_pred=np.var(y_pred)
    sd_true=np.std(y_true)
    sd_pred=np.std(y_pred)
    numerator=2*cor*sd_true*sd_pred
    denominator=var_true+var_pred+(mean_true-mean_pred)**2
    return numerator/denominator

def main():
    parser=argparse.ArgumentParser(
    description=
    """
        This program helps in evaluating the orientation assignment and alignment
             of projection independent of reference structure (prior to initial
             3D map generation, and without calculating similarity matrix of
             projections, which is computationally intensive)

        Additionally, this program informs us completeness of the projections
             required for a better reconstruction and finally autocorrelation
             can point out the presence of projection from diverse conformational
             states.

        The program accepts projections saved as hdf file.

        The results are printed onto the terminal and a graph representing the
            scatter plots will be given as output to save. The output includes,
            name of the file, number of projections considered for analysis,
            and Autocorrelation value.

      Usage: cP.qcheck_poa inputfile.hdf """,formatter_class=RawTextHelpFormatter)
    parser.add_argument('file', type=str, help='input map file')
    args=parser.parse_args()
    #script_name = sys.argv[0]
    a = args.file #sys.argv[1]
    f = h5py.File(a,'r')
    #dataset_list = []
    dataset_list = list_g(f)
    #f.visititems(print_grp_name)
    dataset_list = sorted_nicely(dataset_list)
    res = []
    for i in dataset_list:
        #data = f.get(i).value #for python2.7
        data = f[i]            #for python3.7
        d1 = img_as_float(data)
        mu = moments_central(d1)
        nu = moments_normalized(mu)
        m = moments_hu(nu)
        res.append(m)
    pca = PCA(n_components=1)
    pc = pca.fit_transform(res)
    pc1  = np.roll(pc,1)
    ac = stats.pearsonr(pc[:,0],pc1[:,0])[0]
    cc = lccc(pc[:,0],pc1[:,0])
    #l = len(dataset_list)
    print('Input Map:%s' %(sys.argv[1]))
    print('Number of Particles: %d' %(len(dataset_list)))
    print('Autocorrelation:%5f'%(ac))
    print('lccc:%5f'%(cc))
    plt.scatter(pc1,pc)
    plt.title("Scatter of pc and lag of pc")
    plt.xlabel("Lag 1 of pc1 values")
    plt.ylabel("pc1 values")
    plt.grid(True)
    #fname = sys.argv[1].split(".")[0]
    #plt.savefig(fname + "_ac1.png")
    plt.show()


if __name__ == '__main__':
      main()
  
