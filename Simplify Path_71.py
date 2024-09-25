class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path=="":
            return ""

        index = 0

        directories = []

        while index<len(path):
            while index<len(path) and path[index]=="/":
                index+=1
            if index==len(path):
                break
            else:
                word=""
                while index < len(path) and path[index] != "/":
                    word+=path[index]
                    index += 1
                directories.append(word)

        res="/"
        index = 0
        first = True
        while index<len(directories):
            word = directories[index]

            if word==".":
                directories.pop(index)
            elif word=="..":
                if index>0:
                    directories.pop(index-1)
                    directories.pop(index - 1)
                    index-=1
                else:
                    directories.pop(index)

            else:
                index+=1

        first = True
        for dir in directories:
            if first:
                res+=dir
                first=False
            else:
                res+="/"
                res+=dir
        return res