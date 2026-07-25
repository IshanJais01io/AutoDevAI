class SharedMemory:

    def __init__(self):
        self.data = {
            "repo_url": "",
            "repo_name": "",
            "language": "",
            "files": [],
            "review_report": "",
            "testing_report": "",
            "summary": ""
        }


    def update(self, key, value):
        self.data[key] = value


    def get(self, key):
        return self.data.get(key)


    def get_all(self):
        return self.data