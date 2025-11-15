import re
class Solution:

    def validIPAddressRegex(self, queryIP: str) -> str:

        v4Split = "0|[1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]"

        if re.fullmatch(fr"^({v4Split}\.){{3}}({v4Split})$", queryIP):
            return "IPv4"

    def validIPAddressPython(self, queryIP: str) -> str:

        if queryIP[3] == ".":
            split = queryIP.split(".")
            if len(split) == 4:
                for s in split:
                    if not (s[0] != "0" or s.isdigit() or 0 <= int(s) <= 255):
                        return "Neither"
                return "IPv4"

        if queryIP[4] == ":":
            split = queryIP.split(":")
            if len(split) == 8:
                for s in split:
                    if 1 <= len(s) <= 4:
                        for c in s:
                            if not (
                                    "a" <= c <= "f"
                                    or "A" <= c <= "F"
                                    or "0" <= c <= "9"
                            ):
                                return 'Neither'
                return "IPv6"

        return "Neither"


ip = "256.256.256.256"

print(Solution().validIPAddressPython(ip))
print(Solution().validIPAddressRegex("172.16.254.1"))