# wlan ap - raspi 
Wireless LAN Access Point <br/>

### Setup
> $ sudo apt-get install isc-dhcp-server <br/>
> $ sudo apt-get install hostapd <br/>

### Files
- dhcpd.conf <br/>
  /etc/dhcp/dhcpd.conf <br/>
  DHCP Server <br/>
  addr 192.168.42.1 <br/>
  range 192.168.42.10 192.168.42.50 <br/>
- isc-dhcp-server <br/>
  /etc/default/isc-dhcp-server <br/>
  DHCP Server <br/>  
- hostapd.conf <br/>
  /etc/hostapd/hostapd.conf <br/>
  Access Point Daemon <br/>
  SSID fablab_raspi <br/>
  passphrase 0456649009 <br/>
- hostapd.default <br/>
  /etc/default/hostapd <br/>
  Access Point Daemon <br/>
- interfaces <br/>
  /etc/network/interfaces <br/>
  Static IP Address & Routing <br/>
  wlan0 address 192.168.42.1<br/> 
- sysctl.conf <br/>
  /etc/sysctl.conf <br/>
  Routing <br/>  
- iptables.ipv4.nat <br/>
  /etc/iptables.ipv4.nat <br/>
  Routing <br/>

### Blog (Japanese)
http://android.ohwada.jp/archives/6978
