import numpy as np

# read files
fixb_radi = np.load('fixb_radi.npy', allow_pickle=True)
fixb_pos = np.load('fixb_pos.npy', allow_pickle=True)
b_radi = np.load('b_radi.npy', allow_pickle=True)
b_pos = np.load('b_pos.npy', allow_pickle=True)

# re-save files
np.save('fixb_radi.npy', fixb_radi)
np.save('fixb_pos.npy', fixb_pos)
np.save('b_radi.npy', b_radi)
np.save('b_pos.npy', b_pos)
