# Design Philosophy — contingency-respondent-dsl

> Part of the `contingency-respondent-dsl` package. Records the design
> principles that constrain what this package adds and how it adds it.

---

## 1. Additive-only discipline

This package may add productions to the Core respondent grammar *only*
through the extension point `ExtensionRespondentPrimitive`. The following
are prohibited:

- Redefining any Tier A primitive (`Pair.*`, `Extinction`, `CSOnly`,
  `USOnly`, `Contingency`, `TrulyRandom`, `ExplicitlyUnpaired`,
  `Compound`, `Serial`, `ITI`, `Differential`).
- Introducing new LL(2) decision points. Every Tier B primitive is spelled
  as `IdentUpper "(" ArgList? ")"` and is distinguishable from Tier A at
  the first token via the reserved-keyword test documented in Core's
  `spec/en/respondent/grammar.md §3`.
- Adding Turing-complete constructs. Every Tier B primitive must be a
  finite, declarative procedure whose parameters are literal values
  determined at parse time.
- Requiring changes to `foundations/`, `operant/`, `composed/`,
  `experiment/`, or `annotations/` in Core.

If a proposed primitive requires any of the above, it is out-of-scope for
this package and must be routed to Core as a separate proposal there.

---

## 2. Why Tier B lives in its own package

The EAB-centric Core respondent layer serves experimenters who primarily
run **operant** preparations and need a minimal two-term vocabulary to
describe the respondent components of their procedures (pairing,
extinction, contingency space). The Tier B primitives served by this
package serve a different user: the researcher doing **classical
conditioning** as the primary preparation, who needs names for cue
competition, inhibitory learning, preexposure, extinction–recovery
phenomena, and specialized preparations such as conditioned taste
aversion, the peak procedure, and contextual fear conditioning.

Separating the two audiences has three concrete benefits:

1. **Cognitive scope.** A JEAB experimenter reading `contingency-dsl`
   does not have to navigate around 26 Pavlovian-only primitives whose
   operational definitions reference attention models, consolidation,
   and reconsolidation.
2. **Versioning independence** (in spirit; no version declarations in
   either package — see §5). Tier B can gain primitives as the
   Pavlovian-learning literature gains them, without disturbing the
   EAB Core.
3. **Registry demonstration.** This package is the first working example
   of how a third party extends the Core respondent grammar. A second
   or third such package (e.g., social-learning extensions, drug-self-
   administration extensions) can use the same pattern without needing
   permission from Core.

---

## 3. Program-scoped registries

Extension primitives are resolved at **program scope**, not globally.
Each program (interpreter / runtime instance) that wishes to use Tier B
declares it in the program header (conceptual: `import
respondent_tier_b`), and the registry resolution is local to that
program. Programs that do not import this registry see `Blocking(...)`,
`Renewal(...)`, etc., as unknown identifiers and receive parse errors
(Core `respondent/grammar.md §4`, property 2).

This inherits the Schedule-Extension principle on the operant side
(Core `design-philosophy §5`) and ensures that:

- No primitive "leaks" into a program that did not ask for it.
- Two programs can load conflicting Tier B variants without interfering.
- The Core parser remains program-independent.

---

## 4. Scientific justification for the 26-primitive selection

The selection is not encyclopedic; it is **procedure-centric**. A
phenomenon is listed as a Tier B primitive if and only if:

1. It is named as a distinct preparation in the primary Pavlovian
   literature.
2. Encoding it as a plain composition of Tier A primitives would **lose
   operational intent** — the procedural structure (e.g., the
   Phase 1 / Phase 2 / Test arrangement of blocking) matters and should
   be visible in the AST.
3. At least one peer-reviewed primary source defines the operational
   procedure.

Phenomena that fail (2) — e.g., "US of intensity X" — are handled by the
`respondent-annotator` in Core rather than by this package.

Primary anchors for the 26 primitives:

