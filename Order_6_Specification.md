# Order 6 — Mathematical Specification Before Implementation

**Prepared by:** Manus AI  
**Status:** Specification only; no implementation is included in this document.  
**Source boundary:** The textbook capability map and the verified Order 5 mechanism.

> **Order 6 question:** What is the smallest internal representation that allows experience to preserve different outputs for different inputs?

## 1. Frozen Order 5 baseline

Order 5 established the following chain:

\[
\boxed{
\text{experience}\rightarrow\text{evaluation}\rightarrow\text{persistent correction}\rightarrow\text{changed future prediction}
}
\]

Its minimal mechanism was:

\[
\theta_t\in\{0,1\},
\qquad
\hat y_t=\theta_t,
\qquad
e_t=y_t-\hat y_t,
\]

followed by:

\[
\theta_{t+1}=\begin{cases}
y_t,&e_t\neq0,\\
\theta_t,&e_t=0.
\end{cases}
\]

This is a valid minimal deterministic learning mechanism under the operational definition used in the experiment. However, it has a strict limitation:

> **Order 5 learns one persistent value, not a relation between an input and an output.**

There is no input variable in the learned prediction. Consequently, a later query cannot be treated differently because it has a different input.

## 2. New capability required for Order 6

The smallest capability beyond Order 5 is not a larger scalar, vector, or matrix. It is a finite input-output relation:

\[
f:X\rightarrow Y.
\]

Choose the smallest nontrivial finite domain and codomain:

\[
X=\{0,1\},
\qquad
Y=\{0,1\}.
\]

A learned relation must support two distinct associations:

\[
f(0)=a,
\qquad
f(1)=b,
\qquad a,b\in\{0,1\}.
\]

The relation is nontrivial because the output for input `0` can differ from the output for input `1`. For example:

\[
f(0)=1,
\qquad f(1)=0.
\]

Order 6 is therefore not defined as “a bigger Order 5.” It is defined as the first experiment in which **input identity selects which persistent learned association is evaluated and updated**.

## 3. Minimal internal representation

For the two-element domain, the smallest direct representation is two named persistent scalar values:

\[
m_0\in\{0,1\},
\qquad
m_1\in\{0,1\}.
\]

Their interpretation is:

\[
f(0)=m_0,
\qquad
f(1)=m_1.
\]

The initial relation is deliberately uninformative:

\[
m_0=0,
\qquad
m_1=0.
\]

This representation is equivalent to a two-entry finite function table, but the specification does not require a vector, matrix, dictionary, or general-purpose data structure. Two persistent scalar slots are sufficient for the selected domain.

| Object | Symbol | Meaning |
|---|---|---|
| Input | `x_t` | Either `0` or `1` |
| Desired output | `y_t` | Either `0` or `1` |
| Association slot for input 0 | `m_0` | Current prediction for input 0 |
| Association slot for input 1 | `m_1` | Current prediction for input 1 |
| Prediction | `\hat y_t` | The slot selected by the current input |
| Error | `e_t` | Desired output minus selected prediction |

## 4. Prediction rule

The input selects one association slot:

\[
\hat y_t=f_t(x_t)=
\begin{cases}
m_0,&x_t=0,\\
m_1,&x_t=1.
\end{cases}
\]

This is the minimum input-dependent prediction rule for a two-element domain. The prediction for `x=0` is independent of the prediction for `x=1`.

## 5. Evaluation and update rule

The evaluation signal remains the scalar error used in Order 5:

\[
e_t=y_t-\hat y_t.
\]

Only the association selected by `x_t` may change:

\[
(m_0,m_1)_{t+1}=
\begin{cases}
(y_t,m_1)_t,&x_t=0\
\text{and }e_t\neq0,\\
(m_0,y_t)_t,&x_t=1\
\text{and }e_t\neq0,\\
(m_0,m_1)_t,&e_t=0.
\end{cases}
\]

Equivalently, in words:

1. Select the persistent slot indexed by the current input.
2. Produce the current prediction from that slot.
3. Compare the prediction with the target.
4. If the error is nonzero, correct only the selected slot.
5. Leave the unselected slot unchanged.

This “selected-slot-only” condition is the essential preservation requirement. It prevents learning one relation from destroying another.

## 6. Formal Order 6 capability criterion

Order 6 passes only if all of the following are established:

| Criterion | Required result |
|---|---|
| Multiple input identity | The mechanism distinguishes `x=0` from `x=1`. |
| Separate prediction | `f(0)` and `f(1)` can have different values. |
| Experience-driven correction | A target pair `(x,y)` can modify the selected association. |
| Persistence | The correction remains after the current training event ends. |
| Input-dependent retrieval | Later output depends on the queried input. |
| Non-interference | Updating one input-output pair leaves the other pair unchanged. |
| Repeated-pair stability | Repeating a correctly learned pair produces zero error and no change. |
| Determinism | The same initial table and training sequence produce the same final table. |

The decisive capability is:

\[
\boxed{
\text{experience can alter one input-output association without destroying another association}
}
\]

## 7. Required experiment design

The initial association table is:

\[
f_0(0)=0,
\qquad
f_0(1)=0.
\]

### 7.1 Train the first pair

Present:

\[
(x,y)=(0,1).
\]

