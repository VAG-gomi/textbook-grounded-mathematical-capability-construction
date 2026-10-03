"""Order 8: persistent selected-rule inference for unseen inputs.

Selected hypothesis family:
    f(x) = a*x + b

Identification from two distinct observations:
    a = (y2-y1)/(x2-x1)
    b = y1-a*x1

The identified parameters are persistently retained and can evaluate inputs
not present in the calibration examples. This is restricted affine inference,
not unrestricted function learning.
"""


class Order8:
    """Persistent affine-rule identifier and evaluator."""

    def __init__(self):
        self.slope = None
        self.intercept = None
        self.calibration = None

    @property
    def identified(self):
        return self.slope is not None and self.intercept is not None

    def identify(self, first_example, second_example):
        x1, y1 = first_example
        x2, y2 = second_example
        if x1 == x2:
            raise ValueError("distinct input values are required")

        self.slope = (y2 - y1) / (x2 - x1)
        self.intercept = y1 - self.slope * x1
        self.calibration = (first_example, second_example)
        return {
            "slope": self.slope,
            "intercept": self.intercept,
            "rule": f"f(x) = {self.slope}*x + {self.intercept}",
            "calibration": self.calibration,
        }

    def predict(self, input_value):
        if not self.identified:
            raise ValueError("rule has not been identified")
        return self.slope * input_value + self.intercept

    def evaluate(self, input_value, target):
        prediction = self.predict(input_value)
        error = target - prediction
        return {
            "input": input_value,
            "target": target,
            "prediction": prediction,
            "error": error,
        }


def run_verification():
    learner = Order8()
    identification = learner.identify((0, 1), (1, 3))
    unseen_predictions = [learner.predict(2), learner.predict(3)]
    return identification, unseen_predictions


if __name__ == "__main__":
    identification, unseen_predictions = run_verification()
    print(identification)
    print("UNSEEN PREDICTIONS", unseen_predictions)
