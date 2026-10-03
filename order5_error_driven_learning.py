"""Order 5: minimal deterministic evaluation-driven persistent correction.

Parameter/persistent rule state:
    theta_t in {0, 1}
Prediction:
    y_hat_t = theta_t
Target:
    y_t in {0, 1}
Error:
    e_t = y_t - y_hat_t
Update:
    theta_(t+1) = y_t if e_t != 0 else theta_t

This is a minimal supervised correction mechanism. It has an explicit
experience/evaluation/update chain, but no optimization, probability,
vector, matrix, external library, or generalization claim.
"""


class Order5:
    """Minimal deterministic evaluator with a persistent binary parameter."""

    def __init__(self, initial_parameter=0):
        if initial_parameter not in (0, 1):
            raise ValueError("initial_parameter must be 0 or 1")
        self.parameter = initial_parameter

    def step(self, target):
        if target not in (0, 1):
            raise ValueError("target must be 0 or 1")

        previous_parameter = self.parameter
        prediction = previous_parameter
        error = target - prediction
        corrected = error != 0

        if corrected:
            self.parameter = target
        else:
            self.parameter = previous_parameter

        return {
            "target": target,
            "previous_parameter": previous_parameter,
            "prediction": prediction,
            "error": error,
            "corrected": corrected,
            "next_parameter": self.parameter,
            "next_prediction": self.parameter,
        }


def run_verification():
    learner = Order5(initial_parameter=0)
    targets = [1, 1, 0, 0, 1]
    return [learner.step(target) for target in targets]


if __name__ == "__main__":
    for trace in run_verification():
        print(trace)
