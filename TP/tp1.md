# _I. Basics_
## *Carte réseau WiFi*

### Determiner

```ruby
C:\Users\enzon>ipconfig /all
Adresse physique . . . . . . . . . . . : 30-03-C8-E7-7C-25
```

```ruby
C:\Users\enzon>ipconfig /all
Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.186
```

```ruby
C:\Users\enzon>ipconfig /all
Masque de sous-réseau. . . . . . . . . : 255.255.240.0
255.255.240.0 /20
```
### Déso pas déso

```ruby
C:\Users\enzon>ipconfig /all
10.33.79.0
10.33.79.255
4094
```

### Hostname

```ruby
C:\Users\enzon>hostname
LAPTOP-ADTST2V5
```
### Passerelle du réseau
```ruby
C:\Users\enzon>ipconfig /all
Passerelle par défaut. . . . . . . . . : 10.33.79.254

C:\Users\enzon>arp -a
10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
```

### Serveur DHCP et DNS
```ruby
C:\Users\enzon>ipconfig /all
Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254

C:\Users\enzon>ipconfig /all
Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
```

### Table de routage
```ruby
Table de routage -4
IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.186     40

```

### host
```ruby
# localhost name resolution is handled within DNS itself.
#       127.0.0.1       localhost
#       ::1             localhost

1.1.1.1 b2.hello.vous
PS C:\Windows\System32\drivers\etc> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=10 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=13 ms TTL=57

```

```ruby
PS C:\Users\enzon> nslookup youtube.com
RéponseNom :    youtube.com
Addresses:  2a00:1450:4007:80c::200e
          172.217.20.174
          
PS C:\Users\enzon> netstat -n
TCP    10.33.76.186:54008     172.217.20.174:443     TIME_WAIT
```

### Requêtes DNS
```ruby
PS C:\Users\enzon> nslookup www.ynov.com
Nom :    www.ynov.com
Addresses:  2606:4700:20::ac43:4ae2
          2606:4700:20::681a:be9
          2606:4700:20::681a:ae9
          104.26.11.233
          104.26.10.233
          172.67.74.226

PS C:\Users\enzon> nslookup 174.43.238.89
Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```
### hop hop hop
```ruby
PS C:\Users\enzon> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [172.67.74.226]
avec un maximum de 30 sauts :

  1     1 ms     2 ms     5 ms  10.33.79.254
  2     5 ms     4 ms     3 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     3 ms     3 ms     2 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     3 ms     2 ms     3 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    13 ms    11 ms    10 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  6    11 ms    10 ms    10 ms  12.148.6.194.rev.sfr.net [194.6.148.12]
  7    13 ms    11 ms    10 ms  141.101.67.48
  8    14 ms    13 ms    12 ms  172.71.124.4
  9    12 ms    12 ms    12 ms  172.67.74.226
```

### IP publique
```ruby
195.7.117.146
```

### Scan réseau
```ruby
nombre de machine 37
PS C:\Users\enzon> arp -a | select-string 10.33

Interface : 10.33.76.186 --- 0x3
  10.33.64.136          e0-0a-f6-6d-2d-fd     dynamique
  10.33.65.229          e0-2e-0b-de-eb-7b     dynamique
  10.33.65.240          b0-60-88-51-8d-f8     dynamique
  10.33.66.17           38-fc-98-8d-b4-a9     dynamique
  10.33.66.73           5c-3a-45-c3-a3-0d     dynamique
  10.33.68.205          40-ec-99-f3-3e-14     dynamique
  10.33.68.212          28-cd-c4-ae-00-0f     dynamique
  10.33.68.216          f4-6d-3f-32-3f-5c     dynamique
  10.33.69.103          1c-bf-c0-6d-5d-09     dynamique
  10.33.69.248          14-5a-fc-64-f0-99     dynamique
  10.33.70.3            c4-bd-e5-79-f4-aa     dynamique
  10.33.70.110          ac-74-b1-21-c4-b5     dynamique
  10.33.70.209          00-93-37-9d-52-7e     dynamique
  10.33.71.57           04-ea-56-57-ef-4a     dynamique
  10.33.71.99           b0-3c-dc-ae-ab-6e     dynamique
  10.33.71.104          6c-94-66-1f-be-8b     dynamique
  10.33.71.111          b0-3c-dc-ae-ab-6e     dynamique
  10.33.71.115          c4-23-60-eb-cd-5f     dynamique
  10.33.71.123          b0-3c-dc-ae-ab-6e     dynamique
  10.33.71.128          a0-29-42-24-b0-3f     dynamique
  10.33.72.25           5c-3a-45-2d-99-cd     dynamique
  10.33.72.122          40-1a-58-0a-13-00     dynamique
  10.33.73.204          e4-5e-37-3b-02-a9     dynamique
  10.33.74.177          8c-85-90-cf-7d-95     dynamique
  10.33.75.150          b0-a4-60-63-a1-87     dynamique
  10.33.75.161          50-c2-e8-33-78-5b     dynamique
  10.33.76.10           dc-f5-05-ce-ec-f7     dynamique
  10.33.76.170          8c-b8-7e-9a-b8-5c     dynamique
  10.33.76.181          f8-89-d2-e7-0b-5f     dynamique
  10.33.76.182          60-e3-2b-90-26-e4     dynamique
  10.33.76.222          4c-03-4f-e9-73-f7     dynamique
  10.33.76.225          d8-f3-bc-54-c7-8f     dynamique
  10.33.76.226          48-e7-da-29-d8-b3     dynamique
  10.33.77.14           a8-64-f1-34-88-2f     dynamique
  10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
  10.33.79.255          ff-ff-ff-ff-ff-ff     statique
```

### wireshark

Capture ARP
[arp.pcap](./arp.pcap)  
Capture DNS
[dns.pcap](./dns.pcap)   
Capture TCP 
[tcp.pcap](./tcp.pcap)  



