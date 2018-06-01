from helper import load_files
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from nilearn import plotting
from nilearn.image import resample_to_img, resample_img
import nibabel as nib

from nilearn.datasets import load_mni152_template

def load(x):
    data = nib.load(x).get_data()
    print(data.shape)
    if(data.shape != (221, 186, 221)):
        print(x)
    return data

def pick_oasis_data(prediction_files, label_files):
    prediction_files_numbers = [s for t in prediction_files for s in t.split('_') if s.isdigit() and s != "111"]
    return [label for label in label_files for n in label.split('_') if n in prediction_files_numbers]

def pick_lbpa40_data(prediction_files, label_files):
    prediction_files_numbers = [s[-3:] for t in prediction_files for s in t.split('_') if s[-2:].isdigit()]
    return [label for label in label_files for n in label.split('_') if n[-3:] in prediction_files_numbers]

def pick_st_olavs_data(prediction_files, label_files):
    prediction_files_numbers = [s for t in prediction_files for s in t.split('_') if s.strip('T').isdigit()]
    return [label for label in label_files for n in label.split('_') if n in prediction_files_numbers]

def visualize_errors(prediction_directory, label_directory):
    prediction_files = load_files([prediction_directory])
    label_files = load_files([label_directory])

    # label_files = pick_oasis_data(prediction_files, label_files)
    label_files = pick_lbpa40_data(prediction_files, label_files)
    # label_files = pick_st_olavs_data(prediction_files, label_files)

    predictions = [nib.load(x) for x in prediction_files]
    labels = [nib.load(x) for x in label_files]

    template = labels[0]

    labels = [resample_to_img(x, template, interpolation='linear').get_data() for x in labels]
    predictions = [resample_to_img(x, template, interpolation='linear').get_data() for x in predictions]

    # Assumes that every array is of same shape
    errors = np.zeros(predictions[0].shape)

    for prediction, label in zip(predictions, labels):
        errors += (prediction != label).astype(dtype='float')

    nif = nib.Nifti1Image(errors, nib.load(label_files[0]).affine)
    error_plot = plotting.plot_stat_map(nif, bg_img=None, black_bg=True)

    # plotting.plot_anat(nif)
    # plotting.plot_roi(nif, bg_img=nib.load(prediction_files[0]))
    plotting.show()
    error_plot.savefig("ErrorLBPA40Unet")


visualize_errors("D:\\Master\\predicted\\UnetPredictions\\LBPA40\\", "D:\\MRISCANS\\NormalizedLBPA40Resampled\\labels\\")
