# Order 7 — Scalable Finite-Function Representation

**Prepared by:** Manus AI  
**Status:** Mathematical specification only; implementation deliberately deferred.  
**Primary grounding:** Supplied Higher Mathematics textbook and its Functions and Functions Graphs material.  
**Secondary grounding:** Embedded MCQ/CQ sections and the supplied Order 7 guidance.

> **Order 6:** Learns a finite binary function on the specifically represented domain `X={0,1}` using two named slots.  
> **Order 7:** Derives a canonical, structurally scalable mathematical representation for a finite function on a larger domain, without manually adding a new named slot for every possible input.

## 1. Order 6 is frozen

Order 6 established deterministic supervised learning of a finite binary function over:

\[
X=\{0,1\},
\qquad
Y=\{0,1\}.
\]

Its persistent representation was:

\[
(m_0,m_1),
\]

with:

\[
f(0)=m_0,
\qquad
f(1)=m_1.
\]

The input selected which association was retrieved and modified. Bidirectional non-interference tests showed that changing the association for input `1` left the already learned association for input `0` unchanged, and vice versa.

The limitation is structural:

\[
\boxed{\text{Order 6 is physically represented by exactly two named association slots.}}
\]

It cannot directly scale to a domain such as `X={0,1,2,3}` without adding further separately named slots.

## 2. The Order 7 question

Order 7 is a representation question, not an AI question:

> **What is the smallest mathematical representation that allows the same input-output learning mechanism to operate over a finite domain larger than two elements?**

The new target is a finite function:

\[
f:X\rightarrow Y,
\qquad |X|>2.
\]

Use the smallest illustrative larger domain:

\[
X=\{0,1,2,3\},
\qquad Y=\{0,1\}.
\]

A target example is:

\[
f(0)=1,
\qquad
f(1)=0,
\qquad
f(2)=1,
\qquad
f(3)=0.
\]

No implementation data structure is selected by this specification. The mathematical object must be derived first.

## 3. Primary textbook grounding

The supplied textbook identifies a chapter titled **Functions and Functions Graphs**. The OCR places it as Chapter 8, approximately beginning at page 387. The chapter material and associated examples address domain and range for algebraic, rational, radical, and logarithmic expressions. These examples make the following requirements explicit for any function representation:

| Requirement | Mathematical meaning |
|---|---|
| Domain | Which inputs are admissible |
| Range/codomain | Which outputs are allowed or produced |
| Input-output correspondence | Each admissible input has an assigned output |
| Evaluation | Given an admissible input, retrieve its output |
| Function validity | One input cannot have two different outputs |

The textbook’s function material therefore grounds a representation as an input-output object rather than as an unaddressed sequence of values.

## 4. Secondary MCQ/CQ grounding

The supplied book OCR also contains chapter-wise MCQ sections, MCQ strategy material, creative/constructed-question sections, and CQ-oriented problems. The functions material includes domain restrictions and examples involving rational, radical, and logarithmic expressions. These are treated as **adversarial mathematical tests**, not as instructions for building an AI.

The intended hierarchy is:

| Source layer | Role in Order 7 |
|---|---|
| Definitions and theory | Establish the mathematical object and function conditions |
| Solved examples | Identify evaluation and domain/range operations |
| MCQs | Probe short edge cases such as invalid domains, forbidden duplicate outputs, and range restrictions |
| CQs | Probe multi-step consistency of representation, evaluation, and update |
| Implementation | Deferred until the mathematical object is accepted |

No separate guide-book PDF was located in the supplied upload directory during this analysis. The available secondary evidence is therefore the textbook’s embedded MCQ/CQ material and the user-supplied guidance. This limitation is recorded rather than hidden.

## 5. Derivation of the minimal mathematical object

A function can be represented by its graph:

\[
G_f=\{(x,f(x)):x\in X\}\subseteq X\times Y.
\]

For the example domain and target relation:

\[
G_f=\{(0,1),(1,0),(2,1),(3,0)\}.
\]

This is a single mathematical object: a finite set of ordered pairs. It has structural scalability over finite domains because its form is defined for arbitrary finite `X`, rather than because it offers unlimited scalability. Its cardinality can still grow with `|X|`; the specification simply avoids manually introducing named variables `m_0,m_1,m_2,m_3,\ldots`.

The function conditions are:

\[
\forall x\in X,\;\exists y\in Y\text{ such that }(x,y)\in G_f,
\]

and:

\[
(x,y_1)\in G_f\land(x,y_2)\in G_f
\Rightarrow y_1=y_2.
\]

The first condition gives totality over the chosen finite domain. The second gives uniqueness of output for each input. Together, they distinguish a function graph from an arbitrary relation.

This graph of ordered pairs is a canonical mathematical representation for the Order 7 question because it explicitly preserves input-output identity and scales structurally with the finite domain. It is not claimed to be the only minimal representation: for a known ordered domain, an equivalent tuple of values could also represent the same function. Whether a later implementation stores the graph as a table, array, map, or another structure is a separate engineering decision and is not made here.

## 6. Evaluation rule

Evaluation is membership lookup in the graph:

\[
f(x)=y\quad\Longleftrightarrow\quad(x,y)\in G_f.
\]

For the target graph:

\[
f(0)=1,
\quad f(1)=0,
\quad f(2)=1,
\quad f(3)=0.
\]

An input outside the declared domain is not silently treated as a valid query:

\[
x\notin X\Rightarrow f(x)\text{ is undefined under this finite-function specification.}
\]

An input inside the declared domain may also be temporarily unknown when no pair for it is present in `G_f`. This unknown status is not a third codomain value; it records that no association has yet been learned.

This domain boundary is important because the textbook’s MCQ-oriented function examples emphasize admissibility restrictions.

