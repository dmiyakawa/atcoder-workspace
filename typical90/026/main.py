#!/usr/bin/env python3


def main():
    N = int(input())
    node_to_links = {}
    for a, b in [tuple(int(e) for e in input().split()) for _ in range(N - 1)]:
        node_to_links.setdefault(a, set()).add(b)
        node_to_links.setdefault(b, set()).add(a)

    reds, greens = {1}, set()
    nodes = {1}
    while nodes:
        node = nodes.pop()
        linked_nodes = node_to_links[node]
        opposite = greens if node in reds else reds
        for linked_node in linked_nodes:
            if linked_node not in opposite:
                opposite.add(linked_node)
                nodes.add(linked_node)

    if len(reds) > len(greens):
        print(*sorted(reds)[:N // 2])
    else:
        print(*sorted(greens)[:N // 2])


if __name__ == "__main__":
    main()
