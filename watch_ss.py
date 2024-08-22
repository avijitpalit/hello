from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time, os, shutil, re

def is_numeric_filename(filename):
    return re.fullmatch(r'\d+', filename) is not None

def replace_file(old_file_path, new_file_path):
    if os.path.exists(old_file_path):
        os.remove(old_file_path)
    shutil.copy(new_file_path, old_file_path)

class Watcher:
    def __init__(self, path):
        self.path = path
        self.event_handler = FileSystemEventHandler()
        self.observer = Observer()
    
    def start(self):
        self.event_handler.on_created = self.on_created
        self.observer.schedule(self.event_handler, self.path, recursive=False)
        self.observer.start()
        print(f"Monitoring folder: {self.path}")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Monitoring stopped.")
        self.observer.join()
    
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file created: {event.src_path}")
            new_filename = os.path.basename(event.src_path)
            print(new_filename)
            #if is_numeric_filename(new_filename):
            print('here')
            if os.path.exists(event.src_path): os.remove(event.src_path)
            file_to_copy = "C:/Users/Administrator/Pictures/Screenshots/ss1.jpg"
            time.sleep(1)
            shutil.copy(file_to_copy, f"{os.path.dirname(event.src_path)}{new_filename}")
            time.sleep(1)
            self.observer.stop()
            self.observer.start()

if __name__ == "__main__":
    path_to_watch = "C:/Users/Administrator/Pictures/Screenshots"
    watcher = Watcher(path_to_watch)
    watcher.start()