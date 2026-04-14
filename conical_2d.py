import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import bell_nozzle as bn
import os

def conical_2d(dt_mm, de_mm, ae, at, lc_mm, cd_mm, conv_mm, tha):
    
    dt = dt_mm/1000 # mm to m
    de = de_mm/1000 #mm - m
    rt = dt / 2
    re = de / 2 
    e = ae / at

    throat_angle = tha

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

    # total length
    l = l1 + ln

    # print("r1 =", r1 * 1000)
    # print("cl =", cl * 1000)
    # print("cr =", cr * 1000)
    # print("covergen length =", con_l * 1000)
    # print("e =", e * 1000)
    # print("rt =", rt * 1000)
    # print("re =", re * 1000)
    # print("l1 =", l1 * 1000)
    # print("Re =", Re * 1000)
    # print("rn =", rn * 1000)
    # print("ln =", ln * 1000)
    # print("Total length =", l * 1000)


        # --- PLOTTING CODE ---
    fig, ax = plt.subplots(figsize=(16, 9)) 

    ax.set_aspect('equal')
    ax.axis('off') 

    pad = Re * 0.25

    # ---------------- GEOMETRY ----------------
    x_chamber_start = -(cl + con_l + l1)
    x_chamber_end   = -(con_l + l1)
    x_conv_end      = -l1

    y_conv_end = rt + r1 * (1 - np.cos(theta))

    # ---------------- NOZZLE SHAPE ----------------
    def plot_nozzle(sign=1):

        # Chamber
        ax.plot([x_chamber_start, x_chamber_end], 
                [sign*cr, sign*cr], linewidth=3)

        # Convergent line
        ax.plot([x_chamber_end, x_conv_end], 
                [sign*cr, sign*y_conv_end], linewidth=3)

        # Convergent arc
        t_conv = np.linspace(-np.pi/2 - theta, -np.pi/2, 100)
        x_arc = r1 * np.cos(t_conv)
        y_arc = r1 * np.sin(t_conv) + (rt + r1)

        ax.plot(x_arc, sign*y_arc, linewidth=3)

        # Divergent (straight or bell)
        ax.plot([l1, l], [sign*rn, sign*Re], linewidth=3)


    # Draw both sides
    plot_nozzle(1)
    plot_nozzle(-1)

    # ---------------- CENTERLINE ----------------
    ax.plot([x_chamber_start - pad, l + pad], [0, 0], linestyle='--')
    ax.text(l + pad*1.2, 0, "CL", fontsize=16, va='center')

    # ---------------- KEY POINTS ----------------
    ax.scatter([0, l1, l], [rt, rn, Re])

    ax.text(0, rt + pad*0.3, "Throat", ha='center')
    ax.text(l1, rn + pad*0.3, "N", ha='center')
    ax.text(l, Re + pad*0.3, "Exit", ha='center')

    # ---------------- DIMENSIONS ----------------
    def dim_line(x1, y1, x2, y2, text):

        ax.annotate('', xy=(x1, y1), xytext=(x2, y2),
                    arrowprops=dict(arrowstyle='<->', lw=1.5))

        ax.text((x1+x2)/2, (y1+y2)/2,
                text, ha='center', fontsize=11,
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

    # Radii
    dim_line(-pad*0.5, 0, -pad*0.5, rt, f"Rt\n{rt*1000:.1f} mm")
    dim_line(l1 - pad*0.3, 0, l1 - pad*0.3, rn, f"Rn\n{rn*1000:.1f} mm")
    dim_line(l + pad*0.5, 0, l + pad*0.5, Re, f"Re\n{Re*1000:.1f} mm")

    # Lengths
    dim_line(0, -Re*0.35, l1, -Re*0.35, f"L1\n{l1*1000:.1f} mm")
    dim_line(l1, -Re*0.35, l, -Re*0.35, f"Ln\n{(l-l1)*1000:.1f} mm")
    dim_line(0, -Re*0.6, l, -Re*0.6, f"Ltotal\n{l*1000:.1f} mm")

    # ---------------- ANGLE ----------------
    arc = patches.Arc((l1, rn), l*0.15, l*0.15,
                    theta1=0, theta2=np.degrees(theta))
    ax.add_patch(arc)

    ax.text(l1 + l*0.07, rn + pad*0.3,
            r'$\theta$', fontsize=14)

    # ---------------- DATA BOX ----------------
    stats_text = (
        f"NOZZLE DATA (mm)\n\n"
        f"Chamber L : {cl*1000:.1f}\n"
        f"Chamber R : {cr*1000:.1f}\n"
        f"Conv L    : {con_l*1000:.1f}\n\n"
        f"Rt        : {rt*1000:.1f}\n"
        f"Rn        : {rn*1000:.1f}\n"
        f"Re        : {Re*1000:.1f}\n\n"
        f"L1        : {l1*1000:.1f}\n"
        f"Ln        : {(l-l1)*1000:.1f}\n"
        f"Total L   : {l*1000:.1f}"
    )

    ax.text(0.02, 0.98, stats_text,
            transform=ax.transAxes,
            fontsize=11,
            verticalalignment='top',
            family='monospace',
            bbox=dict(boxstyle='round', alpha=0.4))

    # ---------------- LIMITS ----------------
    ax.set_xlim(x_chamber_start - pad*2, l + pad*3)
    ax.set_ylim(-(Re + pad*3), max(cr, rt + r1) + pad*2)

    plt.tight_layout()

    # SAVE IMAGE
    save_path = "static"
    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, "conical_nozzle.png")
    plt.savefig(file_path, dpi=300, bbox_inches='tight')

    plt.close()
    

    return "/static/conical_nozzle.png"