The mechanism predicts:

\[
\hat y= f_0(0)=0.
\]

Therefore:

\[
e=1-0=1.
\]

The selected slot is corrected:

\[
f_1(0)=1,
\qquad
f_1(1)=0.
\]

### 7.2 Verify the first pair

Query input `0` without changing the target table. The expected result is:

\[
f_1(0)=1.
\]

The prediction must now match the learned association.

### 7.3 Verify preservation of the second pair

Query input `1` before training it. The expected result remains:

\[
f_1(1)=0.
\]

This proves that training `(0,1)` did not modify the association for input `1`.

### 7.4 Separate the preservation and independent-correction tests

The two experimental questions should not be conflated.

**Test A — complementary relation and preservation.** Start with:

\[
(m_0,m_1)=(0,0).
\]

Train `(0,1)` and then `(1,0)`. The expected table progression is:

\[
(0,0)\rightarrow(1,0)\rightarrow(1,0).
\]

The second pair is already correct when presented. This test proves that correcting input `0` does not damage the association for input `1`.

**Test B — independent correction.** Start again with:

\[
(m_0,m_1)=(0,0).
\]

Train `(0,1)` and then `(1,1)`. The expected progression is:

\[
(0,0)\rightarrow(1,0)\rightarrow(1,1).
\]

Here both slots undergo separate corrections. The first update changes only `m_0`; the second update changes only `m_1`. This proves independent addressable correction rather than merely preservation of an already-correct second value.

## 8. Recommended decisive test sequences

**Test A — preservation:**

\[
(0,1),
\qquad
(1,0).
\]

| Step | Input `x` | Target `y` | Selected value | Error | Expected update | Expected table |
|---:|---:|---:|---:|---:|---|---|
| 0 | 0 | 1 | `m_0=0` | 1 | Set `m_0=1` | `(1,0)` |
| 1 | 1 | 0 | `m_1=0` | 0 | No change | `(1,0)` |
| 2 | 0 | 1 | `m_0=1` | 0 | No change | `(1,0)` |
| 3 | 1 | 0 | `m_1=0` | 0 | No change | `(1,0)` |

This proves that correcting input `0` preserves the independent association for input `1`.

**Test B — independent correction:**

\[
(0,1),
\qquad
(1,1).
\]

| Step | Input `x` | Target `y` | Selected value | Error | Expected update | Expected table |
|---:|---:|---:|---:|---:|---|---|
| 0 | 0 | 1 | `m_0=0` | 1 | Set `m_0=1` | `(1,0)` |
| 1 | 1 | 1 | `m_1=0` | 1 | Set `m_1=1` | `(1,1)` |
| 2 | 0 | 1 | `m_0=1` | 0 | No change | `(1,1)` |
| 3 | 1 | 1 | `m_1=1` | 0 | No change | `(1,1)` |

This proves that both slots can undergo separate corrections and that learning one pair does not overwrite the other.

## 9. What Order 6 must not introduce

The specification excludes vectors, matrices, real-valued weights, thresholds, gradients, calculus, probability, optimization, hidden representations, multiple interacting parameters beyond the two necessary association slots, and neural terminology. A general dictionary should not be introduced merely for convenience; the domain has exactly two known values and can be represented by two explicit scalars.

The specification also excludes implementation at this stage. The purpose is to decide the mathematical object and the experimental criterion before writing code.

## 10. Order 5-to-Order 6 boundary

| Property | Order 5 | Order 6 |
|---|---|---|
| Persistent learned content | One binary value `θ` | Two input-indexed binary associations |
| Input variable | Absent from prediction | Selects the association slot |
| Prediction | `ŷ=θ` | `ŷ=f(x)` |
| Evaluation | `e=y−ŷ` | `e=y−ŷ` |
| Correction | Changes one global value | Changes only the selected input association |
| Preservation test | Not applicable | Required |
| Capability | Learn a value | Learn a finite binary function on `X={0,1}` |

The exact new capability is not “more memory” in the abstract. It is **addressable persistent association**: the current input determines which learned value is retrieved and which value can be corrected. The result is learning of a finite function on the specifically chosen domain `X={0,1}`, not general function learning over arbitrary domains.

## 11. What the specification establishes and does not establish

**FACT:** The textbook supports functions, ordered input-output relationships, scalar arithmetic, equality, subtraction, and finite representations.[1]

**INTERPRETATION:** Two named scalar slots are sufficient to represent a function on a two-element domain without vectors or matrices.

**HYPOTHESIS to be tested in the later implementation:** Selected-slot correction can establish a persistent input-output relation while preserving previously learned associations.

Order 6 should be implemented only after this specification is accepted. Its success must be judged by the preservation and input-dependent retrieval tests, not merely by the presence of an update function.

## References

[1]: /home/ubuntu/upload/HigherMath_FirstYear_Capability_Map.md "Textbook mathematical capability map"
[2]: /home/ubuntu/upload/Order_5_Report.md "Order 5 report and verified scalar evaluation-driven correction"
[3]: /home/ubuntu/upload/HigherMath1stKetabuddin2026.pdf "Higher Math 1st Year textbook, supplied PDF"
[4]: /home/ubuntu/upload/pasted_content.txt "Order 6 specification requirements supplied by the user"
