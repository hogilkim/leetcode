from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        ing_to_food = defaultdict(list)
        food_degree = defaultdict(int)
        
        for foodname, items in zip(recipes, ingredients):
            food_degree[foodname] = len(items)
            for item in items: ing_to_food[item].append(foodname)
                
        queue = deque(supplies)
        res = []
        while queue:
            item = queue.popleft()
            
            for food in ing_to_food[item]:
                food_degree[food] -= 1
                if food_degree[food] == 0:
                    queue.append(food)
                    res.append(food)
        
        return res