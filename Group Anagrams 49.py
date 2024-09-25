from queue import PriorityQueue
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap_set = dict()

        set_list=[]

        for string in strs:
            set_str = []
            for letter in string:
                set_str.append(letter)
            set_str.sort()
            key_set = ""
            for sk in set_str:
                key_set+=sk
            print(key_set)
            if key_set not in set_list:
                set_list.append(key_set)

                hashmap_set[key_set]=[string]
            else:
                hashmap_set[key_set].append(string)
        print(hashmap_set)
        result = []
        for k in hashmap_set.keys():
            list_hash = []
            for m in hashmap_set[k]:
                list_hash.append(m)
            result.append(list_hash)

        return result

