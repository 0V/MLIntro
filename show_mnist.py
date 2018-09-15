# import libraries

#%%

import pandas as pd
import keras
from keras.datasets import mnist
import matplotlib.pyplot as plt


# Download MNIST datasets # Downlo 
# This datasets include 2 tapples. x_train, x_test(28,28) and y_train, y_test(9 classes).
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Loaded MNIST")

# show sample data# show s 
fig = plt.figure(figsize=(9,9))

for i in range(36):
    ax = fig.add_subplot(6, 6, i+1, xticks=[], yticks=[])
    ax.imshow(x_train[i], cmap='gist_gray')