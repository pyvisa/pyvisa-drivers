# Keysight PNA Driver

The Keysight PNA driver is taken from scikit-rf<br/>
http://scikit-rf-web.readthedocs.io/

## usage:

```python
from drivers import keysight_pna

pna = keysight_pna.Driver(address=16, interface="GPIB")
# Or use TCPIP
pna = keysight_pna.Driver(address="127.0.0.1", port="5075", interface="SOCKET")

pna.idn  # show the id string of the VNA
ntwk1 = pna.get_oneport(port=2)  # return a skrf.Network object of S22
ntwk2 = pna.get_twoport(ports=(1,2))  # return a skrf.Netork object of (S11, S21, S12, S22)
```

