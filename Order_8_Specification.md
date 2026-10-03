# Order 8 — Rule-Based Inference for an Unseen Input

**Prepared by:** Manus AI  
**Status:** Mathematical specification only; implementation deliberately deferred.  
**Primary grounding:** Supplied Higher Mathematics textbook, especially Functions and Functions Graphs.  
**Secondary grounding:** Chapter MCQ/CQ material and the Order 7 limitation analysis.

> **Order 7:** Stores and selectively corrects explicit finite input-output associations.  
> **Order 8:** Identifies and persistently retains a selected function rule from observed examples, then evaluates that rule at an input that was not previously stored.

## 1. Frozen Order 7 boundary

Order 7 maintains a finite partial function:

\[
G_t\subseteq X\times Y.
\]

If an input `x` is not in the domain of `G_t`, the mechanism reports an unknown association. It does not produce an output from structure learned elsewhere.

The limitation is precise:

\[
\boxed{
\text{Order 7 can retrieve learned associations but cannot infer an output for an unseen input.}
}
\]

Order 8 must therefore answer a narrower question:

> **Can a system infer an output for an unseen input after identifying a selected mathematical rule from observed examples?**

This is not yet unrestricted generalization. The rule family must be specified before inference is claimed.

## 2. Primary textbook grounding

The supplied OCR identifies Chapter 8 as **Functions and Functions Graphs**. The chapter’s function material includes explicit rule forms such as affine expressions of the form:

\[
f(x)=ax+b,
\]

as well as quadratic, rational, radical, and logarithmic expressions. The same material emphasizes domain and range restrictions, and the CQ/MCQ sections test evaluation and properties of these rules.[1]

For the first Order 8 experiment, the affine family is selected because it requires only scalar addition, subtraction, multiplication, division, and evaluation. It is an experimental hypothesis family, not a proof that affine inference is the unique mathematically minimal route. No vector, matrix, calculus, probability, optimization, or neural architecture is required.

## 3. The selected rule family

The hypothesis family is:

\[
\mathcal{F}_{\mathrm{affine}}
=\{f_{a,b}:f_{a,b}(x)=ax+b\mid a,b\in\mathbb{R}\}.
\]

The persistent learned rule state is the pair of scalar parameters:

\[
\theta=(a,b).
\]

This is a deliberately restricted hypothesis class. Two examples do not identify an arbitrary mathematical function; they identify one affine rule after the affine family has been selected.

The claim is therefore:

> **Order 8 performs selected-rule inference for unseen inputs, using the affine family as its first experimental hypothesis; it does not establish unrestricted function learning.**

The rule parameters identified from experience must be persistently retained. Otherwise the mechanism demonstrates only temporary equation solving, not a persistent future rule.

## 4. Minimal parameter inference

Given two observed examples:

\[
(x_1,y_1),
\qquad
(x_2,y_2),
\]

with:

\[
x_1\neq x_2,
\]

the unique affine rule passing through both points has slope:

\[
a=\frac{y_2-y_1}{x_2-x_1},
\]

and intercept:

\[
b=y_1-ax_1.
\]

The persistent rule becomes:

\[
\theta=(a,b).
\]

The rule can then be evaluated at an unseen admissible input `x_3`:

\[
\hat y_3=ax_3+b.
\]

The denominator condition `x_2−x_1\neq0` is essential. If the two inputs are identical, the two examples do not determine a unique affine rule by this procedure.

## 5. Canonical decisive experiment

Use the two training examples:

\[
(0,1),
\qquad
(1,3).
\]

The inferred parameters are:

\[
a=\frac{3-1}{1-0}=2,
\qquad
b=1-2(0)=1.
\]

The inferred rule is:

\[
f(x)=2x+1.
\]

Now query an input that was not present in the training examples:

\[
x_3=2.
\]

The predicted output is:

\[
\hat y_3=f(2)=2(2)+1=5.
\]

The system has not stored the pair `(2,5)` during training. It derives the value by evaluating the learned rule.

A second unseen query provides a stronger check:

\[
f(3)=2(3)+1=7.
\]

The capability is therefore different from Order 7 lookup:

\[
\boxed{
(0,1),(1,3)\rightarrow f(x)=2x+1\rightarrow f(2)=5,
\;f(3)=7
}
\]

## 6. Control comparison with Order 7

Under Order 7, after storing only:

\[
\{(0,1),(1,3)\},
\]

an input `2` remains unknown because no pair `(2,y)` exists. Under Order 8, the same observations produce an affine rule and therefore an inferred value at `2`.

| Capability | Order 7 | Order 8 |
|---|---|---|
| Stores observed examples | Yes | Yes, as calibration data or rule evidence |
| Retrieves known input | Yes | Yes |
| Handles unseen input | Unknown | Evaluates selected affine rule |
| Mathematical object | Finite partial function | Parameterized affine function |
| New operation | Pair lookup/replacement | Parameter inference and rule evaluation |
| Claim scope | Explicit finite associations | Selected affine family only |
| General unrestricted function learning | No | No |

## 7. Persistent rule and input-output evaluation

After identifying `a` and `b`, the mechanism must retain:

\[
\theta=(a,b).
\]

Future predictions use the retained rule:

\[
\hat y_t=f_\theta(x_t)=ax_t+b.
\]

This creates a distinction between three operations:

1. **Identification:** infer `\theta=(a,b)` from the calibration examples.
2. **Persistence:** retain `\theta` after the calibration interaction ends.
3. **Inference:** evaluate the retained rule at an input that was not in the calibration examples.

