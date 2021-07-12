# LRC_MRM_grain_segmentation_minimalistic
By Mallory Wittwer, August 2021

Minimalistic implementation of the LRC-MRM grain segmentation algorithm (command-line implementation).

To test the program, clone the repository in a local folder, then navigate to this folder location and run:

`python main.py -d drm_exmaple.npy`

After a few minutes, the program should produce a segmented map of the DRM datsaet.

Command-line arguments:

   * -d / --data : (required) DRM dataset file. It should be a 4D matrix of type .npy (resolution X, resolution Y, thetas, phis).
   * -c / --cps : (optional) Number of NMF components. Default: 50.
   * -s / --ssize : (optional) Sampling size. Default: 5000.

For any questions, please contact me at mallory.wittwer@gmail.com.
