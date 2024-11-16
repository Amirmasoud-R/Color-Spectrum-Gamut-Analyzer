import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def import_image():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image = image.convert("RGB")
    image_array = np.array(image)
    color_spectrum = np.sum(image_array, axis=(0, 1)) / (image_array.shape[0] * image_array.shape[1])
    plt.figure(figsize=(8, 4))

    plt.subplot(121)
    plt.bar(range(len(color_spectrum)), color_spectrum, color=["red", "green", "blue"])
    plt.title("Color Spectrum")
    plt.xlabel("RGB Channels")
    plt.ylabel("Average Intensity")
    plt.xticks(range(len(color_spectrum)), ["Red", "Green", "Blue"])
    plt.grid(True, axis="y", linestyle="--")

    color_gamut = np.unique(image_array.reshape(-1, 3), axis=0)

    ax = plt.subplot(122, projection='3d')
    ax.scatter(color_gamut[:, 0], color_gamut[:, 1], color_gamut[:, 2], c=color_gamut / 255.0, s=20)
    ax.set_title("Color Gamut")
    ax.set_xlabel("Red")
    ax.set_ylabel("Green")
    ax.set_zlabel("Blue")
    ax.grid(True)

    plt.tight_layout()
    plt.show()

window = tk.Tk()
window.title("color Analyzer")
window.geometry("250x150")
window.resizable(False, False)

frame = ttk.Frame(window, padding="20 20 20 20")
frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

label = ttk.Label(frame, text="Click the button to import an image:")
label.grid(column=0, row=0, padx=10, pady=10)

import_button = ttk.Button(frame, text="Import Image", command=import_image)
import_button.grid(column=0, row=1, padx=10, pady=10)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

window.mainloop()
