"""Order 4A: deterministic history-dependent transition.

Measurement:
    d_t = |x_t - s_t|
Determination:
    ACCEPT iff d_t == 0
Persistent one-bit history state:
    h_t in {0, 1}, updated deterministically from the current determination
Fixed transition rule:
    if ACCEPT: s_(t+1) = s_t
    if REJECT and h_t == 0: s_(t+1) = x_t
    if REJECT and h_t == 1: s_(t+1) = s_t

The rule is fixed. History is an explicit input to the rule; it does not
modify the rule itself. No learning, optimization, probability, vector,
matrix, or external library is used.
"""


class Order4A:
    """Minimal scalar mechanism with a history-dependent fixed transition."""

    def __init__(self, initial_state, initial_history=0):
        if initial_history not in (0, 1):
            raise ValueError("initial_history must be 0 or 1")
        self.state = initial_state
        self.history = initial_history

    def step(self, input_value):
        previous_state = self.state
        previous_history = self.history
        measurement = abs(input_value - previous_state)
        accepted = measurement == 0

        # One fixed transition function T(s, x, D, h). History is data
        # supplied to the fixed rule, not a rule parameter that changes.
        if accepted:
            transition = "RETAIN"
            self.state = previous_state
        elif previous_history == 0:
            transition = "REPLACE"
            self.state = input_value
        else:
            transition = "RETAIN_AFTER_REJECT"
            self.state = previous_state

        output = "ACCEPT" if accepted else "REJECT"

        # Minimal history update: toggle after each rejection; retain after
        # acceptance. This makes prior events causally testable.
        if accepted:
            self.history = previous_history
        else:
            self.history = 1 - previous_history

        return {
            "input": input_value,
            "previous_state": previous_state,
            "previous_history": previous_history,
            "measurement": measurement,
            "decision": accepted,
            "output": output,
            "transition": transition,
            "next_state": self.state,
            "next_history": self.history,
        }


def run_verification():
    mechanism = Order4A(initial_state=2, initial_history=0)
    inputs = [5, 5, 2, 5, 2, 2, 0]
    return [mechanism.step(value) for value in inputs]


if __name__ == "__main__":
    for trace in run_verification():
        print(trace)
