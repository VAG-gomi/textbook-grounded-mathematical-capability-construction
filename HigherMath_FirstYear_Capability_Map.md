# HSC Higher Mathematics First-Year Textbook
## Chapter-by-Chapter Mathematical Capability Map

**Prepared by:** Manus AI  
**Source boundary:** *HigherMath1stKetabuddin2026.pdf*  
**Purpose:** Determine which executable mathematical capabilities are directly supported by the textbook, without designing a neuron, neural network, learning algorithm, or artificial cognitive architecture.

> **Central question:** What is the smallest mathematical substrate from which an executable artificial mechanism could be constructed without deciding its final architecture in advance?

## 1. Scope, method, and evidence discipline

The supplied PDF is a 660-page scanned textbook. It has no usable embedded text layer, so the analysis used page rendering, Bengali/English OCR, and visual inspection of formulas, worked examples, exercises, diagrams, and chapter transitions. The scan visibly contains the standard first-year higher-mathematics sequence: matrices and determinants, vectors, straight lines, circles, permutations and combinations, trigonometric ratios, associated angles, functions and graphs, differentiation, and integration. The sample pages and OCR establish the transition from vectors to straight lines around the early-middle portion of the book, the circle and permutations sections later, functions around the 400s, differentiation around the 460s–520s, and integration in the final mathematical section before board-question material.[1]

The report keeps three layers separate:

| Layer | Meaning in this report |
|---|---|
| **FACT** | A definition, operation, formula, theorem, example type, or chapter topic visibly supported by the textbook. |
| **INTERPRETATION** | A translation of that mathematical content into a programming capability. |
| **HYPOTHESIS** | A cautious possibility for a later experiment. It is not a conclusion that the book itself establishes. |

OCR occasionally corrupts Bengali words and mathematical symbols. Therefore, the capability claims below are based on repeated formulas, surrounding definitions, recognizable notation, and page-level visual checks rather than isolated OCR strings. The source is cited as the supplied PDF; page numbers refer to the scanned PDF where practical.[1]

## 2. Textbook structure

The following ten-chapter structure is the operative chapter map supported by the book’s contents/section sequence and chapter-opening material.

| Chapter | Title | Major sections identified from the textbook | Main objects |
|---:|---|---|---|
| 1 | Matrices and determinants | Matrix definition and order; equality; addition and subtraction; scalar multiplication; matrix multiplication; transpose; determinant; minors/cofactors; adjoint; inverse; matrix equations and systems; powers and special matrices | Scalars, variables, arrays, matrices, determinants, equations |
| 2 | Vectors | Geometric vectors; zero, like/unlike, equal, parallel, collinear, coplanar and free vectors; position vectors; components; addition and subtraction; scalar multiplication; unit vectors; magnitude; dot product; projection; angle; geometric applications | Points, directed segments, vectors, scalars |
| 3 | Straight line | Coordinate representation; distance and section formulas; slope; line equations in point-slope, two-point, intercept, normal and parametric/vector forms; angle between lines; parallel/perpendicular conditions; distance from point to line; loci and line problems | Points, coordinates, lines, slopes, equations |
| 4 | Circle | Standard and general equations; center and radius; tangent and normal; chord and contact; position of a point; pair/common chord and related circle problems | Points, curves, circles, quadratic equations |
| 5 | Permutations and combinations | Counting principle; factorial; permutations; arrangements with restrictions and repetitions; combinations; selections; circular and related arrangements | Finite sets, arrangements, selections, integer counts |
| 6 | Trigonometric ratios | Angles and their measures; trigonometric ratios; signs and quadrants; identities; reduction and evaluation; trigonometric equations and formula-based computation | Angles, real values, ratios, functions |
| 7 | Associated angles | Related-angle identities; compound angles; multiple and submultiple angles; transformations and evaluations; trigonometric equations involving associated angles | Angles, ratios, identities, equations |
| 8 | Functions and graphs | Relations and functions; domain, codomain and range; algebra of functions; composite functions; inverse functions; evaluation; graph interpretation | Sets, ordered pairs, functions, graphs |
| 9 | Differentiation | Limit/intuitive change; derivative definition; rules; derivatives of algebraic, trigonometric, exponential/logarithmic and composite expressions; implicit/parametric forms; higher derivatives; tangent/normal; increasing/decreasing behavior; maxima/minima | Functions, limits, rates, slopes, local extrema |
| 10 | Integration | Antiderivative and indefinite integral; standard forms; substitution; integration by parts and related algebraic methods; definite integrals; evaluation and area-type applications | Functions, intervals, accumulated quantities, areas |

