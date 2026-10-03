"""Order 6: minimal finite input-output relation learner.

Domain and codomain:
    X = {0, 1}, Y = {0, 1}
Persistent relation:
    f(0) = m0, f(1) = m1
Prediction:
    y_hat = m_x
Error:
    e = y - y_hat
Update:
    modify only the selected slot when e != 0

This demonstrates learning of a finite binary function on the specifically defined domain X={0,1}; it does not establish general function learning. No vector, matrix, external library, optimization, or neural-network component is used.
"""


class Order6:
    """Two-slot deterministic learner for a function on {0, 1}."""

    def __init__(self, initial_m0=0, initial_m1=0):
        self._validate_binary(initial_m0, "initial_m0")
        self._validate_binary(initial_m1, "initial_m1")
        self.m0 = initial_m0
        self.m1 = initial_m1

    @staticmethod
    def _validate_binary(value, name):
        if value not in (0, 1):
            raise ValueError(f"{name} must be 0 or 1")

    def predict(self, input_value):
        self._validate_binary(input_value, "input_value")
        return self.m0 if input_value == 0 else self.m1

    def step(self, input_value, target):
        self._validate_binary(input_value, "input_value")
        self._validate_binary(target, "target")

        previous_m0 = self.m0
        previous_m1 = self.m1
        prediction = self.predict(input_value)
        error = target - prediction
        corrected = error != 0

        if corrected:
            if input_value == 0:
                self.m0 = target
            else:
                self.m1 = target

        return {
            "input": input_value,
            "target": target,
            "previous_m0": previous_m0,
            "previous_m1": previous_m1,
            "prediction": prediction,
            "error": error,
            "corrected": corrected,
            "next_m0": self.m0,
            "next_m1": self.m1,
            "next_prediction": self.predict(input_value),
        }

    def table(self):
        return (self.m0, self.m1)


def run_preservation_test():
    learner = Order6(0, 0)
    traces = [
        learner.step(0, 1),
        learner.step(1, 0),
        learner.step(0, 1),
        learner.step(1, 0),
    ]
    return traces, learner.table()


def run_independent_correction_test():
    learner = Order6(0, 0)
    traces = [
        learner.step(0, 1),
        learner.step(1, 1),
        learner.step(0, 1),
        learner.step(1, 1),
    ]
    return traces, learner.table()


if __name__ == "__main__":
    preservation_traces, preservation_table = run_preservation_test()
    independent_traces, independent_table = run_independent_correction_test()
    print("PRESERVATION")
    for trace in preservation_traces:
        print(trace)
    print("FINAL TABLE", preservation_table)
    print("INDEPENDENT CORRECTION")
    for trace in independent_traces:
        print(trace)
    print("FINAL TABLE", independent_table)
