import multiprocessing
import os
import shutil


class WordSearch:
    def findWord(self, args_item):
        (word, folder, filename) = args_item
        with open(folder + os.sep + filename) as f:
            if word in f.read():
                print("Found " + word + " in " + filename)
                if not os.path.exists(folder + os.sep + word):
                    os.mkdir(folder + os.sep + word)
                shutil.copy(folder + os.sep + filename, folder + os.sep + word)

    def thread_search(self, args_list):
        try:
            pool = multiprocessing.Pool()
            res = pool.map(self.findWord, args_list)
            pool.close()
            pool.join()
        except Exception as err:
            print("Error: Exception raised")
            print(err)


if __name__ == '__main__':
    word = r'405F07'
    folder = r'C:\Users\jiang\Desktop\test_data'

    args_list = []
    filenames = os.listdir(folder)
    for filename in filenames:
        if os.path.isfile(folder + os.sep + filename):
            args_list.append((word, folder, filename))
    WordSearch().thread_search(args_list)
