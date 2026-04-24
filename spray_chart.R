library(dplyr)
library(ggplot2)

# Need to download the data set online. It downloads as savant_data. will be changing name to hoerner_2025

hoerner_2025 <- read.csv("C:/Users/hanke/Downloads/hoerner_2025.csv")

# There is a lot of data here. I will condense it
columns = c("pitch_type","pitch_name", "release_speed", "events", "bb_type", "hc_x", "hc_y",
            "hit_distance_sc", "launch_speed", "launch_angle", "release_pos_y",
            "bat_speed", "swing_length")

test = hoerner_2025[, columns]


# If we want a hit spread plot
p = ggplot(test, aes(x = -1*(hc_x), y = -1*(hc_y), color = events)) +
  geom_point(size = 0.75) +
  ggtitle("Nico Hoerner 2025 Spray Chart") +
  xlab("") + ylab("") +
  theme_classic()
p
