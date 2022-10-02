import folium
from IPython.display import display
m=folium.Map(location=[28.644800, 77.216721])
m.save("map.html")
display(m)