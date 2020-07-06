import numpy as np
import math
import tarj_data as td

l1 = 0.08
l2 = 0.25
l3 = 0.25
radio = 40
rate = 1


def leg_ikine(x, y, z):
    joint1 = np.arcsin(y / (-z))
    l = np.sqrt(x ** 2 + y ** 2 + z ** 2 + l1 ** 2 - 2 * l1 * np.sqrt(y ** 2 + z ** 2))
    joint2 = np.arccos((l2 ** 2 + l ** 2 - l3 ** 2) / (2 * l2 * l)) + np.arctan(-x / (np.sqrt(y ** 2 + z ** 2) - l1))
    joint3 = np.arccos((l2 ** 2 + l3 ** 2 - l ** 2) / (2 * l2 * l3)) - np.pi
    return joint1, joint2, joint3


def forward_gait():
    gait_data = np.zeros((radio, 12))
    x_left, y_left, z_left, x_right, y_right, z_right = td.forward_data()
    for t in range(gait_data.shape[0]):
        xl = x_left[t]
        xr = x_right[t]
        yl = y_left[t]
        yr = y_right[t]
        zl = z_left[t]
        zr = z_right[t]
        gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(xl, yl, zl)
        gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(xr, yr, zr)
    return rate, gait_data


def backward_gait():
    gait_data = np.zeros((radio, 12))
    x_left, y_left, z_left, x_right, y_right, z_right = td.backward_data()
    for t in range(gait_data.shape[0]):
        xl = x_left[t]
        xr = x_right[t]
        yl = y_left[t]
        yr = y_right[t]
        zl = z_left[t]
        zr = z_right[t]
        gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(xl, yl, zl)
        gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(xr, yr, zr)
    return rate, gait_data


# def forward_gait():
#     gait_data = np.zeros((radio, 12))
#     x_line, y_line, z_line = gait_line()
#     rate = 2
#     for t in range(gait_data.shape[0]):
#         if (t < 20):
#             xf = x_line[t]
#             xb = x_line[t + 20]
#             yf = y_line[t]
#             yb = y_line[t + 20]
#             zf = z_line[t]
#             zb = z_line[t + 20]
#         else:
#             xf = x_line[t]
#             xb = x_line[t - 20]
#             yf = y_line[t]
#             yb = y_line[t - 20]
#             zf = z_line[t]
#             zb = z_line[t - 20]
#
#         gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(xf, yf + 0.15, zf)
#         gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(xb, -yb + 0.15, zb)
#         gait_data[t, 6], gait_data[t, 7], gait_data[t, 8] = leg_ikine(xb, -yb + 0.15, zb)
#         gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf + 0.15, zf)
#
#     return rate, gait_data
#
#
# def backward_gait():
#     gait_data = np.zeros((radio, 12))
#     x_line, y_line, z_line = gait_line()
#     for t in range(gait_data.shape[0]):
#         if (t < 20):
#             xf = x_line[t]
#             xb = x_line[t + 20]
#             yf = y_line[t]
#             yb = y_line[t + 20]
#             zf = -z_line[t]
#             zb = -z_line[t + 20]
#         else:
#             xf = x_line[t]
#             xb = x_line[t - 20]
#             yf = y_line[t]
#             yb = y_line[t - 20]
#             zf = -z_line[t]
#             zb = -z_line[t - 20]
#
#         gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(xf, yf, zf)
#         gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(xb, yb, zb)
#         gait_data[t, 6], gait_data[t, 7], gait_data[t, 8] = leg_ikine(xb, yb, zb)
#         gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf, zf)
#     return rate, gait_data
#
#
# def turnleft_gait():
#     gait_data = np.zeros((radio, 12))
#     data = turn_line(1)
#     for t in range(gait_data.shape[0]):
#         gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(data[0, t], data[4, t], data[8, t])
#         gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(data[1, t], data[5, t], data[9, t])
#         gait_data[t, 6], gait_data[t, 7], gait_data[t, 8] = leg_ikine(data[2, t], data[6, t], data[10, t])
#         gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(data[3, t], data[7, t], data[11, t])
#     return rate, gait_data
#
#
# def turnright_gait():
#     gait_data = np.zeros((radio, 12))
#     data = turn_line(-1)
#     for t in range(gait_data.shape[0]):
#         gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(data[0, t], data[4, t], data[8, t])
#         gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(data[1, t], data[5, t], data[9, t])
#         gait_data[t, 6], gait_data[t, 7], gait_data[t, 8] = leg_ikine(data[2, t], data[6, t], data[10, t])
#         gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(data[3, t], data[7, t], data[11, t])
#     return rate, gait_data
#
#
# def slantleft_gait():
#     gait_data = np.zeros((radio, 12))
#     data = td.slantleft_gait(1)
#     for t in range(gait_data.shape[0]):
#         gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(data[0, t], data[2, t], data[4, t])
#         gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(data[1, t], data[3, t], data[5, t])
#         gait_data[t, 6], gait_data[t, 7], gait_data[t, 8] = leg_ikine(data[1, t], data[3, t], data[5, t])
#         gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(data[0, t], data[2, t], data[4, t])
#     return rate, gait_data
#
#
# def slantright_gait():
#     gait_data = np.zeros((radio, 12))
#     data = td.slantleft_gait(-1)
#     for t in range(gait_data.shape[0]):
#         gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(data[0, t], data[2, t], data[4, t])
#         gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(data[1, t], data[3, t], data[5, t])
#         gait_data[t, 6], gait_data[t, 7], gait_data[t, 8] = leg_ikine(data[1, t], data[3, t], data[5, t])
#         gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(data[0, t], data[2, t], data[4, t])
#     return rate, gait_data
#
#
# def jump_gait():
#     return


