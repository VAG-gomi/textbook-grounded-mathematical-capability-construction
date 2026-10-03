"""Order 1: minimal scalar measurement and determination mechanism.

Mathematical model:
    d(x, a) = |x - a|
    decision = ACCEPT if d(x, a) == 0 else REJECT

No persistent state, learning, probability, external libraries, or model is used.
"""


def order1(input_value, reference_value):
    """Return the input, measurement, decision, and output trace.

    The reference value is an explicit fixed parameter for one evaluation.
    It is not persistent memory and is not updated by this function.
    """
    measurement = abs(input_value - reference_value)
    accepted = measurement == 0
    output = "ACCEPT" if accepted else "REJECT"
    return {
        "input": input_value,
        "reference": reference_value,
        "measurement": measurement,
        "decision": accepted,
        "output": output,
    }


def run_verification():
    """Run deterministic verification cases and return their traces."""
    reference = 2
    cases = [
        (5, "normal input"),
        (2, "boundary/equality case"),
        (-2, "opposite case"),
        (0, "zero input"),
        (-5, "negative input"),
        (2, "repeated identical input"),
    ]

    results = []
    for value, label in cases:
        trace = order1(value, reference)
        trace["label"] = label
        results.append(trace)

    # Deterministic reproducibility: identical inputs and reference give
    # identical complete traces.
    first = order1(5, reference)
    second = order1(5, reference)
    assert first == second

    # Dimensional consistency for the selected scalar substrate.
    assert isinstance(reference, (int, float))
    assert all(isinstance(value, (int, float)) for value, _ in cases)

    # Exact mathematical assertions.
    assert order1(2, reference)["measurement"] == 0
    assert order1(2, reference)["output"] == "ACCEPT"
    assert order1(5, reference)["measurement"] == 3
    assert order1(-2, reference)["measurement"] == 4
    assert order1(0, reference)["measurement"] == 2

    return results


if __name__ == "__main__":
    for result in run_verification():
        print(result)
