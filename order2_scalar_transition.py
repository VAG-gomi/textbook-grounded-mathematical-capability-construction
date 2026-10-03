"""Order 2: deterministic scalar state transition.

Mathematical model:
    measurement: d_t = |x_t - s_t|
    determination: ACCEPT iff d_t == 0
    transition: s_(t+1) = x_t

The state is persistent across calls to step(), but no learning,
threshold, probability, vector, matrix, or external library is used.
"""


class Order2:
    """A minimal deterministic scalar state-transition mechanism."""

    def __init__(self, initial_state):
        self.state = initial_state

    def step(self, input_value):
        """Process one scalar input and deterministically replace the state."""
        previous_state = self.state
        measurement = abs(input_value - previous_state)
        accepted = measurement == 0
        output = "ACCEPT" if accepted else "REJECT"

        # The sole transition rule: s_(t+1) = x_t.
        self.state = input_value

        return {
            "input": input_value,
            "previous_state": previous_state,
            "measurement": measurement,
            "decision": accepted,
            "output": output,
            "next_state": self.state,
        }


def run_verification():
    """Run a deterministic sequence and return complete transition traces."""
    mechanism = Order2(initial_state=2)
    inputs = [5, 5, 2, 0, -3]
    return [mechanism.step(value) for value in inputs]


if __name__ == "__main__":
    for trace in run_verification():
        print(trace)
