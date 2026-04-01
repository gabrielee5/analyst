#!/usr/bin/env python3
"""Generate charts for Chinese Stock Market report from charts.json."""

import json
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# Standard chart style
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

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CHARTS_JSON = os.path.join(SCRIPT_DIR, 'charts.json')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'output', 'charts')
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(CHARTS_JSON, 'r') as f:
    charts = json.load(f)

for spec in charts:
    chart_id = spec['id']
    chart_type = spec['type']
    title = spec['title']
    data = spec['data']
    x_label = spec.get('x_label', '')
    y_label = spec.get('y_label', '')
    color = spec.get('color', '#2563eb')
    annotations = spec.get('annotations', [])

    if chart_type == 'line':
        fig, ax = plt.subplots(figsize=(8, 3.5))
        ax.plot(data['x'], data['y'], color=color, linewidth=1.5, zorder=3)
        if spec.get('fill', False):
            ax.fill_between(data['x'], data['y'], alpha=0.1, color=color, zorder=2)
        for ann in annotations:
            x_val = ann['x']
            idx = data['x'].index(x_val) if x_val in data['x'] else None
            if idx is not None:
                y_val = data['y'][idx]
                ax.annotate(ann['text'], xy=(x_val, y_val),
                           xytext=(0, 12), textcoords='offset points',
                           fontsize=7, ha='center', color='#555555',
                           arrowprops=dict(arrowstyle='->', color='#999999', lw=0.6))
        ax.set_xlabel(x_label, fontsize=8)
        ax.set_ylabel(y_label, fontsize=8)
        ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
        ax.grid(True, alpha=0.5, zorder=0)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: f'{x:,.0f}'))
        plt.tight_layout()
        fig.savefig(os.path.join(OUTPUT_DIR, f'{chart_id}.png'), dpi=200, bbox_inches='tight')
        plt.close(fig)

    elif chart_type == 'bar':
        fig, ax = plt.subplots(figsize=(8, 3.5))
        x_vals = data['x']
        y_vals = data['y']
        # Color bars: green for positive, red for negative if mixed, else use spec color
        has_negative = any(v < 0 for v in y_vals)
        if has_negative:
            colors = ['#16a34a' if v >= 0 else '#dc2626' for v in y_vals]
        else:
            colors = [color] * len(y_vals)
        bars = ax.bar(range(len(x_vals)), y_vals, color=colors, width=0.7, zorder=3)
        ax.set_xticks(range(len(x_vals)))
        ax.set_xticklabels(x_vals, rotation=45, ha='right', fontsize=7)
        ax.set_xlabel(x_label, fontsize=8)
        ax.set_ylabel(y_label, fontsize=8)
        ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
        ax.grid(True, axis='y', alpha=0.5, zorder=0)
        plt.tight_layout()
        fig.savefig(os.path.join(OUTPUT_DIR, f'{chart_id}.png'), dpi=200, bbox_inches='tight')
        plt.close(fig)

    elif chart_type == 'dual_line':
        fig, ax = plt.subplots(figsize=(8, 3.5))
        for series in data['series']:
            ax.plot(data['x'], series['y'], color=series['color'],
                   linewidth=1.5, label=series['label'], marker='o', markersize=4, zorder=3)
        ax.set_xlabel(x_label, fontsize=8)
        ax.set_ylabel(y_label, fontsize=8)
        ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
        ax.legend(fontsize=8, framealpha=0.9)
        ax.grid(True, alpha=0.5, zorder=0)
        plt.tight_layout()
        fig.savefig(os.path.join(OUTPUT_DIR, f'{chart_id}.png'), dpi=200, bbox_inches='tight')
        plt.close(fig)

    elif chart_type == 'grouped_bar':
        fig, ax = plt.subplots(figsize=(8, 3.5))
        n_groups = len(data['x'])
        n_series = len(data['series'])
        bar_width = 0.8 / n_series
        for i, series in enumerate(data['series']):
            positions = [x + i * bar_width for x in range(n_groups)]
            ax.bar(positions, series['y'], bar_width, label=series['label'],
                  color=series['color'], zorder=3)
        ax.set_xticks([x + bar_width * (n_series - 1) / 2 for x in range(n_groups)])
        ax.set_xticklabels(data['x'], rotation=45, ha='right', fontsize=7)
        ax.set_xlabel(x_label, fontsize=8)
        ax.set_ylabel(y_label, fontsize=8)
        ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
        ax.legend(fontsize=8)
        ax.grid(True, axis='y', alpha=0.5, zorder=0)
        plt.tight_layout()
        fig.savefig(os.path.join(OUTPUT_DIR, f'{chart_id}.png'), dpi=200, bbox_inches='tight')
        plt.close(fig)

    print(f'Generated: {chart_id}.png')

print(f'\nAll charts saved to {OUTPUT_DIR}')
