#!/usr/bin/env python3
"""Generate charts for the Bethlehem Steel report."""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent / "output" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

# --- Style ---
plt.rcParams.update({
    'font.family': 'monospace',
    'font.size': 9,
    'axes.facecolor': '#fafafa',
    'figure.facecolor': 'white',
    'axes.edgecolor': '#333333',
    'axes.linewidth': 0.8,
    'grid.color': '#e0e0e0',
    'grid.linewidth': 0.5,
    'text.color': '#1a1a1a',
    'axes.labelcolor': '#1a1a1a',
    'xtick.color': '#333333',
    'ytick.color': '#333333',
})

def save(fig, name):
    fig.savefig(OUT / name, dpi=200, bbox_inches='tight', pad_inches=0.2)
    plt.close(fig)
    print(f"  saved: {name}")


# =============================================================================
# 1. REVENUE ARC (1940-2001)
# =============================================================================
years_rev = [1940, 1945, 1957, 1966, 1967, 1972, 1981, 1997, 1998, 1999, 2000, 2001]
revenue   = [0.135, 1.33, 2.6, 2.69, 2.62, 3.14, 7.3, 4.63, 4.7, 4.1, 4.2, 3.76]

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.fill_between(years_rev, revenue, alpha=0.15, color='#2563eb')
ax.plot(years_rev, revenue, color='#2563eb', linewidth=2, marker='o', markersize=4)

annotations = {1945: 'WWII Peak\n$1.33B', 1957: 'Post-War Peak\n$2.6B',
               1981: 'Record\n$7.3B', 2001: 'Bankruptcy\n$3.76B'}
for yr, label in annotations.items():
    idx = years_rev.index(yr)
    ax.annotate(label, (yr, revenue[idx]), textcoords="offset points",
                xytext=(0, 12), ha='center', fontsize=7, fontweight='bold')

ax.set_title('Bethlehem Steel Revenue (1940-2001)', fontweight='bold', fontsize=11)
ax.set_ylabel('Revenue ($B)')
ax.set_xlabel('')
ax.grid(True, axis='y', alpha=0.5)
ax.set_xlim(1935, 2005)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('$%.1fB'))
save(fig, 'revenue_arc.png')


# =============================================================================
# 2. NET INCOME / LOSS (1957-2001)
# =============================================================================
years_ni = [1957, 1966, 1967, 1973, 1974, 1977, 1982, 1986, 1987, 1988, 1991, 1997, 1998, 1999, 2000, 2001]
net_inc  = [190, 170.9, 130.4, 207, 342, -448, -1500, -150, 174, 400, -191, 280, 120, -183, -118, -1270]

fig, ax = plt.subplots(figsize=(8, 3.5))
colors = ['#16a34a' if v >= 0 else '#dc2626' for v in net_inc]
bars = ax.bar(years_ni, net_inc, width=1.8, color=colors, alpha=0.8, edgecolor='none')

ax.axhline(y=0, color='#333333', linewidth=0.8)
ax.set_title('Bethlehem Steel Net Income / (Loss) by Year ($M)', fontweight='bold', fontsize=11)
ax.set_ylabel('Net Income ($M)')
ax.grid(True, axis='y', alpha=0.5)
ax.set_xlim(1954, 2004)

# Key annotations
ax.annotate('Record profit\n$342M', (1974, 342), textcoords="offset points",
            xytext=(15, 5), ha='center', fontsize=7, fontweight='bold', color='#16a34a')
ax.annotate('Steel crisis\n($1.5B)', (1982, -1500), textcoords="offset points",
            xytext=(15, -15), ha='center', fontsize=7, fontweight='bold', color='#dc2626')
ax.annotate('Bankruptcy\n($1.27B)', (2001, -1270), textcoords="offset points",
            xytext=(-15, -15), ha='center', fontsize=7, fontweight='bold', color='#dc2626')
save(fig, 'net_income.png')


# =============================================================================
# 3. STOCK PRICE ARC (key milestones)
# =============================================================================
years_stk = [1914, 1917, 1929, 1932, 1957, 1981, 1986, 1997, 2000, 2001]
stock     = [30,   600,  500,  25,   50,   31.75, 4,  15,   2.94, 1.01]
# Note: these are approximate/representative prices, not exact adjusted closes

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.plot(years_stk, stock, color='#7c3aed', linewidth=2, marker='o', markersize=5)
ax.fill_between(years_stk, stock, alpha=0.1, color='#7c3aed')

milestones = {
    1917: ('WWI Peak\n~$600', 12),
    1929: ('1929 Crash', -20),
    1981: ('20yr high\n$31.75', 12),
    1986: ('Low ~$4', -18),
    2001: ('$1.01', -15),
}
for yr, (label, offset) in milestones.items():
    idx = years_stk.index(yr)
    ax.annotate(label, (yr, stock[idx]), textcoords="offset points",
                xytext=(0, offset), ha='center', fontsize=7, fontweight='bold')

