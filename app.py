import time 
from notifypy import Notify

BREAK_INTERVAL = 10
# BREAK_INTERVAL = 20 * 60  # 20 minutes in seconds

def send_notification():
    notification = Notify()
    notification.title = "Eye Break 👀"
    notification.message = "Time to take a break and do your eye exercises!"
    notification.send()

def main():
    notification = Notify()
    notification.title = "Eye Timer Started"
    notification.message = "The eye timer is now running. You will receive a notification every 20 minutes."
    notification.send()
    while True:
        time.sleep(BREAK_INTERVAL)
        send_notification()

if __name__ == "__main__":
    main()
