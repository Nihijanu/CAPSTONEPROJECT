from LEVEL3.demo import Filesearcher
from threading import Thread

class SearchManager:

    def __init__(self):
        pass

    def search(self,file_name,drives):
        print("this is a search method")

        searcher_threads = []
        file_searcher = []

        for drive in drives:
            print(drive)
            file_searcher = Filesearcher()
            file_searcher.search_for_file(drive,file_name)
