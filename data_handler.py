import requests

#vessel historical track - PS06
api_key1 = ""

#vessel particulars: get api key from: VD02
api_key2 = ""
    

#raw data you have
latitude = 0 #range -90, 90
longitude = 0 #range -180, 180
timestamp = 0 #UNT time format

#search parameters
radius = .25 #should be less than 1 (per API parameters)

text = [["477004700","9484405","0","179","-122.4997","25.40754","121","121","2022-10-01T07:11:35","684943"],["477004700","9484405","0","180","-122.4883","25.40134","120","120","2022-10-01T07:13:59","684943"],["477004700","9484405","0","180","-122.4775","25.39549","120","120","2022-10-01T07:16:17","684943"],["477004700","9484405","0","181","-122.4626","25.38744","121","120","2022-10-01T07:19:24","684943"],["477004700","9484405","0","180","-122.4518","25.38156","120","120","2022-10-01T07:21:40","684943"],["477004700","9484405","0","179","-122.4389","25.3746","120","119","2022-10-01T07:24:23","684943"],["477004700","9484405","0","180","-122.4261","25.36774","120","121","2022-10-01T07:26:58","684943"],["477004700","9484405","0","180","-122.4154","25.362","120","121","2022-10-01T07:29:17","684943"],["477004700","9484405","0","179","-122.4048","25.3562","120","119","2022-10-01T07:31:34","684943"],["477004700","9484405","0","179","-122.394","25.35037","121","120","2022-10-01T07:33:52","684943"],["477004700","9484405","0","179","-122.3831","25.34451","120","120","2022-10-01T07:36:11","684943"],["477004700","9484405","0","178","-122.3728","25.33897","120","120","2022-10-01T07:38:22","684943"],["477004700","9484405","0","179","-122.3624","25.3333","121","120","2022-10-01T07:40:35","684943"],["477004700","9484405","0","178","-122.3516","25.3274","120","120","2022-10-01T07:42:53","684943"],["477004700","9484405","0","178","-122.3404","25.32131","121","120","2022-10-01T07:45:16","684943"],["477004700","9484405","0","178","-122.3296","25.31534","121","120","2022-10-01T07:47:34","684943"],["477004700","9484405","0","178","-122.3193","25.30968","121","121","2022-10-01T07:49:46","684943"],["477004700","9484405","0","179","-122.3085","25.30373","120","120","2022-10-01T07:52:05","684943"],["477004700","9484405","0","180","-122.2977","25.29766","121","120","2022-10-01T07:54:23","684943"],["477004700","9484405","0","180","-122.2869","25.29165","122","120","2022-10-01T07:56:40","684943"],["477004700","9484405","0","180","-122.2762","25.28563","121","120","2022-10-01T07:58:58","684943"],["477004700","9484405","0","178","-122.2649","25.27932","121","120","2022-10-01T08:01:23","684943"],["477004700","9484405","0","178","-122.2529","25.27263","121","120","2022-10-01T08:03:58","684943"],["477004700","9484405","0","178","-122.2421","25.2666","122","120","2022-10-01T08:06:17","684943"],["477004700","9484405","0","179","-122.2314","25.26063","122","120","2022-10-01T08:08:35","684943"],["477004700","9484405","0","179","-122.2202","25.25445","121","120","2022-10-01T08:10:58","684943"],["477004700","9484405","0","178","-122.2089","25.24819","121","120","2022-10-01T08:13:23","684943"],["477004700","9484405","0","178","-122.1982","25.24224","122","120","2022-10-01T08:15:40","684943"],["477004700","9484405","0","178","-122.182","25.23323","121","120","2022-10-01T08:19:10","684943"],["477004700","9484405","0","177","-122.1709","25.22697","121","120","2022-10-01T08:21:34","684943"],["477004700","9484405","0","177","-122.1606","25.22127","121","120","2022-10-01T08:23:47","684943"],["477004700","9484405","0","179","-122.1495","25.21499","122","120","2022-10-01T08:26:11","684943"],["477004700","9484405","0","179","-122.1355","25.20721","121","120","2022-10-01T08:29:11","684943"],["477004700","9484405","0","177","-122.1234","25.20053","121","120","2022-10-01T08:31:47","684943"],["477004700","9484405","0","177","-122.1003","25.18775","120","120","2022-10-01T08:36:46","684943"],["477004700","9484405","0","177","-122.0887","25.18136","120","120","2022-10-01T08:39:16","684943"],["477004700","9484405","0","177","-122.078","25.17546","121","120","2022-10-01T08:41:34","684943"],["477004700","9484405","0","177","-122.0549","25.16273","121","120","2022-10-01T08:46:34","684943"],["477004700","9484405","0","178","-122.0452","25.15731","121","120","2022-10-01T08:48:40","684943"],["477004700","9484405","0","179","-122.0348","25.15154","121","120","2022-10-01T08:50:53","684943"],["477004700","9484405","0","179","-122.024","25.14557","121","119","2022-10-01T08:53:11","684943"],["477004700","9484405","0","179","-122.0129","25.13944","121","120","2022-10-01T08:55:34","684943"],["477004700","9484405","0","179","-122.002","25.13347","120","120","2022-10-01T08:57:53","684943"]]
ship_info = [["477004700","9484405","COSCO VENICE","","2013","32.25","49973","","VRME4","HK","11","261.1","150 t\/day at 24.30 kn","","24.5","","CHINA COSCO HOLDINGS CO CCHC","COSCO SHIPPING LINES CO LTD","CONTAINER SHIP"]]

