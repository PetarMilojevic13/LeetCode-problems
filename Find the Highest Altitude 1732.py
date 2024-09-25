class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        maximum = 0
        for g in gain:
            current_altitude+=g
            if current_altitude>maximum:
                maximum=current_altitude
        return maximum