- **Foundational pairing and its control procedures** — Pavlov (1927);
  Rescorla (1967, 1968) — are Tier A in Core.
- **Acquisition variants** beyond simple pairing — higher-order
  conditioning, sensory preconditioning, counterconditioning — Pavlov
  (1927); Brogden (1939); Rizley & Rescorla (1972); Dickinson & Pearce
  (1977).
- **Cue-competition** predictions of Rescorla & Wagner (1972) —
  blocking, overshadowing, overexpectation, super-conditioning,
  retrospective revaluation — Kamin (1969); Mackintosh (1976); Rescorla
  (1970, 1971); Van Hamme & Wasserman (1994).
- **Inhibitory learning** — conditioned inhibition, occasion setting,
  inhibition of delay, summation / retardation test — Rescorla (1969);
  Holland (1983).
- **Preexposure** effects — latent inhibition, US preexposure — Lubow &
  Moore (1959); Randich & LoLordo (1979).
- **Extinction and recovery** — renewal, reinstatement, spontaneous
  recovery, contextual extinction, reconsolidation interference —
  Rescorla & Heth (1975); Bouton & Bolles (1979); Bouton (2004);
  Rescorla (2004); Monfils et al. (2009).
- **Specialized preparations** — conditioned taste aversion, stimulus
  generalization, contextual fear conditioning, peak procedure,
  mediated conditioning — Garcia, Ervin, & Koelling (1966); Hovland
  (1937); Fanselow (1990); Roberts (1981); Holland (1981).

---

## 5. No in-file version markers

This package does **not** embed version-marking prose in tracked files
(no "v1", no "major bump", no "Core freeze"). History is carried by
`git tag` / `git log` and not duplicated in documentation.

---

## 6. References

- Bouton, M. E. (2004). Context and behavioral processes in extinction.
  *Learning & Memory*, 11(5), 485–494. https://doi.org/10.1101/lm.78804
- Bouton, M. E., & Bolles, R. C. (1979). Contextual control of the
  extinction of conditioned fear. *Learning and Motivation*, 10(4),
  445–466. https://doi.org/10.1016/0023-9690(79)90057-2
- Brogden, W. J. (1939). Sensory pre-conditioning. *Journal of
  Experimental Psychology*, 25(4), 323–332. https://doi.org/10.1037/h0058944
- Dickinson, A., & Pearce, J. M. (1977). Inhibitory interactions between
  appetitive and aversive stimuli. *Psychological Bulletin*, 84(4),
  690–711. https://doi.org/10.1037/0033-2909.84.4.690
- Fanselow, M. S. (1990). Factors governing one-trial contextual
  conditioning. *Animal Learning & Behavior*, 18(3), 264–270.
  https://doi.org/10.3758/BF03205285
- Garcia, J., Ervin, F. R., & Koelling, R. A. (1966). Learning with
  prolonged delay of reinforcement. *Psychonomic Science*, 5(3),
  121–122. https://doi.org/10.3758/BF03328311
- Holland, P. C. (1981). Acquisition of representation-mediated
  conditioned food aversions. *Learning and Motivation*, 12(1), 1–18.
  https://doi.org/10.1016/0023-9690(81)90022-9
- Holland, P. C. (1983). Occasion-setting in Pavlovian feature positive
  discriminations. In M. L. Commons, R. J. Herrnstein, & A. R. Wagner
  (Eds.), *Quantitative analyses of behavior* (Vol. 4, pp. 183–206).
  Ballinger.
- Hovland, C. I. (1937). The generalization of conditioned responses: I.
  The sensory generalization of conditioned responses with varying
  frequencies of tone. *Journal of General Psychology*, 17(1), 125–148.
  https://doi.org/10.1080/00221309.1937.9917977
- Kamin, L. J. (1969). Predictability, surprise, attention, and
  conditioning. In B. A. Campbell & R. M. Church (Eds.), *Punishment
  and aversive behavior* (pp. 279–296). Appleton-Century-Crofts.
