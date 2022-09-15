import os
import multiprocessing


class WordSearch:
    def findWord(self, args_item):
        (word, file_path) = args_item
        with open(file_path) as f:
            if word in f.read():
                print("Found " + word + " in " + file_path)

    def thread_search(self, args_list):
        try:
            pool = multiprocessing.Pool()
            res = pool.map(self.findWord, args_list)
            pool.close()
            pool.join()
        except:
            print("Error: unable to start thread")


if __name__ == '__main__':
    word = r'405F'
    folder = r'C:\Users\jiang\Desktop\test_data'
    filenames = os.listdir(folder)

    args_list = []
    for filename in filenames:
        args_list.append((word, folder + os.sep + filename))
    WordSearch().thread_search(args_list)
