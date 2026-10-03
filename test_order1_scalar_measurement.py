from order1_scalar_measurement import order1, run_verification


def main():
    results = run_verification()
    assert len(results) == 6

    # Normal, equality, opposite, zero, and negative cases.
    assert order1(5, 2)["output"] == "REJECT"
    assert order1(2, 2)["output"] == "ACCEPT"
    assert order1(-2, 2)["output"] == "REJECT"
    assert order1(0, 2)["measurement"] == 2
    assert order1(-5, 2)["measurement"] == 7

    # Symmetry of absolute difference, while the decision remains exact-match.
    assert order1(5, 2)["measurement"] == order1(-1, 2)["measurement"]

    # Repeated identical inputs are independent and reproducible.
    assert order1(5, 2) == order1(5, 2)

    # The selected substrate is one-dimensional: vector-shaped inputs are
    # intentionally rejected as outside Order 1, not silently coerced.
    try:
        order1([2], [2])
    except TypeError:
        pass
    else:
        raise AssertionError("Order 1 must remain scalar-only")

    # No persistent state: changing one call cannot alter another call.
    assert order1(2, 2)["output"] == "ACCEPT"
    assert order1(2, 2)["output"] == "ACCEPT"

    # Minimality checks at the behavioral level.
    assert order1(2, 2)["measurement"] == 0
    assert order1(5, 2)["measurement"] == 3
    assert order1(5, 2)["output"] != order1(2, 2)["output"]

    print("ALL ORDER 1 TESTS PASSED")


if __name__ == "__main__":
    main()
