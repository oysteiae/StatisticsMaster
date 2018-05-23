from helper import load_files
import nibabel as nib
import numpy as np

def visualize_errors(prediction_directory, label_directory):
    prediction_files = load_files([prediction_directory])
    label_files = load_files([label_directory])

    predictions = np.asarray([nib.load(x).get_data() for x in prediction_files])
    labels = np.asarray([nib.load(x).get_data() for x in label_files])

    # Assumes that every array is of same shape
    errors = np.zeros(predictions[0].shape)

    for prediction, label in zip(predictions, labels):
        error = np.invert((prediction == label)).astype(int)
        errors += error

    # All that is left to do is to visualize the errors.

def test():
    a = np.array((0, 0, 1))
    b = np.array((0, 1, 1))
    error = np.zeros(a.shape)

    error += np.invert((a == b)).astype(int)
    error += np.invert((a == b)).astype(int)
    print(error)
test()






