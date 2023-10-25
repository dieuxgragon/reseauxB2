### Sur node1.lan1.tp2

```ruby
[enzo@node1 ~]$ ip a
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:a6:42:13 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fea6:4213/64 scope link
       valid_lft forever preferred_lft forever

[enzo@node1 ~]$ ip r s
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.11 metric 100

[enzo@node1 ~]$ ping 10.1.2.11
PING 10.1.2.11 (10.1.2.11) 56(84) bytes of data.
64 bytes from 10.1.2.11: icmp_seq=1 ttl=63 time=2.71 ms
64 bytes from 10.1.2.11: icmp_seq=2 ttl=63 time=2.34 ms
^C
--- 10.1.2.11 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 2.344/2.528/2.712/0.184 ms

[enzo@node1 ~]$ traceroute 10.1.2.11
traceroute to 10.1.2.11 (10.1.2.11), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  3.524 ms  1.242 ms  1.220 ms
 2  10.1.2.11 (10.1.2.11)  3.924 ms !X  3.913 ms !X  3.903 ms !X
```
### interlude acces internet

```ruby
[enzo@router ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=24.1 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=113 time=25.2 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=113 time=22.9 ms
^C
--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2005ms
rtt min/avg/max/mdev = 22.888/24.065/25.240/0.960 ms

[enzo@router ~]$ ping www.gogle.com
PING www.gogle.com (172.217.20.163) 56(84) bytes of data.
64 bytes from par10s49-in-f3.1e100.net (172.217.20.163): icmp_seq=1 ttl=113 time=29.4 ms
64 bytes from par10s49-in-f3.1e100.net (172.217.20.163): icmp_seq=2 ttl=113 time=22.7 ms
64 bytes from par10s49-in-f3.1e100.net (172.217.20.163): icmp_seq=3 ttl=113 time=22.0 ms
^C
--- www.gogle.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2005ms
rtt min/avg/max/mdev = 21.967/24.672/29.374/3.336 ms
```
### acces internet LAN1 et LAN2
```ruby

```