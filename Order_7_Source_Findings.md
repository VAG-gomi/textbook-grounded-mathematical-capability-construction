# Order 7 source findings

## Primary textbook grounding

The supplied textbook OCR identifies Chapter 8 as **Functions and Functions Graphs**. The contents OCR places this chapter at approximately page 387 of the book. The chapter material includes domain/range calculations for algebraic, rational, radical, and logarithmic functions, indicating that a function is treated as an input-output object whose admissible input set and output set matter.

The functions material also contains MCQ-oriented formula and shortcut sections. The OCR includes examples involving domain restrictions such as exclusions from rational-function denominators and restrictions for logarithmic and radical expressions. These are relevant because they show that a representation of a function must preserve at least input admissibility and input-output assignment; a mere unaddressed collection of values is insufficient for the general concept.

## Secondary MCQ/CQ grounding

The supplied OCR indicates that the guide/book format intentionally includes chapter-wise multiple-choice questions and creative/constructed questions. It also contains sections labeled for MCQ strategies and CQ-appropriate problems. No separate guide-book PDF was present in `/home/ubuntu/upload` at the time of this analysis; therefore, the available MCQ/CQ evidence is from the supplied Higher Mathematics book’s embedded question sections and OCR.

The MCQ material is useful as an adversarial source because it varies domain restrictions, range, and functional expressions. The CQ material is useful as a compositional source because it asks for multi-step determination of mathematical properties. Neither source is treated as an instruction for constructing an AI mechanism.

## Derived requirement

For Order 7, the representation must support a finite domain larger than two elements while retaining an input-output assignment for each admissible input. The mathematical object is a finite function:

\[
f:X\rightarrow Y,
\qquad |X|>2.
\]

A useful test instance is:

\[
X=\{0,1,2,3\},
\qquad Y=\{0,1\},
\]

with target relation:

\[
f(0)=1,\quad f(1)=0,\quad f(2)=1,\quad f(3)=0.
\]

The Order 7 question is not yet which programming data structure to use. It is whether one mathematical finite-function object can support input selection, persistent association, selective correction, and non-interference for a domain larger than two without manually adding a new named variable for each input.

## Source-use hierarchy

| Source type | Role in Order 7 |
|---|---|
| Definitions and theory | Establish the mathematical object: finite function, domain, range, and input-output assignment |
| Solved examples | Identify required operations: evaluation, admissibility, and representation |
| MCQs | Adversarially test domain/range and input-output edge cases |
| CQs | Test multi-step consistency and combined function properties |
| Implementation | Deferred until the mathematical representation is accepted |

## Boundary

The findings do not justify vectors, matrices, neural networks, optimization, or generalization. They justify only a scalable finite representation of a function on a finite domain larger than two elements.
