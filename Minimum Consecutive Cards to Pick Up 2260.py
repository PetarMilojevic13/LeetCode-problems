from collections import defaultdict
class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        hashmap = defaultdict(int)
        cards_set = set()
        minimum = -1
        for index in range(len(cards)):
            card = cards[index]
            if card in cards_set:
                length = index - hashmap[card]+1
                if minimum==-1:
                    minimum=length
                else:
                    if length<minimum:
                        minimum=length
                hashmap[card]=index
            else:
                cards_set.add(card)
                hashmap[card]=index
        return minimum