# Order 8 source findings

## Frozen Order 7 limitation

Order 7 stores a finite partial function as a graph of ordered pairs:

\[
G_t\subseteq X\times Y.
\]

If an input `x` is not in the graph domain, the mechanism has no prediction. It can learn an association only after receiving an explicit target pair `(x,y)`. Therefore, Order 7 memorizes explicit finite associations but cannot infer an output for an unseen input.

## Primary textbook evidence

The supplied OCR identifies Chapter 8 as **Functions and Functions Graphs**. A clearer OCR excerpt from the chapter’s MCQ strategy material contains explicit function-rule forms such as affine functions of the form `f(x)=ax+b`, quadratic expressions, rational expressions, radical expressions, and logarithmic expressions. The same excerpt emphasizes domain restrictions and range calculations.

This is important for Order 8 because it provides a textbook-grounded alternative to pure lookup: a function can be represented by an explicit rule, and evaluation at a new admissible input can be performed from that rule.

The textbook material also includes composition and inverse-function questions in the chapter’s constructed-question sample. These show that functions are treated not only as memorized point associations but as rules whose evaluation and transformations can be reasoned about.

## Secondary MCQ/CQ role

The chapter’s MCQ sections can test whether a proposed rule respects domain and range restrictions. The CQ sections can test multi-step derivation and evaluation of a rule at values not explicitly used in its derivation. They should be used as adversarial mathematical tests, not as instructions for building an AI.

## Derived mathematical requirement

To answer an unseen input, the system needs more than a graph of stored examples. It needs:

1. a restricted function family or explicit rule form;
2. a parameter representation for that family;
3. an inference procedure that determines the parameters from observed examples; and
4. an evaluation operation that applies the inferred rule to an unseen admissible input.

The smallest textbook-grounded candidate is the affine family:

\[
f(x)=ax+b.
\]

Two non-identical input-output examples with distinct input values determine `a` and `b` exactly:

\[
a=\frac{y_2-y_1}{x_2-x_1},
\qquad
b=y_1-ax_1,
\qquad x_2\neq x_1.
\]

An unseen input `x_3` can then be evaluated as:

\[
\hat y_3=ax_3+b.
\]

This is not yet accepted as Order 8; it is the candidate to be specified and tested. The experiment must distinguish true rule-based inference from simply inserting the unseen point into a lookup graph.

## Boundary and caution

Two examples do not justify an arbitrary function. They justify an affine rule only after the affine family is explicitly selected as the hypothesis class. The new capability is therefore not “learning from two points” in the unrestricted sense. It is **learning and evaluating a selected mathematical rule family**.

No vectors, matrices, neural networks, optimization, probability, or gradient descent are required by this candidate. The main new mathematical primitives are affine function form, solving two scalar equations, division under the condition `x_2\neq x_1`, and rule evaluation.
