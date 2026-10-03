"""Order 7: direct finite partial-function learner.

Mathematical state:
    X = declared finite domain
    Y = finite codomain
    G_t subseteq X x Y, with at most one output per input

Unknown input:
    x in X but no pair (x, y) in G_t

Known update:
    prediction = f_t(x)
    error = target - prediction
    if error != 0, replace the unique pair for x

The implementation uses a Python set of ordered pairs only as a direct
executable realization of the mathematical graph G_t. It introduces no
vectors, matrices, optimization, or external libraries.
"""


class Order7:
    """Finite partial-function learner over a declared finite domain."""

    def __init__(self, domain, codomain=(0, 1)):
        self.domain = frozenset(domain)
        self.codomain = frozenset(codomain)
        if not self.domain:
            raise ValueError("domain must be non-empty")
        if not self.codomain:
            raise ValueError("codomain must be non-empty")
        self._graph = set()

    def _validate_input(self, input_value):
        if input_value not in self.domain:
            raise ValueError("input is outside the declared domain")

    def _validate_target(self, target):
        if target not in self.codomain:
            raise ValueError("target is outside the declared codomain")

    def _pair_for(self, input_value):
        for pair in self._graph:
            if pair[0] == input_value:
                return pair
        return None

    def predict(self, input_value):
        self._validate_input(input_value)
        pair = self._pair_for(input_value)
        return None if pair is None else pair[1]

    def graph(self):
        return frozenset(self._graph)

    def is_total(self):
        return all(self._pair_for(x) is not None for x in self.domain)

    def step(self, input_value, target):
        self._validate_input(input_value)
        self._validate_target(target)

        old_pair = self._pair_for(input_value)
        previous_graph = self.graph()

        if old_pair is None:
            self._graph.add((input_value, target))
            return {
                "input": input_value,
                "target": target,
                "previous_prediction": None,
                "error": None,
                "status": "UNKNOWN_TO_LEARNED",
                "changed": True,
                "previous_graph": previous_graph,
                "next_graph": self.graph(),
            }

        prediction = old_pair[1]
        error = target - prediction
        if error != 0:
            self._graph.remove(old_pair)
            self._graph.add((input_value, target))
            status = "CORRECTED"
            changed = True
        else:
            status = "CORRECT_NO_UPDATE"
            changed = False

        return {
            "input": input_value,
            "target": target,
            "previous_prediction": prediction,
            "error": error,
            "status": status,
            "changed": changed,
            "previous_graph": previous_graph,
            "next_graph": self.graph(),
        }


def run_verification():
    learner = Order7(domain=(0, 1, 2, 3), codomain=(0, 1))
    traces = [
        learner.step(0, 1),
        learner.step(1, 0),
        learner.step(2, 1),
        learner.step(3, 0),
        learner.step(2, 0),
        learner.step(2, 1),
    ]
    return traces, learner.graph()


if __name__ == "__main__":
    traces, graph = run_verification()
    for trace in traces:
        print(trace)
    print("FINAL GRAPH", sorted(graph))
    completed = Order7((0, 1, 2, 3), (0, 1))
    for pair in ((0, 1), (1, 0), (2, 1), (3, 0)):
        completed.step(*pair)
    print("TOTAL AFTER LEARNING", completed.is_total())
