class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = [(heights[i], names[i]) for i in range(len(names))]  
        
          
        name_height.sort(key=lambda x: x[0], reverse=True)  
        
         
        sorted_names = [name for height, name in name_height]  
        
        return sorted_names  