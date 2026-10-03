from order7_partial_function import UNKNOWN, Order7, run_verification


DOMAIN = (0, 1, 2, 3)


def main():
    learner = Order7(DOMAIN, (0, 1))
    assert learner.graph() == frozenset()
    assert learner.is_total() is False
    assert learner.predict(2) is UNKNOWN

    # Unknown input becomes a stored association without pretending that a
    # numerical prediction or error existed before the first experience.
    first = learner.step(2, 1)
    assert first["status"] == "UNKNOWN_TO_LEARNED"
    assert first["previous_prediction"] is UNKNOWN
    assert first["error"] is None
    assert learner.graph() == frozenset({(2, 1)})

    # The correction rule is numerical, so non-numeric codomains are rejected.
    try:
        Order7(DOMAIN, ("zero", "one"))
    except TypeError:
        pass
    else:
        raise AssertionError("Order 7 codomain must be numeric for subtraction-based correction")

    # Learn the four-element alternating function.
    learner = Order7(DOMAIN, (0, 1))
    for pair in ((0, 1), (1, 0), (2, 1), (3, 0)):
        result = learner.step(*pair)
        assert result["status"] == "UNKNOWN_TO_LEARNED"
    expected = frozenset({(0, 1), (1, 0), (2, 1), (3, 0)})
    assert learner.graph() == expected
    assert learner.is_total() is True
    assert [learner.predict(x) for x in DOMAIN] == [1, 0, 1, 0]

    # Repeating a correct pair produces zero error and no graph change.
    unchanged = learner.step(1, 0)
    assert unchanged["status"] == "CORRECT_NO_UPDATE"
    assert unchanged["error"] == 0
    assert unchanged["changed"] is False
    assert learner.graph() == expected

    # Selective correction changes only the addressed pair.
    corrected = learner.step(2, 0)
    assert corrected["status"] == "CORRECTED"
    assert corrected["error"] == -1
    assert learner.graph() == frozenset({(0, 1), (1, 0), (2, 0), (3, 0)})
    assert learner.predict(0) == 1
    assert learner.predict(1) == 0
    assert learner.predict(3) == 0

    # Reverse selective correction: input 2 changes back while all
    # associations for the other inputs remain unchanged.
    learner.step(2, 1)
    assert learner.graph() == expected
    assert learner.predict(0) == 1
    assert learner.predict(1) == 0
    assert learner.predict(3) == 0

    # Function uniqueness: one input must never have two stored outputs.
    for x in DOMAIN:
        outputs = [pair[1] for pair in learner.graph() if pair[0] == x]
        assert len(outputs) == 1

    # Domain enforcement.
    for bad_input in (-1, 4):
        try:
            learner.predict(bad_input)
        except ValueError:
            pass
        else:
            raise AssertionError("input outside domain must be rejected")
        try:
            learner.step(bad_input, 0)
        except ValueError:
            pass
        else:
            raise AssertionError("input outside domain must be rejected")

    # Codomain enforcement.
    for bad_target in (-1, 2):
        try:
            learner.step(0, bad_target)
        except ValueError:
            pass
        else:
            raise AssertionError("target outside codomain must be rejected")

    # Deterministic reproducibility.
    first_run = run_verification()
    second_run = run_verification()
    assert first_run == second_run
    assert first_run[1] == expected

    # Structural boundary: no vector-like input is silently accepted.
    try:
        learner.predict([0])
    except (ValueError, TypeError):
        pass
    else:
        raise AssertionError("Order 7 input must be a declared scalar domain element")

    print("ALL ORDER 7 TESTS PASSED")


if __name__ == "__main__":
    main()
