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

