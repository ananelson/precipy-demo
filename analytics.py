import matplotlib
matplotlib.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

HDF5_CANONICAL_FILENAME = "store.h5"

def write_data_file_without_object(batch, x, y):
    for cache_file in batch.generate_and_upload_file(HDF5_CANONICAL_FILENAME, write_mode=None):
        with pd.HDFStore(cache_file) as store: # write directly to the CACHE file location
            df = pd.DataFrame(np.random.randn(x, y))
            store['df'] = df

def read_data_file_without_object(batch):
    filepath = batch.working_path_to_file(HDF5_CANONICAL_FILENAME)
    print(filepath)
    store = pd.HDFStore(filepath)
    print(store['df'])
    store.close()

def generate_data(batch, filename, a, b, n, seed=None):
    if not seed:
        seed = int(time.time())
    np.random.seed(seed)
    data = np.random.randint(a, b, n)
    assert filename.endswith(".npy"), "use .npy for file extension"
    for _, f in batch.save_binary(filename):
        np.save(f, data)
    return n

def plot_values(batch, input_filename, c, n, output_filename):
    for f in batch.read_binary(input_filename):
        ary = np.load(f)
    plt.plot(ary, 'ro')
    plt.plot([0, n], [c, c])

    batch.save_matplotlib_plt(plt, output_filename)
