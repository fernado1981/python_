from API.getApi.data import data
from API.getApi.getAPiStartWars import getApiStartWars


class launch(data):
    val = data.dataApiGetSW['value'][0]
    p = getApiStartWars()
    p.getData()
    p.showData(val)
