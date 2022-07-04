import socket


def construct_message(protocol_version, mes_id, station_id, longitude, latitude):
    #payload and headers generator
    protocol_version =  '{0:07b}'.format(protocol_version)
    mes_id =  '{0:07b}'.format(mes_id)
    station_id =  '{0:017b}'.format(station_id)
    longitude =  '{0:031b}'.format(longitude)
    latitude =  '{0:031b}'.format(latitude)
    message = protocol_version + mes_id + station_id + longitude + latitude
    return(message)


def send_message(protocol_version, mes_id, station_id, longitude, latitude):
    send_data = construct_message(protocol_version, mes_id, station_id, longitude, latitude)
    # Create socket for server
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    try:
        s.sendto(send_data.encode('utf-8'), ('127.0.0.1', 7082))
        data, _ = s.recvfrom(7082) # test bits or bytes -> change 7082 to minimum power of 2
    except Exception as e:
        s.close()
        raise e
    s.close()
    return(data.decode('utf-8'))