class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse = True)
        
        units = 0
        
        for boxnum, unitsperbox in boxTypes:
            loading_boxes = min(boxnum, truckSize)
            units += loading_boxes * unitsperbox
            
            truckSize -= loading_boxes
            
            if not truckSize: return units
        return units
        
        