class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        def parse(email):
            first, second = email.split('@')
            # ignore .
            first = ("").join(list(first.split('.')))
            first = list(first.split('+'))[0]
            return first +'@'+ second
        
        res = set()
        for email in emails:
            e = parse(email)
            res.add(e)
        return len(res)