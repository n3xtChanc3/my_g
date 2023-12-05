from datetime import datetime
from playsound import playsound
import threading
import time
import os
import psutil

class AlarmClock:
    def __init__(self):
        self.alarm_thread = None
        self.is_alarm_set = False

    def set_alarm(self, alarm_time, sound_file_path):
        self.alarm_time = alarm_time
        self.sound_file_path = sound_file_path
        self.is_alarm_set = True

        # Start a new thread for the alarm
        self.alarm_thread = threading.Thread(target=self.run_alarm)
        self.alarm_thread.start()

    def run_alarm(self):
        while self.is_alarm_set:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Current Time: {now} | Alarm Time: {self.alarm_time}", end='\r')

            if datetime.now().strftime("%H:%M:%S") == self.alarm_time:
                print("\nWake Up!")
                playsound(self.sound_file_path)
                self.is_alarm_set = False
                break

            # Print CPU and memory usage
            self.print_resource_usage()

            time.sleep(1)

    def print_resource_usage(self):
        pid = os.getpid()
        process = psutil.Process(pid)

        cpu_percent = process.cpu_percent()
        memory_percent = process.memory_percent()

        print(f"CPU Usage: {cpu_percent:.2f}% | Memory Usage: {memory_percent:.2f}%", end='\r')

if __name__ == "__main__":
    alarm_clock = AlarmClock()

    while True:
        alarm_time = input("Enter the time of alarm to be set (HH:MM:SS 24-hour format, 'exit' to quit)\n")

        if alarm_time.lower() == 'exit':
            break

        sound_file_path = "/home/decoder/Desktop/my_g/alarm.mp3"
        alarm_clock.set_alarm(alarm_time, sound_file_path)
