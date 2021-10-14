# write a program to detect down and up speeds


import time
import subprocess
import re
import os


def get_interface():
    """
    get the interface name
    """
    interface = input("Enter the interface name: ")
    return interface


def get_ip_address(interface):
    """
    get the ip address of the interface
    """
    ip_address = subprocess.check_output(["ifconfig", interface])
    ip_address = ip_address.decode("utf-8")
    ip_address = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip_address)
    ip_address = ip_address.group(0)
    return ip_address


def get_down_speed(interface):
    """
    get the down speed of the interface
    """
    down_speed = subprocess.check_output(["ifconfig", interface])
    down_speed = down_speed.decode("utf-8")
    down_speed = re.search(r"RX bytes:(\d{1,}).*", down_speed)
    down_speed = down_speed.group(1)
    down_speed = int(down_speed)
    return down_speed


def get_up_speed(interface):
    """
    get the up speed of the interface
    """
    up_speed = subprocess.check_output(["ifconfig", interface])
    up_speed = up_speed.decode("utf-8")
    up_speed = re.search(r"TX bytes:(\d{1,}).*", up_speed)
    up_speed = up_speed.group(1)
    up_speed = int(up_speed)
    return up_speed


def get_time():
    """
    get the time
    """
    time = subprocess.check_output(["date"])
    time = time.decode("utf-8")
    time = re.search(r"\d{2}:\d{2}:\d{2}", time)
    time = time.group(0)
    return time


def get_date():
    """
    get the date
    """
    date = subprocess.check_output(["date"])
    date = date.decode("utf-8")
    date = re.search(r"\w{3} \d{1,2} \w{3} \d{4}", date)
    date = date.group(0)
    return date


def get_down_speed_mb(interface):
    """
    get the down speed in mb
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024 / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_mb(interface):
    """
    get the up speed in mb
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024 / 1024
    up_speed = round(up_speed, 2)
    return up_speed


def get_down_speed_kb(interface):
    """
    get the down speed in kb
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_kb(interface):
    """
    get the up speed in kb
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024
    up_speed = round(up_speed, 2)
    return up_speed


def get_down_speed_mb_per_sec(interface):
    """
    get the down speed in mb per sec
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024 / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_mb_per_sec(interface):
    """
    get the up speed in mb per sec
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024 / 1024
    up_speed = round(up_speed, 2)
    return up_speed


def get_down_speed_kb_per_sec(interface):
    """
    get the down speed in kb per sec
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_kb_per_sec(interface):
    """
    get the up speed in kb per sec
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024
    up_speed = round(up_speed, 2)
    return up_speed


def get_down_speed_mb_per_sec_average(interface):
    """
    get the down speed in mb per sec average
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024 / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_mb_per_sec_average(interface):
    """
    get the up speed in mb per sec average
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024 / 1024
    up_speed = round(up_speed, 2)
    return up_speed


def get_down_speed_kb_per_sec_average(interface):
    """
    get the down speed in kb per sec average
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_kb_per_sec_average(interface):
    """
    get the up speed in kb per sec average
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024
    up_speed = round(up_speed, 2)
    return up_speed


def get_down_speed_mb_per_sec_average_average(interface):
    """
    get the down speed in mb per sec average average
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024 / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_mb_per_sec_average_average(interface):
    """
    get the up speed in mb per sec average average
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024 / 1024
    up_speed = round(up_speed, 2)
    return up_speed


def get_down_speed_kb_per_sec_average_average(interface):
    """
    get the down speed in kb per sec average average
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_kb_per_sec_average_average(interface):
    """
    get the up speed in kb per sec average average
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024
    up_speed = round(up_speed, 2)
    return up_speed


def get_down_speed_mb_per_sec_average_average_average(interface):
    """
    get the down speed in mb per sec average average average
    """
    down_speed = get_down_speed(interface)
    down_speed = down_speed / 1024 / 1024
    down_speed = round(down_speed, 2)
    return down_speed


def get_up_speed_mb_per_sec_average_average_average(interface):
    """
    get the up speed in mb per sec average average average
    """
    up_speed = get_up_speed(interface)
    up_speed = up_speed / 1024 / 1024
    up_speed = round(up_speed, 2)
    return up_speed
