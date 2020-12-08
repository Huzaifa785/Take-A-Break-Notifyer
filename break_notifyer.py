import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "Please Take A Break...",
            message = "Research has also found that short breaks throughout the day can result in being more alert. It's no surprise to find that working long hours can lead to fatigue.",
            app_icon = r"C:\Users\Rkct\PycharmProjects\Take A Break Notifyer\break.ico",  # Mention your image path here
            timeout = 10
        )
        time.sleep(60*60)