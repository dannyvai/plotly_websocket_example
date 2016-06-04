import numpy as np
import json
import time

_GOODBYE_MESSAGE = u'Goodbye'

x = np.arange(0,np.pi*10,0.1).tolist()
y = np.sin(x).tolist()
data_size = len(x)
counter = 0
graph_size = 100

samples = 0
tic = time.time()

def web_socket_do_extra_handshake(request):
    # This example handler accepts any request. See origin_check_wsh.py for how
    # to reject access from untrusted scripts based on origin value.

    pass  # Always accept.


def get_graph_data():

    global counter,data_size,graph_size,x,y
    global samples,tic

    #Calculate FPS
    samples += 1
    if (time.time() - tic) > 2:
        print "FPS is : ",samples /(time.time() - tic)
        samples = 0
        tic = time.time()
    
    counter += 1
    if counter > (data_size - graph_size):
        counter = 0

    graph_to_send = json.dumps({
        'x':x[counter:counter+graph_size],
        'y':y[counter:counter+graph_size]
    })
    return graph_to_send

def web_socket_transfer_data(request):
    while True:
        line = request.ws_stream.receive_message()
        if line is None:
            return
        if isinstance(line, unicode):
            request.ws_stream.send_message(get_graph_data(), binary=False)
            if line == _GOODBYE_MESSAGE:
                return
        else:
            request.ws_stream.send_message(get_graph_data(), binary=True)


# vi:sts=4 sw=4 et