The book also contains model tests, board-style multiple-choice and written questions, and examination material. Those sections exercise the preceding mathematics; they do not add a new primitive domain.

## 3. Chapter capability map

### Chapter 1 — Matrices and determinants

**A. Mathematical domain.** FACT: This chapter treats rectangular and square arrays of quantities, their dimensions, algebraic operations, determinants, inverse-related constructions, and matrix equations. The core objects are scalars, variables, ordered rows and columns, matrices, determinants, and systems of equations.

**B. Core primitives.**

| Primitive | Mathematical form/notation | Definition or condition | Prerequisites | Textbook-style example | Computational interpretation |
|---|---|---|---|---|---|
| Matrix | `A=[a_ij]` | An ordered rectangular array with specified rows and columns | Scalar notation and indexing | A 2×2 or 3×3 matrix | Structured finite state or data table |
| Equality | `A=B` | Same order and corresponding entries equal | Matrix representation, scalar equality | Compare two matrices entrywise | Exact structural comparison |
| Addition/subtraction | `A±B` | Corresponding entries are added/subtracted; same order required | Scalars and equal-order matrices | Add two 2×2 matrices | Componentwise accumulation/difference |
| Scalar multiplication | `kA` | Every entry is multiplied by `k` | Scalar multiplication | Multiply a matrix by a real number | Uniform scaling |
| Matrix product | `AB` | `(AB)_ij=Σ_k a_ik b_kj`; dimensions must conform | Multiplication, addition, indexing | Product of compatible matrices | Composed structured transformation |
| Transpose | `A^T` | Rows and columns are interchanged | Matrix indexing | Transpose a rectangular matrix | Reorientation/reindexing |
| Determinant | `|A|` or `det(A)` | Scalar associated with a square matrix, computed by expansion/formulas | Scalar arithmetic, signed sums/products | Determinant of a 2×2 or 3×3 matrix | Collapsed invertibility/orientation-like summary |
| Adjoint/cofactor | `adj(A)` | Constructed from minors and cofactors, then transposed | Determinants and signs | `A^{-1}=adj(A)/|A|` when `|A|≠0` | Intermediate for inversion |
| Inverse | `A^{-1}` | Matrix satisfying `AA^{-1}=A^{-1}A=I` when it exists | Product, identity, determinant/adjoint | Solve `AX=B` by `X=A^{-1}B` | Reversible transformation/linear system solution |

**C. Computational capabilities.** FACT: The chapter supports finite structured representation, exact arithmetic on arrays, linear combinations of rows/columns, compatibility checking, determinant-based tests, and solution of certain simultaneous equations. INTERPRETATION: Ordinary loops, indexing, arithmetic, and conditionals are sufficient to implement these operations. HYPOTHESIS: Matrices could later encode a multi-component transition, but the chapter does not make a matrix necessary for a first mechanism.

**Minimality classification: POTENTIALLY USEFUL.** A scalar or vector state can use the same arithmetic without introducing matrix multiplication. Matrices become more valuable when many components must be transformed simultaneously or when a system of linear equations is itself the object of study. They are **not required initially** merely because modern computational systems often use them.

### Chapter 2 — Vectors

**A. Mathematical domain.** FACT: The chapter provides geometric and coordinate vectors, including three-dimensional component notation such as `a=a_1 i+a_2 j+a_3 k`, position vectors, magnitude, direction, addition, subtraction, scalar multiplication, dot product, projection, angle, and geometric applications.

**B. Core primitives.**

| Primitive | Mathematical form/notation | Definition or condition | Prerequisites | Computational interpretation |
|---|---|---|---|---|
| Vector representation | `a=a_1 i+a_2 j+a_3 k` or `(a_1,a_2,a_3)` | Ordered components with direction/magnitude interpretation | Scalars and coordinates | Structured finite input/state |
| Vector addition | `a+b` | Add corresponding components | Component arithmetic | Accumulation and composition |
| Vector subtraction | `a-b` | Subtract corresponding components | Addition and negation | Difference/error signal |
| Scalar multiplication | `λa` | Multiply each component by `λ` | Scalar arithmetic | Scaling |
| Magnitude | `|a|=√(a_1²+a_2²+a_3²)` | Length/norm in the textbook’s Euclidean setting | Squares, sum, square root | Size/intensity measurement |
| Unit vector | `a/|a|` when `a≠0` | Vector of magnitude one in the same direction | Magnitude and division | Normalized representation |
| Dot product | `a·b=|a||b|cosθ=Σa_i b_i` | Scalar product of corresponding components | Multiplication, addition, magnitude/angle | Alignment or similarity-like scalar |
| Projection | `(a·b)/|b|` or vector projection form | Component of one vector along another | Dot product and magnitude | Directional measurement |
| Angle | `cosθ=(a·b)/(|a||b|)` | Included angle under nonzero-vector conditions | Dot product and magnitude | Angular comparison |

