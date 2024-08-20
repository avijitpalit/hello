import schedule
import time
import generate_image

def my_task():
  # Your task logic here
  print("Task executed at:", time.strftime("%H:%M:%S"))

def run_background_task(interval):
  schedule.every(interval).seconds.do(generate_image.generate)
  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  run_background_task(3 * 60 * 60)