# Frozen Work Build-Up and Upgrade Plan

## Status

This plan treats the completed Orders 1–8 as a preserved knowledge base. It does not delete, rewrite, or invalidate the earlier experiments.

## Preserved foundation

- **Orders 1–2:** scalar measurement and persistent deterministic state.
- **Order 3:** preserved formal determination-controlled control flow; behaviorally degenerate with Order 2 under exact equality.
- **Order 4A:** independently causal compressed state.
- **Order 4B:** persistent rule-state modification without learning.
- **Order 5:** evaluation-driven persistent correction of one value.
- **Order 6:** addressable correction of a two-input finite relation.
- **Order 7:** finite graph representation with explicit unknown status and function validity.
- **Order 8:** persistent affine rule identification and unseen-input evaluation.

Every implementation, report, source finding, and verification output remains part of the historical record.

## Upgrade principle

> Build upward from the strongest verified boundary instead of restarting from the earliest experiment.

The current strongest boundary is Order 8:

\[
\text{two observed scalar pairs}
\rightarrow
\text{identified affine parameters}
\rightarrow
\text{persistent rule}
\rightarrow
\text{unseen-input evaluation}.
\]

## Candidate next capabilities

### Candidate A — Selection among stated rule families

Keep the candidate families explicit, for example:

\[
\mathcal F_0=\{f(x)=c\},
\qquad
\mathcal F_1=\{f(x)=ax+b\}.
\]

The new capability would be to evaluate which supplied family is consistent with the observations. This must not be described as discovering an arbitrary law; the candidate family set is given in advance.

### Candidate B — Revision of a retained rule

Keep the affine rule persistent, then supply a later observation that conflicts with it. Define the smallest deterministic textbook-grounded operation that can represent the conflict and revise or reject the retained rule. This is a different experiment from family selection and should be specified separately.

## Recommended work sequence

1. Freeze the audit and current Order 8 boundary.
2. Write one specification for Candidate A and one for Candidate B.
3. For each specification, state the exact limitation of Order 8 that forces it.
4. Design a counterexample that Order 8 cannot pass.
5. Reject any candidate that imports unforced vectors, matrices, probability, optimization, or neural terminology.
6. Implement only the candidate that survives the necessity comparison.
7. Preserve the rejected candidate as a documented alternative, not as lost work.

## Current recommendation

Do not implement Order 9 yet. The immediate build-up task is a **specification comparison** between rule-family selection and rule revision. This keeps the methodology faithful to the textbook-only and one-capability-at-a-time requirements.

## Acceptance gate for the next Order

A next Order may be accepted only if:

- its mathematical object is explicitly grounded in the supplied textbook;
- the preceding Order has a demonstrated limitation requiring the new object;
- the new capability is separable from all other additions;
- a deterministic test exists that the preceding Order cannot pass;
- the implementation uses only the required mechanism;
- the boundary of the claim is stated explicitly.
