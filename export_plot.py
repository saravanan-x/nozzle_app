import os
import numpy as np
import pandas as pd

def export_plot(tita_n, r1, rt, x, rx):

    # ✅ Use STATIC folder (Flask can serve this)
    save_path = "static/plot"
    os.makedirs(save_path, exist_ok=True)

    # 1. Divergent Arc
    t_vals_div = np.linspace(-np.pi/2, -np.pi/2 + tita_n, 100)
    x_div_arc = r1 * np.cos(t_vals_div)
    y_div_arc = r1 * np.sin(t_vals_div) + (rt + r1)

    # 2. Combine
    X_coords = np.concatenate([x_div_arc, x])
    Y_coords = np.concatenate([y_div_arc, rx])
    Z_coords = np.zeros_like(X_coords)

    df = pd.DataFrame({
        'X_mm': X_coords * 1000,
        'Y_mm': Y_coords * 1000,
        'Z_mm': Z_coords * 1000
    })

    df = df.round(6).drop_duplicates().reset_index(drop=True)

    # File paths
    excel_file = os.path.join(save_path, "Bell_Profile.xlsx")
    txt_file   = os.path.join(save_path, "Bell_Profile.txt")

    # Save
    df.to_excel(excel_file, index=False)
    df.to_csv(txt_file, sep='\t', index=False, header=False)

    # ✅ Return BOTH paths
    return {
        "excel": "/static/plot/Bell_Profile.xlsx",
        "txt": "/static/plot/Bell_Profile.txt"
    }