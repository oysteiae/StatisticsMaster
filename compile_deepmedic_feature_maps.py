import nibabel as nib
import nilearn
from nilearn import plotting
from main import load_files
import numpy as np
import matplotlib.pyplot as plt

def compile_deep_medic_feature_maps(path):
    layers = ["layer" + str(x) for x in range(4)]
    feature_map_files = load_files([path])
    print(layers)

    images_per_row = 10

    for layer in layers:
        feature_map_files = load_files([path + "\\" + layer])
        feature_maps = [nib.load(x).get_data()[:, : 176, :] for x in feature_map_files]

        n_features = len(feature_map_files)
        print(n_features)
        size = feature_maps[0].shape[-1]
        n_cols = n_features // images_per_row
        print(n_cols)
        display_grid = np.zeros((size * n_cols, images_per_row * size))
        for col in range(n_cols):
            for row in range(images_per_row):
                feature_map = feature_maps[col * images_per_row + row]
                channel_image = feature_map[10, :, :]
                channel_image -= channel_image.mean()
                channel_image /= channel_image.std()
                channel_image *= 64
                channel_image += 128
                display_grid[col * size : (col + 1) * size, row * size : (row + 1) * size] = channel_image

        scale = 1. / size
        plt.figure(figsize=(scale * display_grid.shape[1], scale * display_grid.shape[0]))
        plt.title(layer)
        plt.grid(False)
        plt.imshow(display_grid, aspect='auto', cmap='viridis')
        plt.savefig("D:\\Master\\Graphs\\featuremapsDeepMedic\\" + "pathway1" + layer + ".png")
        plt.show()

    # plotting.plot_roi(feature_maps[1], bg_img=None, cmap='Greys')
    # plotting.show()

compile_deep_medic_feature_maps("D:\\Master\\features\\pathway1\\")