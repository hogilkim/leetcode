# Union Find Very hard - solve again
# Dec 8, 2023 721

from collections import defaultdict
class UnionFind:
    def __init__(self, length):
        self.parent = [i for i in range(length)]
        self.rank = [1] * length
    def find(self, i):
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2: return False
        if p1 > p2:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = {} # key: email, val: index

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    uf.union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i
        
        rootParentToEmails = defaultdict(list)

        for email, idx in emailToAccount.items():
            root = uf.find(idx)
            rootParentToEmails[root].append(email)
        
        res = []
        for rootParent, emails in rootParentToEmails.items():
            name = accounts[rootParent][0]
            res.append([name] + sorted(rootParentToEmails[rootParent]))
        
        return res