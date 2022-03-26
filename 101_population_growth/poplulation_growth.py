current_pop = 380123456
born_rate = 6
die_rate = 12
immigrate_rate = 40

#number of people born a year
min_born = 60 / 6
hour_born = min_born * 60
day_born = hour_born * 24
year_born = day_born * 365
# print(year_born)

#number of people die a year
min_die = 60 / 12
hour_die = min_die * 60
day_die = hour_die * 24
year_die = day_die * 365
# print(year_die)

#number of poeple immigrates a year
min_immigrate = 60 / 40
hour_immigrate = min_immigrate * 60
day_immigrate = hour_immigrate * 24
year_immigrate = day_immigrate * 365
# print(year_immigrate)

#In 3 years, the total population count for this country
pop_in_3years = current_pop + (3 * year_born) - (3 * year_die) - (3 * year_immigrate)
print(pop_in_3years)

