"""Forensic Order 3 mismatch investigation.

The candidate keeps the allowed Order 3 ingredients:
- scalar state s
- current scalar input x
- d = abs(x - s)
- exact determination
- deterministic transition control

It does not add history, a second memory variable, a target, learning,
rule-state modification, vectors, matrices, or function inference.
"""

from order2_scalar_transition import Order2
from order3_determination_control import Order3


class CandidateOrder3:
    """Non-degenerate determination-controlled scalar transition candidate."""

    def __init__(self, initial_state):
        self.state = initial_state

    def step(self, input_value):
        previous_state = self.state
        measurement = abs(input_value - previous_state)
        accepted = measurement == 0
        if accepted:
            transition = "ACCEPT_INCREMENT"
            self.state = previous_state + 1
        else:
            transition = "REJECT_REPLACE"
            self.state = input_value
        return {
            "input": input_value,
            "previous_state": previous_state,
            "measurement": measurement,
            "decision": accepted,
            "transition": transition,
            "next_state": self.state,
        }


def compare_existing_orders():
    """Exhaustively compare Order 2 and existing Order 3 over short sequences."""
    alphabet = (-2, -1, 0, 1, 2)
    sequences = [[]]
    for _ in range(4):
        sequences = sequences + [sequence + [value] for sequence in sequences for value in alphabet]

    compared = 0
    for sequence in sequences:
        order2 = Order2(initial_state=0)
        order3 = Order3(initial_state=0)
        for value in sequence:
            trace2 = order2.step(value)
            trace3 = order3.step(value)
            assert trace2["input"] == trace3["input"]
            assert trace2["measurement"] == trace3["measurement"]
            assert trace2["decision"] == trace3["decision"]
            assert trace2["next_state"] == trace3["next_state"]
        compared += 1
    return compared


def test_candidate_is_behaviorally_distinct():
    existing = Order3(initial_state=2)
    candidate = CandidateOrder3(initial_state=2)

    existing_trace = existing.step(2)
    candidate_trace = candidate.step(2)

    assert existing_trace["decision"] is True
    assert candidate_trace["decision"] is True
    assert existing_trace["next_state"] == 2
    assert candidate_trace["next_state"] == 3
    assert existing_trace["next_state"] != candidate_trace["next_state"]
    return existing_trace, candidate_trace


def test_candidate_uses_no_later_capability():
    mechanism = CandidateOrder3(initial_state=2)
    reject_trace = mechanism.step(5)
    accept_trace = mechanism.step(5)
    assert reject_trace["decision"] is False
    assert reject_trace["next_state"] == 5
    assert accept_trace["decision"] is True
    assert accept_trace["next_state"] == 6
    return reject_trace, accept_trace


if __name__ == "__main__":
    compared = compare_existing_orders()
    existing_trace, candidate_trace = test_candidate_is_behaviorally_distinct()
    reject_trace, accept_trace = test_candidate_uses_no_later_capability()
    print("EXISTING ORDER 2/3 SEQUENCES COMPARED", compared)
    print("EXISTING ORDER 3 EQUALITY TRACE", existing_trace)
    print("CANDIDATE ORDER 3 EQUALITY TRACE", candidate_trace)
    print("CANDIDATE REJECT TRACE", reject_trace)
    print("CANDIDATE ACCEPT TRACE", accept_trace)
    print("ORDER 3 MISMATCH INVESTIGATION PASSED")