ax.set_title('Bethlehem Steel Stock Price -- Key Milestones (1914-2001)', fontweight='bold', fontsize=11)
ax.set_ylabel('Stock Price ($)')
ax.set_yscale('log')
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('$%.0f'))
ax.grid(True, axis='y', alpha=0.5)
ax.set_xlim(1910, 2005)
save(fig, 'stock_price.png')


# =============================================================================
# 4. EMPLOYMENT DECLINE
# =============================================================================
years_emp = [1914, 1918, 1925, 1943, 1957, 1964, 1977, 1982, 1986, 1997, 2001]
employees = [15.6, 31, 60, 283.8, 165, 167, 105, 80, 48.5, 15.6, 13]

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.fill_between(years_emp, employees, alpha=0.15, color='#ea580c')
ax.plot(years_emp, employees, color='#ea580c', linewidth=2, marker='o', markersize=4)

ax.annotate('WWII Peak\n283,765', (1943, 283.8), textcoords="offset points",
            xytext=(0, 10), ha='center', fontsize=7, fontweight='bold')
ax.annotate('Post-war\n165,000', (1957, 165), textcoords="offset points",
            xytext=(15, 8), ha='center', fontsize=7, fontweight='bold')
ax.annotate('Bankruptcy\n13,000', (2001, 13), textcoords="offset points",
            xytext=(-20, 10), ha='center', fontsize=7, fontweight='bold')

ax.set_title('Bethlehem Steel Employment (thousands)', fontweight='bold', fontsize=11)
ax.set_ylabel('Employees (thousands)')
ax.grid(True, axis='y', alpha=0.5)
ax.set_xlim(1910, 2005)
save(fig, 'employment.png')


# =============================================================================
# 5. STEEL PRODUCTION VOLUME
# =============================================================================
years_prod = [1914, 1925, 1945, 1957, 1964, 1966, 1973, 1982, 1991, 2001]
production = [1.1, 8.5, 12.2, 19, 19.4, 21.3, 23.7, 10, 8, 8]

fig, ax = plt.subplots(figsize=(8, 3.5))
ax.fill_between(years_prod, production, alpha=0.15, color='#0891b2')
ax.plot(years_prod, production, color='#0891b2', linewidth=2, marker='o', markersize=4)

ax.annotate('All-time record\n23.7M tons', (1973, 23.7), textcoords="offset points",
            xytext=(0, 10), ha='center', fontsize=7, fontweight='bold')
ax.annotate('Post-crisis\n~8M tons', (1991, 8), textcoords="offset points",
            xytext=(15, 10), ha='center', fontsize=7, fontweight='bold')

ax.set_title('Bethlehem Steel Annual Raw Steel Production (M tons)', fontweight='bold', fontsize=11)
ax.set_ylabel('Million Tons')
ax.grid(True, axis='y', alpha=0.5)
ax.set_xlim(1910, 2005)
save(fig, 'production.png')


# =============================================================================
# 6. IMPORT PENETRATION vs MINI-MILL SHARE
# =============================================================================
fig, ax1 = plt.subplots(figsize=(8, 3.5))

years_imp = [1958, 1968, 1974, 1978, 1981, 1985, 1995, 2000]
imports   = [2, 13, 13.7, 18, 23, 21, 22, 23]

years_mm = [1971, 1980, 1989, 2000, 2004]
minimill = [17.4, 18, 25, 46, 47]

ax1.plot(years_imp, imports, color='#dc2626', linewidth=2, marker='s', markersize=4, label='Import penetration (% of US consumption)')
ax1.plot(years_mm, minimill, color='#2563eb', linewidth=2, marker='^', markersize=4, label='Mini-mill share (% of US production)')

ax1.set_title('Twin Threats: Import Penetration & Mini-Mill Market Share', fontweight='bold', fontsize=11)
ax1.set_ylabel('Percentage (%)')
ax1.set_xlabel('')
ax1.grid(True, axis='y', alpha=0.5)
ax1.legend(fontsize=7, loc='upper left')
ax1.set_xlim(1955, 2007)
ax1.set_ylim(0, 55)

# Shade the "danger zone" after 1982
ax1.axvspan(1982, 2005, alpha=0.05, color='red')
ax1.annotate('1982 Steel Crisis', (1982, 50), fontsize=7, color='#dc2626', fontweight='bold')
save(fig, 'competitive_threats.png')


# =============================================================================
# 7. TECHNOLOGY GAP: CONTINUOUS CASTING ADOPTION
# =============================================================================
countries = ['US', 'Japan', 'W. Germany']
cc_1975 = [9, 31, 24]
cc_1990 = [67, 95, 90]  # approximate

x = np.arange(len(countries))
width = 0.3

