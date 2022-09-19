from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # content to path
        dup_paths = defaultdict(list)
        
        for path in paths:
            line = path.split()
            for i in range(1, len(line)):
                name, content = line[i].split("(")
                dup_paths[content[:-1]].append(line[0] + "/" + name)
        
        return [duplicates for duplicates in dup_paths.values() if len(duplicates)>1]