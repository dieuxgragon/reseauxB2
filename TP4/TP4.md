# I. Simple bs program

## 1. First steps

### [bs_serveur.py](./bs_server_I1.py)   
### [ bs_client.py](./bs_client_I1.py)

CLIENT
```py
[enzo@bsclientI1]$ sudo dnf install python
[enzo@bsclientI1 TP4]$ python bs_client_I1.py
Le serveur a répondu b'Hi, Mate'
```
SERVEUR
```py
[enzo@bsserveurI1]$ sudo dnf install python
[enzo@bsserverI1 TP4]$ sudo firewall-cmd --add-port=13337/tcp --permanent
[enzo@bsserverI1 TP4]$ sudo firewall-cmd --reload
[enzo@bsserverI1 TP4]$ python bs_server_I1.py
Connected by ('10.1.1.1', 55832)
Données reçues du client : b'Meooooo !'
Error Occured.
[enzo@bsserverI1 TP4]$ ss -plant |grep 13337
TIME-WAIT 0      0          10.1.1.10:13337     10.1.1.1:55832
``` 

# II. You say dev I say good practices

## 1. Args