**C. Computational capabilities.** FACT: Vectors support representation, addition, subtraction, scaling, magnitude, direction through components, dot-product comparison, projection, and coordinate/geometric problem solving. INTERPRETATION: A program can distinguish inputs by equality, component difference, magnitude, dot product, angle, or projection. A vector can represent an input, an internal state, or an output, but it is only a container until an update rule is supplied. HYPOTHESIS: A vector-only state is a defensible initial substrate if the experiment needs more than one scalar channel.

**Minimality classification: REQUIRED for multi-component representation; POTENTIALLY USEFUL for a scalar-only first experiment.** The book directly supplies the smallest natural extension from scalar arithmetic to structured state. It does not, by itself, supply memory, adaptation, or a decision policy.

### Chapter 3 — Straight line

**A. Mathematical domain.** FACT: The chapter treats coordinate geometry of points and lines, slope, equations, distances, section ratios, parallelism, perpendicularity, angles, and distance from a point to a line. It uses scalar coordinates and equations, with vectors appearing as an alternative representation in relevant problems.

**B. Core primitives.**

| Primitive | Form | Computational meaning |
|---|---|---|
| Point | `P(x,y)` | Two-component coordinate representation |
| Difference/displacement | `(x₂−x₁,y₂−y₁)` | Input-state difference |
| Distance | `d(P,Q)=√((x₂−x₁)²+(y₂−y₁)²)` | Euclidean separation in 2D |
| Slope | `m=(y₂−y₁)/(x₂−x₁)` when defined | Rate/ratio of coordinate change |
| Line equation | `y−y₁=m(x−x₁)`, `ax+by+c=0`, and related forms | Constraint or decision boundary |
| Comparison of lines | Conditions for equal, parallel, or perpendicular slopes | Relational classification |
| Point-line distance | `|ax₀+by₀+c|/√(a²+b²)` | Distance from an input to a linear boundary |

**C. Computational capabilities.** FACT: The chapter can represent geometric positions and linear relationships, calculate distances and slopes, test line relationships, and evaluate whether points lie on a line. INTERPRETATION: A line equation can serve as a mathematically explicit boundary for a binary comparison. This does not imply that the textbook defines a classifier; it supplies the representation and arithmetic from which such a rule could be programmed.

**Minimality classification: POTENTIALLY USEFUL.** The straight-line chapter is not required for a one-dimensional state update. It is useful if the experiment requires geometric proximity, a linear boundary, or coordinate relations.

### Chapter 4 — Circle

**A. Mathematical domain.** FACT: The chapter studies the equation of a circle, center and radius, points relative to a circle, tangents, normals/chords, contact conditions, and related quadratic equations.

**B. Core primitives.** The main primitives are point coordinates, squared differences, addition, equality to a constant radius-squared, quadratic expressions, tangent constraints, and point-to-circle comparison. A standard form is `(x−h)²+(y−k)²=r²`.

**C. Computational capabilities.** INTERPRETATION: A program can test inside/on/outside relations, calculate radial distance or squared distance, construct a nonlinear boundary, and solve selected geometric constraints. The circle supplies a richer boundary than a line but does not supply a new memory mechanism.

**Minimality classification: NOT REQUIRED FOR INITIAL EXPERIMENT.** Circle mathematics is a specialized nonlinear geometric capability. It should enter only if evidence shows that a circular boundary or radial relation is needed.

### Chapter 5 — Permutations and combinations

**A. Mathematical domain.** FACT: This chapter provides finite counting, factorials, permutations, combinations, arrangements, selections, and restrictions such as repeated objects or circular arrangements.

**B. Core primitives.** Factorial `n!`, multiplication of counts, division by factorials, ordered selection `^nP_r`, unordered selection `^nC_r`, and finite-case enumeration are the central operations.

**C. Computational capabilities.** INTERPRETATION: Ordinary integer arithmetic and loops can enumerate or count finite possibilities. The chapter can represent discrete alternatives and calculate the size of finite search spaces. It does not by itself provide probability, stochastic sampling, a search strategy, or a state-update rule.

