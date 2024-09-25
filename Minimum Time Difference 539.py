class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        timePoints_minutes = []
        for ti in timePoints:
            hours,minutes = ti.split(":")
            timePoints_minutes.append(int(hours)*60+int(minutes))
        timePoints_minutes.sort()
        minimum = 20000
        difference = None
        for index in range(len(timePoints_minutes)):
            if index>0:
                difference = timePoints_minutes[index]-timePoints_minutes[index-1]
                if difference<minimum:
                    minimum=difference
                if minimum==0:
                    return 0
        difference = timePoints_minutes[0]-timePoints_minutes[len(timePoints_minutes)-1]+1440
        if difference < minimum:
            minimum = difference
        return minimum