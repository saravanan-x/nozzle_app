import numpy as np
import math
import nozzle_geomentry as noz_geo
import importlib
import geomentry_graph as gg
import flow_properties as fp
import bell_nozzle as bn
import bell_3d as b3
import bell_2d as b2
import conical_2d as c2
import export_plot as exp
import result as rs
import bell_cfd as bc

importlib.reload(noz_geo)

# Parameters

g = 9.80665
pi = np.pi

# f = 10000       # N
# pc = 5.468e6    # mpa - pa (e6) Chamber pressure
# tc = 3300       # K  - Chamber Tempreture
# y = 1.22        # Gamma  K Specific heat ratio
# r = 355.4       # J/Kgh   gas constant
# altitude = 10   #km changed exit tem and pressure based on altitude
# sy = 250e6      # Pa for thickness
# SF = 2          # for thickness
# # angles
# divergent_angle = 15    #(12 - 18)
# convergent_a = 30       #(30 - 45)
# # characteristic length for chamber
# length = 0.5            # (0.5 - 1)M
# # angle for bell_nozzle
# ta = 25  # throat angle for bell nozzle
# sa = 30 # slop angle for bell nozzle
# # Angle foor conical_nozzle
# tha = 17 # throat angle for conical angle

def run_simulation(f, pc, tc, y, r, altitude, sy, SF, divergent_angle, convergent_a, length, ta, sa, tha):

    #-----1.nozzle_geomentry--------------

    ve,m, at, me, ae, dt_mm, de_mm,cd_mm, lc_mm, conv_mm, div_mm, total_mm, s_mm, h, t, temp_k, p, pressure_mpa, pressure_pa, rho = noz_geo.geometry(
        g, f, pc, tc, y, r, sy, SF, altitude, divergent_angle, convergent_a, length
    )

    pe = pressure_pa  # pa exit pressure or atmosphere pressure

    #  -----2.geomentry graph-----------

    geo_path = gg.geomentry_graphs(cd_mm, dt_mm, de_mm, lc_mm, conv_mm, div_mm)

    #-------3.Flow Properties-------

    me, Ar, ar, ρ0, vt, ρt, ep, et, v_e, mg, mc, m0, F, isp = fp.flow_properties(
        pc, pe, temp_k, tc, y, r, g, at, ae
    )

    #------- 4.bell nozzle calculatons-------


    r1, cl, cr, con_l, e, rt, re, l1, Re, rn, ln, r_start, r_exit, slope_N, slope_exit, tita_n, tita_e, l, theta, x, xn, rx, yn, θn = bn.bell_nozzle(
        dt_mm, de_mm, ae, at, lc_mm, cd_mm, conv_mm, ta,sa)

    #----------5.3d plot graph---------

    d3_path = b3.bell_3d(r1, cl, cr, con_l, e, rt, re, l1, Re, rn, ln, r_start, r_exit, slope_N, slope_exit, tita_n, tita_e, l, theta, x, xn, rx, yn, θn)

    #----------6.2d plot graph---------

    d2_path = b2.bell_2d(r1, cl, cr, con_l, e, rt, re, l1, Re, rn, ln, r_start, r_exit, slope_N, slope_exit, tita_n, tita_e, l, theta, x, xn, rx, yn, θn)

    #----------7.2D conical design-----------

    conical_path = c2.conical_2d(dt_mm, de_mm, ae, at, lc_mm, cd_mm, conv_mm,tha)

    #------------solidwork plot values ---------
    cad_plot =  exp.export_plot(tita_n, r1, rt, x, rx)

    #--------------result excel--------
    result_exl = rs.result(f, m, cd_mm, lc_mm, conv_mm, dt_mm, div_mm, de_mm, total_mm,
        ar, ρ0, vt, ρt, me, mg, mc, ep, et, v_e, isp, m0, F)

    #--------------bell CFD graph--------
    bellcfd = bc.bell_cfd(r1, cl, cr, con_l, e, rt, re, l1, Re, rn, ln, r_start, r_exit, slope_N, slope_exit, tita_n, tita_e, l, theta, x, xn, rx, yn, θn)


    return {
        # -------- Geometry --------
        "ve": ve,
        "m": m,
        "at": at,
        "me": me,
        "ae": ae,

        "cd_mm": cd_mm,
        "lc_mm": lc_mm,
        "conv_mm": conv_mm,
        "dt_mm": dt_mm,
        "div_mm": div_mm,
        "de_mm": de_mm,
        "total_mm": total_mm,
        "s_mm": s_mm,

        # -------- Atmosphere --------
        "h": h,
        "t": t,
        "temp_k": temp_k,
        "p": p,
        "pressure_pa": pressure_pa,
        "pressure_mpa": pressure_mpa,
        "rho": rho,

        # -------- Flow --------
        "Ar": Ar,
        "ar": ar,
        "rho0": ρ0,
        "vt": vt,
        "rhot": ρt,
        "ep": ep,
        "et": et,
        "v_e": v_e,
        "mg": mg,
        "mc": mc,
        "m0": m0,
        "F": F,
        "isp": isp,

        # -------- Bell Nozzle --------
        "r1": r1,
        "cl": cl,
        "cr": cr,
        "con_l": con_l,
        "e": e,
        "rt": rt,
        "re": re,
        "l1": l1,
        "Re": Re,
        "rn": rn,
        "ln": ln,

        "r_start": r_start,
        "r_exit": r_exit,
        "slope_N": slope_N,
        "slope_exit": slope_exit,

        "tita_n": tita_n,
        "tita_e": tita_e,
        "l": l,

        #-----graph img path file locations-----
        "geo_plot": geo_path,
        "3d_plot": d3_path,
        "2d_plot": d2_path,
        "coni_plot": conical_path,
        "bell_cfd_plot": bellcfd,

        #-------download-----
        "excel_file": cad_plot["excel"],
        "txt_file": cad_plot["txt"],
        "result_exl":result_exl
    }



