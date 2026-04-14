import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import bell_nozzle as bn
import os

def bell_2d(r1, cl, cr, con_l, e, rt, re, l1, Re, rn, ln, r_start, r_exit, slope_N, slope_exit, tita_n, tita_e, l, theta, x, xn, rx, yn, θn):
  

    # ---------------- GEOMETRY ----------------
    x_chamber_start = -(cl + con_l + l1)
    x_chamber_end   = -(con_l + l1)
    x_conv_end      = -l1

    y_conv_end = rt + r1 * (1 - np.cos(theta))

    # PRESERVED CONVERGENT GEOMETRY
    r1_conv = 1.5 * rt
    l1_conv = r1_conv * np.sin(theta)
    y_conv_end = rt + r1_conv * (1 - np.cos(theta))

    plt.figure(figsize=(14,6))

    # ---------- CHAMBER ----------
    x_chamber = np.linspace(x_chamber_start, x_chamber_end, 40)
    y_chamber = np.full_like(x_chamber, cr)

    # ---------- CONVERGENT ----------
    x_conv = np.linspace(x_chamber_end, x_conv_end, 50)
    y_conv = np.linspace(cr, y_conv_end, 50)

    # ---------- CONVERGENT ARC ----------
    t_conv = np.linspace(-np.pi/2 - theta, -np.pi/2, 100)
    x_arc_conv = r1_conv * np.cos(t_conv)
    y_arc_conv = r1_conv * np.sin(t_conv) + (rt + r1_conv)

    # ---------- THROAT TO N ARC ----------
    t_div = np.linspace(-np.pi/2, -np.pi/2 + tita_n, 100)
    x_arc_div = r1 * np.cos(t_div)
    y_arc_div = r1 * np.sin(t_div) + (rt + r1)

    # ---------- COLOR ----------
    c = "red"

    # ---------- TOP ----------
    plt.plot(x_chamber, y_chamber, color=c, linewidth=2)
    plt.plot(x_conv, y_conv, color=c, linewidth=2)
    plt.plot(x_arc_conv, y_arc_conv, color=c, linewidth=2)
    plt.plot(x_arc_div, y_arc_div, color=c, linewidth=2)
    plt.plot(x, rx, color=c, linewidth=2)

    # ---------- BOTTOM ----------
    plt.plot(x_chamber, -y_chamber, color=c, linewidth=2)
    plt.plot(x_conv, -y_conv, color=c, linewidth=2)
    plt.plot(x_arc_conv, -y_arc_conv, color=c, linewidth=2)
    plt.plot(x_arc_div, -y_arc_div, color=c, linewidth=2)
    plt.plot(x, -rx, color=c, linewidth=2)

    # ---------- CENTERLINE ----------
    plt.axhline(0, linestyle='--', linewidth=1)

    # ---------- FLOW VISUALIZATION ----------
    # Create multiple streamlines inside nozzle
    num_lines = 12
    y_vals = np.linspace(-rt*0.9, rt*0.9, num_lines)

    # ---------- FLOW VISUALIZATION ----------
    num_lines = 6

    for i in range(num_lines):
        factor = (i+1)/(num_lines+1)

        # Convergent flow
        x_flow1 = np.linspace(x_chamber_end, 0, 80)
        y_flow1 = factor * np.linspace(cr, rt, 80)

        # Bell flow (FIXED)
        x_flow2 = x                     # same as bell curve
        y_flow2 = factor * rx           # scaled inside nozzle

        plt.plot(x_flow1, y_flow1, color='orange', alpha=0.6, linewidth=1)
        plt.plot(x_flow2, y_flow2, color='orange', alpha=0.6, linewidth=1)

        # Mirror bottom
        plt.plot(x_flow1, -y_flow1, color='orange', alpha=0.6, linewidth=1)
        plt.plot(x_flow2, -y_flow2, color='orange', alpha=0.6, linewidth=1)

    # ---------- KEY POINTS ----------
    plt.scatter([0, xn, l], [rt, yn, Re], color='black')

    plt.text(0, rt + Re*0.08, "Throat", ha='center', fontsize=10)
    plt.text(xn, yn + Re*0.08, "N", ha='center', fontsize=10)
    plt.text(l, Re + Re*0.08, "Exit", ha='center', fontsize=10)

    # ---------- DIMENSION FUNCTION ----------
    def dim_line(x1, y1, x2, y2):
        plt.annotate('', xy=(x1, y1), xytext=(x2, y2),
                    arrowprops=dict(arrowstyle='<->', lw=1.2, color='black'))

    # ---------- DIMENSIONS ----------
    dim_line(-0.015, 0, -0.015, rt)
    dim_line(xn-0.015, 0, xn-0.015, yn)
    dim_line(l+0.015, 0, l+0.015, Re)

    dim_line(0, -Re*0.20, xn, -Re*0.20)
    dim_line(xn, -Re*0.30, l, -Re*0.30)
    dim_line(0, -Re*0.40, l, -Re*0.40)

    # ---------- DIMENSION TEXT ----------
    plt.text(-0.02, rt/2, f"Rt = {rt*1000:.3f}MM", fontsize=10, rotation=90, va='center')
    plt.text(xn-0.02, yn/2, f"Rn = {yn*1000:.3f}MM", fontsize=10, rotation=90, va='center')
    plt.text(l+0.02, Re/2, f"Re = {Re*1000:.3f}MM", fontsize=10, rotation=90, va='center')

    plt.text(xn/2, -Re*0.25, f"Ln = {xn*1000:.3f}MM", ha='center', fontsize=10)
    plt.text((xn+l)/2, -Re*0.30, f"Lbell = {(l-xn)*1000:.3f}MM", ha='center', fontsize=10)
    plt.text(l/2, -Re*0.45, f"Ltotal = {l*1000:.3f}MM", ha='center', fontsize=10)

    # ---------- STYLE ----------
    plt.title("Bell Nozzle with Flow Expansion Visualization")
    plt.xlabel("Length (m)")
    plt.ylabel("Radius (m)")
    plt.axis("equal")
    plt.grid(alpha=0.2)

    # SAVE IMAGE
    save_path = "static"
    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, "Bell_nozzle.png")
    plt.savefig(file_path, dpi=300, bbox_inches='tight')

    plt.close()
    

    return "/static/Bell_nozzle.png"