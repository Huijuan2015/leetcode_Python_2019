class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        email_account_map = defaultdict(list)
        visited = [False]*len(accounts)
        res = []
        # build an email:account map  
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email_account_map[account[j]].append(i)
        
        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in email_account_map[email]:
                     dfs(neighbor, emails)
                        
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name]+sorted(emails))
        return res        


        
         
        