**Minimality classification: OUTSIDE CURRENT SCOPE for the first continuous/numeric mechanism; POTENTIALLY USEFUL for discrete branching or finite hypothesis spaces.** Counting is mathematically valid but not a prerequisite for scalar/vector measurement and update.

### Chapter 6 — Trigonometric ratios

**A. Mathematical domain.** FACT: The chapter treats angle measures, sine/cosine/tangent and related ratios, signs by quadrant, identities, evaluation, and trigonometric equations.

**B. Core primitives.** Angle representation, ratio evaluation, multiplication/addition of real values, identity substitution, and equation solving are available. In a right-triangle interpretation, ratios relate sides and angles; in a function interpretation, they provide periodic mappings.

**C. Computational capabilities.** INTERPRETATION: A program can transform an angle into a bounded periodic scalar, compare angular relationships, solve selected trigonometric equations, and encode rotation-related quantities. HYPOTHESIS: These functions may be useful for periodic state or geometric transformations, but the textbook does not establish them as necessary for the initial loop.

**Minimality classification: POTENTIALLY USEFUL, not required initially.** A first mechanism can use arithmetic and comparisons without trigonometric functions.

### Chapter 7 — Associated angles

**A. Mathematical domain.** FACT: The chapter extends trigonometric computation through compound, multiple, submultiple, and related-angle identities. It supplies algebraic transformations among trigonometric expressions.

**B. Computational capabilities.** A program can normalize or transform angle expressions, calculate derived values, and solve broader classes of trigonometric equations. These are transformations of already available angle/ratio objects rather than a new state primitive.

**Minimality classification: NOT REQUIRED FOR INITIAL EXPERIMENT.** It is an advanced trigonometric convenience and should be withheld unless periodic or angular behavior is demonstrated to be necessary.

### Chapter 8 — Functions and graphs

**A. Mathematical domain.** FACT: The chapter addresses relations, functions, domain, codomain, range, function evaluation, algebra of functions, composite functions, inverse functions, and graphs. The OCR-visible pages explicitly identify “functions and graphs” and examples involving `P(x)`, `Q(x)`, and composite evaluation.[1]

**B. Core primitives.**

| Primitive | Form | Computational interpretation |
|---|---|---|
| Ordered pair | `(x,y)` | Input-output association |
| Function | `f:X→Y` | Single-valued mapping from input domain to output codomain |
| Evaluation | `y=f(x)` | Executable transformation |
| Composition | `(f∘g)(x)=f(g(x))` | Sequential transformations |
| Inverse | `f^{-1}` when an inverse exists | Reversal under domain/range conditions |
| Domain/range test | Membership and output conditions | Valid-input and output constraints |
| Graph | Set of represented input-output pairs | Observable relation/behavior |

**C. Computational capabilities.** FACT: The chapter supplies input-output mapping and composition. INTERPRETATION: A function is the clearest textbook-supported abstraction for a deterministic transformation. It can represent a rule, but it does not automatically contain memory; `f(x)` maps the present input unless a prior state is included among its arguments.

**Minimality classification: REQUIRED as an abstraction; POTENTIALLY USEFUL rather than mandatory as a separate chapter.** An executable mechanism needs some rule from current quantities to new quantities. That rule can be written directly with arithmetic, but the function concept provides the mathematically clean representation.

### Chapter 9 — Differentiation

**A. Mathematical domain.** FACT: The chapter provides derivative/rate-of-change ideas, derivative rules, chain and product/quotient rules, derivatives of common functions, implicit/parametric derivatives, higher derivatives, tangents/normals, and maxima/minima analysis. OCR-visible pages contain derivative expressions and trigonometric/logarithmic derivative examples.[1]

**B. Core primitives.** The derivative `f'(x)` is a local rate of change; higher derivatives iterate this operation; sign tests support increasing/decreasing and extrema conclusions. Tangent slope is a geometric interpretation.

**C. Computational capabilities.** INTERPRETATION: Calculus supplies continuous-change measurement, local sensitivity, stationary-point tests, and calculus-based optimization. HYPOTHESIS: It could later support a rule that adjusts quantities in response to a slope or sensitivity. That would be an experimental design, not a textbook conclusion.

**Minimality classification: NOT REQUIRED FOR INITIAL EXPERIMENT; POTENTIALLY USEFUL LATER.** A discrete mechanism can represent a state and update it with arithmetic, comparison, and recurrence without derivatives. Calculus becomes justified only if the experiment requires continuous-time behavior, local sensitivity, or an optimization principle.

### Chapter 10 — Integration

**A. Mathematical domain.** FACT: The chapter provides antiderivatives, indefinite and definite integrals, standard forms, substitution, integration by parts/related methods, and area or accumulated-quantity applications.

