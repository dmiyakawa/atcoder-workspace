#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(2 * (10 ** 5))
Inf = INF = float("INF")
{% if mod or yes_str or no_str %}


{% endif %}
{% if mod %}
MOD = {{ mod }}  # type: int
{% endif %}
{% if yes_str %}
YES = "{{ yes_str }}"  # type: str
{% endif %}
{% if no_str %}
NO = "{{ no_str }}"  # type: str
{% endif %}


def main():
    {% if prediction_success %}

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    {{ input_part }}
    solve({{ actual_arguments }})
    {% else %}
    sys.stdin.readline()
    {% endif %}
{% if prediction_success %}


def solve({{ formal_arguments }}):
    return
{% endif %}


if __name__ == "__main__":
    main()
