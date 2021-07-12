"""
@ Mallory Wittwer (mallory.wittwer@gmail.com), August 2021
Python implementation of the LRC-MRM automated grain segmentaiton algorithm.
My goal is that, by reading through this code base, one should be able to 
understand the implementation of the algorithm and use it in other applications.

Usage:
    Run python grain_seg.py --data mydata.npy in a command line.
    
Expected output:
    After 2-3 min on a laptop, it should show a segmented map of the DRM dataset.
    Note that running time increases non-linearly with dataset size, so maybe avoid
    running the algorithm on high-res datasets (> 500 x 500 px, for ex.).
"""
import os
import argparse
import numpy as np
from segmentation import run_lrc_mrm

import matplotlib.pyplot as plt

def run(data_path, cps, ssize):
    # Load the data
    data = np.load(data_path)
    print('\n> Loaded DRM data: ', data.shape)
    rx, ry, s0, s1 = data.shape
    
    # This is just a convention
    dataset = {
        'data':data.reshape((rx*ry, s0*s1)), 
        'spatial_resol':(rx, ry), 
        'angular_resol':(s0, s1),
    }
    
    print('\n> Started segmentation. Fitting NMF model...')
    dataset = run_lrc_mrm(
        dataset, # Dataset, formatted as above
        cps, # NMF components
        ssize, # Sampling size
    )
    print('\n> Finished segmentation!')
    
    # Reshape the maps
    segmentation = dataset.get('segmentation').reshape((rx, ry))
    gbs = dataset.get('boundaries').reshape((rx, ry))
    
    return segmentation, gbs
     
            
if __name__ == '__main__':
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", required=True)  # (required) path to a DRM dataset as 4D .npy matrix
    parser.add_argument("-c", "--cps", required=False)  # (optional) Number of NMF components
    parser.add_argument("-s", "--ssize", required=False)  # (optional) Sampling size
    args = parser.parse_args()
    data_path = args.data
    
    # Set default sampling size and NMF components if none provided
    ssize = 5000 if args.ssize is None else args.ssize
    cps = 50 if args.cps is None else args.cps
    
    # Get path to file
    data_path = os.path.join(os.getcwd(), data_path)
    
    # Run segmentation (returns segmentation as labels map and binary grain boundary map)
    segmentation, gbs = run(data_path, cps, ssize)
    
    ### To show segmentation as an image:
    segmentation = segmentation - segmentation.min()
    segmentation = segmentation / segmentation.max()
    segmentation = plt.cm.jet(segmentation)
    segmentation[gbs] = [1,1,1,0]
    
    fig, ax = plt.subplots(figsize=(4,4), dpi=200)
    ax.imshow(segmentation)
    ax.axis('off')
    plt.show()