# cryoPack

This package is work in progess which contains programs that help in model building and quality assessment for maps from cryoEM experiment. 

The "qcheck" package presently constitutes two programs 

1. cP_qcheck.mqa : This helps evalute phase values from the 3D cryoEM reconstructed map and calcuates two statistical parameter to judge the quality of the cryoEM 3D map reconstruction. 
2. cP_qcheck.poa : This helps assess the orientation of projections selected for reconstruction. 

"cP_qcheck.mqa" program helps in quantitatively assess the presence of non-particles in the reconstructed map. The program takes two input parameters to perform calculations, 
one is the cryo-EM map which can have both mrc or map extension and second parameter is the map's contour value. 

The contour value is used to create a mask and then perform the calcualation. 


"cP_qcheck.poa" program help in evaluating orientation assignment and alignmen of projections selected for reconstruction process. The output numerical also indicates the completness of projections required.      

For both the programs once the calucaltions are done, the output numerical values are printed on the console and a graph. 

Usage:

cP.qcheck_mqa inputfile.mrc 1.5

cP.qcheck_poa inputfile.hdf

Both the programs have help function with a short discription which can be used as shown below. 

cP.qcheck_mqa -h

The details for one of the function is publised as a preprint in biorxiv.

Please follow the link to the paper. "https://www.biorxiv.org/content/10.1101/2022.12.31.521834v1"

Changes will be made to the up comming versions and accompied with paper published. 
