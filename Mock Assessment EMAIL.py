class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        set_emails = set()

        for email in emails:
            at_index = email.index("@")
            names = set()
            email_name = email[0:at_index]
            dots = []
            name = ""
            dot_counter = 0
            for index in range(len(email_name)):
                letter = email[index]
                if letter=="+":
                    break
                if letter==".":
                    dots.append(index)
                name+=letter
            if len(dots)==0:
                names.add(name)
            else:
                #string , counter of erased dots so far
                name_dots = [(name,0)]
                for dot in dots:
                    length = len(name_dots)
                    counter = 0
                    while counter<length:
                        n,counter_erased_dots = name_dots.pop(0)

                        place = dot - counter_erased_dots
                        n = n[0:place] + n[place+1:]

                        name_dots.append((n,counter_erased_dots+1))


                        counter+=1
                for n in name_dots:
                    names.add(n[0])



            doman = email[at_index:]

            for name in names:
                res = name+doman
                set_emails.add(res)
        return len(set_emails)
test = Solution()
print(test.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

