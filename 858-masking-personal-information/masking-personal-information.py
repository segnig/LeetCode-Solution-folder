class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            email = s.split("@")
            domain = email[-1].split(".")
            return email[0][0].lower() + "*****" + email[0][-1].lower() + "@" + domain[0].lower() + "." + domain[-1].lower()

        number = set("09877654321")
        nums = ""
        for x in s:
            if x in number:
                nums += x

        if len(nums) == 10:
            return "***-***-" + nums[-4:]
        if len(nums) == 11:
            return "+*-***-***-" + nums[-4:]
        
        if len(nums) == 12:
            return "+**-***-***-" + nums[-4:]
        return "+***-***-***-" + nums[-4:]
        

        

    