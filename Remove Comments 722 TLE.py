class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        index = 0
        multi_line_comment = False
        current_string = ""
        start_multi_comment_index = -1
        while index < len(source):
            if multi_line_comment==True:
                if "*/" in source[index]:
                    res=""
                    for ind in range(source[index].index("*/")+2,len(source[index])):
                        res+=source[index][ind]
                    current_string+=res
                    source[start_multi_comment_index]=current_string
                    source.pop(index)
                    index=start_multi_comment_index
                    multi_line_comment=False
                else:
                    source.pop(index)
            else:
                oneline_index = len(source[index])
                if "//" in source[index]:
                    oneline_index = source[index].index("//")
                multi_line_index = len(source[index])
                if "/*" in source[index]:
                    multi_line_index = source[index].index("/*")
                if oneline_index!=len(source[index]) and oneline_index<multi_line_index:
                    if oneline_index==0:
                        source.pop(index)
                    else:
                        res=""
                        for i in range(oneline_index):
                            res+=source[index][i]
                        source[index]=res
                        index+=1
                elif multi_line_index != len(source[index]) and multi_line_index < oneline_index:
                    start_multi_comment_index = index
                    multi_line_comment=True
                    if ("*/" not in source[index]) or ("*/" in source[index] and source[index].index("*/") ==multi_line_index+1 and source[index].count("*/")==1):
                        if multi_line_index==0:
                            source.pop(index)
                        else:
                            res=""
                            for i in range(multi_line_index):
                                res+=source[index][i]
                            current_string=res
                            source[index]=res
                            index+=1
                    else:
                        ending_multi_line = source[index].index("*/")

                        while True:
                            if ending_multi_line==source[index].index("/*")+1:
                                source[index] = source[index][:ending_multi_line+1] + source[index][ending_multi_line+2:]
                                ending_multi_line = source[index].index("*/")
                            else:
                                break

                        multi_line_comment=False
                        if multi_line_index==0 and ending_multi_line==len(source[index])-2:
                            source.pop(index)
                        else:
                            res=""
                            for i in range(multi_line_index):
                                res+=source[index][i]
                            for i in range(ending_multi_line+2,len(source[index])):
                                res+=source[index][i]
                            source[index]=res
                else:
                    index+=1

        return source

test = Solution()
print(test.removeComments(["main() { ", "  int a = 1; /* Its comments here ", "", "  ", "  */ return 0;", "} "]))