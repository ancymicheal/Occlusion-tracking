import matplotlib.pyplot as plt
import numpy as np

# Dataset-specific metrics
datasets = {
    'UAV123': {
        'models': ['SORT', 'DSORT', 'MCMOT', 'Videotrack', 'TransRMOT', 'UCMCTrack', 'Proposed'],
        'mota': [72.63, 72.79, 92.76, 92.84, 91.42, 93.69, 94.53],
        'ids': [3568, 3483, 1202, 1183, 1256, 1102, 906]
    },
    'VisDrone': {
        'models': ['GOG', 'IOUT', 'UAVMOT', 'MCMOT', 'TransRMOT', 'Videotrack', 'UCMCTrack', 'Proposed'],
        'mota': [28.7, 28.1, 36.1, 38.2, 36.4, 38.8, 39.0, 39.6],
        'ids': [1387, 2393, 2775, 2520, 2678, 2331, 2195, 1989]
    },
    'UAVDT': {
        'models': ['SORT', 'DSORT', 'UAVMOT', 'MCMOT', 'TransRMOT', 'Videotrack', 'UCMCTrack', 'Proposed'],
        'mota': [39.0, 40.7, 46.4, 48.8, 48.7, 47.9, 49.1, 49.3],
        'ids': [2350, 2061, 456, 320, 323, 358, 299, 291]
    }
}

# Set up a 2x3 grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 8))
#fig.suptitle("MOTA and IDSwitch Comparison Across UAV Datasets", fontsize=18)

# Loop through datasets
for idx, (dataset, data) in enumerate(datasets.items()):
    x = np.arange(len(data['models']))

    # MOTA subplot (top row)
    ax_mota = axes[0, idx]
    bars_mota = ax_mota.bar(x, data['mota'], color='tab:blue')
    ax_mota.set_title(f"{dataset} - MOTA", fontsize=11)
    ax_mota.set_ylim(0, 105)
    ax_mota.set_xticks(x)
    ax_mota.set_xticklabels(data['models'], rotation=30, ha='right', fontsize=7)  # smaller font size
    ax_mota.set_ylabel('MOTA (%)' if idx == 0 else '')
    ax_mota.grid(axis='y', linestyle='--', alpha=0.5)

    for j, bar in enumerate(bars_mota):
        ax_mota.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                     f"{data['mota'][j]:.1f}", ha='center', fontsize=7)

    # IDSwitch subplot (bottom row)
    ax_ids = axes[1, idx]
    bars_ids = ax_ids.bar(x, data['ids'], color='tab:orange')
    ax_ids.set_title(f"{dataset} - IDSwitch", fontsize=11)
    ax_ids.set_ylim(0, max(data['ids']) + 500)
    ax_ids.set_xticks(x)
    ax_ids.set_xticklabels(data['models'], rotation=30, ha='right', fontsize=7)  # smaller font size
    ax_ids.set_ylabel('ID Switches' if idx == 0 else '')
    ax_ids.grid(axis='y', linestyle='--', alpha=0.5)

    for j, bar in enumerate(bars_ids):
        ax_ids.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 30,
                    f"{data['ids'][j]}", ha='center', fontsize=7)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.show()
