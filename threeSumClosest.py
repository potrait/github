'''
solution1_jun20
'''

class object():
    def __init__(self):
        return

class Solution(object):

    def axis0(self, point):
        return point

    def axis1(self, point):
        return point[-1]

    def order(self, alist, axis):
        if len(alist): return self.put(self.order(alist[:-1], axis), alist[-1], axis)
        return []

    def put(self, alist, ele, axis):
        if len(alist) == 0: return [ele]

        if len(alist) == 1:
            if axis(alist[-1]) > axis(ele): return [ele , alist[-1]]
            return [alist[-1] , ele]

        n_half = len(alist)/2
        if axis(alist[n_half]) > axis(ele): return self.put(alist[:n_half], ele, axis) + alist[n_half:]
        return alist[:n_half] + self.put(alist[n_half:], ele, axis)

    def find_nearest_neighborhood_in_orderedlist(self, alist, ele):
        if len(alist) == 1: return alist[-1], abs(alist[-1]-ele)

        if len(alist) > 1:
            n_half = len(alist)/2
            if ele < alist[n_half-1]: return self.find_nearest_neighborhood_in_orderedlist(alist[:n_half], ele)
            else:
                if ele < alist[n_half]:
                    if ele-alist[n_half-1] < alist[n_half]-ele: return alist[n_half-1], ele-alist[n_half-1]
                    return alist[n_half], alist[n_half]-ele
                if ele >= alist[-1]: return alist[-1], ele-alist[-1]
                return self.find_nearest_neighborhood_in_orderedlist(alist[n_half:], ele)

        return False

    def threeSumClosest(self, nums, target):

        nums = self.order(nums, self.axis0); n = len(nums); threesumclosestlist = []

        for i in range(n-2):#min(n_neg, n-2)):#n-2):
            for j in range(i+1, n-1):
                target_twosum_diff = target-(nums[i]+nums[j])
                nearest = self.find_nearest_neighborhood_in_orderedlist(nums[j+1:], target_twosum_diff)
                if nearest: threesumclosestlist.append([nums[i], nums[j], nearest[0], nearest[1]])

        threesumclosestlist = self.order(threesumclosestlist, self.axis1)

        closestlist = []
        if threesumclosestlist:
            '''
            min_norm = threesumclosestlist[0][-1]; closestlist=[threesumclosestlist[0][:-1]]
            for i in range(1, len(threesumclosestlist)):
                if threesumclosestlist[i][-1] == min_norm: closestlist.append(threesumclosestlist[i][:-1])
        return closestlist
        '''
            return sum(threesumclosestlist[0][:-1])
        #return 'null' 