**B. Core primitives.** The integral `∫f(x)dx` represents an antiderivative family; a definite integral `∫_a^b f(x)dx` produces an accumulated quantity over an interval. The chapter also supplies algebraic substitution and evaluation rules.

**C. Computational capabilities.** INTERPRETATION: A program can calculate accumulated quantities, areas in textbook-defined settings, and discrete approximations to integrals. An integral can represent accumulation, but the mathematical notation alone does not implement a running memory or numerical update.

**Minimality classification: NOT REQUIRED FOR INITIAL EXPERIMENT; POTENTIALLY USEFUL LATER.** Integration is unnecessary for a first finite-step input–measurement–decision–update loop unless accumulation over a continuum is specifically required.

## 4. Dependency graph

The dependency structure supported by the textbook can be stated as follows:

```text
scalar values and arithmetic
        |
        +--> equations and inequalities
        |        |
        |        +--> coordinate points and distances
        |        |        |
        |        |        +--> straight lines and circles
        |        |
        |        +--> matrices and determinants
        |
        +--> functions and evaluation
                 |
                 +--> trigonometric functions and associated-angle identities
                 |
                 +--> limits / derivatives / rates of change
                 |              |
                 |              +--> extrema and tangent behavior
                 |
                 +--> antiderivatives / definite integrals
                                |
                                +--> accumulation and area

scalars + ordered components
        |
        +--> vectors
                 |
                 +--> vector addition, subtraction, scaling
                 |
                 +--> magnitude and unit vector
                 |
                 +--> dot product
                                |
                                +--> projection, angle, vector comparison
```

The foundational capabilities are scalar representation, arithmetic, equality/ordering, and finite sequences of operations. Vectors and functions are the most direct higher-level extensions. Matrices are partly redundant with componentwise vector operations for a minimal system: they become necessary only when the experiment requires a general multi-input/multi-output linear transformation or simultaneous-equation machinery. Geometry is a specialized application of coordinates, equations, and vectors. Differentiation and integration are advanced extensions, not prerequisites for a discrete state machine.

## 5. Measurement capability map

The word **metric** must be used narrowly. A metric is a function `d:X×X→R` satisfying non-negativity, identity of indiscernibles, symmetry, and the triangle inequality. The textbook’s magnitude `|x|` is a scalar size operation; it is not itself a two-input metric. On real numbers, `d(x,y)=|x−y|` is a metric, while a vector Euclidean distance `d(u,v)=||u−v||` is the analogous metric when the norm and vector space are defined.

| Measurement/comparison | What is measured | Operation | Objects | Preserved | Lost | Distinguishes inputs? | Close-to-state test? | Boundary potential |
|---|---|---|---|---|---|---|---|---|
| Scalar magnitude | Size of one real value | `|x|` | Scalars | Nonnegative size | Sign | Sometimes; `x` and `−x` coincide | Yes, only relative to a chosen state/range | Threshold on magnitude |
| Absolute difference | Separation on the number line | `|x−y|` | Scalars | Pairwise separation | Direction/sign of difference | Yes | Yes | Threshold `|x−s|≤ε` |
| Vector magnitude/norm | Length of one vector | `||v||=√Σv_i²` | Euclidean vectors | Overall size | Direction and component allocation | Not always; many vectors share a norm | Only against a norm-based state | Spherical/radial threshold |
| Vector distance | Separation of two vectors/points | `||u−v||` | Vectors or coordinates | Euclidean pairwise separation | Direction of displacement | Yes in exact arithmetic | Yes | Sphere/ball boundary |
| Dot product | Alignment and scaled projection | `u·v=Σu_iv_i` | Vectors | A signed alignment scalar | Most component detail; not a distance by itself | Sometimes; distinct vectors may share dot product | Yes for directional similarity if reference state is fixed | Half-space threshold |
| Projection | Component along a direction | `(u·v)/||v||` or vector form | Vectors | Directional component | Orthogonal component | Only along selected direction | Yes for one-direction closeness | Linear threshold |
| Angle | Directional separation | `cosθ=(u·v)/(||u||||v||)` | Nonzero vectors | Relative direction | Absolute magnitude | Yes for direction | Yes for angular state | Conical boundary |
| Ratio/slope | Relative change | `(y₂−y₁)/(x₂−x₁)` | Coordinates or scalars | Proportional relation | Absolute scale | Sometimes | Only if the state is a ratio | Ratio threshold |
| Rate of change | Local change per input change | `f'(x)` | Functions | Local sensitivity | Global behavior | Yes for local behavior | Yes for local-sensitivity state | Derivative sign/threshold |
| Integral/accumulation | Total over an interval | `∫_a^b f(x)dx` | Functions and intervals | Aggregate quantity | Fine-grained path/order information | Sometimes | Only for accumulated-state comparisons | Integral threshold |
| Equality/order | Exact or ordered relation | `x=y`, `x>y`, etc. | Scalars, components, expressions | Relation outcome | Magnitudes beyond relation | Yes for the tested relation | Yes with explicit tolerance only if added | Direct decision boundary |

