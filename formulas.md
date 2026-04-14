
<divalign="center"style="

    padding: 15px;

    border-radius: 12px;

    background: linear-gradient(135deg, #0F2027, #203A43, #2C5364);

    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);">

<h1style="

    color: #4FC3F7;

    font-size: 38px;

    margin: 0;

    font-weight: bold;">

Rocket Nozzle Design

</h1>

<pstyle="

    color: #B0BEC5;

    font-size: 16px;

    margin-top: 5px;">

Flow Calculations • Simulation • Geometry

</p>

</div>

<palign="center">

  [imgsrc=&#34;https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&amp;logo=python&#34;/](imgsrc=%22https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python%22/)

  [imgsrc=&#34;https://img.shields.io/badge/Aerospace-Propulsion-black?style=for-the-badge&#34;/](imgsrc=%22https://img.shields.io/badge/Aerospace-Propulsion-black?style=for-the-badge%22/)

  [imgsrc=&#34;https://img.shields.io/badge/Focus-Nozzle%20Design-orange?style=for-the-badge&#34;/](imgsrc=%22https://img.shields.io/badge/Focus-Nozzle%20Design-orange?style=for-the-badge%22/)

  [imgsrc=&#34;https://img.shields.io/badge/Status-Active-success?style=for-the-badge&#34;/](imgsrc=%22https://img.shields.io/badge/Status-Active-success?style=for-the-badge%22/)

</p>

<divalign="center"style="

    padding: 15px;

    border-radius: 12px;

    background: linear-gradient(135deg, #0F2027, #203A43, #2C5364);

    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);">

<h1style="

    color: #4FC3F7;

    font-size: 38px;

    margin: 0;

    font-weight: bold;">

Rocket Nozzle Design

</h1>

<pstyle="

    color: #B0BEC5;

    font-size: 16px;

    margin-top: 5px;">

Flow Calculations • Simulation • Geometry

</p>

</div>

<palign="center">

  [imgsrc=&#34;https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&amp;logo=python&#34;/](imgsrc=%22https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python%22/)

  [imgsrc=&#34;https://img.shields.io/badge/Aerospace-Propulsion-black?style=for-the-badge&#34;/](imgsrc=%22https://img.shields.io/badge/Aerospace-Propulsion-black?style=for-the-badge%22/)

  [imgsrc=&#34;https://img.shields.io/badge/Focus-Nozzle%20Design-orange?style=for-the-badge&#34;/](imgsrc=%22https://img.shields.io/badge/Focus-Nozzle%20Design-orange?style=for-the-badge%22/)

  [imgsrc=&#34;https://img.shields.io/badge/Status-Active-success?style=for-the-badge&#34;/](imgsrc=%22https://img.shields.io/badge/Status-Active-success?style=for-the-badge%22/)

</p>

## <spanstyle="color: lightgreen">Rocket Nozzle Design Calculations

### Given Parameters

| Parameter | Variable | Parameter | Variable |

| :--- | :--- | :--- | :--- |

| **Thrust (N)** | $F$ | **Chamber Temp (K)** | $T_c$ |

| **Chamber Pressure (Pa)** | $P_c$ | **Specific Heat Ratio** | $\gamma$ |

| **Exit Pressure (Pa)** | $P_e$ | **Gas Constant (J/kg·K)** | $R$ |

### Flow & Area Dynamics

| Metric | Formula | Metric | Formula |

| :--- | :--- | :--- | :--- |

| **Exit Velocity** | $\displaystyle V_e = \sqrt{\frac{2\gamma}{\gamma - 1} \cdot R T_c \cdot \left(1 - \left(\frac{P_e}{P_c}\right)^{\frac{\gamma - 1}{\gamma}}\right)}$ | **Exit Mach No.** | $\displaystyle M_e = \sqrt{\frac{2}{\gamma - 1} \left[ \left(\frac{P_c}{P_e}\right)^{\frac{\gamma - 1}{\gamma}} - 1 \right]}$ |

| **Mass Flow Rate** | $\displaystyle \dot{m} = \frac{F}{V_e}$ | **Area Ratio** | $\displaystyle \frac{A_e}{A_t} = \frac{1}{M_e} \left[ \frac{1 + \frac{\gamma - 1}{2} M_e^2}{\frac{\gamma + 1}{2}} \right]^{\frac{\gamma + 1}{2(\gamma - 1)}}$ |

| **Throat Area** | $\displaystyle A_t = \frac{\dot{m}}{P_c} \cdot \sqrt{\frac{R T_c}{\gamma} \cdot \left(\frac{\gamma + 1}{2}\right)^{\frac{\gamma + 1}{2(\gamma - 1)}}}$ | **Exit Area** | $\displaystyle A_e = A_t \cdot \frac{A_e}{A_t}$ |

| **Throat Diameter** | $\displaystyle d_t = \sqrt{\frac{4A_t}{\pi}}$ | **Exit Diameter** | $\displaystyle d_e = \sqrt{\frac{4A_e}{\pi}}$ |

### Geometry & Structural Design

| Metric | Formula | Metric | Formula |

| :--- | :--- | :--- | :--- |

| **Chamber Diameter** | $\displaystyle d_c = 3 d_t$ | **Convergent Length** | $\displaystyle L_{conv} = \frac{d_c - d_t}{2 \tan(\alpha)}$ |

| **Chamber Area** | $\displaystyle A_c = \frac{\pi d_c^2}{4}$ | **Divergent Length** | $\displaystyle L_{div} = \frac{d_e - d_t}{2 \tan(\beta)}$ |

| **Chamber Length** | $\displaystyle L_c = \frac{L^* \cdot A_t}{A_c}$ | **Total Length** | $\displaystyle L_{total} = L_c + L_{conv} + L_{div}$ |

| **Wall Thickness** | $\displaystyle t_w = \frac{P_c \cdot d_c}{16000}$ | **Stress Check** | $\displaystyle \sigma = \frac{P_c \cdot d_c}{2 t_w}$ |

| **Design Thickness** | $\displaystyle t = \frac{P_c \cdot d_c \cdot SF}{2 \sigma_{yield}}$ | | |

## Nozzle Flow & Performance Analysis

#### *Analytical Framework for Isentropic Expansion*

### 1. Mach & Area Relations

*Determines the expansion state based on pressure ratios and nozzle geometry.*

| Parameter | Formula | Description |

| :--- | :--- | :--- |

| **Exit Mach ($M_e$)** |

$$
M_e = \sqrt{\frac{2}{\gamma - 1} \left[\left(\frac{P_c}{P_e}\right)^{\frac{\gamma - 1}{\gamma}} - 1\right]}
$$

 | Mach number at the exit plane. |

| **Area Ratio ($\epsilon$)** |

$$
\frac{A_e}{A_t} = \left(\frac{\gamma+1}{2}\right)^{-\frac{\gamma+1}{2(\gamma-1)}} \cdot \frac{\left(1 + \frac{\gamma-1}{2} M_e^2\right)^{\frac{\gamma+1}{2(\gamma-1)}}}{M_e}
$$

 | Ratio of exit area to throat area. |

### 2. Mass Flow Rates ($\dot{m}$)

*Calculates the rate of propellant consumption through the nozzle.*

***General Flow:**

$$
\dot{m}_g = \frac{A_t P_c}{\sqrt{T_c}} \sqrt{\frac{\gamma}{R}} \cdot\left[M_e \left(1 + \frac{\gamma - 1}{2} M_e^2\right)^{-\frac{\gamma + 1}{2(\gamma - 1)}}\right]
$$

***Choked Flow:**

$$
\dot{m}_c = \frac{A_t P_c}{\sqrt{T_c}} \sqrt{\frac{\gamma}{R}} \cdot\left(\frac{\gamma + 1}{2}\right)^{-\frac{\gamma + 1}{2(\gamma - 1)}}
$$

***Continuity Equation:**

$$
\dot{m} = \rho_t\cdot V_t \cdot A_t
$$

### 3. Thermodynamic Properties

*State variables at the stagnation (chamber) and sonic (throat) points.*

| Location | Quantity | Formula |

| :--- | :--- | :--- |

| **Chamber** | **Stagnation Density** |

$$
\rho_0 = \frac{P_c}{R T_c}
$$

 |

| **Throat** | **Velocity ($V_t$)** |

$$
V_t = \sqrt{\frac{2 \gamma R T_c}{\gamma + 1}}
$$

 |

| **Throat** | **Density ($\rho_t$)** |

$$
\rho_t = \rho_0 \left(\frac{2}{\gamma+1}\right)^{\frac{1}{\gamma-1}}
$$

 |

### 4. Exit Plane Properties

*Conditions of the exhaust gas as it leaves the nozzle.*

***Exit Pressure ($P_e$):**

$$
P_e = P_c \left(1 + \frac{\gamma - 1}{2} M_e^2\right)^{-\frac{\gamma}{\gamma-1}}
$$

***Exit Temperature ($T_e$):**

$$
T_e = T_c \left(1 + \frac{\gamma - 1}{2} M_e^2\right)^{-1}
$$

***Exit Velocity ($V_e$):**

$$
V_e = M_e \sqrt{\gamma R T_e}
$$

### 5. Performance Metrics

*The final output efficiency and power of the motor.*

***Total Thrust ($F$):**

$$
F = \dot{m} V_e + (P_e - P_a) A_e
$$

*Where $P_a$ is the ambient atmospheric pressure.*

***Specific Impulse ($I_{sp}$):**

$$
I_{sp} = \frac{V_e}{g}
$$

## Bell Nozzle Geometry (Rao Method)

### 1. Geometric Constants & Point N

| Quantity | Formula | Quantity | Formula |

| :--- | :--- | :--- | :--- |

| **Throat Radius** | $r_t = d_t / 2$ | **Expansion Ratio** | $\epsilon = A_e / A_t$ |

| **Exit Radius** | $r_e = d_e / 2$ | **Throat Arc $R_1$** | $R_1 = 0.382 \, r_t$ |

| **X-Coord at N** | $x_n = R_1 \sin \theta_n$ | **Y-Coord at N** | $y_n = r_t + R_1 (1 - \cos \theta_n)$ |

### 2. Convergent & Bell Angles

| Quantity | Formula | Quantity | Formula |

| :--- | :--- | :--- | :--- |

| **Conv. Angle $\theta$** | $25^\circ$ | **Arc Radius $R_c$** | $1.5 \, r_t$ |

| **Start Angle $\theta_n$** | $30^\circ$ | **Arc End Rad $r_n$** | $r_t + R_c (1 - \cos \theta)$ |

| **Exit Angle $\theta_e$** | $8.5^\circ$ | **Arc Length $l_1$** | $R_c \sin \theta$ |

| **Conical Length $l_n$** | $\frac{r_t(\sqrt{\epsilon}-1) + R_c(\cos\theta - 1)}{\tan\theta}$ | **Fractional Len $f$** | *User Defined (e.g. 0.8)* |

### 3. Core Design Equations

**Nozzle Length (Rao Approximation):**

$$
\displaystyle L = f \cdot\frac{r_t}{\tan(15^\circ)} \left[ \sqrt{\epsilon - 1} + 1.5\left(\frac{1}{\cos(15^\circ)} - 1\right) \right]
$$

**Parabolic Bell Contour Equation:**

$$
\displaystyle r(x) = y_n + \tan(\theta_n)(x - x_n) + \frac{\tan(\theta_e) - \tan(\theta_n)}{2(L - x_n)} (x - x_n)^2
$$

### 4. Boundary Conditions

| Condition | Formula | Condition | Formula |

| :--- | :--- | :--- | :--- |

| **Radius at N** | $r(x_n) = y_n$ | **Slope at N** | $\displaystyle \left.\frac{dr}{dx}\right\|_{x_n} = \tan(\theta_n)$ |

| **Radius at Exit** | $r(L) = r_e$ | **Slope at Exit** | $\displaystyle \left.\frac{dr}{dx}\right\|_{L} = \tan(\theta_e)$ |
