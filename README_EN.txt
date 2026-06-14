# **Reconstruction of the Collatz Mapping via Jacobsthal-Normalized Spinor Representation**

Hiroshi Harada — June 14, 2026  

## **Overview**
This project redefines the transition of odd nuclei in the Collatz conjecture ($3n+1$ problem), moving beyond the conventional procedural operations of “multiply by 3 and add 1, then divide by $2^c$,” and reformulating it as a **linear transition of Jacobsthal-normalized two-component discrete spinors (J-spinors)**.

Any odd nucleus $N_{\mathrm{current}}$ is uniquely represented as the J-spinor $J_c(a,b)$, and the transition to the next odd nucleus is deterministically governed by the simple sum of the wave sources:
$$N_{\mathrm{next}} = a+b$$

---

## **Contents**
- `REPORT_EN.md` / `REPORT_JP.md`: Research reports detailing the mathematical proofs and theoretical framework  
- `collatz_jacobsthal_spinor.py`: Python script for generating and visualizing J-spinor trajectories for any initial value $n$  
- `collatz_jacobsthal_spinor_n7.csv`, etc.: Complete J-sequence datasets of the generated trajectories  
- `collatz_jacobsthal_spinor_n7.png`, etc.: Visualization plots of the Jacobsthal tracks within the 2-adic logarithmic spiral space  

---

## **Usage**
Running the following script in a Python 3.x environment will generate the CSV dataset and a high-resolution PNG image for the specified initial value in your current directory.

```bash
# Install dependencies
pip install numpy matplotlib pandas

# Execute the script
python collatz_jacobsthal_spinor.py
```

*Note: You can analyze the trajectory for any initial value by modifying the argument of `generate_artifacts(n)` at the bottom of the script.*

---

## **License**
- **Research Documents & Artifacts**: CC BY 4.0  
- **Python Source Code**: MIT License  

Copyright (c) 2026 Hiroshi Harada

---