#returns name of company that owns ship
def parse_ID(info, param):
    
    data = info[0][param]
    return(data)

#returns list of Boat IMOs in string form
def get_boat_IDs(text, key):
    IDs = []
    KEY = key
    locs = []
    for boat in text:
        if boat not in IDs:
            IDs.append(boat)
            locs.append([parse_ID(text[0][0], 5), parse_ID(text_ID(text[0][0]), 4)])
        else:
            locs.append([parse_ID(text[0][len(text[0])], 5), parse_ID(text_ID(text[0][len(text[0])]), 4)])
    print(IDs)
    
    '''
    web = str.format('https://services.marinetraffic.com/api/vesselmasterdata/{0}?v=3&imo={1}&interval=minutes&protocol=json&page=1'.format(KEY, IDs))
    req = requests.get(web)
    response = req.text
    '''
    response = ['9484405']
    return(parse_ID(response), locs)
    
def get_boat_frequency (ID_number):
    return(number_of_times_boat_in_search_area)

def get_boats_in_area(latitude, longitude, timestamp):
    #set box for looking for boats
    MAXLAT = latitude + radius
    MINLAT = latitude - radius
    MAXLON = longitude + radius
    MINLON = longitude - radius
    
    final = []

    '''
    web1 = str.format('https://services.marinetraffic.com/api/exportvesseltrack/{4}%20?v=3&days=1&MINLAT={0}&MAXLAT={1}&MINLON={2}&MAXLON={3}&msgtype=simple&protocol=json'.format(MINLAT, MAXLAT, MINLON, MAXLON, api_key1))
    req = requests.get(web1)
    response = req.text
    print(response)
    '''
    
    # list_of_IDs = get_boat_IDs(response, api_key2)[0]
    
    # for e in list_of_IDs:
    #     temp = []
        
    #     #this line adds boat ID to temporary list
    #     temp[0] =  list_of_IDs[list_of_IDs.index(e)]
        
    #     #this line adds the company name to the temporary list
    #     temp[1] = pasre_ID(ship_info, 16)
        
    #     #this line gets first and last instance of valid boat locations 
    #     #in search radius to track boat trajectory around trash
    #     temp[2] = get_boat_IDs(response, api_key2)[1]
        
        
    #     #this line adds how often the boat has passed through location in past year
    #     #with lots of data points, one could scale this to see how likely a company was to leave the trash there
    #     temp[3] = get_boat_frequency(boat_ID)
        
    #     final.append(temp)
    # print(final)
    return (final)
    
def request_handler(request):
    lat = request[0]
    lon = request[1]
    timestamp = request[2]
    x = get_boats_in_area(lat, lon, timestamp)
    return (x)

def get_boat_tracks(boats):
    ships = [[[-122.4883,25.40134],
            [-122.4775,25.39549],
            [-122.4997,25.40754],
            [-122.4626,25.38744],
            [-122.4518,25.38156],
            [-122.4389,25.3746],
            [-122.4261,25.36774],
            [-122.4154,25.362],
            [-122.4048,25.3562],
            [-122.394,25.35037],
            [-122.3831,25.34451],
            [-122.3728,25.33897],
            [-122.3624,25.3333],
            [-122.3516,25.3274],
            [-122.3404,25.32131],
            [-122.3296,25.31534],
            [-122.3193,25.30968],
            [-122.3085,25.30373],
            [-122.2977,25.29766],
            [-122.2869,25.29165],
            [-122.2762,25.28563],
            [-122.2649,25.27932],
            [-122.2529,25.27263],
            [-122.2421,25.2666],
            [-122.2314,25.26063],
            [-122.2202,25.25445],
            [-122.2089,25.24819],
            [-122.1982,25.24224],
            [-122.182,25.23323],
            [-122.1709,25.22697],
            [-122.1606,25.22127],
            [-122.1495,25.21499],
            [-122.1355,25.20721],
            [-122.1234,25.20053],
            [-122.1003,25.18775],
            [-122.0887,25.18136],
            [-122.078,25.17546],
            [-122.0549,25.16273],
            [-122.0452,25.15731],
            [-122.0348,25.15154],
            [-122.024,25.14557],
            [-122.0129,25.13944],
            [-122.002,25.13347]]]
    newShips = [[ [0.0]*2 for i in range(43)]]
    for i in range(0,len(ships[0])):
        newShips[0][i][1] = ships[0][i][0]
        newShips[0][i][0] = ships[0][i][1]
    ships = newShips
    return newShips
    
#parse_ID(ship_info,)    
#get_boat_IDs(text, api_key2)
#get_boats_in_area(latitude, longitude, 0 )
