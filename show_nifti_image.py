import nilearn
import nibabel as nib
from nilearn import plotting, image
from helper import compute_scores
import numpy as np
from nilearn.image import resample_to_img
from matplotlib.colors import ListedColormap

def expand_dim_of_nifti_image(nifti_image):
    new_data = np.expand_dims(nifti_image.get_data(), axis=-1)
    return nib.Nifti1Image(new_data, None, nifti_image.get_header())

def show_images():
    # prediction_file_location = "D:\\Master\\predicted\\predicted\\oasis\\CNNAllFinal_pred__OAS1_0012_MR1_mpr_n4_anon_111_t88_gfc_masked.nii.gz"
    # prediction_file_location = "D:\\Master\\predicted\\predictions\\"
    prediction_file_location = "D:\\Master\\predicted\\predictions\\volume-0_processed_pred_Segm.nii.gz"
    data_file_location = "D:\\MRISCANS\\LITS\\LITSTrainingData\\"
    data_file_name = "volume-0_processed.nii.gz"
    label_file_location = "D:\\MRISCANS\\LITS\\LITSTrainingLabels\\segmentation-0_processed.nii.gz"

    arcSaveName = "DeepMedic"

    prediction = nib.load(prediction_file_location)
    data = nib.load(data_file_location + data_file_name)
    label = nib.load(label_file_location)

    # prediction_plot = plotting.plot_roi(prediction, bg_img=data, cmap='Greys')
    # label_plot = plotting.plot_roi(label, bg_img=data, cmap='Greys')

    pred = resample_to_img(prediction, label, interpolation='linear').get_data()
    error_map = np.zeros(pred.shape)
    lab = label.get_data()

    error_map = np.zeros(pred.shape)
    error_map += np.array((pred != lab), dtype=float) * 2

    error_map += lab

    # Don't know why I have to have these random colours in the beginning.
    cmap = ListedColormap(['green', 'green', 'red', 'red', 'red', 'green', 'red', 'cyan'], 'indexed')

    print("jjjj")
    nif = nib.Nifti1Image(error_map, label.affine)
    # label_and_prediction_plot = plotting.plot_stat_map(nif, bg_img=label, cmap=cmap, cut_coords=(10, 10, 10))
    label_and_prediction_plot = plotting.plot_roi(nif, bg_img=data, cmap=cmap, colorbar=False, cut_coords=(-4, -71, 10))
    print("jjjj")

    data_file_name = data_file_name.split('.')[0]
    plotting.show()
    # prediction_plot.savefig(arcSaveName + data_file_name + "Prediction")
    # label_plot.savefig(arcSaveName + data_file_name + "Label")
    # label_and_prediction_plot.savefig(arcSaveName + data_file_name + "LabelAndPrediction")

def calculate_percentage_true():
    # data = nib.load("D:\\MRISCANS\\LITS\\LITSTrainingLabels\\segmentation-0_processed.nii.gz").get_data()
    # data = nib.load("D:\MRISCANS\\la\\OAS1_0001_MR1_mpr_n4_anon_111_t88_masked_gfc_fseg_processed.nii.gz").get_data()

    elems = data.size
    liver = np.count_nonzero(data)

    percentage_liver = float(liver)/float(elems)
    print(percentage_liver * 100)

def main():
    # calculate_percentage_true()
    show_images()

main()