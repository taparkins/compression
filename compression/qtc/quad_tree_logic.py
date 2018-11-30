class QtcLeaf:
    def __init__(self, payload, width, height):
        self.payload = payload
        self.width = width
        self.height = height


class QtcNode:
    def __init__(self, nw_node, ne_node, se_node, sw_node):
        self.nw_node = nw_node
        self.ne_node = ne_node
        self.se_node = se_node
        self.sw_node = sw_node


def _is_leaf_node(node):
    return isinstance(node, QtcLeaf)


def get_tree_for_data_grid(data, threshold, min_size=1):
    assert len(data) > 0 and len(data[0]) > 0

    mini = data[0][0]
    maxi = data[0][0]
    for y in range(len(data)):
        for x in range(len(data[0])):
            cur = data[y][x]
            maxi = max(maxi, cur)
            mini = min(mini, cur)

    if len(data) <= min_size or len(data[0]) <= min_size:
        return QtcLeaf(
            payload=int(round((maxi + mini) / 2)),
            width=len(data[0]),
            height=len(data),
        )

    if maxi - mini > threshold:
        nw_node, ne_node, se_node, sw_node = _subdivide(data, threshold, min_size)
        return QtcNode(nw_node, ne_node, se_node, sw_node)

    return QtcLeaf(
        payload=int(round((maxi + mini) / 2)),
        width=len(data[0]),
        height=len(data),
    )


def _subdivide(data, threshold, min_size):
    ns_div = int(len(data) / 2)
    we_div = int(len(data[0]) / 2)

    n_data = data[:ns_div]
    s_data = data[ns_div:]

    nw_data = []
    ne_data = []
    for row in n_data:
        nw_data.append(row[:we_div])
        ne_data.append(row[we_div:])

    sw_data = []
    se_data = []
    for row in s_data:
        sw_data.append(row[:we_div])
        se_data.append(row[we_div:])

    return (
        get_tree_for_data_grid(nw_data, threshold, min_size),
        get_tree_for_data_grid(ne_data, threshold, min_size),
        get_tree_for_data_grid(se_data, threshold, min_size),
        get_tree_for_data_grid(sw_data, threshold, min_size)
    )


def node_count(root):
    if _is_leaf_node(root):
        return 1
    return (
        1 +
        node_count(root.nw_node) +
        node_count(root.ne_node) +
        node_count(root.se_node) +
        node_count(root.sw_node)
    )


def depth(root):
    if _is_leaf_node(root):
        return 1
    return 1 + max([
        depth(root.nw_node),
        depth(root.ne_node),
        depth(root.se_node),
        depth(root.sw_node)
    ])


def tree_structure_array(root):
    """
    Generates an array describing the structure of this tree.
    The result array holds 0 or 1, representing whether a particular node
    is a leaf or a parent. The array is ordered by a depth-first traversal,
    traveling clockwise starting from the North-West. That is:
        North-West -> North-East -> South-East -> South-West
    """
    if _is_leaf_node(root):
        return [0]

    return (
        [1] +
        tree_structure_array(root.nw_node) +
        tree_structure_array(root.ne_node) +
        tree_structure_array(root.se_node) +
        tree_structure_array(root.sw_node)
    )

