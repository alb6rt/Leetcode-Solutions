int search(int* nums, int numsSize, int target) {
    int L = 0;
    int R = numsSize - 1;

    while (L <= R) {
        int M = L + (R-L)/2;
        if (target > nums[M]) {
            L = M + 1;
        }
        else if (target < nums[M]) {
            R = M - 1;
        }
        else {
            return M;
        }
    }
    return -1;
}
