from compression.qtc.quad_tree_logic import *

def test_flat_data():
    data = [
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
    ]

    result = get_tree_for_data_grid(data, 1)
    assert isinstance(result, QtcLeaf)
    assert result.payload == 2
    assert result.width == 4
    assert result.height == 4


def test_four_square():
    data = [
        [0, 0, 2, 2],
        [0, 0, 2, 2],
        [2, 2, 0, 0],
        [2, 2, 0, 0],
    ]

    result = get_tree_for_data_grid(data, 1)
    assert isinstance(result, QtcNode)
    nw_result = result.nw_node
    ne_result = result.ne_node
    se_result = result.se_node
    sw_result = result.sw_node

    assert isinstance(nw_result, QtcLeaf)
    assert nw_result.payload == 0
    assert nw_result.width == 2
    assert nw_result.height == 2

    assert isinstance(ne_result, QtcLeaf)
    assert ne_result.payload == 2
    assert ne_result.width == 2
    assert ne_result.height == 2

    assert isinstance(se_result, QtcLeaf)
    assert se_result.payload == 0
    assert se_result.width == 2
    assert se_result.height == 2

    assert isinstance(sw_result, QtcLeaf)
    assert sw_result.payload == 2
    assert sw_result.width == 2
    assert sw_result.height == 2


def test_five_square():
    data = [
        [0, 0, 1, 2, 2],
        [0, 0, 1, 2, 2],
        [1, 1, 1, 1, 1],
        [2, 2, 1, 0, 0],
        [2, 2, 1, 0, 0],
    ]

    result = get_tree_for_data_grid(data, 1)
    assert isinstance(result, QtcNode)
    nw_result = result.nw_node
    ne_result = result.ne_node
    se_result = result.se_node
    sw_result = result.sw_node

    assert isinstance(nw_result, QtcLeaf)
    assert nw_result.payload == 0
    assert nw_result.width == 2
    assert nw_result.height == 2

    assert isinstance(ne_result, QtcLeaf)
    assert 1 <= ne_result.payload <= 2
    assert ne_result.width == 3
    assert ne_result.height == 2

    assert isinstance(se_result, QtcLeaf)
    assert 0 <= se_result.payload <= 1
    assert se_result.width == 3
    assert se_result.height == 3

    assert isinstance(sw_result, QtcLeaf)
    assert 1 <= sw_result.payload <= 2
    assert sw_result.width == 2
    assert sw_result.height == 3


