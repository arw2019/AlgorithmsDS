from collections import defaultdict
import re


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        tokens = [c for c in re.split("([A-Z]{1}[a-z]?|\(|\)|\d+)", formula) if c]
        stack, i = [defaultdict(int)], 0
        while i < len(tokens):
            token = tokens[i]
            if token == "(":
                stack.append(defaultdict(int))
            else:
                count = 1
                # Check if next token is a number.
                if i + 1 < len(tokens) and tokens[i + 1].isdigit():
                    count = int(tokens[i + 1])
                    i += 1
                atoms = stack.pop() if token == ")" else {token: 1}
                # Combine counts of atoms.
                for atom in atoms:
                    stack[-1][atom] += atoms[atom] * count
            i += 1
        return "".join(
            [
                atom + (str(count) if count > 1 else "")
                for atom, count in sorted(stack[-1].items())
            ]
        )