- Lubow, R. E., & Moore, A. U. (1959). Latent inhibition. *Journal of
  Comparative and Physiological Psychology*, 52(4), 415–419.
  https://doi.org/10.1037/h0046700
- Mackintosh, N. J. (1975). A theory of attention: Variations in the
  associability of stimuli with reinforcement. *Psychological Review*,
  82(4), 276–298. https://doi.org/10.1037/h0076778
- Mackintosh, N. J. (1976). Overshadowing and stimulus intensity. *Animal
  Learning & Behavior*, 4(2), 186–192.
  https://doi.org/10.3758/BF03214033
- Monfils, M.-H., Cowansage, K. K., Klann, E., & LeDoux, J. E. (2009).
  Extinction-reconsolidation boundaries. *Science*, 324(5929), 951–955.
  https://doi.org/10.1126/science.1167975
- Pavlov, I. P. (1927). *Conditioned reflexes*. Oxford University Press.
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning.
  *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532
- Randich, A., & LoLordo, V. M. (1979). Associative and nonassociative
  theories of the UCS preexposure phenomenon. *Psychological Bulletin*,
  86(3), 523–548. https://doi.org/10.1037/0033-2909.86.3.523
- Rescorla, R. A. (1967). Pavlovian conditioning and its proper control
  procedures. *Psychological Review*, 74(1), 71–80.
  https://doi.org/10.1037/h0024109
- Rescorla, R. A. (1968). Probability of shock in the presence and
  absence of CS in fear conditioning. *Journal of Comparative and
  Physiological Psychology*, 66(1), 1–5. https://doi.org/10.1037/h0025984
- Rescorla, R. A. (1969). Pavlovian conditioned inhibition. *Psychological
  Bulletin*, 72(2), 77–94. https://doi.org/10.1037/h0027760
- Rescorla, R. A. (1970). Reduction in the effectiveness of reinforcement
  after prior excitatory conditioning. *Learning and Motivation*, 1(4),
  372–381. https://doi.org/10.1016/0023-9690(70)90101-3
- Rescorla, R. A. (1971). Variation in the effectiveness of reinforcement
  and nonreinforcement following prior inhibitory conditioning. *Learning
  and Motivation*, 2(2), 113–123.
  https://doi.org/10.1016/0023-9690(71)90002-6
- Rescorla, R. A. (2004). Spontaneous recovery. *Learning & Memory*,
  11(5), 501–509. https://doi.org/10.1101/lm.77504
- Rescorla, R. A., & Heth, C. D. (1975). Reinstatement of fear to an
  extinguished conditioned stimulus. *Journal of Experimental Psychology:
  Animal Behavior Processes*, 1(1), 88–96.
  https://doi.org/10.1037/0097-7403.1.1.88
- Rescorla, R. A., & Solomon, R. L. (1967). Two-process learning theory.
  *Psychological Review*, 74(3), 151–182.
  https://doi.org/10.1037/h0024475
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian
  conditioning. In A. H. Black & W. F. Prokasy (Eds.), *Classical
  conditioning II* (pp. 64–99). Appleton-Century-Crofts.
- Rizley, R. C., & Rescorla, R. A. (1972). Associations in second-order
  conditioning and sensory preconditioning. *Journal of Comparative and
  Physiological Psychology*, 81(1), 1–11. https://doi.org/10.1037/h0033333
- Roberts, S. (1981). Isolation of an internal clock. *Journal of
  Experimental Psychology: Animal Behavior Processes*, 7(3), 242–268.
  https://doi.org/10.1037/0097-7403.7.3.242
- Van Hamme, L. J., & Wasserman, E. A. (1994). Cue competition in
  causality judgments: The role of nonpresentation of compound stimulus
  elements. *Learning and Motivation*, 25(2), 127–151.
  https://doi.org/10.1006/lmot.1994.1008

