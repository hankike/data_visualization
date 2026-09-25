from pybaseball import playerid_lookup
from pybaseball import statcast_batter
import seaborn as sns
import matplotlib.pyplot as plt

# First we will look up a batter. Here I use Nico Hoener as he had the highest batting average on the Cubs last year
playerid_lookup('hoerner', 'nico')
hoener_stats = statcast_batter('2025-03-18', '2025-09-28', 663538)

# First I will flip the hc_x and hc_y values to make the plots look more familiar
hoener_stats.hc_x = hoener_stats.hc_x*-1
hoener_stats.hc_y = hoener_stats.hc_y*-1

# Spray chart using events
# First I will make a palette
event_pal = ['#F60000', '#F60000', '#3783FF', '#3783FF', '#F60000',
             '#3783FF', '#F60000', '#3783FF', '#3783FF', '#F60000',
             '#F60000', '#3783FF', '#F60000', '#F60000', '#F60000',
             '#F60000']

# Next the spray chart
sns.scatterplot(x=hoener_stats['hc_x'],
                y=hoener_stats['hc_y'],
                hue=hoener_stats['events'],
                legend=False,
                palette=event_pal)

# Using hc_x and hc_y we can find which pitches Hoener hit where
sns.scatterplot(x=hoener_stats['hc_x'],
                y=hoener_stats['hc_y'],
                hue=hoener_stats['pitch_type'],
                legend=False)
