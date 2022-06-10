#!/usr/bin/env python3

import re
from typing import List


class Calculator:
    def __init__(self):
        self._dic = {}

    def parse_line(self, line):
        if line.startswith("int"):
            m = re.match(r"int ([a-z]) = (.+) ;", line)
            self._dic[m.group(1)] = self.parse_int_expression(m.group(2))
        elif line.startswith("print_int"):
            m = re.match(r"print_int (.+) ;", line)
            print(self.parse_int_expression(m.group(1)))
        elif line.startswith("vec"):
            m = re.match(r"vec ([a-z]) = (.+) ;", line)
            vec = self.parse_vec_expression(m.group(2))
            self._dic[m.group(1)] = vec
        elif line.startswith("print_vec"):
            m = re.match(r"print_vec (.+) ;", line)
            print("[", *self.parse_vec_expression(m.group(1)), "]")
        else:
            raise RuntimeError(f"Unexpected expression \"{line}\"")

    def parse_int_term(self, term: str) -> int:
        return self._dic[term] if term.isalpha() else int(term)

    def parse_int_expression(self, expr) -> int:
        term_or_ops = expr.split()
        terms = term_or_ops[::-2]
        ops = term_or_ops[-2::-2]
        val = self.parse_int_term(terms.pop())
        while ops:
            next_val = self.parse_int_term(terms.pop())
            op = ops.pop()
            if op == "-":
                val = val - next_val
            else:
                val = val + next_val
        return val

    def parse_vec_term(self, term: str) -> List[int]:
        if term.isalpha():
            return self._dic[term]
        else:
            return [self.parse_int_term(term) for term in term.split()[1::2]]

    def parse_vec_expression(self, expr) -> List[int]:
        term_or_ops = re.split(r"(\+|-)", expr)
        terms = [term.strip() for term in term_or_ops[::-2]]
        ops = term_or_ops[-2::-2]
        val = self.parse_vec_term(terms.pop())
        while ops:
            next_val = self.parse_vec_term(terms.pop())
            op = ops.pop()
            if op == "-":
                val = [a - b for a, b in zip(val, next_val)]
            else:
                val = [a + b for a, b in zip(val, next_val)]
        return val


def main():
    N = int(input())
    calc = Calculator()
    for _ in range(N):
        calc.parse_line(input())


if __name__ == "__main__":
    main()
