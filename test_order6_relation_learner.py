from order6_relation_learner import (
    Order6,
    run_independent_correction_test,
    run_preservation_test,
)


def main():
    # Test A: complementary relation and non-interference.
    preservation, table = run_preservation_test()
    assert preservation[0]["input"] == 0
    assert preservation[0]["prediction"] == 0
    assert preservation[0]["error"] == 1
    assert preservation[0]["corrected"] is True
    assert preservation[0]["next_m0"] == 1
    assert preservation[0]["next_m1"] == 0
    assert table == (1, 0)

    # Training input 0 must not modify the association for input 1.
    assert preservation[1]["input"] == 1
    assert preservation[1]["prediction"] == 0
    assert preservation[1]["error"] == 0
    assert preservation[1]["corrected"] is False
    assert preservation[1]["next_m0"] == 1
    assert preservation[1]["next_m1"] == 0
    assert preservation[2]["prediction"] == 1
    assert preservation[3]["prediction"] == 0
    assert preservation[3]["corrected"] is False

    # Test B: both slots undergo independent corrections.
    independent, independent_table = run_independent_correction_test()
    assert independent[0]["error"] == 1
    assert independent[0]["next_m0"] == 1
    assert independent[0]["next_m1"] == 0
    assert independent[1]["input"] == 1
    assert independent[1]["prediction"] == 0
    assert independent[1]["error"] == 1
    assert independent[1]["corrected"] is True
    assert independent[1]["next_m0"] == 1
    assert independent[1]["next_m1"] == 1
    assert independent_table == (1, 1)
    assert independent[2]["corrected"] is False
    assert independent[3]["corrected"] is False

    # Input-dependent retrieval: distinct learned associations remain distinct.
    learner = Order6(0, 0)
    learner.step(0, 1)
    learner.step(1, 0)
    assert learner.predict(0) == 1
    assert learner.predict(1) == 0

    # Updating one selected slot leaves the other slot unchanged.
    learner = Order6(0, 0)
    learner.step(0, 1)
    assert learner.table() == (1, 0)
    learner.step(1, 1)
    assert learner.table() == (1, 1)
    assert learner.predict(0) == 1
    assert learner.predict(1) == 1

    # Bidirectional cross-input non-interference: changing m1 back to 0
    # leaves the already learned m0=1 invariant.
    learner.step(1, 0)
    assert learner.table() == (1, 0)
    assert learner.predict(0) == 1
    assert learner.predict(1) == 0

    # Deterministic reproducibility.
    assert run_preservation_test() == run_preservation_test()
    assert run_independent_correction_test() == run_independent_correction_test()

    # Binary domain and codomain boundaries.
    for bad_input in (-1, 2):
        try:
            Order6().predict(bad_input)
        except ValueError:
            pass
        else:
            raise AssertionError("input domain must remain {0, 1}")

    for bad_target in (-1, 2):
        try:
            Order6().step(0, bad_target)
        except ValueError:
            pass
        else:
            raise AssertionError("target codomain must remain {0, 1}")

    # No vector/matrix coercion is allowed.
    try:
        Order6().step([0], 1)
    except ValueError:
        pass
    except TypeError:
        pass
    else:
        raise AssertionError("Order 6 must remain a two-slot scalar relation")

    print("ALL ORDER 6 TESTS PASSED")


if __name__ == "__main__":
    main()
