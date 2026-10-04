class Solution:
    def checkValidString(self, s: str) -> bool:
        open = 0
        close = 0
        star = 0
        for ch in s:
            if ch == '(':
                open += 1
            elif ch == ')':
                close += 1
            else:
                star += 1
        if abs(open - close) > star:
            return False
        balance = 0
        for ch in s:
            if ch == '(':
                balance += 1
            elif ch == ')':
                balance -= 1
            else:
                balance += 1

            if balance < 0:
                return False
        balance = 0
        for ch in reversed(s):
            if ch == ')':
                balance += 1
            elif ch == '(':
                balance -= 1
            else:
                balance += 1
            if balance < 0:
                return False
        return True