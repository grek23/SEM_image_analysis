from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# image take from
# https://journals.plos.org/plosone/article/figure?id=10.1371/journal.pone.0215447.g001


def main():
    print("Analyze a SEM image!")

    img_path = "red_blood02.jpeg"
    im = Image.open(img_path)
    print(f"im.format: {im.format}")
    print(f"im.size: {im.size}")
    print(f"im.mode: {im.mode}")
    print(f"im.size[0]: {im.size[0]}")
    im.show()

    data = np.array(im)

    # 60 px = 2um
    meas_px = 2000/60  # nm per pixle [px]
    print(f"Scale = {meas_px} nm/px")
    sem_row = 100

    row_of_image = []
    i = 0
    while i < im.size[0]:
        row_of_image.append(np.mean(data[sem_row][i]))
        i = i + 1

    plt.figure()
    plt.plot(row_of_image)
    plt.show()

    smooth_row = row_smoother(row_of_image, 9)

    plt.figure()
    plt.plot(smooth_row)
    plt.show()

    # print_px_data(data)

    print(f"Red Blood cell lenght = {(200 - 50)*meas_px}nm")


def row_smoother(data, kern):
    X = []
    i = kern
    while i < len(data) - kern:
        X.append(np.mean(data[i - kern:i]))
        i = i + 1
    return X


def print_px_data(px_data):
    L = len(px_data)
    K = len(px_data[:])
    print(f"K = {K}")

    i = 1
    while i < L:
        if i % 7 == 0:
            print(f"{px_data[250][i - 1]}")
            print()
        else:
            print(f"{px_data[250][i - 1]}", end=' ')

        i = i+1


if __name__ == '__main__':
    main()
