import matplotlib
matplotlib.use('Agg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

RANDOM_FILENAME = None # supplied in config
PLOT_FILENAME = None # supplied in config
HDF5_CANONICAL_FILENAME = "store.h5"

def write_data_file_without_object(af, x, y):
    with pd.HDFStore(HDF5_CANONICAL_FILENAME) as store: # write directly to the CACHE file location
        df = pd.DataFrame(np.random.randn(x, y))
        store['df'] = df
    af.add_existing_file(HDF5_CANONICAL_FILENAME, remove=True)

def read_data_file_without_object(af):
    print("RANDOM_FILENAME is %s" % RANDOM_FILENAME)
    filepath = af.path_to_cached_file(HDF5_CANONICAL_FILENAME, "write_data_file_without_object")
    print(filepath)
    store = pd.HDFStore(filepath)
    print(store['df'])
    store.close()

def generate_data(af, a, b, n, seed=None):
    if not seed:
        seed = int(time.time())
    np.random.seed(seed)
    data = np.random.randint(a, b, n)
    assert RANDOM_FILENAME.endswith(".npy"), "use .npy for file extension"
    for f in af.generate_file(RANDOM_FILENAME, mode='wb'):
        np.save(f, data)
    return n

def plot_values(af, c, n):
    print(af.path_to_cached_file(RANDOM_FILENAME, "generate_data"))
    for f in af.read_file(RANDOM_FILENAME, "generate_data", mode="rb"):
        ary = np.load(f)
    plt.plot(ary, 'ro')
    plt.plot([0, n], [c, c])
    plt.savefig(PLOT_FILENAME)
    af.add_existing_file(PLOT_FILENAME, remove=True)