A new observed target can then be used for evaluation:

\[
e_t=y_t-f_\theta(x_t).
\]

Order 8 does not yet specify how a later error should update the affine rule. It first establishes persistent selected-rule inference for an unseen input.

## 8. Required mathematical validity conditions

The later implementation must enforce or expose the following conditions:

| Condition | Meaning |
|---|---|
| Affine family selected | The inference claim is restricted to `f(x)=ax+b` |
| Two distinct calibration inputs | `x_1\neq x_2` is required |
| Scalar inputs and outputs | No vectors or matrices are introduced |
| Rule evaluation | `\hat y=ax+b` |
| Unseen-input distinction | Query input is not one of the calibration inputs |
| Domain validity | Query must lie in the declared admissible domain |
| Determinism | Same two examples and same rule family yield same parameters |
| Scope limitation | No claim is made for non-affine target functions |

## 9. Adversarial MCQ/CQ-inspired tests

The textbook’s MCQ material tests domain and range restrictions, while CQ material tests multi-step function reasoning.[1] Order 8 should use analogous tests as mathematical adversaries.

### 9.1 Distinct-input test

Use examples with `x_1\neq x_2`. The parameters must be uniquely determined.

### 9.2 Repeated-input failure test

Use two examples with the same input. The inference procedure must reject or explicitly classify the case as underdetermined/inconsistent. It must not divide by zero or invent a unique rule.

### 9.3 Unseen-input test

Train on `(0,1)` and `(1,3)` and query `x=2`. The expected inferred output is `5`.

### 9.4 Multiple unseen-input consistency test

Using the same inferred rule, query `x=2` and `x=3`. The outputs must be `5` and `7` without adding those pairs to a lookup graph.

### 9.5 Perturbed-rule test

Train on `(0,1)` and `(1,4)`. The inferred rule is:

\[
f(x)=3x+1,
\]

so the unseen query `x=2` must produce `7`, not `5`. This proves that the prediction follows the inferred rule parameters rather than a fixed memorized answer.

### 9.6 Non-affine limitation test

A later implementation must not silently claim success on arbitrary nonlinear examples. For example, two points from a nonlinear relation can still define an affine line, but a third point may disagree. That disagreement should be recorded as a limitation of the selected affine family, not hidden by changing the rule without specification.

### 9.7 Domain and range test

Queries outside the declared domain must be rejected or marked undefined. The affine formula alone does not erase domain restrictions.

## 10. Exact Order 7-to-Order 8 boundary

| Property | Order 7 | Order 8 |
|---|---|---|
| Persistent object | Partial graph `G_t` | Persistently retained affine rule parameters `(a,b)` |
| Unknown input | No stored association | May be evaluated if within rule domain |
| Learning content | Explicit pairs | Selected rule inferred from examples |
| New operation | Pair insertion/replacement | Solving for rule parameters |
| Unseen-input behavior | Unknown | Rule-based inference |
| Function family | Finite arbitrary associations | Affine only |
| Generalization claim | None | Restricted rule-family inference only |
| Vectors/matrices | Not used | Not used |

The new capability is:

\[
\boxed{
\text{selected-rule inference for an unseen input}
}
\]

not unrestricted generalization.

## 11. Minimality analysis

### 11.1 Why one scalar parameter is insufficient

The affine rule has two independent degrees of freedom: slope `a` and intercept `b`. One scalar cannot generally represent both.

### 11.2 Why two calibration examples are sufficient for the selected family

Two distinct inputs provide two scalar equations:

\[
y_1=ax_1+b,
\qquad
y_2=ax_2+b.
\]

When `x_1\neq x_2`, the equations have one unique solution for `(a,b)`.

### 11.3 Why this is not arbitrary function learning

Many non-affine functions can pass through the same two points. The affine rule is selected as a hypothesis family before inference. The experiment establishes inference within that family only.

### 11.4 Why no vectors or matrices are required

The parameters, examples, and evaluation are scalar. The next capability is rule selection/evaluation, not multidimensional representation.

## 12. What Order 8 demonstrates if later implemented

Order 8 will demonstrate:

> **Deterministic selected-rule inference: identify and persistently retain an affine function from two distinct observed input-output examples, then evaluate it at an unseen scalar input.**

It will not demonstrate general function approximation, robust statistical learning, interpolation outside a selected rule family, extrapolation reliability, optimization, probability, neural computation, abstraction, or intelligence.

## 13. Implementation boundary

Implementation is not included in this specification. It should begin only after the affine-family choice, distinct-input condition, unseen-input test, and non-affine limitation are accepted.

The first implementation must store the identified scalar rule parameters persistently and expose enough calibration evidence to audit the derivation. It should demonstrate that a later unseen-input query uses the retained rule after calibration has ended. It should not add a general-purpose machine-learning framework.

## References

[1]: /home/ubuntu/upload/Order_8_Source_Findings.md "Order 8 textbook and MCQ/CQ source findings"
[2]: /home/ubuntu/upload/Order_7_Report.md "Order 7 finite partial-function implementation report"
[3]: /home/ubuntu/upload/Order_7_Specification.md "Order 7 mathematical specification"
[4]: /home/ubuntu/upload/HigherMath_FirstYear_Capability_Map.md "Textbook mathematical capability map"
[5]: /home/ubuntu/upload/HigherMath1stKetabuddin2026.pdf "Higher Math 1st Year textbook, supplied PDF"
[6]: /home/ubuntu/upload/pasted_content.txt "Order 8 derivation requirements supplied by the user"
