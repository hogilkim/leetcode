class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        
        for i, t1 in enumerate(transactions):
            name1, time1, amount1, city1 = t1.split(',')
            if int(amount1) > 1000:
                invalid.append(t1)
                continue
            for j, t2 in enumerate(transactions):
                if i != j: 
                    name2, time2, amount2, city2 = t2.split(',')
                    if name1 == name2 and city1 != city2 and abs(int(time1) - int(time2)) <= 60:
                        invalid.append(t1)
                        break
        
        return invalid


# Not good Q

# import collections
# class Solution:
#     def invalidTransactions(self, transactions: List[str]) -> List[str]:
#         trans_dic = collections.defaultdict(list)
#         up_to = collections.defaultdict(int)
#         res = []
        
#         for trans in transactions:
#             name, time, amount, city = trans.split(",")                
#             if int(amount) > 1000:
#                 res.append(trans)
#                 up_to[name] = len(trans_dic[name]) + 1
#             elif trans_dic[name] and (abs(int(time) - int(trans_dic[name][-1][1])) <= 60) and (city != trans_dic[name][-1][3]):       
#                 while trans_dic[name] and int(trans_dic[name][-1][2]) <= 1000 and up_to[name] < len(trans_dic[name]):
#                     popped = trans_dic[name].pop()
#                     res.append(",".join(popped))
#                 res.append(trans)
#                 up_to[name] = len(trans_dic[name]) + 1
            
            
#             trans_dic[name].append([name, time, amount, city])
        
#         return res
                