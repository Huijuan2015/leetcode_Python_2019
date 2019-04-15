class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = collections.Counter()
        for cpdomain in cpdomains:
            times, domain = cpdomain.split(" ") #50 / yahoo.com
            times = int(times) 
            count[domain] += times # yahoo.com
            for i, ch in enumerate(domain):# 0y 1a 2h 3o 4o 5. 6com
                if ch == '.':
                    count[domain[i+1:]] += times
        return [str(times) + " " + domain for domain, times in count.items()]