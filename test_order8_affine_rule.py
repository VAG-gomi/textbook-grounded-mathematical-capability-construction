from order8_affine_rule import Order8, run_verification


def main():
    # Canonical identification: (0,1), (1,3) -> f(x)=2x+1.
    learner = Order8()
    result = learner.identify((0, 1), (1, 3))
    assert result["slope"] == 2.0
    assert result["intercept"] == 1.0
    assert learner.identified is True
    assert learner.calibration == ((0, 1), (1, 3))

    # Unseen inputs are evaluated from the retained rule, not lookup pairs.
    assert learner.predict(2) == 5.0
    assert learner.predict(3) == 7.0
    assert learner.predict(2) == learner.predict(2)

    # Persistence: later predictions work after identification returns.
    saved_slope = learner.slope
    saved_intercept = learner.intercept
    assert learner.evaluate(2, 5)["error"] == 0.0
    assert learner.slope == saved_slope
    assert learner.intercept == saved_intercept

    # Perturbing the calibration examples changes the retained rule.
    perturbed = Order8()
    perturbed.identify((0, 1), (1, 4))
    assert perturbed.slope == 3.0
    assert perturbed.intercept == 1.0
    assert perturbed.predict(2) == 7.0
    assert perturbed.predict(2) != learner.predict(2)

    # Repeated input values cannot identify a unique affine rule.
    try:
        Order8().identify((1, 2), (1, 4))
    except ValueError:
        pass
    else:
        raise AssertionError("repeated calibration input must be rejected")

    # No prediction is available before persistent rule identification.
    try:
        Order8().predict(2)
    except ValueError:
        pass
    else:
        raise AssertionError("unidentified rule must not produce a prediction")

    # Evaluation exposes nonzero error without silently changing the rule.
    mismatch = learner.evaluate(2, 6)
    assert mismatch["prediction"] == 5.0
    assert mismatch["error"] == 1.0
    assert learner.predict(2) == 5.0

    # Deterministic reproducibility.
    assert run_verification() == run_verification()

    # Scalar boundary: lists are not silently coerced into vector operations.
    try:
        Order8().identify(([0], 1), (1, 3))
    except (TypeError, ValueError):
        pass
    else:
        raise AssertionError("Order 8 must remain scalar affine inference")

    print("ALL ORDER 8 TESTS PASSED")


if __name__ == "__main__":
    main()
