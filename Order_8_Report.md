# Order 8 — Persistent Selected-Rule Inference

**Prepared by:** Manus AI  
**Status:** PASS — implementation verified  
**Selected hypothesis family:** Affine functions `f(x)=ax+b`  
**Implementation:** Pure Python standard runtime only

## Executive result

Order 7 could only answer inputs explicitly represented in its finite graph. Order 8 adds a different capability: it identifies a selected mathematical rule from observed examples, retains the rule parameters, and evaluates the retained rule at an input that was not present during calibration.

The selected experimental family is:

\[
\mathcal F_{\mathrm{affine}}=\{f(x)=ax+b\mid a,b\in\mathbb R\}.
\]

Given two observations with distinct inputs:

\[
(x_1,y_1),\qquad(x_2,y_2),\qquad x_1\neq x_2,
\]

parameters are identified by:

\[
a=\frac{y_2-y_1}{x_2-x_1},
\qquad
b=y_1-ax_1.
\]

The parameters are persistently retained as:

\[
\theta=(a,b).
\]

The retained rule then evaluates an unseen input:

\[
\hat y_3=ax_3+b.
\]

The complete suite reports:

```text
ALL ORDER 8 TESTS PASSED
```

## A. Tightened capability claim

Order 8 is not claimed to be the uniquely minimal route to unseen-input inference. The rigorous claim is:

> **Order 8 is selected-rule inference for unseen inputs, with the affine family as the first experimental hypothesis.**

This is narrower than unrestricted function learning. The affine family is chosen explicitly before parameter inference. Two examples determine an affine rule, but they do not determine an arbitrary function.

The learning/inference chain is:

\[
\boxed{
\text{experience}
\rightarrow
\text{parameter identification}
\rightarrow
\text{persistent rule}
\rightarrow
\text{unseen-input evaluation}
}
\]

Without persistence, the mechanism would demonstrate temporary equation solving rather than a future rule.

## B. Implementation state

The implementation stores three auditable pieces of state:

| State | Meaning |
|---|---|
| `slope` | Persistent affine parameter `a` |
| `intercept` | Persistent affine parameter `b` |
| `calibration` | The two observations used for identification |

Before identification, prediction is rejected. After identification, future predictions use only the retained parameters:

\[
\hat y=f_\theta(x)=ax+b.
\]

No lookup graph is used to answer unseen queries, and no target is inserted merely because it was queried.

## C. Canonical identification experiment

The calibration observations are:

\[
(0,1),
\qquad
(1,3).
\]

The identified parameters are:

\[
a=\frac{3-1}{1-0}=2,
\qquad
b=1-2(0)=1.
\]

The retained rule is:

\[
f(x)=2x+1.
\]

The implementation records:

```text
slope: 2.0
intercept: 1.0
rule: f(x) = 2.0*x + 1.0
calibration: ((0, 1), (1, 3))
```

## D. Unseen-input inference

The training inputs were `0` and `1`. The implementation then evaluates unseen inputs:

\[
f(2)=2(2)+1=5,
\]

and:

\[
f(3)=2(3)+1=7.
\]

The executable output is:

```text
UNSEEN PREDICTIONS [5.0, 7.0]
```

This is the decisive difference from Order 7. Order 7 would report input `2` as unknown unless `(2,y)` had been explicitly stored. Order 8 derives the output from the retained rule.

## E. Persistence verification

After identification returns, the learner retains:

\[
\theta=(2,1).
\]

A later query at `x=2` still returns `5`. A later evaluation against target `5` reports zero error without altering the parameters:

\[
e=5-f(2)=5-5=0.
\]

A mismatched later target can expose error:

\[
e=6-f(2)=6-5=1,
\]

but the current Order 8 specification does not silently update the affine rule from that error. Rule revision is a separate future question.

## F. Perturbed-rule verification

A second learner is calibrated on:

\[
(0,1),
\qquad
(1,4).
\]

It identifies:

\[
a=3,
\qquad b=1,
\qquad f(x)=3x+1.
\]

Therefore:

\[
f(2)=7.
\]

This differs from the first learner’s value `5`, proving that the unseen prediction follows the identified parameters rather than a fixed hard-coded answer.

