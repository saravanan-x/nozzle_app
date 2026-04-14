import numpy as np
import math
import atmosphere_data as at_data

def flow_properties(pc, pe, temp_k, tc, y, r, g, at, ae):
     # Envinomental values
     pa = pe  
     ta = temp_k 
     #Throat Radius
     Trs = 3.6837
     tr = (2*Trs)/1000

     #Exit Radius
     Er = 0.0807
     er = (Er*2)/1000

     #outside air pressure and tempreture
     p = 24.5
     t = 245

     # Exit Mach
     me = np.sqrt((2/(y-1))*((pc/pe)**((y-1)/y)-1))

     # ratio of area
     Ar = ((y+1)/2)**(- (y+1)/(2 * (y-1))) * (((1 + ((y-1)/2) * me**2)**((y+1)/(2 * (y-1)))) / me)

     # Nozzle area ratio
     ar = ae/at

     # Stagnation Density
     ρ0 = pc / (r * tc)

     # Throart Velocity (where mach = 1)
     vt = np.sqrt( (2*y*r*tc) / (y+1) )

     # Throat Density
     ρt = ρ0 * (2/(y+1))**(1/(y-1))

     #Exit Pressure
     ep = pc * (1+((y-1)/2)*(me**2))**(-(y/(y-1)))

     # Exit Tempreture
     et = tc * (1 + (((y-1)/2) * (me**2)))**-1

     # Exit Vlecity 
     v_e = np.sqrt(y * r * et) * me

     # General mass flow rate (check)
     mg = ((at * pc) / np.sqrt(tc)) * np.sqrt(y / r) * (
          me * (1 + ((y - 1) / 2) * me**2)**(-(y + 1) / (2 * (y - 1))))

     # Choked mass flow rate:
     mc = ((at * pc) / np.sqrt(tc)) * (np.sqrt(y / r)) * (
          ((y + 1) / 2)**(-((y + 1) / (2 * (y - 1)))))

     #Exit Mass flow

     #m0 = ρt * vt * at 
     m0 = (pc * at / np.sqrt(tc)) * (np.sqrt(y / r) ) * (2 / (y + 1))**((y + 1) / (2 * (y - 1)))

     #FORCE
     F = m0 * v_e + (ep - pa) * ae
     isp = v_e / g


     return me, Ar, ar, ρ0, vt, ρt, ep, et, v_e, mg, mc, m0, F, isp

       