The textbook supports measurement and comparison, but it does not prescribe tolerance handling, numerical precision, noise models, or a decision procedure. Those would be implementation choices or later hypotheses.

## 6. Vector capability map

| Capability | Textbook support | Possible role | Limitation |
|---|---|---|---|
| Representation | Direct | Input, state, output | A container is not an update mechanism |
| Addition/subtraction | Direct | Accumulation and error/difference | Requires a chosen update rule |
| Scalar multiplication | Direct | Scaling and normalization components | Does not determine the scalar |
| Magnitude | Direct | Measurement of size | Discards direction |
| Direction | Direct through components/unit vectors | Orientation or state comparison | Requires a coordinate basis |
| Dot product | Direct | Alignment, projection, comparison | Not a metric by itself |
| Projection | Direct | One-direction measurement | Discards orthogonal components |
| Angle | Direct | Directional comparison | Undefined for zero vector; magnitude removed |
| Distance | Direct through displacement and magnitude | Closeness and separation | Depends on Euclidean norm |
| Linear combinations | Direct through addition/scalar multiplication | Constructive transformation | Coefficients must be supplied |
| Vector transformations | Partly direct through operations; general matrix form in Chapter 1 | Input/state transformation | General transformation requires a specified rule/matrix |

**Test of sufficiency:** Vectors are sufficient for representation, but not sufficient alone for an executable mechanism. The smallest mechanism still needs an input acquisition convention, a measurement operation, a comparison/decision rule, a state variable, an update equation, and an output convention.

## 7. Matrix capability map

The book genuinely contains matrix mathematics: order, equality, operations, determinants, adjoint/inverse, and matrix-equation use. Matrices add compact representation of many simultaneous linear relationships and reusable multi-component transformations. They also provide a formal way to encode `As_t+Bx_t` when `A` and `B` have been selected.

However, a vector-only possibility such as

```text
s_t = (s_1,...,s_n),  x_t = (x_1,...,x_m)
componentwise arithmetic and explicitly specified update rules
```

does not require matrices. A matrix-based mechanism

```text
s_{t+1}=As_t+Bx_t
```

is a convenient abstraction for a family of linear transformations, not a logical prerequisite for state, measurement, or update. **Conclusion:** matrices are **POTENTIALLY USEFUL** and should be admitted only when the experiment needs general linear multi-channel transformation, simultaneous equations, or compact parameterization. They are not required in Order 1.

## 8. Calculus necessity assessment

**Conclusion: NO for the first discrete mechanism; CONDITIONAL for later continuous or optimization experiments.**

A first mechanism can use a finite state `s_t`, an input `x_t`, arithmetic operations, a measurement such as `|x_t−s_t|` or `||x_t−s_t||`, a comparison, and an explicit update. None of these requires a derivative or integral. Differentiation becomes necessary only if the update is defined by local rate, sensitivity, tangent information, or a gradient-like optimization principle. Integration becomes necessary only if the mechanism must accumulate a quantity over a continuous interval or compute area/continuous total. This is a mathematical justification, not a rejection of calculus by preference.

## 9. Geometry necessity assessment

**Conclusion: ABSTRACT VECTOR/COORDINATE MATHEMATICS IS OPTIONAL BUT USEFUL; PHYSICAL 2D/3D VISUALIZATION IS NOT REQUIRED.**

A vector is an ordered mathematical object and does not require physical three-dimensional space. The textbook’s 2D and 3D coordinate geometry provides useful examples of distance, angle, lines, circles, and projections, but the same finite-component operations can be executed symbolically or in arbitrary dimension. A first experiment may therefore use scalar or abstract vector states without drawing a plane or embedding the state in physical space. Straight lines and circles should enter only if their boundary or spatial semantics are experimentally needed.

## 10. Pure programming implementability

