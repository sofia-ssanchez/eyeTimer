import time 
from notifypy import Notify
import os
import sys

BREAK_INTERVAL = 10
# BREAK_INTERVAL = 20 * 60  # 20 minutes in seconds

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), relative_path)

ICON_PATH = resource_path("icon.icns")

def send_notification():
    notification = Notify(
        default_notification_application_name="Eye Break",
        default_notification_application_icon=ICON_PATH)
    notification.title = "Eye Break 👀"
    notification.message = "Time to take a break and do your eye exercises!"
    notification.icon = ICON_PATH
    notification.send()

def main():
    notification = Notify(
        default_notification_application_name="Eye Break",
        default_notification_application_icon=ICON_PATH)
    notification.title = "Eye Timer Started"
    notification.message = "The eye timer is now running. You will receive a notification every 20 minutes."
    notification.icon = ICON_PATH
    notification.send()
    while True:
        time.sleep(BREAK_INTERVAL)
        send_notification()

if __name__ == "__main__":
    main()
