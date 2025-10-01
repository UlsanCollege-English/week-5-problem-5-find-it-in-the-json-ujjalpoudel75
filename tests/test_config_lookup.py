from src.config_lookup import find_key

# ---- Normal (4) ----
def test_found_at_top_level():
    d = {"a": 1, "b": {"a": 2}}
    assert find_key(d, "a") == 1

def test_found_nested_in_dict():
    d = {"x": {"y": {"z": {"flag": True}}}}
    assert find_key(d, "flag") is True

def test_found_in_list_of_dicts():
    d = [{"k": 1}, {"k": 2}, {"target": 9}]
    assert find_key(d, "target") == 9

def test_not_found_returns_none():
    d = {"x": [1, 2, {"y": 3}]}
    assert find_key(d, "nope") is None

# ---- Edge (3) ----
def test_value_is_falsy_but_present():
    d = {"a": 0}
    assert find_key(d, "a") == 0

def test_empty_structures():
    assert find_key([], "a") is None
    assert find_key({}, "a") is None

def test_tuple_handling():
    d = ({"a": 1}, {"b": 2})
    assert find_key(d, "b") == 2

# ---- Complex (3) ----
def test_large_nested_mix():
    d = {"a":[{"b":[{"c":[{"d":{"target":42}}]}]}]}
    assert find_key(d, "target") == 42

def test_early_short_circuit_left_to_right():
    d = [{"target": 1}, {"target": 2}]
    assert find_key(d, "target") == 1

def test_multiple_levels_same_key_first_is_returned():
    d = {"k": {"k": {"k": 7}}}
    assert find_key(d, "k") == {"k": {"k": 7}}
