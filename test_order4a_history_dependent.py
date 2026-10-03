from order4a_history_dependent import Order4A, run_verification


def main():
    traces = run_verification()
    assert len(traces) == 7

    # Baseline sequence from state 2, history 0.
    assert traces[0]["input"] == 5
    assert traces[0]["previous_state"] == 2
    assert traces[0]["previous_history"] == 0
    assert traces[0]["measurement"] == 3
    assert traces[0]["decision"] is False
    assert traces[0]["transition"] == "REPLACE"
    assert traces[0]["next_state"] == 5
    assert traces[0]["next_history"] == 1

    # Same state/input/determination as a normal rejection, but history=1
    # selects the history-dependent retain branch.
    mechanism = Order4A(initial_state=5, initial_history=1)
    controlled = mechanism.step(2)
    assert controlled["previous_state"] == 5
    assert controlled["input"] == 2
    assert controlled["measurement"] == 3
    assert controlled["decision"] is False
    assert controlled["transition"] == "RETAIN_AFTER_REJECT"
    assert controlled["next_state"] == 5

    # Causal history comparison: identical current state, input, and decision;
    # differing history causes different next state.
    history_zero = Order4A(initial_state=5, initial_history=0)
    history_one = Order4A(initial_state=5, initial_history=1)
    result_zero = history_zero.step(2)
    result_one = history_one.step(2)
    assert result_zero["previous_state"] == result_one["previous_state"] == 5
    assert result_zero["input"] == result_one["input"] == 2
    assert result_zero["measurement"] == result_one["measurement"] == 3
    assert result_zero["decision"] == result_one["decision"] is False
    assert result_zero["next_state"] == 2
    assert result_one["next_state"] == 5
    assert result_zero["next_state"] != result_one["next_state"]

    # Build history through prior events rather than supplying it directly.
    path_a = Order4A(initial_state=5, initial_history=0)
    path_a.step(5)       # ACCEPT -> state 5, history remains 0
    path_a_result = path_a.step(2)

    path_b = Order4A(initial_state=5, initial_history=0)
    path_b.step(2)       # REJECT -> state 2, history becomes 1
    path_b.step(5)       # REJECT with history 1 -> state 2, history becomes 0
    path_b.step(5)       # REJECT with history 0 -> state 5, history becomes 1
    path_b_result = path_b.step(2)

    # Both paths begin their final step at state 5 with input 2 and REJECT;
    # only generated history differs: path A has h=0, path B has h=1.
    assert path_a_result["previous_state"] == path_b_result["previous_state"] == 5
    assert path_a_result["input"] == path_b_result["input"] == 2
    assert path_a_result["measurement"] == path_b_result["measurement"] == 3
    assert path_a_result["decision"] == path_b_result["decision"] is False
    assert path_a_result["previous_history"] == 0
    assert path_b_result["previous_history"] == 1
    assert path_a_result["next_state"] == 2
    assert path_b_result["next_state"] == 5
    assert path_a_result["next_state"] != path_b_result["next_state"]

    # Acceptance retains state and leaves history unchanged.
    accepted = Order4A(initial_state=5, initial_history=1).step(5)
    assert accepted["measurement"] == 0
    assert accepted["decision"] is True
    assert accepted["transition"] == "RETAIN"
    assert accepted["next_state"] == 5
    assert accepted["next_history"] == 1

    # Deterministic reproducibility.
    assert run_verification() == run_verification()

    # Scalar-only boundary.
    try:
        Order4A([2]).step([5])
    except TypeError:
        pass
    else:
        raise AssertionError("Order 4A must remain scalar-only")

    # No rule modification: branch behavior is fixed regardless of history.
    assert Order4A(5, 0).step(2)["transition"] == "REPLACE"
    assert Order4A(5, 1).step(2)["transition"] == "RETAIN_AFTER_REJECT"

    print("ALL ORDER 4A TESTS PASSED")


if __name__ == "__main__":
    main()
