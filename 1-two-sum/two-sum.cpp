class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> arr;
        for(int i=0;i<nums.size()-1;i++){
            if(nums[i]+nums[i+1]==target){
                arr.push_back(i);
                arr.push_back(i+1);
                return arr;
            }
        }
        for(int i=0,j=nums.size()-1;i<j;i++,j--){
            if(nums[i]+nums[j]==target){
                 arr.push_back(i);
                arr.push_back(j);
                return arr;
            }
        }
        for(int k = nums.size()-1; k>0;k--){
            if(nums[0]+nums[k]==target){
                arr.push_back(0);
                arr.push_back(k);
                return arr;
            }
        }
        for(int l = 0; l<nums.size()-1;l++){
            if(nums[nums.size()-1]+nums[l]==target){
                arr.push_back(l);
                arr.push_back(nums.size()-1);
                return arr;
            }
        }
        for(int i = 0; i+2<nums.size();i++){
            if(nums[i]+nums[i+2]==target){
                 arr.push_back(i);
                arr.push_back(i+2);
                return arr;
            }
        }
        for(int i = 0; i+3<nums.size();i++){
            if(nums[i]+nums[i+3]==target){
                 arr.push_back(i);
                arr.push_back(i+3);
                break;
            }
        }
        
        return arr;
        
    }
};