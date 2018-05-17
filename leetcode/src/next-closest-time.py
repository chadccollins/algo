# Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

# You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        # convert the time from a string to minutes
        minutes = time[3:4]
        hours = time[1:2]

        startminutes = int(hours) * 60 + int(minutes)

        # 1440 minutes in a day, so now we need to figure out the minimum number of minutes we can add
        # starting from one minute from now, until a full day later
        for i in range(startminutes + 1, startminutes + 1440):
            # t 
            t = i % 1440

            # reconsruct a candidate time from t
            hours = t // 60
            minutes = t % 60

            # reformat it into a time string
            closest = "%02d:%02d" %(hours, minutes)

            # compare the set of characters in the candidate to those in time
            # if the candidate set is a sub-set of time, then we have found the 
            # closest next time that contains only the digits in the original
            if set(closest) <= set(time):
                break
        
        return closest


import sys

#time = sys.argv[1]

print (Solution.nextClosestTime(Solution, "19:34"))