def keep_gait():
    gait_data = np.zeros((radio, 12))
    data = td.keep_gait()
    x_line = data[0, :]
    y_line = data[1, :]
    z_line = data[2, :]

    for t in range(gait_data.shape[0]):
        if t < 20:
            xf = x_line[t]
            xb = x_line[t + 20]
            yf = y_line[t]
            yb = y_line[t + 20]
            zf = z_line[t]
            zb = z_line[t + 20]
        else:
            xf = x_line[t]
            xb = x_line[t - 20]
            yf = y_line[t]
            yb = y_line[t - 20]
            zf = z_line[t]
            zb = z_line[t - 20]

        gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(xf, yf, zf)
        gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(xb, yb, zb)
        gait_data[t, 6], gait_data[t, 7], gait_data[t, 8] = leg_ikine(xb, yb, zb)
        gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf, zf)
    return rate, gait_data


# def clam_gait():
#     gait_data = np.zeros((radio, 12))
#     rate = 2
#     x_line, y_line, z_line = keep_line()
#     for t in range(gait_data.shape[0]):
#         if (t < 20):
#             xf = 0.4
#             xb = 0.4
#             yf = 0.15
#             yb = 0.15
#             zf = 0.1
#             zb = 0.1
#         else:
#             xf = 0.4
#             xb = 0.4
#             yf = 0.15
#             yb = 0.15
#             zf = 0.1
#             zb = 0.1
#
#         gait_data[t, 0], gait_data[t, 1], gait_data[t, 2] = leg_ikine(xf, yf, zf)
#         gait_data[t, 3], gait_data[t, 4], gait_data[t, 5] = leg_ikine(xb, yb, zb)
#         gait_data[t, 6], gait_data[t, 7], gait_data[t, 8] = leg_ikine(xb, yb, zb)
#         gait_data[t, 9], gait_data[t, 10], gait_data[t, 11] = leg_ikine(xf, yf, zf)
#     return rate, gait_data
#
#
# def gait_line():
#     data = td.forward_gait()
#     x_line = data[0, :]
#     y_line = data[1, :]
#     z_line = data[2, :]
#     return x_line, y_line, z_line


# def turn_line(direction):
#     data = td.turn_gait(direction)
#     return data
#
#
# def jump_line():
#     xf_line = np.zeros((20))
#
#     return
