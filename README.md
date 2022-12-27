# gptCozmo
Cozmo and GPT integration

pip install openai
pip install dotenv

pip install pycozmo
pip install libopenjp2-7-dev

/etc/wpa_supplicant/
wpa_supplicant-wlan0.conf  wpa_supplicant-wlan1.conf

# gptCozmo
Cozmo and GPT integration

pip install openai
pip install dotenv

pip install pycozmo
pip install libopenjp2-7-dev

/etc/wpa_supplicant/
wpa_supplicant-wlan0.conf  wpa_supplicant-wlan1.conf

wpa_supplicant-wlan1.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=CA
network={
        ssid="Cozmo_71374E"
        psk="ZZHP0SMI27GM"
}

sudo systemctl restart wpa_supplicant@wlan1.service
sudo systemctl status wpa_supplicant@wlan1.service

iwconfig

wlan1     IEEE 802.11  ESSID:"Cozmo_71374E"
          Mode:Managed  Frequency:2.462 GHz  Access Point: 5E:CF:7F:C3:8E:EC
          Bit Rate=54 Mb/s   Tx-Power=31 dBm
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:on
          Link Quality=70/70  Signal level=-39 dBm
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:0   Missed beacon:0

ifconfig
wlan1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.31.1.56  netmask 255.255.255.0  broadcast 172.31.1.255
        inet6 fe80::1c97:4e60:6553:b458  prefixlen 64  scopeid 0x20<link>
        ether dc:a6:32:c9:3a:08  txqueuelen 1000  (Ethernet)
        RX packets 325  bytes 53515 (52.2 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 424  bytes 56025 (54.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

