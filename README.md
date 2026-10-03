# Textbook-Grounded Mathematical Capability Construction

## Orders 1–8: from scalar measurement to selected-rule inference

This is a **research and forensic repository** that constructs and tests a sequence of minimal deterministic artificial mechanisms from mathematical capabilities supplied by the provided HSC Higher Mathematics textbook.

It is not a neural-network implementation and does not claim general intelligence. The central question is:

> What capability is mathematically forced by the demonstrated limitation of the previous mechanism?

## Method

```text
textbook mathematics
        ↓
mathematical specification
        ↓
logical necessity
        ↓
minimal mechanism
        ↓
executable implementation
        ↓
adversarial boundary test
        ↓
capability classification
```

The repository preserves successful mechanisms, failed candidates, degeneracies, mismatches, and the reasons later capabilities must not be silently imported into earlier Orders.

## Capability progression

| Order | Capability | Boundary |
|---|---|---|
| 1 | Scalar measurement and exact determination | No persistent state |
| 2 | Persistent scalar state and deterministic transition | No independent history variable |
| 3 | Determination-controlled control flow | Formal milestone; behaviorally degenerate with Order 2 under exact equality |
| 4A | Persistent compressed causal history | Transition rule remains fixed |
| 4B | Persistent rule-state modification | Predetermined modification, not learning |
| 5 | Evaluation-driven persistent correction | Learns one value, not a relation |
| 6 | Addressable finite relation learning | Fixed two-slot domain |
| 7 | Structurally scalable finite-function graph | No unseen-input inference |
| 8 | Persistent affine selected-rule inference | Restricted to the selected affine family |

## Read first

1. [`REPOSITORY_GUIDE.md`](REPOSITORY_GUIDE.md) — complete outsider explanation and every-file inventory.
2. [`HigherMath_FirstYear_Capability_Map.md`](HigherMath_FirstYear_Capability_Map.md) — textbook-derived mathematical capability map.
3. [`Order_1_to_8_Progression_Audit.md`](Order_1_to_8_Progression_Audit.md) — necessity audit and Order 3 finding.
4. [`Frozen_Order_Ladder.md`](Frozen_Order_Ladder.md) — accepted historical classification.
5. [`Frozen_Work_Build_Upgrade_Plan.md`](Frozen_Work_Build_Upgrade_Plan.md) — how to extend the frozen work without rewriting history.

## Verification

Run the `test_order*.py` files with Python 3. All nine deterministic suites should report `ALL ORDER ... TESTS PASSED`.

## Large source and archive assets

The supplied textbook PDF and complete historical ZIP exceed GitHub's ordinary Git file-size limit. They are preserved as exact assets in [Release v1.0.0](https://github.com/VAG-gomi/textbook-grounded-mathematical-capability-construction/releases/tag/v1.0.0).

## Historical architecture branch

The recovered notes also mention a possible future branch transforming an existing agentic pipeline into a cognitive-style architecture. That branch is preserved as historical context only; it is not silently treated as Order 9 and must receive its own mathematical decomposition and falsification tests.