fig, ax = plt.subplots(figsize=(6, 3.5))
bars1 = ax.bar(x - width/2, cc_1975, width, label='1975', color='#94a3b8', edgecolor='none')
bars2 = ax.bar(x + width/2, cc_1990, width, label='~1990', color='#2563eb', edgecolor='none')

ax.set_title('Continuous Casting Adoption (% of steel output)', fontweight='bold', fontsize=11)
ax.set_ylabel('% of Output')
ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.legend(fontsize=8)
ax.grid(True, axis='y', alpha=0.5)
ax.set_ylim(0, 105)

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            f'{int(bar.get_height())}%', ha='center', fontsize=8, fontweight='bold')
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            f'{int(bar.get_height())}%', ha='center', fontsize=8, fontweight='bold')
save(fig, 'technology_gap.png')


# =============================================================================
# 8. LEGACY COST BURDEN: RETIREES vs ACTIVE WORKERS
# =============================================================================
years_ratio = ['1945', '1957', '1975', '1983', '1986', '1997', '2001']
active   = [300, 165, 115, 55, 48.5, 15.6, 13]
retirees = [5, 30, 60, 60, 80, 95, 95]  # approximate

fig, ax = plt.subplots(figsize=(8, 3.5))
x = np.arange(len(years_ratio))
width = 0.35

ax.bar(x - width/2, active, width, label='Active Employees (K)', color='#2563eb', alpha=0.8)
ax.bar(x + width/2, retirees, width, label='Retirees/Dependents (K)', color='#dc2626', alpha=0.8)

ax.set_title('Active Workers vs. Retirees (thousands)', fontweight='bold', fontsize=11)
ax.set_ylabel('Thousands')
ax.set_xticks(x)
ax.set_xticklabels(years_ratio)
ax.legend(fontsize=8)
ax.grid(True, axis='y', alpha=0.5)

# Mark the crossover
ax.annotate('Crossover:\nretirees > workers', (3, 62), fontsize=7, fontweight='bold',
            color='#dc2626', ha='center')
save(fig, 'legacy_burden.png')


# =============================================================================
# 9. PENSION UNDERFUNDING
# =============================================================================
years_pen = ['1993', '1997', '2001', '2002\n(PBGC)']
unfunded  = [1.6, 0.44, 3.2, 3.7]

fig, ax = plt.subplots(figsize=(6, 3.5))
colors_pen = ['#f59e0b', '#16a34a', '#dc2626', '#991b1b']
ax.bar(years_pen, unfunded, color=colors_pen, alpha=0.85, edgecolor='none', width=0.6)

for i, (yr, val) in enumerate(zip(years_pen, unfunded)):
    ax.text(i, val + 0.1, f'${val}B', ha='center', fontsize=9, fontweight='bold')

ax.set_title('Unfunded Pension Liability ($B)', fontweight='bold', fontsize=11)
ax.set_ylabel('Billions ($)')
ax.grid(True, axis='y', alpha=0.5)
ax.set_ylim(0, 4.5)
ax.annotate('Bull market\nreduced gap', (1, 0.44), textcoords="offset points",
            xytext=(0, 25), ha='center', fontsize=7, color='#16a34a',
            arrowprops=dict(arrowstyle='->', color='#16a34a', lw=0.8))
save(fig, 'pension_underfunding.png')


# =============================================================================
# 10. NUCOR vs BETHLEHEM REVENUE DIVERGENCE (1996-2005)
# =============================================================================
years_comp = [1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005]
beth_rev   = [4.3, 4.63, 4.7, 4.1, 4.2, 3.76, None, None, None, None]
nucor_rev  = [3.64, 4.18, 4.15, 4.0, 4.58, 4.13, 4.97, 6.26, 11.37, 12.70]

fig, ax = plt.subplots(figsize=(8, 3.5))
# Filter out None for Bethlehem
beth_years = [y for y, r in zip(years_comp, beth_rev) if r is not None]
beth_vals  = [r for r in beth_rev if r is not None]

ax.plot(beth_years, beth_vals, color='#dc2626', linewidth=2.5, marker='o', markersize=5, label='Bethlehem Steel')
ax.plot(years_comp, nucor_rev, color='#16a34a', linewidth=2.5, marker='s', markersize=5, label='Nucor')

# Mark bankruptcy
ax.axvline(x=2001, color='#dc2626', linestyle='--', alpha=0.5)
ax.annotate('Bankruptcy\n(Oct 2001)', (2001, 8), fontsize=7, fontweight='bold', color='#dc2626', ha='center')

ax.set_title('Revenue Divergence: Bethlehem Steel vs. Nucor ($B)', fontweight='bold', fontsize=11)
ax.set_ylabel('Revenue ($B)')
ax.legend(fontsize=8)
ax.grid(True, axis='y', alpha=0.5)
ax.set_xlim(1995, 2006)
save(fig, 'nucor_divergence.png')


print("\nAll charts generated.")
