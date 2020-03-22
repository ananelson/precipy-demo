import matplotlib
matplotlib.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

HDF5_CANONICAL_FILENAME = "store.h5"

def write_data_file_without_object(af, x, y):
    with pd.HDFStore(HDF5_CANONICAL_FILENAME) as store: # write directly to the CACHE file location
        df = pd.DataFrame(np.random.randn(x, y))
        store['df'] = df
    af.add_existing_file(HDF5_CANONICAL_FILENAME)

def read_data_file_without_object(af):
    filepath = af.path_to_cached_file(HDF5_CANONICAL_FILENAME, "write_data_file_without_object")
    print(filepath)
    store = pd.HDFStore(filepath)
    print(store['df'])
    store.close()

def generate_data(af, filename, a, b, n, seed=None):
    if not seed:
        seed = int(time.time())
    np.random.seed(seed)
    data = np.random.randint(a, b, n)
    assert filename.endswith(".npy"), "use .npy for file extension"
    for f in af.generate_file(filename, mode='wb'):
        np.save(f, data)
    return n

def plot_values(af, input_filename, c, n, output_filename):
    print(af.path_to_cached_file(input_filename, "generate_data"))
    for f in af.read_file(input_filename, "generate_data", mode="rb"):
        ary = np.load(f)
    plt.plot(ary, 'ro')
    plt.plot([0, n], [c, c])
    
    plt.savefig(output_filename)
    af.add_existing_file(output_filename)
    os.remove(output_filename)
