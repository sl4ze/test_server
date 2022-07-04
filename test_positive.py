import pytest
import init 

#first byte match
def test_protocolVersion():     
    assert init.send_message(2, 1, 432, 65432543, 54325423)[0:8] == '00000010'       

#second byte match
# limit values message_id
@pytest.mark.parametrize('protocol_version, mes_id, station _id, latitude, longitude', [(2, 0, 432, 65432543, 54325423), (2, 1, 432, 65432543, 54325423), (2, 255, 432, 65432543, 54325423)])  
def test_messageID(protocol_version, mes_id, station_id, latitude, longitude):
    assert init.send_message(protocol_version, mes_id, station_id, latitude, longitude)[8:16] == mes_id       


#3.0 bit match
def test_status():
    assert init.send_message(2, 1, 432, 65432543, 54325423)[16] == '1'   

#3.1 bit match
# limit values station_id
@pytest.mark.parametrize('protocol_version, mes_id, station _id, latitude, longitude', [(2, 1, 0, 65432543, 54325423), (2, 1, 1, 65432543, 54325423), (2, 1, 65535, 65432543, 54325423)])  
def test_stationID(protocol_version, mes_id, station_id, latitude, longitude):
    assert init.send_message(protocol_version, mes_id, station_id, latitude, longitude)[17] == '1'     


#3.3 bit match
# limit values latitude
@pytest.mark.parametrize('protocol_version, mes_id, station _id, latitude, longitude', [(2, 1, 432, 0, 54325423), (2, 1, 432, 1, 54325423), (2, 1, 432, 4294967295, 54325423)])  
def test_longitude(protocol_version, mes_id, station_id, latitude, longitude):
    assert init.send_message(protocol_version, mes_id, station_id, latitude, longitude)[19] =='1'    


#3.2 bit match
# limit values longitude
@pytest.mark.parametrize('protocol_version, mes_id, station _id, loatitude, longitude',  [(2, 1, 432, 65432543, 0), (2, 1, 432, 65432543, 1), (2, 1, 432, 65432543, 4294967295)])
def test_latitude(protocol_version, mes_id, station_id, latitude, longitude):
    assert init.send_message(protocol_version, mes_id, station_id, latitude, longitude)[18] == '1'     

