Implementation of the LRC-MRM grain segmentation algorithm; executable from a CLI.

## Installation

We recommend installing Python > 3.6 and the dependencies in `requirements.txt` in a fresh environment. Alternatively, one can execute the code in the provided virtual environement **environment.yml** using [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) (to install Anaconda: see [here](https://www.anaconda.com/)). To create the environement, use:

`conda env create -f environment.yml`

This will create an environment with the name *drm_ml*. To activate that environment, use:

`conda activate drm_ml`

We tested the code using the following dependencies:

- python 3.8.10
- numpy 1.19.5
- pandas 1.3.1
- matplotlib 3.4.2
- scikit-image 0.18.2
- scikit-learn 0.24.2
- tensorflow 2.5.0
- psutil 5.8.0

## Execution

To execute the program, clone the repository in a local folder, navigate to this folder, and run:

`python main.py -d drm_exmaple.npy`

The program should produce a segmented map of the input DRM datsaet in a few minutes for datasets with resolution < 400 x 400 px.

## Command-line arguments

   * -d / --data : (required) DRM dataset file. It should be a 4D matrix of type .npy (resolution X, resolution Y, thetas, phis).
   * -c / --cps : (optional) Number of NMF components. Default: 50.
   * -s / --ssize : (optional) Sampling size. Default: 5000.

For any inquiries, please contact [Mallory Wittwer](https://www.linkedin.com/in/m-wittwer/).
