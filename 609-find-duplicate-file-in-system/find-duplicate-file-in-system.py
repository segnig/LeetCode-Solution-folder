class Solution:
    def findDuplicate(self, paths):
        files = defaultdict(list)

        for path in paths:
            parts = path.split()
            root = parts[0]
            file_names = parts[1:]

            for file_name in file_names:
                file_n, content = file_name.split("(")
                content = content.rstrip(')')
                files[content].append(root + "/" + file_n)
        
        result = [files[path] for path in files if len(files[path]) > 1]

        return result
