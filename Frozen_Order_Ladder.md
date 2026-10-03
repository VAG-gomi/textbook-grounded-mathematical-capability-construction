# Frozen Order Ladder Before the 4A–8 Necessity Audit

## Classification

| Label | Status | Capability claim |
|---|---|---|
| Order 1 | PASS | Scalar measurement and exact determination |
| Order 2 | PASS | Persistent scalar state with deterministic replacement |
| Original Order 3 | FORMAL PASS / BEHAVIOURAL DEGENERACY | Determination-controlled decomposition whose numerical transition equals Order 2 |
| `+1` Order 3 candidate | EXPERIMENTAL VARIANT | Behaviorally distinct but not forced by Order 2 |
| Forced non-arbitrary Order 3 | NOT FOUND | No unique new transition is logically selected by the preceding evidence |
| Order 4A | NEXT JUSTIFIED CAPABILITY | A new persistent causal state variable independently influences transition |

## Corrected ladder

The rigorous capability ladder is therefore:

\[
O_1\rightarrow O_2\rightarrow O_{4A}\rightarrow O_{4B}\rightarrow O_5\rightarrow O_6\rightarrow O_7\rightarrow O_8.
\]

Original Order 3 remains preserved as a formal decomposition experiment, not as a distinct capability milestone.

## Causal-state terminology

Order 2 already has temporal state. Its current scalar state may contain information inherited from earlier inputs. The precise Order 4A claim is therefore not merely “history is introduced.” It is:

> **Order 4A introduces a separate persistent causal state variable whose value can affect the transition independently of the current scalar state and current input relationship.**

Formally, Order 2 has only:

\[
s_{t+1}=T(s_t,x_t,D_t).
\]

Order 4A adds a persistent compressed state `h_t` such that:

\[
s_{t+1}=T(s_t,x_t,D_t,h_t),
\]

and there exist two executions with identical present conditions but:

\[
h_t^{(A)}\ne h_t^{(B)},\qquad s_{t+1}^{(A)}\ne s_{t+1}^{(B)}.
\]

This is the first genuinely new causal state dimension in the current ladder.

## Methodological rule

An order is added only when the previous order has a demonstrated limitation that forces a new capability. A construction that is merely possible, aesthetically appealing, or numerically different is insufficient.
