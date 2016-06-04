# ploty_websocket_example
Use Ploty(js) and Websockets to animate graphs  and show realtime data

I used [pywebsocket](https://github.com/google/pywebsocket) in order to test this

I've created a handler named send_graph which sends a moving sine-wave graph to the websocket

In order to make it work you need to install the pywebsocket
Then you copy the send_graph_wsh.py file into pywebsocket/example/

Usage : 
```
cd pywebsocket/mod_pywebsocket
python standalone.py -p 9998 -w ../example/
```
Then open the `plot_graphs_from_websocket.html` in your browser


