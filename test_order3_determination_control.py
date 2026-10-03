from order3_determination_control import Order3, run_verification


def main():
    traces = run_verification()
    assert len(traces) == 7

    # Initial state 2, inputs [5, 5, 2, 2, 0, 0, -3].
    assert traces[0] == {
        "input": 5,
        "previous_state": 2,
        "measurement": 3,
        "decision": False,
        "output": "REJECT",
        "transition": "REPLACE",
        "next_state": 5,
    }
    assert traces[1] == {
        "input": 5,
        "previous_state": 5,
        "measurement": 0,
        "decision": True,
        "output": "ACCEPT",
        "transition": "RETAIN",
        "next_state": 5,
    }
    assert traces[2]["input"] == 2
    assert traces[2]["previous_state"] == 5
    assert traces[2]["measurement"] == 3
    assert traces[2]["transition"] == "REPLACE"
    assert traces[2]["next_state"] == 2
    assert traces[3]["measurement"] == 0
    assert traces[3]["transition"] == "RETAIN"
    assert traces[3]["next_state"] == 2
    assert traces[4]["input"] == 0
    assert traces[4]["previous_state"] == 2
    assert traces[4]["transition"] == "REPLACE"
    assert traces[4]["next_state"] == 0
    assert traces[5]["measurement"] == 0
    assert traces[5]["transition"] == "RETAIN"
    assert traces[5]["next_state"] == 0
    assert traces[6]["input"] == -3
    assert traces[6]["previous_state"] == 0
    assert traces[6]["measurement"] == 3
    assert traces[6]["transition"] == "REPLACE"
    assert traces[6]["next_state"] == -3

    # Both determination outcomes control distinct named branches.
    mechanism = Order3(2)
    rejected = mechanism.step(5)
    accepted = mechanism.step(5)
    assert rejected["decision"] is False
    assert rejected["transition"] == "REPLACE"
    assert accepted["decision"] is True
    assert accepted["transition"] == "RETAIN"

    # A retained state remains unchanged across repeated accepted inputs.
    before = mechanism.state
    repeat = mechanism.step(5)
    assert repeat["transition"] == "RETAIN"
    assert repeat["next_state"] == before == 5

    # Deterministic reproducibility.
    assert run_verification() == run_verification()

    # Scalar-only boundary.
    try:
        Order3([2]).step([5])
    except TypeError:
        pass
    else:
        raise AssertionError("Order 3 must remain scalar-only")

    # No learning: branch behavior is fixed and state is not a fitted parameter.
    mechanism = Order3(10)
    result = mechanism.step(4)
    assert result["transition"] == "REPLACE"
    assert result["next_state"] == 4

    print("ALL ORDER 3 TESTS PASSED")


if __name__ == "__main__":
    main()
