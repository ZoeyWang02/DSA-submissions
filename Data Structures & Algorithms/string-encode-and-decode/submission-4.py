class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "？"
        ch = ""
        for s in strs:
            ch = ch+s+"！"
        return ch[:-1]
    def decode(self, s: str) -> List[str]:
        if s=="？":
            return []
        return s.split('！')