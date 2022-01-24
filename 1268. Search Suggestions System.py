class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products = sorted(products)
        
        search = ""
        
        result = []
        starting_index = 0
        
        for i in range(len(searchWord)):
            search += searchWord[i]
            suggestions = []
            for j in range(starting_index, len(products)):
                if search == products[j][:i+1]:
                    if not suggestions:
                        starting_index = j
                    suggestions.append(products[j])
                if len(suggestions) == 3:
                    break
            result.append(suggestions.copy())
        
        return result