# #-----1.nozzle_geomentry-----------

# print(f"Exit velocity           : {ve:.2f} m/s")
# print(f"Required Mass flow rate : {m:.4f} kg/s")
# print(f"Area of throat          : {at:.6f} m^2")
# print(f"Exit Mach number        : {me:.2f}")
# print(f"Area of Exit            : {ae:.6f} m^2")

# print(f"\nChamber diameter        : {cd_mm:.2f} mm")
# print(f"Chamber length          : {lc_mm:.2f} mm")
# print(f"Convergent length       : {conv_mm:.2f} mm")
# print(f"Throat diameter         : {dt_mm:.2f} mm")
# print(f"Divergent length        : {div_mm:.2f} mm")
# print(f"Exit diameter           : {de_mm:.2f} mm")
# print(f"Total length            : {total_mm:.2f} mm")
# print(f"Chamber wall thickness  : {s_mm:.2f} mm")

# print(f"\nAltitude                : {h} m")
# print(f"Temperature             : {t:.2f} °C")
# print(f"Temperature             : {temp_k:.2f} K")
# print(f"Pressure                : {p:.2f} kPa")
# print(f"Pressure                : {pressure_pa:.2f} Pa")
# print(f"Pressure                : {pressure_mpa:.6f} MPa")
# print(f"Density                 : {rho:.4f} kg/m³")


# #-------------3.Flow Properties---------
# print("\n-----Flow properties--------")
# print(f"Exit Mach number        : {me:.2f}")
# print(f"Ratio of area           : {Ar:.2f}")
# print(f"Nozzle area ratio       : {ar:.2f}")
# print(f"Stagnation Density      : {ρ0:.2f} kg/m^3")
# print(f"Throart Velocity        : {vt:.2f} m/s")
# print(f"Throat density          : {ρt:.2f} kg/m^3")
# print(f"Exit Pressure           : {ep:.2f} pa")
# print(f"Exit Tempreture         : {et:.2f} K")
# print(f"EXit velocity           : {v_e:.2f} m/s")
# print(f"General mass flow rate  : {mg:.4f} kg/s")
# print(f"Choked mass flow rate   : {mc:.4f} kg/s")
# print(f"Mass flow rate          : {m0:.4f} kg/s")
# print(f"Thrust Final            : {F:.2f} N")
# print(f"specific impluse        : {isp} S")

# #----------Bell nozzle----------

# print("\n--- CONICAL / CONVERGENT DATA ---")
# print("r1 =", r1 * 1000)
# print("cl =", cl * 1000)
# print("cr =", cr * 1000)
# print("CL =", con_l * 1000)
# print("e =", e * 1000)
# print("rt =", rt * 1000)
# print("re =", re * 1000)
# print("l1 =", l1 * 1000)
# print("Re =", Re * 1000)
# print("rn =", rn * 1000)
# print("ln =", ln * 1000)
    
# print("\n---- BELL BOUNDARY CHECK ----")
# print("At N (radius)        :", r_start)
# print("At Exit (radius)     :", r_exit, "Expected:", re)
# print("Slope at N           :", slope_N, "Expected:", np.tan(tita_n))
# print("Slope at Exit        :", slope_exit, "Expected:", np.tan(tita_e))
# print(f"LENGTH (Rao method)  : {l*1000}")

# print("\n CURVE PLOT FOR SOLIDWORKS EXCEL / TEXT SAVED ")
# print("\n Result Saved ")
