import pybaseball
from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher

# First let us gather the player id's of every Cubs pitcher in 2025 who remained on the team through the postseason, ranked by innings pitch (minimum 20)
playerid_lookup('boyd', 'matt')
playerid_lookup('rea', 'colin')
playerid_lookup('imanaga', 'shota')
playerid_lookup('taillon', 'jameson')
playerid_lookup('horton', 'cade')
playerid_lookup('brown', 'ben')
playerid_lookup('keller', 'brad')
playerid_lookup('thielbar', 'caleb')
playerid_lookup('palencia', 'daniel')
playerid_lookup('pomeranz', 'drew')
playerid_lookup('assad', 'javier')
playerid_lookup('hodge', 'porter')
playerid_lookup('steele', 'justin')
playerid_lookup('kittredge', 'andrew')

# Next let us create a dataset for all of our pitchers
# Matthew Boyd player id = 571510
boyd_stats = statcast_pitcher('2025-03-18', '2025-09-28', 571510)
# Colin Rea player id = 607067
rea_stats = statcast_pitcher('2025-03-18', '2025-09-28', 607067)
# Shota Imanaga player id = 684007
imanaga_stats = statcast_pitcher('2025-03-18', '2025-09-28', 684007)
# Jameson Taillon player id = 592791
taillon_stats = statcast_pitcher('2025-03-18', '2025-09-28', 592791)
# Cade Horton player id = 690990
horton_stats = statcast_pitcher('2025-03-18', '2025-09-28', 690990)
# Ben Brown player id = 676962
brown_stats = statcast_pitcher('2025-03-18', '2025-09-28', 676962)
# Brad Keller player id = 641745
keller_stats = statcast_pitcher('2025-03-18', '2025-09-28', 641745)
# Caleb Thielbar player id = 573204
thielbar_stats = statcast_pitcher('2025-03-18', '2025-09-28', 573204)
# Daniel Palencia player id = 694037
palencia_stats = statcast_pitcher('2025-03-18', '2025-09-28', 694037)
# Drew Pomeranz player id = 519141
pomeranz_stats = statcast_pitcher('2025-03-18', '2025-09-28', 519141)
# Javier Assad player id = 665871
assad_stats = statcast_pitcher('2025-03-18', '2025-09-28', 665871)
# Porter Hodge player id = 687863
hodge_stats = statcast_pitcher('2025-03-18', '2025-09-28', 687863)
# Justin Steele player id = 657006
steele_stats = statcast_pitcher('2025-03-18', '2025-09-28', 657006)
# Andrew Kittredge player id = 552640
kittredge_stats = statcast_pitcher('2025-03-18', '2025-09-28', 552640)
