from pybaseball import team_pitching
from pybaseball import statcast_pitcher
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("TkAgg")

# First grab data
skenes_stats = statcast_pitcher('2025-03-18', '2025-09-28', 694973)

# Custom color palette
pitch_colors = ['#FF007D', '#F79E70', '#FE6100',
                '#67E18D', '#1BB999', '#98165D', '#3025CE']

# Make a scatterplot
sns.scatterplot(x=skenes_stats["release_speed"],
                y=skenes_stats["release_spin_rate"],
                hue=skenes_stats["pitch_type"],
                legend=False,
                palette= pitch_colors)

# Title
plt.title("Paul Skenes RPM vs Velocity 2025")

# Plot
plt.show()

# Looking to add a legend to the right side for labeling but can't figure it out right now
