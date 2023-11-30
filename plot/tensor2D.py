import matplotlib.pyplot as plt

import numpy as np

# Create a random matrix
k = 5000
a = np.random.randint(0, 100, [2, k])
v = np.random.random(a.shape[-1])

# Show plot without altering
plt.figure(figsize=[6, 6])
plt.scatter(a[0], a[1], c=v, 
            cmap='Blues', marker=".", s=100, linewidth=0, vmax=1, vmin=0)
plt.tight_layout()
#plt.savefig("sparse_matrix1.jpg")
plt.show()

# Only show elements with large value
mask = v > 0.6

plt.figure(figsize=[6, 6])
plt.scatter(a[0, mask], a[1, mask], 
            c=v[mask], cmap='Blues', marker=".", s=100, linewidth=0, vmax=1, vmin=0)
plt.tight_layout()
#plt.savefig("sparse_matrix2.jpg")
plt.show()
