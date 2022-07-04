import pytest
from utils import send_message 

#first byte match
#wrong protocol_version
@pytest.mark.parametrize('protocol_version, mes_id, station _id, latitude, longitude', 
[
    (1, 1, 432, 65432543, 54325423),
    (3, 1, 432, 65432543, 54325423), 
    (0, 1, 432, 65432543, 54325423)
    ]
)
def test_protocolVersion(protocol_version, mes_id, station_id, latitude, longitude):     
    assert send_message(protocol_version, mes_id, station_id, latitude, longitude)[16] == '0'       

#second byte match
#out of limit values message_id
@pytest.mark.parametrize('protocol_version, mes_id, station _id, latitude, longitude', 
[
    (2, -1, 432, 65432543, 54325423), 
    (2, 256, 432, 65432543, 54325423)
    ]
)
def test_messageID(protocol_version, mes_id, station_id, latitude, longitude):
    assert send_message(protocol_version, mes_id, station_id, latitude, longitude)[16] == '0'      


#3.1 bit match
# out of limit values station_id
@pytest.mark.parametrize('protocol_version, mes_id, station _id, latitude, longitude', 
[
    (2, 1, 0, 65432543, 54325423), 
    (2, 1, 65536, 65432543, 54325423)
    ]
)  
def test_stationID(protocol_version, mes_id, station_id, latitude, longitude):
    assert send_message(protocol_version, mes_id, station_id, latitude, longitude)[17] == '0'     


#3.3 bit match
# out of limit values latitude
@pytest.mark.parametrize('protocol_version, mes_id, station _id, latitude, longitude', 
[
    (2, 1, 432, 0, 54325423), 
    (2, 1, 432, 429321324967295, 54325423)
    ]
)  
def test_longitude(protocol_version, mes_id, station_id, latitude, longitude):
    assert send_message(protocol_version, mes_id, station_id, latitude, longitude)[19] =='0'    


#3.2 bit match
# out limit values longitude
@pytest.mark.parametrize('protocol_version, mes_id, station _id, loatitude, longitude',  
[
    (2, 1, 432, 65432543, 0), 
    (2, 1, 432, 65432543, 4212394967295)])
def test_latitude(protocol_version, mes_id, station_id, latitude, longitude):
    assert send_message(protocol_version, mes_id, station_id, latitude, longitude)[18] == '0'     

