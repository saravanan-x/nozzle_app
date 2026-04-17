import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
import bell_nozzle as bn
import os

def bell_cfd(r1, cl, cr, con_l, e, rt, re, l1, Re, rn, ln, r_start, r_exit, slope_N, slope_exit, tita_n, tita_e, l, theta, x, xn, rx, yn, θn):

    # ---------------- STYLE ----------------
    plt.style.use('dark_background')
    plt.figure(figsize=(14,6), facecolor='#0b0f1a')
    ax = plt.gca()
    ax.set_facecolor('#0b0f1a')

    # ---------------- GEOMETRY ----------------
    x_chamber_start = -(cl + con_l + l1)
    x_chamber_end   = -(con_l + l1)
    x_conv_end      = -l1

    r1_conv = 1.5 * rt
    y_conv_end = rt + r1_conv * (1 - np.cos(theta))

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

    # =========================================================
    # 🔥 CFD-LIKE FIELD (MACH + TEMPERATURE + SHOCK EFFECT)
    # =========================================================

    X = np.linspace(x_chamber_start, l, 500)
    Y = np.linspace(-Re, Re, 350)
    X, Y = np.meshgrid(X, Y)

    # Nozzle wall interpolation
    wall = np.interp(X[0], x, rx, left=cr, right=Re)
    R_local = np.interp(X, x, rx, left=cr, right=Re)

    mask = np.abs(Y) <= R_local

    # ---- Mach field (approx expansion) ----
    Me = 3.0
    M = 1 + (Me - 1) * (X - x_chamber_start) / (l - x_chamber_start)

    # radial decay (boundary effect)
    M = M * (1 - (np.abs(Y) / (R_local + 1e-6))**2)

    # ---- Temperature field (isentropic) ----
    gamma = 1.4
    Tc = 3000
    T = Tc / (1 + (gamma - 1)/2 * M**2)

    # ---- Shock-like effect ----
    shock_region = (X > l*0.6) & (X < l*0.7)
    M[shock_region] *= 0.6

    # mask outside nozzle
    M[~mask] = np.nan

    # ---- Contour Plot ----
    contour = plt.contourf(
        X, Y, M,
        levels=100,
        cmap='turbo',
        alpha=0.9
    )

    cbar = plt.colorbar(contour)
    cbar.set_label("Mach Number", color='white')

    # =========================================================
    # 🔥 NOZZLE WALL (ON TOP)
    # =========================================================
    c = "white"

    plt.plot(x_chamber, y_chamber, color=c, linewidth=2)
    plt.plot(x_conv, y_conv, color=c, linewidth=2)
    plt.plot(x_arc_conv, y_arc_conv, color=c, linewidth=2)
    plt.plot(x_arc_div, y_arc_div, color=c, linewidth=2)
    plt.plot(x, rx, color=c, linewidth=2)

    plt.plot(x_chamber, -y_chamber, color=c, linewidth=2)
    plt.plot(x_conv, -y_conv, color=c, linewidth=2)
    plt.plot(x_arc_conv, -y_arc_conv, color=c, linewidth=2)
    plt.plot(x_arc_div, -y_arc_div, color=c, linewidth=2)
    plt.plot(x, -rx, color=c, linewidth=2)

    # =========================================================
    # 🔥 STREAMLINES (IMPROVED)
    # =========================================================
    for i in np.linspace(-0.8, 0.8, 12):
        x_stream = np.linspace(x_chamber_start, l, 200)
        y_stream = i * rt * (1 + 0.4 * (x_stream/l)**2)

        plt.plot(x_stream, y_stream, color='white', alpha=0.3, linewidth=0.8)

    # =========================================================
    # CENTERLINE
    # =========================================================
    plt.axhline(0, linestyle='--', linewidth=1, color='gray')

    # =========================================================
    # KEY POINTS
    # =========================================================
    plt.scatter([0, xn, l], [rt, yn, Re], color='cyan')

    plt.text(0, rt + Re*0.08, "Throat", ha='center', fontsize=10, color='white')
    plt.text(xn, yn + Re*0.08, "N", ha='center', fontsize=10, color='white')
    plt.text(l, Re + Re*0.08, "Exit", ha='center', fontsize=10, color='white')

    # =========================================================
    # DIMENSIONS (kept same)
    # =========================================================
    def dim_line(x1, y1, x2, y2):
        plt.annotate('', xy=(x1, y1), xytext=(x2, y2),
                    arrowprops=dict(arrowstyle='<->', lw=1.2, color='white'))

    dim_line(-0.015, 0, -0.015, rt)
    dim_line(xn-0.015, 0, xn-0.015, yn)
    dim_line(l+0.015, 0, l+0.015, Re)

    dim_line(0, -Re*0.20, xn, -Re*0.20)
    dim_line(xn, -Re*0.30, l, -Re*0.30)
    dim_line(0, -Re*0.40, l, -Re*0.40)

    # TEXT
    plt.text(-0.02, rt/2, f"Rt = {rt*1000:.3f}MM", fontsize=10, rotation=90, color='white')
    plt.text(xn-0.02, yn/2, f"Rn = {yn*1000:.3f}MM", fontsize=10, rotation=90, color='white')
    plt.text(l+0.02, Re/2, f"Re = {Re*1000:.3f}MM", fontsize=10, rotation=90, color='white')

    plt.text(xn/2, -Re*0.25, f"Ln = {xn*1000:.3f}MM", ha='center', fontsize=10, color='white')
    plt.text((xn+l)/2, -Re*0.30, f"Lbell = {(l-xn)*1000:.3f}MM", ha='center', fontsize=10, color='white')
    plt.text(l/2, -Re*0.45, f"Ltotal = {l*1000:.3f}MM", ha='center', fontsize=10, color='white')

    # =========================================================
    # FINAL STYLE
    # =========================================================
    plt.title("CFD-Style Bell Nozzle (Mach Contour)", color='white')
    plt.xlabel("Length (m)", color='white')
    plt.ylabel("Radius (m)", color='white')

    plt.axis("equal")
    plt.grid(alpha=0.1)

    # =========================================================
    # SAVE IMAGE
    # =========================================================
    save_path = "static"
    os.makedirs(save_path, exist_ok=True)

    file_path = os.path.join(save_path, "out/Bell_CDF.png")
    plt.savefig(file_path, dpi=300, bbox_inches='tight')

    plt.close()

    return "/static/out/Bell_CDF.png"