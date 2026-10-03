"""Order 3: determination-controlled deterministic transition.

Measurement:
    d_t = |x_t - s_t|
Determination:
    ACCEPT iff d_t == 0
Controlled transition:
    ACCEPT -> s_(t+1) = s_t       (retain)
    REJECT -> s_(t+1) = x_t       (replace)

The branch is selected by the current determination. No learning,
threshold, probability, vector, matrix, or external library is used.
"""


class Order3:
    """Minimal scalar state machine with determination-controlled transition."""

    def __init__(self, initial_state):
        self.state = initial_state

    def step(self, input_value):
        previous_state = self.state
        measurement = abs(input_value - previous_state)
        accepted = measurement == 0

        if accepted:
            transition = "RETAIN"
            self.state = previous_state
        else:
            transition = "REPLACE"
            self.state = input_value

        output = "ACCEPT" if accepted else "REJECT"
        return {
            "input": input_value,
            "previous_state": previous_state,
            "measurement": measurement,
            "decision": accepted,
            "output": output,
            "transition": transition,
            "next_state": self.state,
        }


def run_verification():
    mechanism = Order3(initial_state=2)
    inputs = [5, 5, 2, 2, 0, 0, -3]
    return [mechanism.step(value) for value in inputs]


if __name__ == "__main__":
    for trace in run_verification():
        print(trace)
