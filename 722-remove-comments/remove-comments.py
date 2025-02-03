class Solution(object):
    def removeComments(self, source):
        result = []
        in_block_comment = False
        current_line = []
        
        for line in source:
            i = 0
            while i < len(line):
                if not in_block_comment:
                    if i + 1 < len(line) and line[i:i + 2] == "//":
                        break

                    elif i + 1 < len(line) and line[i:i + 2] == "/*":
                        in_block_comment = True
                        i += 1  
                    else:
                        current_line.append(line[i])
                else: 
                    if i + 1 < len(line) and line[i:i + 2] == "*/":
                        in_block_comment = False
                        i += 1  
                i += 1
            
            if not in_block_comment and current_line:
                result.append("".join(current_line))
                current_line = [] 
        
        return result
