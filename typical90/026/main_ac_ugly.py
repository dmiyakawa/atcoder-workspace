#!/usr/bin/env python3


def main():
    N = int(input())
    node_to_links = {}
    num_link_to_nodes = {}
    for a, b in [tuple(int(e) for e in input().split()) for _ in range(N - 1)]:
        node_to_links.setdefault(a, set()).add(b)
        node_to_links.setdefault(b, set()).add(a)
    for node, links in node_to_links.items():
        num_link_to_nodes.setdefault(len(links), set()).add(node)

    nodes_to_show = set()
    while True:
        edge_node = next(iter(num_link_to_nodes[1]))
        nodes_to_show.add(edge_node)
        if len(nodes_to_show) == N // 2:
            break

        linked_nodes = node_to_links[edge_node]
        assert len(linked_nodes) == 1
        linked_node = next(iter(linked_nodes))
        for n in node_to_links[linked_node]:
            num_link_to_nodes[len(node_to_links[n])].remove(n)
            node_to_links[n].remove(linked_node)
            if len(node_to_links[n]) == 0:
                nodes_to_show.add(n)
                if len(nodes_to_show) == N // 2:
                    break
            else:
                num_link_to_nodes.setdefault(len(node_to_links[n]), set()).add(n)
        if len(nodes_to_show) == N // 2:
            break

        num_link_to_nodes[len(node_to_links[linked_node])].remove(linked_node)
    print(*sorted(nodes_to_show))


if __name__ == "__main__":
    main()
