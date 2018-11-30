from compression.qtc import quad_tree_logic

def serialize(root):
    header = _get_header_bytes(root)
    body = _get_body_bytes(root)

    return header + body


def _is_leaf_node(node):
    return isinstance(node, quad_tree_logic.QtcLeaf)


def _get_header_bytes(root):
    def _leaf_structure_array(node):
        if _is_leaf_node(node):
            return [0]
        return (
            [1] +
            _leaf_structure_array(node.nw_node) +
            _leaf_structure_array(node.ne_node) +
            _leaf_structure_array(node.se_node) +
            _leaf_structure_array(node.sw_node)
        )

    return _leaf_structure_array(root)


def _get_body_bytes(root):
    if _is_leaf_node(root):
        return [root.payload]
    return (
        _get_body_bytes(root.nw_node) +
        _get_body_bytes(root.ne_node) +
        _get_body_bytes(root.se_node) +
        _get_body_bytes(root.sw_node)
    )

