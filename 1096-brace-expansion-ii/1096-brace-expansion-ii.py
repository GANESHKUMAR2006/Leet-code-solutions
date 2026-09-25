class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)
        index = 0
        def parse_union():
            nonlocal index
            result = parse_concat()
            while index < n and expression[index] == ',':
                index += 1  
                next_set = parse_concat()
                result |= next_set
            return result
        def parse_concat():
            nonlocal index
            result = {""}
            while (index < n and expression[index] != '}' and expression[index] != ','):
                if expression[index] == '{':
                    index += 1  
                    current = parse_union()
                    index += 1  
                else:
                    current = {expression[index]}
                    index += 1
                combined = set()
                for a in result:
                    for b in current:
                        combined.add(a + b)
                result = combined
            return result

        result = parse_union()

        return sorted(result)