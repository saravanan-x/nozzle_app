                                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BELL NOZZLE GEOMETRY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# CONVERGENT & CONICAL SETUP CALCULATIONS
import numpy as np
import math

def bell_nozzle(dt_mm, de_mm, ae, at, lc_mm, cd_mm, conv_mm, ta, sa):

    dt = dt_mm/1000 # mm to m
    de = de_mm/1000 #mm - m
    rt = dt / 2     #throat dia
    re = de / 2     #exit dia
    e = ae / at

    throat_angle = ta
    theta = np.radians(throat_angle) 

    r1 = 1.5 * rt
    Re = np.sqrt(e) * rt
    rn = rt + r1 * (1 - np.cos(theta))

    # arc length
    l1 = r1 * np.sin(theta)

    # CONVERTING MILLIMETERS TO METERS FOR PLOTTING
    cl = lc_mm / 1000              # Chamber length converted to meters
    cr = (cd_mm / 2) / 1000        # Chamber radius converted to meters
    con_l = (conv_mm / 1000) - l1  # Convergent length converted to meters

    # conical length
    ln = (rt * (np.sqrt(e) - 1) + r1 * (np.cos(theta) - 1)) / np.tan(theta)

    # BELL NOZZLE DESIGN (AFTER N POINT)
    # OVERWRITING r1 for the Bell throat downstream radius

    # Slop Angles
    θn = sa
    θe = 8.5

    # angles (convert to radians)
    tita_n = np.radians(θn)
    tita_e = np.radians(θe)

    # Point N
    xn = r1 * np.sin(tita_n)
    yn = rt + r1 * (1 - np.cos(tita_n))

    # LENGTH (Rao method) 
    f = 0.8   # length factor (60%–80%)
    l = f * (rt / np.tan(np.radians(15))) * (
            (np.sqrt(e )-1) + 1.5 * ((1 / np.cos(np.radians(15))) - 1))

    # ---- PARABOLIC BELL EQUATION ----
    # r(x) from Rao
    x = np.linspace(xn, l, 100)
    rx = yn + np.tan(tita_n) * (x - xn) \
            + ((np.tan(tita_e) - np.tan(tita_n)) / (2 * (l - xn))) * (x - xn)**2

    # 4 BOUNDARY CONDITION CHECKS
    r_start = yn
    r_exit = yn + np.tan(tita_n) * (l - xn) \
                + ((np.tan(tita_e) - np.tan(tita_n)) / (2 * (l - xn))) * (l - xn)**2
    slope_N = np.tan(tita_n)
    slope_exit = np.tan(tita_n) + \
                    ((np.tan(tita_e) - np.tan(tita_n)) / (l - xn)) * (l - xn)


    return r1, cl, cr, con_l, e, rt, re, l1, Re, rn, ln, r_start, r_exit, slope_N, slope_exit, tita_n, tita_e, l, theta, x, xn, rx, yn, θn