def test_number_hot_mess():
    data = [
        [5, 3, 6, 1, 9],
        [8, 1, 8, 5, 3],
        [2, 5, 0, 2, 7],
        [4, 9, 7, 5, 3],
        [0, 2, 5, 7, 0],
    ]

    result = get_tree_for_data_grid(data, 1)
    assert isinstance(result, QtcNode)
    nw_result = result.nw_node
    ne_result = result.ne_node
    se_result = result.se_node
    sw_result = result.sw_node


    assert isinstance(nw_result, QtcNode)
    nw_nw_result = nw_result.nw_node
    ne_nw_result = nw_result.ne_node
    se_nw_result = nw_result.se_node
    sw_nw_result = nw_result.sw_node

    assert isinstance(nw_nw_result, QtcLeaf)
    assert nw_nw_result.payload == 5
    assert nw_nw_result.width == 1
    assert nw_nw_result.height == 1

    assert isinstance(ne_nw_result, QtcLeaf)
    assert ne_nw_result.payload == 3
    assert ne_nw_result.width == 1
    assert ne_nw_result.height == 1

    assert isinstance(se_nw_result, QtcLeaf)
    assert se_nw_result.payload == 1
    assert se_nw_result.width == 1
    assert se_nw_result.height == 1

    assert isinstance(sw_nw_result, QtcLeaf)
    assert sw_nw_result.payload == 8
    assert sw_nw_result.width == 1
    assert sw_nw_result.height == 1


    assert isinstance(ne_result, QtcNode)
    nw_ne_result = ne_result.nw_node
    ne_ne_result = ne_result.ne_node
    se_ne_result = ne_result.se_node
    sw_ne_result = ne_result.sw_node

    assert isinstance(nw_ne_result, QtcLeaf)
    assert nw_ne_result.payload == 6
    assert nw_ne_result.width == 1
    assert nw_ne_result.height == 1

    assert isinstance(ne_ne_result, QtcLeaf)
    assert 1 <= ne_ne_result.payload <= 9
    assert ne_ne_result.width == 2
    assert ne_ne_result.height == 1

    assert isinstance(se_ne_result, QtcLeaf)
    assert 3 <= se_ne_result.payload <= 5
    assert se_ne_result.width == 2
    assert se_ne_result.height == 1

    assert isinstance(sw_ne_result, QtcLeaf)
    assert sw_ne_result.payload == 8
    assert sw_ne_result.width == 1
    assert sw_ne_result.height == 1


    assert isinstance(se_result, QtcNode)
    nw_se_result = se_result.nw_node
    ne_se_result = se_result.ne_node
    se_se_result = se_result.se_node
    sw_se_result = se_result.sw_node

    assert isinstance(nw_se_result, QtcLeaf)
    assert nw_se_result.payload == 0
    assert nw_se_result.width == 1
    assert nw_se_result.height == 1

    assert isinstance(ne_se_result, QtcLeaf)
    assert 2 <= ne_se_result.payload <= 7
    assert ne_se_result.width == 2
    assert ne_se_result.height == 1

    assert isinstance(se_se_result, QtcNode)
    nw_se_se_result = se_se_result.nw_node
    ne_se_se_result = se_se_result.ne_node
    se_se_se_result = se_se_result.se_node
    sw_se_se_result = se_se_result.sw_node

    assert isinstance(nw_se_se_result, QtcLeaf)
    assert nw_se_se_result.payload == 5
    assert nw_se_se_result.width == 1
    assert nw_se_se_result.height == 1

    assert isinstance(ne_se_se_result, QtcLeaf)
    assert ne_se_se_result.payload == 3
    assert ne_se_se_result.width == 1
    assert ne_se_se_result.height == 1

    assert isinstance(se_se_se_result, QtcLeaf)
    assert se_se_se_result.payload == 0
    assert se_se_se_result.width == 1
    assert se_se_se_result.height == 1

    assert isinstance(sw_se_se_result, QtcLeaf)
    assert sw_se_se_result.payload == 7
    assert sw_se_se_result.width == 1
    assert sw_se_se_result.height == 1

    assert isinstance(sw_se_result, QtcLeaf)
    assert 5 <= sw_se_result.payload <= 7
    assert sw_se_result.width == 1
    assert sw_se_result.height == 2


    assert isinstance(sw_result, QtcNode)
    nw_sw_result = sw_result.nw_node
    ne_sw_result = sw_result.ne_node
    se_sw_result = sw_result.se_node
    sw_sw_result = sw_result.sw_node

    assert isinstance(nw_sw_result, QtcLeaf)
    assert nw_sw_result.payload == 2
    assert nw_sw_result.width == 1
    assert nw_sw_result.height == 1

    assert isinstance(ne_sw_result, QtcLeaf)
    assert ne_sw_result.payload == 5
    assert ne_sw_result.width == 1
    assert ne_sw_result.height == 1

    assert isinstance(se_sw_result, QtcLeaf)
    assert 2 <= se_sw_result.payload <= 9
    assert se_sw_result.width == 1
    assert se_sw_result.height == 2

    assert isinstance(sw_sw_result, QtcLeaf)
    assert 0 <= sw_sw_result.payload <= 4
    assert sw_sw_result.width == 1
    assert sw_sw_result.height == 2


