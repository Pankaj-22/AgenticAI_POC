import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d0 = pd.read_csv('./minst_train.csv')

print(d0.head(5))

# save the lables into a variable 1.
l = d0['label']

#drop the label feature and store the pixel data in d.
d = d0.drop("label",axis=1)

#print shape
print(d.shape)
print(l.shape)

#display or plot a number.
plt.figure(figsize=(7,7))
idx = 100
#reshape from 1d to 2d
grid_data =d.iloc[idx].to_numpy().reshape(28,28)
plt.imshow(grid_data, interpolation = "none", cmap = "gray")
plt.show()
print(l[idx])


