class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for s in strs:
            encoded_s += f"{len(s):04d}"+s
        return encoded_s


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            l = int(s[i:i+4])
            res.append(s[i+4:i+4+l])
            i+=4+l
        return res