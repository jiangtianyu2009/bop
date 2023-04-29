import os
import shutil
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


# 建立新的目录
def make_new_dir(dir, type_dir):
    for td in type_dir:
        new_td = os.path.join(dir, td)
        if not os.path.isdir(new_td):
            os.makedirs(new_td)


# 定义子类继承FileSystemEventHandler并重写on_any_event方法
class FileEventHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        if not event.is_directory:
            if event.event_type == 'created':
                print(f"file created:{event.src_path}.")
                self.move_file(event.src_path)

# 移动文件至相应的目录
    @staticmethod
    def move_file(src_path: str):
        time.sleep(5)
        for file_type, file_ext in file_type_mapping.items():
            if src_path.endswith(file_ext):
                shutil.move(src_path, os.path.join(source_dir, file_type))
                print(
                    f"file {src_path} has been successfully moved to {os.path.join(source_dir, file_type)}")


# 定义Watcher类包含observer和event_handler
class Watcher:

    def __init__(self, event_handler: FileSystemEventHandler, path: str):
        self.event_handler = event_handler
        self.observer = Observer()
        self.path = path

    def run(self):
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print(f'Error')

        self.observer.join()


if __name__ == "__main__":
    source_dir = r"C:\Users\jiang\Desktop\cp38"
    # 定义文件类型和它的扩展名
    file_type_mapping = {
        "music": ("mp3", "wav"),
        "movie": ("mp4", "rmvb", "rm", "avi"),
        "execute": ("exe", "bat"),
        "sheet": ("csv", "xlsx")
    }
    # 建立新的文件夹
    make_new_dir(source_dir, file_type_mapping)
    # 创建Watcher实例并传入监控目录和FileEventHandler
    w = Watcher(path=source_dir, event_handler=FileEventHandler())
    w.run()


# 如果需要在后台不间断运行的话，可以用nohup python watchdog_auto_classify &gt;output.log 2&gt;&amp;1 &amp;。</p>
