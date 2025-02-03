class Solution(object):
    def removeComments(self, source):
        result = []
        in_block_comment = False
        current_line = []
        
        for line in source:
            idx = 0
            while idx < len(line):
                # if not in block comment
                if not in_block_comment:
                    if idx + 1 < len(line) and line[idx:idx + 2] == "//":
                        break

                    elif idx + 1 < len(line) and line[idx:idx + 2] == "/*":
                        in_block_comment = True
                        idx += 1
                    else:
                        current_line.append(line[idx])
                        
                # if in block comment
                else:
                    if idx + 1 < len(line) and line[idx:idx + 2] == "*/":
                        in_block_comment = False
                        idx += 1
                idx += 1
            
            if not in_block_comment and current_line:
                result.append("".join(current_line))
                current_line = []
        
        return result
