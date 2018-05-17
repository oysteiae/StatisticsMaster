import nilearn
import nibabel as nib
from nilearn import plotting, image
from compute_scores import compute_scores
import numpy as np

def expand_dim_of_nifti_image(nifti_image):
    new_data = np.expand_dims(nifti_image.get_data(), axis=-1)
    return nib.Nifti1Image(new_data, None, nifti_image.get_header())

def show_images():
    prediction_file_location = "C:\\Users\\oyste\\Documents\\Visual Studio 2015\\Projects\\SkullStripping\\BrainSegmentationStOlavs\\predicted\\CNNAll_pred__coreg_T1237_processed_masked.nii.gz"
    prediction_file_location = "D:\\Master\\deepmedicexperiments\\predictions\\coreg_T1237_processed_pred_Segm.nii.gz"
    data_file_location = "D:\\MRISCANS\\da\\"
    data_file_name = "coreg_T1237_processed.nii.gz"
    label_file_location = "D:\\MRISCANS\\la\\icvMaskAuto_2013_T117_processed.nii.gz"

    arcSaveName = "DeepMedic"

    prediction = nib.load(prediction_file_location)
    data = nib.load(data_file_location + data_file_name)
    label = nib.load(label_file_location)

    prediction_plot = plotting.plot_roi(prediction, bg_img=data, cmap='Greys')
    label_plot = plotting.plot_roi(label, bg_img=data, cmap='Greys')
    label_and_prediction_plot = plotting.plot_roi(prediction, bg_img=label)

    data_file_name = data_file_name.split('.')[0]

    prediction_plot.savefig(arcSaveName + data_file_name + "Prediction")
    label_plot.savefig(arcSaveName + data_file_name + "Label")
    label_and_prediction_plot.savefig(arcSaveName + data_file_name + "LabelAndPrediction")

def main():
    show_images()

main()