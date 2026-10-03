"""Test whether Order 2 forces a unique non-degenerate Order 3 rule.

Allowed ingredients: scalar state s, scalar input x, exact determination
D=(x==s), deterministic current-step transition, and ordinary scalar
arithmetic. No history, second state, target, learning, or rule state.
"""


def transition(rule, state, value):
    accepted = abs(value - state) == 0
    return rule(state, value, accepted)


def replace_on_reject_increment_on_accept(state, value, accepted):
    return state + 1 if accepted else value


def replace_on_reject_add_seven_on_accept(state, value, accepted):
    return state + 7 if accepted else value


def replace_on_reject_double_on_accept(state, value, accepted):
    return 2 * state if accepted else value


def replace_on_reject_square_on_accept(state, value, accepted):
    return state * state if accepted else value


def run():
    rules = {
        "increment": replace_on_reject_increment_on_accept,
        "add_seven": replace_on_reject_add_seven_on_accept,
        "double": replace_on_reject_double_on_accept,
        "square": replace_on_reject_square_on_accept,
    }
    equality_outputs = {
        name: transition(rule, 2, 2) for name, rule in rules.items()
    }
    rejection_outputs = {
        name: transition(rule, 2, 5) for name, rule in rules.items()
    }

    assert equality_outputs == {
        "increment": 3,
        "add_seven": 9,
        "double": 4,
        "square": 4,
    }
    assert all(output == 5 for output in rejection_outputs.values())
    assert len(set(equality_outputs.values())) > 1
    return equality_outputs, rejection_outputs


if __name__ == "__main__":
    equality_outputs, rejection_outputs = run()
    print("EQUALITY OUTPUTS", equality_outputs)
    print("REJECTION OUTPUTS", rejection_outputs)
    print("NO UNIQUE NON-DEGENERATE RULE IS FORCED")
