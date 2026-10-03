from order4b_dynamic_rule import Order4B, run_verification


def main():
    traces = run_verification()
    assert len(traces) == 6

    # Initial rule state 0: acceptance retains state and does not change rule.
    assert traces[0]["previous_state"] == 5
    assert traces[0]["previous_rule_state"] == 0
    assert traces[0]["measurement"] == 0
    assert traces[0]["decision"] is True
    assert traces[0]["transition"] == "T_RETAIN_ACCEPT"
    assert traces[0]["next_state"] == 5
    assert traces[0]["next_rule_state"] == 0

    # First rejection under rule 0 replaces state, then updates the rule state.
    assert traces[1]["previous_state"] == 5
    assert traces[1]["previous_rule_state"] == 0
    assert traces[1]["measurement"] == 3
    assert traces[1]["decision"] is False
    assert traces[1]["transition"] == "T0_REPLACE"
    assert traces[1]["next_state"] == 2
    assert traces[1]["next_rule_state"] == 1

    # The modified rule state persists after the rejection that activated it.
    # This case is ACCEPT and therefore checks persistence, not the behavioral
    # difference between T0 and T1; that difference is tested below on REJECT.
    assert traces[2]["previous_state"] == 2
    assert traces[2]["previous_rule_state"] == 1
    assert traces[2]["input"] == 2
    assert traces[2]["measurement"] == 0
    assert traces[2]["decision"] is True
    assert traces[2]["transition"] == "T_RETAIN_ACCEPT"

    # Direct effective-rule comparison with identical current conditions.
    before = Order4B(initial_state=5, initial_rule_state=0)
    after = Order4B(initial_state=5, initial_rule_state=1)
    before_result = before.step(2)
    after_result = after.step(2)
    assert before_result["previous_state"] == after_result["previous_state"] == 5
    assert before_result["input"] == after_result["input"] == 2
    assert before_result["measurement"] == after_result["measurement"] == 3
    assert before_result["decision"] == after_result["decision"] is False
    assert before_result["transition"] == "T0_REPLACE"
    assert after_result["transition"] == "T1_RETAIN"
    assert before_result["next_state"] == 2
    assert after_result["next_state"] == 5

    # Strong causal test: both systems begin with rule state 0. System B
    # reaches rule state 1 through a prior rejection, while both systems then
    # face the same current state, input, and determination.
    system_a = Order4B(initial_state=5, initial_rule_state=0)
    present_a = system_a.step(2)

    system_b = Order4B(initial_state=2, initial_rule_state=0)
    prior_b = system_b.step(5)  # prior rejection: state 5, rule state 1
    present_b = system_b.step(2)

    assert prior_b["next_state"] == 5
    assert prior_b["next_rule_state"] == 1
    assert present_a["previous_state"] == present_b["previous_state"] == 5
    assert present_a["input"] == present_b["input"] == 2
    assert present_a["measurement"] == present_b["measurement"] == 3
    assert present_a["decision"] == present_b["decision"] is False
    assert present_a["previous_rule_state"] == 0
    assert present_b["previous_rule_state"] == 1
    assert present_a["next_state"] == 2
    assert present_b["next_state"] == 5
    assert present_a["next_state"] != present_b["next_state"]

    # Generated rule state: prior rejection modifies theta, then the modified
    # rule persists across later interactions.
    generated = Order4B(initial_state=5, initial_rule_state=0)
    activation = generated.step(2)
    later = generated.step(5)
    later_again = generated.step(0)
    assert activation["next_rule_state"] == 1
    assert later["previous_rule_state"] == 1
    assert later["decision"] is False
    assert later["transition"] == "T1_RETAIN"
    assert later["next_state"] == 2
    assert later_again["previous_rule_state"] == 1
    assert later_again["decision"] is False
    assert later_again["transition"] == "T1_RETAIN"
    assert later_again["next_state"] == 2

    # Acceptance does not reset the modified rule state.
    accepted = generated.step(2)
    assert accepted["decision"] is True
    assert accepted["next_rule_state"] == 1

    # Deterministic reproducibility.
    assert run_verification() == run_verification()

    # Scalar-only boundary.
    try:
        Order4B([5]).step([2])
    except TypeError:
        pass
    else:
        raise AssertionError("Order 4B must remain scalar-only")

    # No learning: rule state update is fixed and has no objective or error.
    assert Order4B(5, 0).step(2)["next_rule_state"] == 1

    print("ALL ORDER 4B TESTS PASSED")


if __name__ == "__main__":
    main()
