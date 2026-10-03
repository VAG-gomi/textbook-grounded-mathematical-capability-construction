# Order 7 — Direct Finite Partial-Function Learner

**Prepared by:** Manus AI  
**Status:** PASS — implementation verified  
**Mathematical object:** `G_t ⊆ X × Y`, a finite graph with function uniqueness  
**Implementation:** Pure Python standard runtime only

## Executive result

Order 7 implements the frozen specification directly as a finite graph of ordered pairs. The declared finite numeric domain is:

\[
X=\{0,1,2,3\},
\]

and the codomain is:

\[
Y=\{0,1\}.
\]

The persistent learned state is:

\[
G_t\subseteq X\times Y.
\]

The graph is initially empty:

\[
G_0=\varnothing.
\]

This means an input can be **unknown** without being incorrectly treated as known to map to `0`. When an unknown input receives an experience pair `(x,y)`, the pair is inserted. When a known input receives a target that differs from its stored output, the unique pair for that input is replaced.

The full test suite reports:

```text
ALL ORDER 7 TESTS PASSED
```

## A. Mathematical state and invariants

The implementation realizes the graph:

\[
G_t=\{(x,y):x\text{ currently has learned output }y\}.
\]

The central invariant is function uniqueness:

\[
(x,y_1)\in G_t\land(x,y_2)\in G_t
\Rightarrow y_1=y_2.
\]

The implementation never retains two different output pairs for the same input. A correction removes the existing pair before adding the new pair.

During learning, `G_t` is a **partial function** over the declared domain because some inputs may have no stored pair. After all declared inputs have been learned, the graph becomes a total function over `X`.

| State condition | Meaning |
|---|---|
| `x∈X` and no pair for `x` | Unknown association |
| Exactly one pair `(x,y)` | Known association |
| Two pairs with same `x` and different outputs | Invalid function graph; never permitted |
| Every `x∈X` has one pair | Total learned function over the declared domain |

## B. Learning and update mechanism

For an experience pair `(x_t,y_t)`, the mechanism first checks whether `x_t` is known.

If it is unknown:

\[
x_t\notin\operatorname{dom}(G_t)
\Rightarrow
G_{t+1}=G_t\cup\{(x_t,y_t)\}.
\]

No numerical prediction error is claimed because no prior prediction existed.

If it is known:

\[
\hat y_t=f_t(x_t),
\qquad
 e_t=y_t-\hat y_t.
\]

If `e_t=0`, the graph is unchanged. If `e_t≠0`:

\[
G_{t+1}=
\left(G_t\setminus\{(x_t,\hat y_t)\}\right)
\cup\{(x_t,y_t)\}.
\]

This is selective correction. Only the pair addressed by the current input can change.

## C. Direct executable representation

The implementation uses a Python set of ordered pairs as a direct realization of the mathematical graph. This is an engineering representation of `G_t`, not a replacement for the mathematical derivation. Because correction computes `e=y-ŷ`, the implementation restricts codomain values to real numeric values. Unknown status uses the explicit `UNKNOWN` sentinel so it cannot collide with a legal codomain value.

The core operations are:

| Mathematical operation | Implementation behavior |
|---|---|
| Graph membership | Search for the unique pair whose first coordinate is `x` |
| Function evaluation | Return the second coordinate of that pair |
| Unknown status | Return the explicit `UNKNOWN` sentinel and expose an unknown-to-learned transition |
| New association | Insert `(x,y)` |
| Known correction | Remove `(x,old)` and insert `(x,new)` |
| Function validity | Enforced by unique-pair replacement |
| Domain validity | Reject inputs outside the declared domain |
| Codomain validity | Reject targets outside the declared numeric codomain |

No vectors, matrices, optimization, neural libraries, probabilities, or external packages are used.

## D. Verification experiment 1 — unknown to learned

Start with:

\[
G_0=\varnothing.
\]

Present `(2,1)`. The input is in the declared domain but has no stored association. The mechanism records:

\[
G_1=\{(2,1)\}.
\]

The trace correctly reports the explicit unknown sentinel (shown as `UNKNOWN` in the current implementation):

```text
status: UNKNOWN_TO_LEARNED
previous_prediction: UNKNOWN
error: None
```

This distinguishes learning a first association from correcting a previously known numerical prediction.

## E. Verification experiment 2 — four-element function

Starting from an empty graph, present:

\[
(0,1),(1,0),(2,1),(3,0).
\]

The graph becomes:

\[
G_4=\{(0,1),(1,0),(2,1),(3,0)\}.
\]

The graph is now total over the declared domain `X`:

\[
\forall x\in X,\;\exists!y\in Y:(x,y)\in G_4.
\]

Evaluation returns:

\[
f(0)=1,
\quad f(1)=0,
\quad f(2)=1,
\quad f(3)=0.
\]