def test_min_size():
    data = [
        [0, 2, 4, 6, 8, 0, 2, 4],
        [2, 4, 6, 8, 0, 2, 4, 6],
        [4, 6, 8, 0, 2, 4, 6, 8],
        [6, 8, 0, 2, 4, 6, 8, 0],
        [8, 0, 2, 4, 6, 8, 0, 2],
        [0, 2, 4, 6, 8, 0, 2, 4],
        [2, 4, 6, 8, 0, 2, 4, 6],
        [4, 6, 8, 0, 2, 4, 6, 8],
    ]

    result = get_tree_for_data_grid(data, 1, min_size=4)
    assert isinstance(result, QtcNode)
    nw_result = result.nw_node
    ne_result = result.ne_node
    se_result = result.se_node
    sw_result = result.sw_node

    assert isinstance(nw_result, QtcLeaf)
    assert 0 <= nw_result.payload <= 8
    assert nw_result.width == 4
    assert nw_result.height == 4

    assert isinstance(ne_result, QtcLeaf)
    assert 0 <= ne_result.payload <= 8
    assert ne_result.width == 4
    assert ne_result.height == 4

    assert isinstance(se_result, QtcLeaf)
    assert 0 <= se_result.payload <= 8
    assert se_result.width == 4
    assert se_result.height == 4

    assert isinstance(sw_result, QtcLeaf)
    assert 0 <= sw_result.payload <= 8
    assert sw_result.width == 4
    assert sw_result.height == 4


def test_node_count_leaf():
    leaf = QtcLeaf(5, 1, 1)
    assert node_count(leaf) == 1


def test_node_count_one_layer():
    node_a = QtcLeaf(5, 1, 1)
    node_b = QtcLeaf(6, 1, 1)
    node_c = QtcLeaf(7, 1, 1)
    node_d = QtcLeaf(8, 1, 1)
    root = QtcNode(node_a, node_b, node_c, node_d)

    assert node_count(root) == 5


def test_node_count_extra_layer():
    node_a = QtcLeaf(5, 2, 2)
    node_b = QtcLeaf(6, 2, 2)
    node_c = QtcLeaf(7, 2, 2)

    node_da = QtcLeaf(8, 1, 1)
    node_db = QtcLeaf(9, 1, 1)
    node_dc = QtcLeaf(0, 1, 1)
    node_dd = QtcLeaf(1, 1, 1)
    node_d = QtcNode(node_da, node_db, node_dc, node_dd)

    root = QtcNode(node_a, node_b, node_c, node_d)

    assert node_count(root) == 9


def test_depth_leaf():
    leaf = QtcLeaf(5, 1, 1)
    assert depth(leaf) == 1


def test_depth_one_layer():
    node_a = QtcLeaf(5, 1, 1)
    node_b = QtcLeaf(6, 1, 1)
    node_c = QtcLeaf(7, 1, 1)
    node_d = QtcLeaf(8, 1, 1)
    root = QtcNode(node_a, node_b, node_c, node_d)

    assert depth(root) == 2


def test_depth_extra_layer():
    node_a = QtcLeaf(5, 2, 2)
    node_b = QtcLeaf(6, 2, 2)
    node_c = QtcLeaf(7, 2, 2)

    node_da = QtcLeaf(8, 1, 1)
    node_db = QtcLeaf(9, 1, 1)
    node_dc = QtcLeaf(0, 1, 1)
    node_dd = QtcLeaf(1, 1, 1)
    node_d = QtcNode(node_da, node_db, node_dc, node_dd)

    root = QtcNode(node_a, node_b, node_c, node_d)

    assert depth(root) == 3


def test_tree_structure_array_leaf():
    leaf = QtcLeaf(5, 1, 1)
    assert tree_structure_array(leaf) == [0]


def test_depth_one_layer():
    node_a = QtcLeaf(5, 1, 1)
    node_b = QtcLeaf(6, 1, 1)
    node_c = QtcLeaf(7, 1, 1)
    node_d = QtcLeaf(8, 1, 1)
    root = QtcNode(node_a, node_b, node_c, node_d)

    assert tree_structure_array(root) == [1,0,0,0,0]


