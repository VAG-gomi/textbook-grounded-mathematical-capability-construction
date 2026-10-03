"""Order 4B: deterministic history-dependent rule modification.

Measurement:
    d_t = |x_t - s_t|
Determination:
    ACCEPT iff d_t == 0
Rule state:
    theta_t in {0, 1}
Transition family:
    T_0(REJECT): REPLACE state with input
    T_1(REJECT): RETAIN state
    ACCEPT retains state under both rule states
Rule-state update:
    theta_(t+1) = 1 after any REJECT; otherwise theta_t

The transition rule is selected by explicit theta, which is updated
persistently by prior events. This is dynamic rule configuration, not
learning: no objective, error criterion, parameter fitting, or external
library exists.
"""


class Order4B:
    """Minimal scalar mechanism with a persistent transition-rule state."""

    def __init__(self, initial_state, initial_rule_state=0):
        if initial_rule_state not in (0, 1):
            raise ValueError("initial_rule_state must be 0 or 1")
        self.state = initial_state
        self.rule_state = initial_rule_state

    def step(self, input_value):
        previous_state = self.state
        previous_rule_state = self.rule_state
        measurement = abs(input_value - previous_state)
        accepted = measurement == 0

        # T_theta is the currently selected transition function.
        if accepted:
            transition = "T_RETAIN_ACCEPT"
            self.state = previous_state
        elif previous_rule_state == 0:
            transition = "T0_REPLACE"
            self.state = input_value
        else:
            transition = "T1_RETAIN"
            self.state = previous_state

        output = "ACCEPT" if accepted else "REJECT"

        # U updates the rule state after the current determination. A rejection
        # activates rule configuration 1 and it persists thereafter.
        if accepted:
            self.rule_state = previous_rule_state
        else:
            self.rule_state = 1

        return {
            "input": input_value,
            "previous_state": previous_state,
            "previous_rule_state": previous_rule_state,
            "measurement": measurement,
            "decision": accepted,
            "output": output,
            "transition": transition,
            "next_state": self.state,
            "next_rule_state": self.rule_state,
        }


def run_verification():
    mechanism = Order4B(initial_state=5, initial_rule_state=0)
    inputs = [5, 2, 2, 0, 0, -3]
    return [mechanism.step(value) for value in inputs]


if __name__ == "__main__":
    for trace in run_verification():
        print(trace)
