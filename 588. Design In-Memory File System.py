class FileSystem:

    def __init__(self):
        self.directory = {}

    def ls(self, path: str) -> List[str]:
        paths = []
        if path != '/':
            paths = path.split('/')[1:]
        
        dir_dic = self.directory
        if paths:
            for p in paths[:-1]:
                if p not in dir_dic: dir_dic = dir_dic[p]
                dir_dic = dir_dic[p]
        else:
            return [key for key in sorted(dir_dic.keys())]
        
        res = []
        if type(dir_dic[paths[-1]]) == str:
            return [paths[-1]]
        else:
            
            for key in sorted(dir_dic[paths[-1]].keys()):
                res.append(key)
        
        return res

    def mkdir(self, path: str) -> None:
        paths = path.split('/')
        dir_dic = self.directory
        
        for p in paths[1:]:
            if p not in dir_dic:
                dir_dic[p] = {}
            dir_dic = dir_dic[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        paths = filePath.split('/')
        dir_dic = self.directory
        for p in paths[1:-1]:
            if p not in dir_dic: dir_dic[p] = {}
            dir_dic = dir_dic[p]
        if paths[-1] not in dir_dic:
            dir_dic[paths[-1]] = content
        else:
            dir_dic[paths[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        paths = filePath.split('/')
        dir_dic = self.directory
        for p in paths[1:-1]:
            dir_dic = dir_dic[p]
        
        return dir_dic[paths[-1]]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)