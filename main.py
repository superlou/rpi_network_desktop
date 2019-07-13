#!/usr/bin/python3
import socket
import subprocess
import fcntl
import struct
import time
import json
import hashlib
from status_image_builder import StatusImageBuilder


def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode())
        )[20:24])
    except Exception:
        return "(unknown)"


def get_ssid():
    try:
        result = subprocess.run(['iwgetid', '-r'], stdout=subprocess.PIPE)
        return result.stdout.decode().strip()
    except Exception:
        return "(unknown)"


def get_network_info():
    return {
        "hostname": socket.gethostname(),
        "eth0": get_ip_address('eth0'),
        "wlan0": get_ip_address('wlan0'),
        "ssid": get_ssid()
    }    


def main():
    prev_info = {}
    image_builder = StatusImageBuilder()

    while True:
        info = get_network_info()
        
        if info != prev_info:
            info_hash = hashlib.md5(json.dumps(info).encode()).hexdigest()
            image_path = '/tmp/status-{}.png'.format(info_hash)
            image_builder.generate(info, image_path)
            subprocess.run(['pcmanfm', '--set-wallpaper', image_path])       
            prev_info = info

        time.sleep(1)


if __name__ == '__main__':
    main()