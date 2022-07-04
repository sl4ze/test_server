import socket


def decimal_to_binary(n: int) -> str:                        
    # int to binary str and removing the prefix(0b)
    return bin(n).replace("0b", "")

def construct_message(protocol_version, mes_id, station_id, longitude, latitude):
    #payload and headers generator
    protocol_version = decimal_to_binary(protocol_version)
    protocol_version = '0' * (8 - len(protocol_version)) + protocol_version
    mes_id = decimal_to_binary(mes_id)
    mes_id = '0' * (8 - len(mes_id)) + mes_id
    station_id = decimal_to_binary(station_id)
    station_id = '0' * (16 - len(station_id)) + station_id
    longitude = decimal_to_binary(longitude)
    longitude = '0' * (32 - len(longitude)) + longitude
    latitude = decimal_to_binary(latitude)
    latitude = '0' * (32 - len(latitude)) + latitude
    message = '00000010' + mes_id + station_id + longitude + latitude
    return(message)


def send_message(protocol_version, mes_id, station_id, longitude, latitude):
    send_data = construct_message(protocol_version, mes_id, station_id, longitude, latitude)
    # Create socket for server
    try:
        # my be open only once for whole test suite
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        s.sendto(send_data.encode('utf-8'), (ip, port))
        data, _ = s.recvfrom(7082)
        s.close()           # close the socket
    except Exception as e:
        s.close()
        raise e
    s.close()
    return(data.decode('utf-8'))


ip = '127.0.0.1'                                     
port = 7082