## 7. Learning/update rule to be tested later

Order 7 should preserve Order 6’s evaluation-driven selective correction, but apply it to a scalable function graph.

Given an experience pair:

\[
(x_t,y_t)\in X\times Y,
\]

first inspect whether an association for `x_t` exists. If `x_t` is unknown, the experience creates the first pair `(x_t,y_t)`; no numerical prediction error is claimed because no prior prediction existed. If `x_t` is known, retrieve:

\[
\hat y_t=f_t(x_t).
\]

Compute:

\[
e_t=y_t-\hat y_t.
\]

If `e_t=0`, the graph remains unchanged. If `e_t\neq0`, update only the pair associated with `x_t`:

\[
G_{t+1}=\left(G_t\setminus\{(x_t,\hat y_t)\}\right)\cup\{(x_t,y_t)\}.
\]

The update must preserve the function conditions. In particular, it must never leave both `(x_t,old)` and `(x_t,new)` in the graph when `old\neq new`.

For a fixed known domain, every input already has one pair. If the representation later allows incremental domain growth, adding a new input must be treated as an explicit domain-extension operation rather than silently confusing an unknown input with an existing one.

## 8. Formal Order 7 capability criterion

Order 7 passes only if a later implementation demonstrates all of the following:

| Criterion | Required result |
|---|---|
| Larger finite domain | Operates on at least `X={0,1,2,3}` |
| Single mathematical object | Represents the function without manually named `m_0,m_1,m_2,m_3` slots |
| Input-dependent retrieval | Each valid input retrieves its own output |
| Selective correction | An update changes only the pair addressed by the current input |
| Persistence | Corrected pairs remain corrected after later interactions |
| Non-interference | Updating one input does not change other input-output pairs |
| Function validity | No input has two different stored outputs |
| Domain enforcement | Inputs outside `X` are rejected or explicitly treated as undefined |
| Determinism | Same initial graph and same experience sequence produce the same graph |

The decisive new capability is:

\[
\boxed{
\text{addressable persistent learning over a finite domain larger than two with structural, not unlimited, scalability}
}
\]

## 9. Required adversarial tests

The MCQ/CQ-inspired tests should challenge the representation rather than instruct its construction.

### 9.1 Four-element alternating function

Declare the domain `X={0,1,2,3}` and start with an empty graph:

\[
G_0=\varnothing.
\]

An unencountered input is therefore **unknown**, not known to map to zero. Present:

\[
(0,1),(1,0),(2,1),(3,0).
\]

The expected graph is:

\[
\{(0,1),(1,0),(2,1),(3,0)\}.
\]

Each input must retrieve the correct output after training.

### 9.2 Selective correction

Starting from the learned alternating function, present:

\[
(2,0).
\]

The expected graph becomes:

\[
\{(0,1),(1,0),(2,0),(3,0)\}.
\]

The pairs for inputs `0`, `1`, and `3` must remain unchanged.

### 9.3 Reverse selective correction

Then present:

\[
(2,1).
\]

The graph must return to:

\[
\{(0,1),(1,0),(2,1),(3,0)\},
\]

without changing any other pair.

### 9.4 Function-validity test

The representation must reject or correctly replace a conflicting pair. It must never accept both:

\[
(2,0)\quad\text{and}\quad(2,1)
\]

as simultaneous members of a function graph.

### 9.5 Domain test

Queries such as `x=4` must not be silently mapped to an existing value. The mechanism must identify `4\notin X` as undefined or invalid under the declared finite domain.

### 9.6 Repeated correct pair

Repeating a pair already present in the graph must produce zero error and no graph change.

## 10. Order 6-to-Order 7 boundary

| Property | Order 6 | Order 7 |
|---|---|---|
| Domain | Exactly two explicitly represented inputs | Finite domain with `|X|>2` |
| Representation | Named slots `(m_0,m_1)` | One finite graph of ordered pairs `G_f` |
| Retrieval | Conditional selection between two slots | Evaluation of a finite function object |
| Correction | Selected slot update | Replace the unique pair addressed by `x` |
| Function validity | Implicit in two-slot construction | Explicit totality and uniqueness conditions |
| Scalability question | Not tested | Central experimental target |
| Data structure | Not selected | Deferred until after mathematical derivation |

Order 7 is therefore not “more AI.” It is a representation escalation forced by the fixed two-slot limitation of Order 6.

## 11. What Order 7 does not yet claim

Order 7 does not yet claim general function approximation, continuous-domain learning, interpolation, extrapolation, generalization beyond the represented finite domain, unlimited scalability, vector or matrix representation, optimization, probability, neural computation, abstraction, concept formation, or intelligence.

It claims only that a finite function can be represented as a scalable mathematical object whose input-output pairs can be evaluated and selectively corrected.

## 12. Implementation boundary

Implementation should begin only after this specification is accepted. The first implementation should test the graph-of-ordered-pairs semantics directly. A convenient programming data structure may be chosen later, but it must be justified as an implementation of the mathematical object rather than substituted for the mathematical derivation.

## References

[1]: /home/ubuntu/upload/HigherMath_FirstYear_Capability_Map.md "Textbook mathematical capability map"
[2]: /home/ubuntu/upload/Order_6_Specification.md "Order 6 finite binary-function specification"
[3]: /home/ubuntu/upload/Order_6_Source_Findings.md "Order 7 source findings from textbook OCR and MCQ/CQ sections"
[4]: /home/ubuntu/upload/HigherMath1stKetabuddin2026.pdf "Higher Math 1st Year textbook, supplied PDF"
[5]: /home/ubuntu/upload/pasted_content.txt "Order 7 requirements and MCQ/CQ guidance supplied by the user"
