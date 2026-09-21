"""Per-consumer cost across the socialized-to-individualized range, with the line of
stability marked.

The simulation stays in Julia (JuMP/HiGHS); this reads the plot-ready CSV/JSON exported by
scripts/FigureScripts/socializedVsIndividualizedCosts.jl (see data_io.load_mixed_allocation).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt

import style


def plot_socialized_vs_individualized(mixed_allocation_cost_per_mwh_df, clients, negative_excess_step=None):
    final_costs = [mixed_allocation_cost_per_mwh_df[c].iloc[-1] for c in clients]
    cost_order = sorted(range(len(clients)), key=lambda i: final_costs[i])  # low to high
    colors = style.four_color_gradient(len(clients), cost_order)

    fig, ax = plt.subplots()
    for i, c in enumerate(clients):
        ax.plot(
            mixed_allocation_cost_per_mwh_df["step"], mixed_allocation_cost_per_mwh_df[c],
            color=colors[i], linewidth=1,
            label="Individual consumer cost" if i == 0 else None,
        )
    if negative_excess_step is not None:
        ax.axvline(
            negative_excess_step, color="red", linestyle="--", linewidth=2,
            label="Line of stability",
        )
    ax.set_xlabel("Individualization grade")
    ax.set_ylabel("Imbalance cost (EUR/MWh)")
    ax.legend(fontsize=8)
    fig.tight_layout()

    return fig
