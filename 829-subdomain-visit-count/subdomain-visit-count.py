class Solution(object):
    def subdomainVisits(self, cpdomains):
        count_paired_domain = defaultdict(int)

        for domain in cpdomains:
            views, domains = domain.split()

            domains = domains.split(".")

            n = len(domains) - 1

            for i in range(n, -1, -1):
                count_paired_domain[".".join(domains[i:])] += int(views)

        result = []

        for key in count_paired_domain:
            result.append(str(count_paired_domain[key]) + " " + key)

        

        return result