## F. Verification experiment 3 — selective correction

Starting from the learned alternating graph, present `(2,0)`.

The stored pair `(2,1)` is replaced:

\[
G'=
\{(0,1),(1,0),(2,0),(3,0)\}.
\]

The pairs for inputs `0`, `1`, and `3` remain unchanged. The trace reports:

```text
status: CORRECTED
previous_prediction: 1
error: -1
```

Present `(2,1)` again. The graph returns to:

\[
\{(0,1),(1,0),(2,1),(3,0)\}.
\]

The reverse correction also leaves every other pair unchanged.

## G. Verification experiment 4 — repeated correct pair

Present `(1,0)` when the graph already contains `(1,0)`. The mechanism computes:

\[
e=0-0=0.
\]

It reports `CORRECT_NO_UPDATE`, leaves the graph unchanged, and preserves function validity.

## H. Adversarial tests

| Test | Result |
|---|---|
| Unknown input becomes learned association | Passed |
| Domain `X={0,1,2,3}` enforced | Passed |
| Codomain `Y={0,1}` enforced | Passed |
| Four-element alternating function learned | Passed |
| Input-dependent retrieval | Passed |
| Selective replacement for input `2` | Passed |
| Reverse selective replacement | Passed |
| Other inputs remain unchanged | Passed |
| No duplicate output pairs for one input | Passed |
| Repeated correct pair produces zero error/no update | Passed |
| Totality after all four inputs are learned | Passed |
| Deterministic reproducibility | Passed |
| Vector-like input rejected | Passed |

The executable output ends with:

```text
FINAL GRAPH [(0, 1), (1, 0), (2, 1), (3, 0)]
TOTAL AFTER LEARNING True
```

## I. Order 6 versus Order 7

| Property | Order 6 | Order 7 |
|---|---|---|
| Persistent representation | Two named slots `(m_0,m_1)` | Finite graph `G_t⊆X×Y` |
| Domain | Exactly two represented inputs | Declared finite domain larger than two |
| Unknown status | Not represented separately | Explicitly distinguished from known zero |
| Retrieval | Conditional selection between two slots | Graph evaluation by input identity |
| Correction | Selected slot replacement | Unique ordered-pair replacement |
| Function validity | Implicit | Explicit uniqueness invariant |
| Scalability | Fixed two-slot structure | Structural scalability over finite domains |

Order 7 is not unlimited scalability. A larger finite domain can require a larger graph. The capability increase is that the mathematical representation is defined over arbitrary finite domains without manually naming `m_0,m_1,m_2,m_3,\ldots` in the specification.

## J. What Order 7 demonstrates

The strongest defensible statement is:

> **Order 7 demonstrates deterministic supervised learning of a finite binary function over a declared finite domain larger than two, using a persistent graph of ordered pairs, input-dependent evaluation, explicit unknown-to-known insertion, and selective numerical correction that preserves function validity.**

The causal cycle is:

\[
\boxed{
 x_t
 \rightarrow
 G_t\text{ lookup}
 \rightarrow
 \hat y_t\text{ or unknown}
 \rightarrow
 e_t\text{ when known}
 \rightarrow
 \text{insert or replace addressed pair}
 \rightarrow
 G_{t+1}
}
\]

## K. What Order 7 does not demonstrate

Order 7 does not demonstrate general function approximation, continuous-domain learning, interpolation, extrapolation, generalization beyond the represented finite domain, unlimited scalability, vector or matrix representation, optimization, probability, neural computation, abstraction, concept formation, or intelligence.

It demonstrates one precise capability: **addressable persistent learning over a structurally scalable finite function representation**.

## L. Implementation boundary for the next order

Order 7 is now implemented and verified. The next order should be derived from a limitation of this system rather than from a desire to add familiar AI machinery. Candidate limitations include the finite domain being explicitly declared, the graph growing with the number of learned inputs, and the absence of generalization to an input not represented in the graph. These are questions for a later specification, not capabilities to add prematurely.

## References

[1]: /home/ubuntu/upload/Order_7_Specification.md "Frozen Order 7 mathematical specification"
[2]: /home/ubuntu/upload/Order_7_Source_Findings.md "Order 7 textbook and MCQ/CQ source findings"
[3]: /home/ubuntu/upload/Order_6_Specification.md "Order 6 finite binary-function specification"
[4]: /home/ubuntu/upload/HigherMath_FirstYear_Capability_Map.md "Textbook mathematical capability map"
[5]: /home/ubuntu/upload/HigherMath1stKetabuddin2026.pdf "Higher Math 1st Year textbook, supplied PDF"
[6]: /home/ubuntu/upload/pasted_content.txt "Order 7 implementation requirements supplied by the user"