def test_depth_extra_layer__sw():
    node_a = QtcLeaf(5, 2, 2)
    node_b = QtcLeaf(6, 2, 2)
    node_c = QtcLeaf(7, 2, 2)

    node_da = QtcLeaf(8, 1, 1)
    node_db = QtcLeaf(9, 1, 1)
    node_dc = QtcLeaf(0, 1, 1)
    node_dd = QtcLeaf(1, 1, 1)
    node_d = QtcNode(node_da, node_db, node_dc, node_dd)

    root = QtcNode(node_a, node_b, node_c, node_d)

    assert tree_structure_array(root) == [1,0,0,0,1,0,0,0,0]


def test_depth_extra_layer__se():
    node_a = QtcLeaf(5, 2, 2)
    node_b = QtcLeaf(6, 2, 2)

    node_ca = QtcLeaf(8, 1, 1)
    node_cb = QtcLeaf(9, 1, 1)
    node_cc = QtcLeaf(0, 1, 1)
    node_cd = QtcLeaf(1, 1, 1)
    node_c = QtcNode(node_ca, node_cb, node_cc, node_cd)

    node_d = QtcLeaf(7, 2, 2)

    root = QtcNode(node_a, node_b, node_c, node_d)

    assert tree_structure_array(root) == [1,0,0,1,0,0,0,0,0]


def test_depth_extra_layer__ne():
    node_a = QtcLeaf(5, 2, 2)

    node_ba = QtcLeaf(8, 1, 1)
    node_bb = QtcLeaf(9, 1, 1)
    node_bc = QtcLeaf(0, 1, 1)
    node_bd = QtcLeaf(1, 1, 1)
    node_b = QtcNode(node_ba, node_bb, node_bc, node_bd)

    node_c = QtcLeaf(6, 2, 2)
    node_d = QtcLeaf(7, 2, 2)

    root = QtcNode(node_a, node_b, node_c, node_d)

    assert tree_structure_array(root) == [1,0,1,0,0,0,0,0,0]


def test_depth_extra_layer__nw():
    node_aa = QtcLeaf(8, 1, 1)
    node_ab = QtcLeaf(9, 1, 1)
    node_ac = QtcLeaf(0, 1, 1)
    node_ad = QtcLeaf(1, 1, 1)
    node_a = QtcNode(node_aa, node_ab, node_ac, node_ad)

    node_b = QtcLeaf(5, 2, 2)
    node_c = QtcLeaf(6, 2, 2)
    node_d = QtcLeaf(7, 2, 2)

    root = QtcNode(node_a, node_b, node_c, node_d)

    assert tree_structure_array(root) == [1,1,0,0,0,0,0,0,0]


def test_depth_extra_layer__complex():
    node_aaa = QtcLeaf(8, 1, 1)
    node_aab = QtcLeaf(8, 1, 1)
    node_aac = QtcLeaf(8, 1, 1)
    node_aad = QtcLeaf(8, 1, 1)

    node_aa = QtcNode(node_aaa, node_aab, node_aac, node_aad)
    node_ab = QtcLeaf(9, 2, 2)
    node_ac = QtcLeaf(0, 2, 2)
    node_ad = QtcLeaf(1, 2, 2)
    node_a = QtcNode(node_aa, node_ab, node_ac, node_ad)

    node_baa = QtcLeaf(8, 1, 1)
    node_bab = QtcLeaf(8, 1, 1)
    node_bac = QtcLeaf(8, 1, 1)
    node_bad = QtcLeaf(8, 1, 1)
    node_ba = QtcNode(node_baa, node_bab, node_bac, node_bad)

    node_bb = QtcLeaf(9, 2, 2)

    node_bca = QtcLeaf(8, 1, 1)
    node_bcb = QtcLeaf(8, 1, 1)
    node_bcc = QtcLeaf(8, 1, 1)
    node_bcd = QtcLeaf(8, 1, 1)
    node_bc = QtcNode(node_bca, node_bcb, node_bcc, node_bcd)

    node_bd = QtcLeaf(1, 2, 2)
    node_b = QtcNode(node_ba, node_bb, node_bc, node_bd)

    node_c = QtcLeaf(6, 4, 4)
    node_d = QtcLeaf(7, 2, 2)

    root = QtcNode(node_a, node_b, node_c, node_d)

    assert tree_structure_array(root) == [1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0]

