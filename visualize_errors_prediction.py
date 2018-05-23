from helper import load_files
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from nilearn import plotting
import nibabel as nib

def load(x):
    data = nib.load(x).get_data()
    print(data.shape)
    if(data.shape != (221, 186, 221)):
        print(x)
    return data

def visualize_errors(prediction_directory, label_directory):
    prediction_files = load_files([prediction_directory])
    label_files = load_files([label_directory])

    predictions = np.asarray([nib.load(x).get_data() for x in prediction_files])
    labels = np.asarray([nib.load(x).get_data() for x in label_files])

    # Assumes that every array is of same shape
    errors = np.zeros(predictions[0].shape)

    for prediction, label in zip(predictions, labels):
        errors += np.invert((prediction == label)).astype(dtype='float')

    nif = nib.Nifti1Image(errors, nib.load(label_files[0]).affine)
    error_plot = plotting.plot_stat_map(nif, bg_img=None, black_bg=True)

    # plotting.plot_anat(nif)
    # plotting.plot_roi(nif, bg_img=nib.load(prediction_files[0]))
    plotting.show()
    error_plot.savefig("ErrorLBPA40CNN")


visualize_errors("D:\\Master\\predictedLBPA40CNN\\predicted\\", "D:\\MRISCANS\\NormalizedLBPA40Resampled\\labels\\")