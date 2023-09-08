import numpy as np
from numba import njit

# без jit max fps 61
@njit
def m(x, y, z):  # moving matrix
    return np.array([(1, 0, x),
                     (0, 1, y),
                     (0, 0, 1)])


@njit
def s(w, h, d):  # scaling matrix
    return np.array([(w, 0, 0),
                     (0, h, 0),
                     (0, 0, d)])


@njit
def rot_xy(a):  # XY rotation matrix
    sin_a, cos_a = np.sin(a), np.cos(a)
    return np.array([(cos_a, -sin_a, 0),
                     (sin_a, cos_a, 0),
                     (0, 0, 1)])


@njit
def rot_xz(a):  # XZ rotation matrix
    sin_a, cos_a = np.sin(a), np.cos(a)
    return np.array([(cos_a, 0, sin_a),
                     (0, 1, 0),
                     (-sin_a, 0, cos_a)])


@njit
def rot_yz(a):  # YZ rotation matrix
    sin_a, cos_a = np.sin(a), np.cos(a)
    return np.array([(1, 0, 0),
                     (0, cos_a, -sin_a),
                     (0, sin_a, cos_a)])


# @njit
def calc_norm(vec, basis):
    l1 = vec[1] - vec[0]
    l2 = vec[2] - vec[0]
    norm = np.cross(l1, l2)
    norm = basis @ norm
    return norm / np.linalg.norm(norm)
