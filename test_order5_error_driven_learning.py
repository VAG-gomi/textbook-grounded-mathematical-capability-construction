from order5_error_driven_learning import Order5, run_verification


def main():
    traces = run_verification()
    assert len(traces) == 5

    # Initial parameter 0, target sequence [1, 1, 0, 0, 1].
    assert traces[0] == {
        "target": 1,
        "previous_parameter": 0,
        "prediction": 0,
        "error": 1,
        "corrected": True,
        "next_parameter": 1,
        "next_prediction": 1,
    }
    assert traces[1] == {
        "target": 1,
        "previous_parameter": 1,
        "prediction": 1,
        "error": 0,
        "corrected": False,
        "next_parameter": 1,
        "next_prediction": 1,
    }
    assert traces[2]["target"] == 0
    assert traces[2]["prediction"] == 1
    assert traces[2]["error"] == -1
    assert traces[2]["corrected"] is True
    assert traces[2]["next_parameter"] == 0
    assert traces[3]["error"] == 0
    assert traces[3]["corrected"] is False
    assert traces[3]["next_parameter"] == 0
    assert traces[4]["error"] == 1
    assert traces[4]["next_parameter"] == 1

    # Persistent correction changes future prediction.
    learner = Order5(initial_parameter=0)
    first = learner.step(1)
    later = learner.step(1)
    assert first["prediction"] == 0
    assert first["next_parameter"] == 1
    assert later["prediction"] == 1
    assert later["error"] == 0

    # Error-free evaluation does not modify the parameter.
    stable = Order5(initial_parameter=1)
    result = stable.step(1)
    assert result["error"] == 0
    assert result["corrected"] is False
    assert result["next_parameter"] == 1

    # A changed target causes a new evaluated correction.
    reversal = Order5(initial_parameter=1)
    result = reversal.step(0)
    assert result["error"] == -1
    assert result["corrected"] is True
    assert result["next_parameter"] == 0

    # Deterministic reproducibility.
    assert run_verification() == run_verification()

    # Binary minimality boundary.
    try:
        Order5(initial_parameter=2)
    except ValueError:
        pass
    else:
        raise AssertionError("Order 5 parameter must remain binary")

    try:
        Order5().step(2)
    except ValueError:
        pass
    else:
        raise AssertionError("Order 5 target must remain binary")

    # No external state or hidden adjustment: parameter equals target exactly
    # after correction and remains unchanged after zero error.
    learner = Order5(0)
    assert learner.step(1)["next_parameter"] == 1
    assert learner.step(1)["next_parameter"] == 1

    print("ALL ORDER 5 TESTS PASSED")


if __name__ == "__main__":
    main()
