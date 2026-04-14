import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import importlib
import atmosphere_data as at_data
import pandas as pd


importlib.reload(at_data)
# Parameters

g = 9.80665
pi = np.pi

def geometry(g, f, pc, tc, y, r, sy, SF, altitude, divergent_angle, convergent_a, length):

    alt = altitude*1000
    t, p, rho, h = at_data.get_atmosphere_data(alt)

    temp_k = t + 273.15
    pressure_pa = p * 1000
    pressure_mpa = pressure_pa / 1e6

    pe = pressure_pa  # pa exit pressure or atmosphere pressure

    da = np.radians(divergent_angle)
    ca = np.radians(convergent_a)

    # Exit velocity
    ve = np.sqrt((2*y/(y-1))*r*tc*(1-(pe/pc)**((y-1)/y)))

    # mass flow
    m = f/ve

    # throat area
    at = (m/pc)* (np.sqrt( ((r*tc) / y)) * (((y+1) / 2)**((y+1) / (2*(y-1)))))

    # throat diameter
    dt = np.sqrt((4*at)/pi)

    #  Exit Mach
    me = np.sqrt((2/(y-1))*(((pc/pe)**((y-1)/y))-1))

    # Exit area 
    # ae = at * Ar
    ae = (at/me) * (((1+((y-1)/2)*(me**2)) / ((y+1)/2))**((y+1)/(2*(y-1))))

    #exit diameter
    de = np.sqrt((4*ae)/pi)

    # chamber diameter
    cd = 3*dt

    # chamber area
    ac = (pi*(cd**2))/4

    # chamber length
    lc = (length*at)/ac

    # convergent length
    convergent_length = (cd-dt)/(2*np.tan(ca))

    # divergent length
    divergent_length = (de-dt)/(2*np.tan(da))

    # total length
    total_length = lc + convergent_length + divergent_length

    # Chamber wall thickness
    tw = (pc*cd)/16000
    s = (pc*cd)/(2*tw)

    # thickness
    th = (pc * cd * SF) / (2 * sy)

    # convert to mm
    dt_mm = dt*1000
    de_mm = de*1000
    cd_mm = cd*1000
    lc_mm = lc*1000
    conv_mm = convergent_length*1000
    div_mm = divergent_length*1000
    total_mm = total_length*1000
    s_mm = th*1000


    return ve,m, at, me, ae, dt_mm, de_mm,cd_mm, lc_mm, conv_mm, div_mm, total_mm, s_mm, h, t, temp_k, p, pressure_mpa, pressure_pa, rho
