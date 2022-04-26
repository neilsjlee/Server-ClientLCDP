import datetime
import threading


def clock():
    print(datetime.datetime.now().strftime('%H:%M'))


def set_alarm():
    alarm_time = input('Set Alarm (XX:XX) : ')
    alarm_hour = alarm_time[:alarm_time.find(':')]
    alarm_minute = alarm_time[alarm_time.find(':') + 1:]
    alarm_thread = threading.Thread(target=alert_thread, args=(alarm_time, alarm_hour, alarm_minute))
    alarm_thread.start()


def alert_thread(alarm_time, alarm_hour, alarm_minute):
    print("Ringing at {}:{}".format(alarm_hour, alarm_minute))
    while True:
        now = datetime.datetime.now()
        if str(now.hour) == str(alarm_hour) and str(now.minute) == str(alarm_minute):
            print("Ring.. Ring..")
            break


# program start here
while True:
    print('1) Clock')
    print('2) Alarm')
    print('3) Quit')
    choice = input('Choose (1-6) : ')

    if choice == "1":
        clock()
    elif choice == "2":
        set_alarm()
    elif choice == "3":
        break
