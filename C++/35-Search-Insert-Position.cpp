// Brute force that checks out of bounds
// Binary search that checks in bounds

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                return i;
            }
        }

        if (nums[nums.size()-1] < target) {
            return nums.size();
        }
        else if (nums[0] > target) {
            return 0;
        }
        
        int l = 0;
        int r = nums.size() - 1;
        while (l <= r) {
            int m = l + (r-l)/2;
            if (nums[m] > target) {
                r = m;
            }
            else if (nums[m] < target) {
                l = m;
            }
            if (m + 1 == r) {
                return r;
            }
        }
        return 0;
    }
};
