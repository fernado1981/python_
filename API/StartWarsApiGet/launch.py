from API.StartWarsApiGet.data import data
from API.StartWarsApiGet.getAPiStartWars import getApiStartWars


class launch(data):
    #values ['people', 'planets', 'films', 'species', 'vehicles', 'starships']
    val = data.dataApiGetSW['value'][5]
    p = getApiStartWars()
    p.getData()
    p.showData(val)