| Capability | Ordinary arithmetic/code | External library | Special hardware |
|---|---|---|---|
| Scalar arithmetic, equality, ordering | Yes: variables, loops, conditionals | No | No |
| Absolute difference and scalar distance | Yes | No | No |
| Vectors, addition, scaling, dot product | Yes: arrays/loops | No | No |
| Euclidean magnitude/distance | Yes, with square root | Optional numerical library for convenience | No |
| Matrix operations and determinants | Yes, with nested loops | Optional for speed/large size | No |
| Function evaluation | Yes when formula is coded | Optional | No |
| Trigonometric/logarithmic/exponential evaluation | Basic implementation possible; ordinary code can call a standard math library | Standard library is convenient, not conceptually required | No |
| Comparison boundary | Yes: conditionals | No | No |
| Finite sequence/recurrence | Yes: variables and loops | No | No |
| Derivative | Finite differences or symbolic rules can be coded | Optional numerical/symbolic library | No |
| Integral | Numerical summation or coded rules | Optional numerical/symbolic library | No |
| Plot/visual graph | Code can generate coordinates; display needs a plotting facility | Usually library for visualization | No |

The distinction is important: a library may provide implementation convenience or numerical robustness, but it does not create the mathematical capability. Every Order-1 capability identified here can be implemented with ordinary variables, arithmetic, loops, and conditionals.

## 11. AI-relevant capability without assuming AI

| Mathematical capability | Possible computational role | Sufficient by itself? |
|---|---|---|
| Scalar | Quantity, parameter, or state | No |
| Equality/order | Exact or relational decision | No |
| Absolute difference | Scalar discrepancy | No |
| Vector | Structured input/state/output | No |
| Vector distance | Closeness measurement | No |
| Dot product | Alignment or projection score | No |
| Function | Deterministic input-output mapping | No |
| Sequence/recurrence | Time-indexed state and update | Potentially important, but needs a rule |
| Matrix transformation | Compact multi-component transformation | No; not initially necessary |
| Line equation | Explicit linear relation/boundary | No |
| Circle equation | Explicit radial/nonlinear boundary | No |
| Permutation/combination | Finite alternative counting | No |
| Trigonometric function | Periodic or angular transformation | No |
| Derivative | Local rate/sensitivity | No; conditional later |
| Integral | Accumulation over an interval | No; conditional later |

None of these entries warrants a conclusion about intelligence, cognition, learning, or a neuron. They are mathematical building blocks and computational roles only.

## 12. Smallest closed mathematical set

For the abstract loop

```text
Input → Representation → Measurement → Decision → State Update → Output
```

the smallest defensible substrate is:

| Required element | Smallest form | Textbook supply |
|---|---|---|
| Input | One scalar `x_t`, or a finite tuple if needed | Ch. 1 arithmetic; Ch. 2 vector components; Ch. 8 function inputs |
| Representation | Scalar `x_t` and state `s_t`; optionally a vector | Ch. 1, Ch. 2 |
| Measurement | Absolute difference `|x_t−s_t|`; for vectors, `||x_t−s_t||` | Ch. 1 scalar arithmetic; Ch. 2 magnitude and subtraction |
| Comparison | Equality/order or threshold comparison | Ch. 1 equations/inequalities and Ch. 3 boundary relations |
| State | A stored scalar or finite vector `s_t` | Ch. 1 variables; Ch. 2 vector representation |
| Update | Explicit recurrence such as `s_{t+1}=F(s_t,x_t)` using addition/subtraction/scaling | Ch. 1 algebra; Ch. 8 function/composition; recurrence is an interpretation, not a named memory mechanism |
| Output | Scalar or vector value, possibly selected by a condition | Ch. 1 and Ch. 2; Ch. 8 evaluation |

The smallest mathematical set is therefore **scalar arithmetic, absolute difference, comparison, a finite state variable, an explicitly supplied function/recurrence, and scalar output**. If the first experiment needs structured inputs, replace scalar representation and scalar difference with **finite vectors, vector subtraction, and Euclidean magnitude**. No matrix, trigonometric identity, circle, permutation count, derivative, or integral is required for closure of this loop.

This conclusion must be qualified: the textbook supplies the mathematical ingredients, not the actual storage device, input sensor, execution schedule, update-selection principle, tolerance policy, or output interface. A mathematical state is not itself memory; memory requires an executable mechanism that preserves and updates a value.

## 13. Complete chapter capability table

