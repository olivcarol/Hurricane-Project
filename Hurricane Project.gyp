# GIVEN DATA:

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# Creating a damage function where the recorded data is converted to float values and the missing data is retained as "Damages not recorded":
# (B stands for billions (1000000000) and M stands for millions (1000000))
def convert_damages(damages):
    conversion ={"M": 1000000, "B": 1000000000}
    updated_damages = []
    
    for num in damages:
        if num == "Damages not recorded":
            updated_damages.append(num)
        if num[-1] == "M":
            updated_damages.append(float(num.strip("M")) * conversion["M"])
        if num[-1] == "B":
            updated_damages.append(float(num.strip("B")) * conversion["B"])
    return updated_damages

updated_damages = convert_damages(damages)
print(updated_damages)

# Building a hurricane dictionary function (keys are the names of the hurricanes and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year, Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane:
def new_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes = {}
    num_hurricanes = len(names)

    for x in range(num_hurricanes):
        hurricanes[names[x]] = {"Name": names[x], "Month": months[x], "Year": years[x], "Max Sustained Winds": max_sustained_winds[x], "Areas affected": areas_affected[x], "Damage": updated_damages[x], "Deaths": deaths[x]}
    return hurricanes

hurricanes = new_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)

# Organizing the hurricanes by year:
#OPTION 1:
def updated_dict(names, months, max_sustained_winds, areas_affected, updated_damages, deaths):
    canes = {}
    num_canes = len(names)

    for y in range(num_canes):
        canes[years[y]] = {"Name": names[y], "Month": months[y], "Max Sustained Winds": max_sustained_winds[y], "Areas affected": areas_affected[y], "Damage": updated_damages[y], "Deaths": deaths[y]}
    return canes

canes = updated_dict(names, months, max_sustained_winds, areas_affected, updated_damages, deaths)
print(canes)

#OPTION 2:
years_dict = []

for n, m, y, ma, a, da, z in zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    dict = {y: {'Name': n, 'Month':m, 'Year': y, 'Max_sustained_wind': ma, 'Area_affected': a, 'Damage': da, 'Deaths': z}}
    years_dict.append(dict)

print(years_dict)

# Counting affected areas:
count_affected_areas = {}

for k in areas_affected:
    for b in k:
        if b not in count_affected_areas:
            count_affected_areas[b] = 1
        else:
            count_affected_areas[b] += 1

print(count_affected_areas)

# Finding the most affected areas (by the most hurricanes, and how often it was hit):
def most_affected(count_affected_areas):
    most_area = ""
    most_count = 0

    for area in count_affected_areas:
        if count_affected_areas[area] > most_count:
            most_area = area
            most_count = count_affected_areas[area]
    return most_area, most_count

most_area, most_count = most_affected(count_affected_areas)
print(most_area, most_count)

# Finding the greatest number of deaths:
def most_deaths(hurricanes):
    hurricane_most_deaths = ""
    number_of_deaths = 0

    for canes in hurricanes:
        if hurricanes[canes]["Deaths"] > number_of_deaths:
            hurricane_most_deaths = canes
            number_of_deaths = hurricanes[canes]["Deaths"]
    return number_of_deaths, hurricane_most_deaths

number_of_deaths, hurricane_most_deaths = most_deaths(hurricanes)
print(number_of_deaths)

# Categorizing the hurricanes by mortality (scale given as below):
def mortality(hurricanes):
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}

    for canes in hurricanes:
        rate = 0
        deaths = hurricanes[canes]["Deaths"]

        if deaths < 100:
            rate = 0
        elif deaths >= 100 and deaths < 500:
            rate = 1
        elif deaths >= 500 and deaths < 1000:
            rate = 2
        elif deaths >= 1000 and deaths < 10000:
            rate = 3
        else:
            rate = 4

        if rate not in hurricanes_by_mortality:
            hurricanes_by_mortality[rate] = hurricanes[canes]
        else:
            hurricanes_by_mortality[rate].append(hurricanes[canes])
    return hurricanes_by_mortality

hurricanes_by_mortality = mortality(hurricanes)
print(hurricanes_by_mortality)

# Finding the hurricane that caused the greatest damage:
def greatest_damage(hurricanes):
    most_damage = ""
    cost = 0

    for hurricane in hurricanes:
        if hurricanes[hurricane]["Damage"] == "Damages not recorded":
            continue
        if hurricanes[hurricane]["Damage"] > cost:
            most_damage = hurricanes[hurricane]["Name"]
            cost = hurricanes[hurricane]["Damage"]
    return most_damage, cost

most_damage, cost = greatest_damage(hurricanes)
print(most_damage, cost)

# Catgeorizing by damage:
def damage_scale(hurricanes):
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: []}

    for canes in hurricanes:
        rate = 0
        damages = hurricanes[canes]["Damage"]

        if damages == "Damages not recorded":
            continue
        elif damages < 100000000:
            rate = 0
        elif damages >= 100000000 and damages < 1000000000:
            rate = 1
        elif damages >= 1000000000 and damages < 10000000000:
            rate = 2
        elif damages >= 10000000000 and damages < 50000000000:
            rate = 3
        else:
            rate = 4

        if rate not in hurricanes_by_damage:
            hurricanes_by_damage[rate] = hurricanes[canes]
        else:
            hurricanes_by_damage[rate].append(hurricanes[canes])
    return hurricanes_by_damage

hurricanes_by_damage = damage_scale(hurricanes)
print(hurricanes_by_damage)