## G. Boundary and failure tests

| Test | Result |
|---|---|
| Two distinct observations identify slope and intercept | Passed |
| Parameters are persistently retained | Passed |
| Unseen input `2` is evaluated as `5` | Passed |
| Second unseen input `3` is evaluated as `7` | Passed |
| Perturbed calibration changes the inferred rule | Passed |
| Repeated calibration input is rejected | Passed |
| Prediction before identification is rejected | Passed |
| Later target error is exposed without silent rule mutation | Passed |
| Repeated runs are deterministic | Passed |
| Vector-like inputs are not silently accepted | Passed |

The exact suite result is:

```text
ALL ORDER 8 TESTS PASSED
```

## H. Order 7 versus Order 8

| Property | Order 7 | Order 8 |
|---|---|---|
| Mathematical object | Partial finite graph `G_t` | Persistently retained affine rule `f_θ` |
| Knowledge | Explicit input-output pairs | Rule parameters identified from examples |
| Known input | Lookup | Evaluation |
| Unseen input | Unknown | Rule-based inference |
| New operation | Pair insertion/replacement | Parameter identification |
| Persistence | Graph persists | `(a,b)` persists |
| Generalization claim | None | Restricted to affine family |
| Neural machinery | None | None |

The conceptual transition is:

\[
\boxed{
\text{memorization of instances}
\longrightarrow
\text{inference from a selected mathematical rule}
}
\]

## I. Minimality analysis

### I.1 Why the affine family is an experimental hypothesis, not a universal minimum

Other selected rule families could also support unseen-input inference. The affine family is chosen because it is mathematically simple, explicitly present in the textbook functions material, and identifiable from two distinct scalar observations. The experiment does not prove that every route to Order 8 must be affine.

### I.2 Why two parameters are required for this family

An affine rule has two independent degrees of freedom:

\[
a\text{ and }b.
\]

One scalar parameter cannot generally determine both slope and intercept.

### I.3 Why two distinct observations are required

The observations generate:

\[
y_1=ax_1+b,
\qquad
 y_2=ax_2+b.
\]

If `x_1=x_2`, the denominator in the slope formula is zero and the rule is not uniquely identified by this procedure.

### I.4 Why no vectors, matrices, or optimization are needed

The parameters, calibration examples, and evaluation operation are scalar. The new capability is selected-rule identification, not multidimensional representation or numerical optimization.

## J. What Order 8 demonstrates

The strongest defensible statement is:

> **Order 8 demonstrates deterministic selected-rule inference: it identifies and persistently retains an affine function from two distinct observed scalar input-output examples, then evaluates the retained rule at an unseen scalar input.**

## K. What Order 8 does not demonstrate

Order 8 does not demonstrate unrestricted function learning, general function approximation, reliable extrapolation outside the selected family, statistical learning, optimization, probability, neural computation, abstraction, intelligence, or automatic selection of the best rule family.

It demonstrates inference within one explicitly selected family.

## L. Boundary to Order 9

The next order should be derived from a demonstrated limitation. Order 8 currently has at least two clear boundaries:

1. It assumes the affine family in advance rather than selecting among competing rule families.
2. It can expose later error but does not yet specify how a persistent affine rule should be revised from new evidence.

Either limitation could motivate a later experiment, but neither should be addressed until a separate mathematical specification identifies the smallest required capability.

## References

[1]: /home/ubuntu/upload/Order_8_Specification.md "Order 8 mathematical specification with tightened selected-rule terminology"
[2]: /home/ubuntu/upload/Order_8_Source_Findings.md "Order 8 textbook and MCQ/CQ source findings"
[3]: /home/ubuntu/upload/Order_7_Report.md "Order 7 finite partial-function implementation report"
[4]: /home/ubuntu/upload/HigherMath_FirstYear_Capability_Map.md "Textbook mathematical capability map"
[5]: /home/ubuntu/upload/HigherMath1stKetabuddin2026.pdf "Higher Math 1st Year textbook, supplied PDF"
[6]: /home/ubuntu/upload/pasted_content.txt "Order 8 implementation requirements supplied by the user"
