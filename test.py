# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd

# Reading cvs file using pandas
df = pd.read_csv('cneos_fireball_data.csv', 
                 usecols=["Peak Brightness Date/Time (UT)", 
                 "Calculated Total Impact Energy (kt)", 
                 "Latitude (deg.)", "Longitude (deg.)"])
df = df.rename(columns={"Peak Brightness Date/Time (UT)": 
                        'Datetime',
                        "Calculated Total Impact Energy (kt)": 
                        'Impact Energy [kt]',
                        "Latitude (deg.)": 'Latitude',
                        "Longitude (deg.)": 'Longitude'})

# Showing raw data and data types
print(pd.DataFrame(df))
print('\n')
print(df.dtypes)
print('\n')

# Converting to a datetime datatype
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Applying +/- based on direction and converting to numeric datatype
for x in range(len(df['Longitude'])):
    if str(df.loc[x, 'Longitude'])[-1] == 'E':
        df.loc[x, 'Longitude'] = str(df.loc[x, 'Longitude'])[:-1]
    if str(df.loc[x, 'Longitude'])[-1] == 'W':
        df.loc[x, 'Longitude'] = \
            '-' + str(df.loc[x, 'Longitude'])[:-1]

for x in range(len(df['Latitude'])):
    if str(df.loc[x, 'Latitude'])[-1] == 'N':
        df.loc[x, 'Latitude'] = str(df.loc[x, 'Latitude'])[:-1]
    if str(df.loc[x, 'Latitude'])[-1] == 'S':
        df.loc[x, 'Latitude'] = \
            '-' + str(df.loc[x, 'Latitude'])[:-1]

df['Longitude'] = pd.to_numeric(df['Longitude'], errors='coerce')
df['Latitude'] = pd.to_numeric(df['Latitude'], errors='coerce')

# Converting to numeric datatype
threshold = 20
df = df[df['Impact Energy [kt]'] < threshold]
df['Impact Energy [kt]'] = pd.to_numeric(df['Impact Energy [kt]'], 
                                         errors='coerce')

                                         # Dropping the errors from data conversions and resetting index
df.dropna()
df = df.reset_index(drop=True)

# Showing cleaned data and data types
print(pd.DataFrame(df))
print('\n')
print(df.dtypes)
print('\n')



# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/zoom_inset_axes.html





# From GeoPandas, our world map data
worldmap = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Creating axes and plotting world map
fig, ax = plt.subplots(figsize=(12, 6))
worldmap.plot(color="lightgrey", ax=ax)

axins = ax.inset_axes([1, 0, 0.47, 0.47])
x1, x2, y1, y2 = -50, 50, -50, 50
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

ax.indicate_inset_zoom(axins, edgecolor="black")

# # Plotting our Impact Energy data with a color map
# x = df['Longitude']
# y = df['Latitude']
# z = df['Impact Energy [kt]']
# plt.scatter(x, y, s=20*z, c=z, alpha=0.6, vmin=0, vmax=threshold,
#             cmap='autumn')
# plt.colorbar(label='Impact Energy [kt]')

# # Creating axis limits and title
# plt.xlim([-180, 180])
# plt.ylim([-90, 90])

# first_year = df["Datetime"].min().strftime("%Y")
# last_year = df["Datetime"].max().strftime("%Y")
# plt.title("NASA: Fireballs Reported by Government Sensors\n" +     
#           str(first_year) + " - " + str(last_year))
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
plt.show()