| Chapter | Mathematical domain | Core objects | Core operations | Measurement capabilities | Computational capabilities | Dependency level | Initial relevance |
|---:|---|---|---|---|---|---|---|
| 1 | Matrices/determinants | Scalars, arrays, matrices, determinants | Entrywise operations, products, transpose, determinant, inverse | Equality, determinant/non-singularity tests | Structured data and linear transformation | Foundational to advanced | Potentially useful |
| 2 | Vectors | Components, directed segments, points | Add, subtract, scale, dot, project | Magnitude, distance, angle, alignment | Structured representation and comparison | Foundational extension | Required for multi-component state |
| 3 | Straight lines | Coordinates, slopes, line equations | Distance, slope, line construction | Point/line distance, relative slope | Linear relation and boundary | Dependent on coordinates/algebra | Potentially useful |
| 4 | Circles | Points, quadratic curves | Circle equation, tangent/chord relations | Radial distance, inside/on/outside | Nonlinear geometric boundary | Dependent on coordinates/algebra | Not required initially |
| 5 | Permutations/combinations | Finite sets and counts | Factorial, ordered/unordered selection | Count of alternatives | Finite enumeration/branch-space size | Arithmetic and finite sets | Outside current scope initially |
| 6 | Trigonometric ratios | Angles and ratios | Ratio evaluation, identities, equations | Angular ratio and periodic value | Periodic transformation | Function/algebra dependent | Potentially useful later |
| 7 | Associated angles | Angles and trig expressions | Compound/multiple/submultiple identities | Derived angular comparisons | Advanced periodic transformation | Depends on Ch. 6 | Not required initially |
| 8 | Functions/graphs | Sets, pairs, mappings | Evaluate, compose, invert, graph | Domain/range and output comparison | Deterministic transformation | Arithmetic/relations | Required as an abstraction |
| 9 | Differentiation | Functions, limits, rates | Derivative rules, higher derivatives | Rate/sensitivity, extrema tests | Continuous-change analysis | Functions and limits | Not required initially |
| 10 | Integration | Functions, intervals, accumulated values | Antiderivative, definite integral | Accumulation/area | Continuous aggregation | Functions and calculus | Not required initially |

## 14. Missing capabilities

The selected minimal subset does **not** by itself provide a physical input channel, persistent storage, a scheduler or clock, a numerical precision policy, noise handling, a tolerance parameter, a rule for choosing among multiple measurements, a learning procedure, a probabilistic model, a search policy, semantic labels, or a guarantee of useful behavior. These are not silently imported from the textbook.

The subset also does not provide a general metric on arbitrary objects unless a domain, difference operation, and norm are specified. It does not provide probability merely because permutations and combinations count finite arrangements. It does not provide optimization merely because differentiation can locate stationary points. It does not provide memory merely because sequences or vectors can be written down.

## 15. Recommended Order-1 boundary

**Allow in Order 1:** real or rational scalar values; finite tuples/vectors if required; addition, subtraction, multiplication, division where defined; absolute value; squares and square roots where needed for Euclidean magnitude; equality and ordering; finite conditionals; explicit functions; a stored scalar/vector state; and an explicitly stated recurrence/update rule.

**Prohibit until experimental evidence justifies introduction:** matrices as a general parameterization; circles and other nonlinear geometric boundaries; permutations/combinations as a search theory; trigonometric and associated-angle machinery; derivatives and gradient-like adjustment; integration; probability; stochastic sampling; optimization objectives; learning algorithms; neural terminology; and any architecture-specific equation.

The boundary is not a claim that the prohibited topics are unimportant. It is a minimality control: each later capability must be introduced only when an observed failure of the Order-1 substrate makes it mathematically necessary.

## 16. Final conclusion

**FACT:** The textbook supplies scalar algebra, equations, coordinate and vector mathematics, matrices, functions, trigonometric transformations, differentiation, and integration. **INTERPRETATION:** These support representation, measurement, transformation, comparison, and—in the presence of an explicitly defined recurrence—state update. **HYPOTHESIS:** The smallest defensible starting substrate is scalar arithmetic plus absolute difference, comparison, stored scalar/vector state, an explicit function/recurrence, and output selection.

The strongest minimality conclusion is therefore:

> **Begin with scalar or finite-vector representation, subtraction, absolute difference or Euclidean distance, equality/ordering, an explicit finite-step state variable, and an ordinary programmed update. Add matrices, calculus, geometry, trigonometry, counting, or other chapters only when experimental evidence demonstrates that the smaller substrate cannot express the required behavior.**

This conclusion deliberately does not design a neuron, neural network, learning algorithm, weight system, threshold architecture, activation function, gradient descent procedure, or backpropagation mechanism.

## References

[1]: /home/ubuntu/upload/HigherMath1stKetabuddin2026.pdf "Higher Math 1st Year textbook, supplied PDF (660 scanned pages)"
