from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time, os, shutil, re, random

def is_numeric_filename(filename):
    return re.fullmatch(r'\d+', filename) is not None

def replace_file(old_file_path, new_file_path):
    if os.path.exists(old_file_path):
        os.remove(old_file_path)
    shutil.copy(new_file_path, old_file_path)

files = [
    'C:/Users/Administrator/Pictures/Screenshots/ss1.jpg',
    'C:/Users/Administrator/Pictures/Screenshots/ss2.jpg',
    'C:/Users/Administrator/Pictures/Screenshots/ss3.jpg',
    'C:/Users/Administrator/Pictures/Screenshots/ss4.jpg'
]
path_to_watch = "C:/Users/Administrator/AppData/Local/Temp/WebWorkTracker/screenshots/166203"

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
            old_path = event.src_path
            new_filename = os.path.basename(event.src_path)
            print(new_filename)
            if not new_filename == "do_not_delete" or new_filename == "do_not_delete_2":
                time.sleep(1)
                if os.path.exists(event.src_path): os.remove(event.src_path)
                print("File deleted")
            file_to_copy = random.choice(files)
            print(file_to_copy)
            r = shutil.copy(file_to_copy, f"{os.path.dirname(event.src_path)}/do_not_delete")
            print(r)
            dnd_path = f"{os.path.dirname(event.src_path)}/do_not_delete"
            if not os.path.exists(old_path):
                os.rename(dnd_path, old_path)
                time.sleep(1)
                if(os.path.exists(dnd_path)):
                    os.remove(dnd_path)
                    print('do_not_delete removed')
                else:
                    print('do_not_delete not exists')

if __name__ == "__main__":
    watcher = Watcher(path_to_watch)
    watcher.start()