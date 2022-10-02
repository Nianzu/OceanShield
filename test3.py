import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
africa = world[world.continent == 'Africa']
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

ax = africa.plot()
cities.plot(ax=ax, color='r')

minx, miny, maxx, maxy = africa.total_bounds
ax.set_xlim(minx, maxx)
ax.set_ylim(miny, maxy)

