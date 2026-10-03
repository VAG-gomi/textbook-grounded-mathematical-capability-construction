from order2_scalar_transition import Order2, run_verification


def main():
    traces = run_verification()
    assert len(traces) == 5

    # Sequence: initial state 2; inputs 5, 5, 2, 0, -3.
    assert traces[0] == {
        "input": 5,
        "previous_state": 2,
        "measurement": 3,
        "decision": False,
        "output": "REJECT",
        "next_state": 5,
    }
    assert traces[1]["previous_state"] == 5
    assert traces[1]["measurement"] == 0
    assert traces[1]["output"] == "ACCEPT"
    assert traces[1]["next_state"] == 5
    assert traces[2]["previous_state"] == 5
    assert traces[2]["measurement"] == 3
    assert traces[2]["next_state"] == 2
    assert traces[3]["previous_state"] == 2
    assert traces[3]["measurement"] == 2
    assert traces[3]["next_state"] == 0
    assert traces[4]["previous_state"] == 0
    assert traces[4]["measurement"] == 3
    assert traces[4]["next_state"] == -3

    # State is persistent: a repeated input can become an exact match after
    # the first transition, without any learning or parameter adjustment.
    mechanism = Order2(2)
    first = mechanism.step(5)
    second = mechanism.step(5)
    assert first["output"] == "REJECT"
    assert second["output"] == "ACCEPT"
    assert second["previous_state"] == 5

    # History dependence: the same current input can produce different output
    # depending on the prior state.
    from_initial = Order2(2).step(5)
    after_prior_input = Order2(2)
    after_prior_input.step(5)
    after_prior = after_prior_input.step(5)
    assert from_initial["output"] == "REJECT"
    assert after_prior["output"] == "ACCEPT"

    # Exact deterministic reproducibility for the same initial state and input.
    first_run = run_verification()
    second_run = run_verification()
    assert first_run == second_run

    # Scalar-only dimensional consistency. Vector-shaped inputs are not
    # silently accepted as Order 2 has not introduced vector mathematics.
    try:
        Order2([2]).step([5])
    except TypeError:
        pass
    else:
        raise AssertionError("Order 2 must remain scalar-only")

    # No learning: state becomes the current input exactly, with no parameter
    # inferred from the sequence.
    mechanism = Order2(10)
    trace = mechanism.step(4)
    assert trace["next_state"] == 4
    assert mechanism.state == 4

    print("ALL ORDER 2 TESTS PASSED")


if __name__ == "__main__":
    main()
