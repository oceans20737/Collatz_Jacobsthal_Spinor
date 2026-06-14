# -*- coding: utf-8 -*-
"""code_01_collatz_jacobsthal_spinor.ipynb
"""

# Title: Collatz-Jacobsthal Spinor with PNG/CSV Export
# Author: Hiroshi Harada
# Date: June 14, 2026
# License: MIT
# Copyright (c) 2026 Hiroshi Harada

import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib.lines import Line2D

def collatz_odd_path(n):
    path = [n]
    while n != 1:
        n = 3 * n + 1
        while n % 2 == 0:
            n //= 2
        path.append(n)
    return path

def get_J_params(n_next):
    """
    Reconstruct the source wave components (a, b) of the Jacobsthal spinor
    from the subsequent node N_next.
    """
    S = n_next
    if S % 3 == 1:
        a = (S - 1) // 3
    elif S % 3 == 2:
        a = (S + 1) // 3
    else:
        a = S // 3
    return int(a), int(S - a)

def generate_J_sequence(a, b, length=9):
    """
    Generate the Jacobsthal track sequence satisfying J_m = J_{m-1} + 2*J_{m-2}.
    """
    seq = [a, b]
    for _ in range(length - 2):
        seq.append(seq[-1] + 2 * seq[-2])
    return seq

def generate_artifacts(n_val):
    odd_path = collatz_odd_path(n_val)

    # Figure Configuration
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(12, 12))
    fig.patch.set_facecolor('#0d0d0d')
    ax.set_facecolor('#0d0d0d')

    csv_filename = f'collatz_jacobsthal_spinor_n{n_val}.csv'
    png_filename = f'collatz_jacobsthal_spinor_n{n_val}.png'

    csv_header = ['Odd', 'J(a,b)_m', 'a+b', 'm = 0', '1', '2', '3', '4', '5', '6', '7', '8']
    csv_data = []

    # Map and Plot Jacobsthal Tracks
    for i in range(len(odd_path) - 1):
        n_current = odd_path[i]
        n_next = odd_path[i+1]

        # Calculate space-shift count (c) dynamically
        temp = 3 * n_current + 1
        c = 0
        while temp % 2 == 0:
            temp //= 2
            c += 1

        a, b = get_J_params(n_next)
        j_seq = generate_J_sequence(a, b, length=9)
        j_label = f"J({a},{b})_{c}"
        next_nucleus = a + b

        csv_data.append([n_current, j_label, next_nucleus] + j_seq)

        valid_seq = [x for x in j_seq if x > 0]
        if not valid_seq:
            continue

        r_j = np.log2(valid_seq)
        theta_j = r_j * 2 * np.pi

        # Plot structural tracks
        ax.plot(theta_j, r_j, color='gold', linestyle=':', linewidth=1.5, alpha=0.6)
        ax.scatter(theta_j, r_j, color='gold', s=20, alpha=0.6)

        # Track Labeling
        ax.text(theta_j[-1], r_j[-1] + 0.2, f"{j_label} Track",
                color='gold', fontsize=9, fontweight='bold', alpha=0.8)

    # Export to CSV Dataset
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)
        writer.writerows(csv_data)

    # Plot the Experimental Collatz Trajectory
    r_path = np.log2(odd_path)
    theta_path = r_path * 2 * np.pi

    ax.plot(theta_path, r_path, color='cyan', linewidth=3, zorder=10)
    ax.scatter(theta_path, r_path, color='cyan', s=80, zorder=11)

    # Node Annotation
    for i, n_node in enumerate(odd_path):
        ax.annotate(str(n_node),
                    xy=(theta_path[i], r_path[i]),
                    xytext=(theta_path[i] + 0.08, r_path[i] - 0.4),
                    color='white', fontsize=12, fontweight='bold',
                    zorder=12)

    # Polar Grid Formatting
    ax.set_rticks([])
    ax.set_yticklabels([])
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.grid(True, color='gray', alpha=0.2, linestyle='-')

    # Legend Construction
    custom_lines = [
        Line2D([0], [0], color='cyan', lw=3, marker='o', markersize=8),
        Line2D([0], [0], color='gold', lw=1.5, linestyle=':', marker='o', markersize=5)
    ]
    ax.legend(custom_lines, ['Collatz Transfer Path', 'Jacobsthal Track'],
              loc='upper right', bbox_to_anchor=(1.25, 1.05),
              fontsize=10, facecolor='#1a1a1a', labelcolor='white')

    # Scientific Title and Footnote
    plt.title(f"Collatz-Jacobsthal Spiral Plot (Seed n={n_val})",
              pad=30, fontsize=18, fontweight='bold', color='white')

    plt.figtext(0.5, 0.02, "© 2026 Hiroshi Harada — Licensed under MIT License",
            ha="center", fontsize=9, color="gray")

    plt.tight_layout()

    # Save high-resolution PNG
    plt.savefig(png_filename, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()

    print(f"Artifacts successfully generated:\n1. {csv_filename}\n2. {png_filename}")

    # Let's print the actual file tags to be safe by keeping references to paths or output
    import os
    print(f"CSV PATH: {os.path.abspath(csv_filename)}")
    print(f"PNG PATH: {os.path.abspath(png_filename)}")

generate_artifacts(7)

