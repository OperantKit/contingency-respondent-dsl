# Theory Framework — Pointer-level

> Part of the `contingency-respondent-dsl` package. This is a short
> framework sketch, **not** a derivation. It exists to ground the
> naming and parameter choices of the 26 Tier B primitives in the
> principal Pavlovian-learning theories, and to point readers to the
> primary textbooks for a full treatment.

---

## 1. Why a framework section at all

The 26 primitive pages in [`tier-b-primitives/`](tier-b-primitives/)
each cite their own primary source. But several of them — blocking,
overshadowing, overexpectation, super-conditioning, retrospective
revaluation — are intelligible only in light of a quantitative model of
Pavlovian associability. This page names the models that Core and this
package assume a reader has seen, and states which parameter choices on
which primitives are derived from which model. It does **not** derive
the equations.

---

## 2. Rescorla–Wagner (error-correcting associability)

Rescorla & Wagner (1972) model associative strength as an
error-correcting delta rule:

- Each US supports a fixed asymptote λ for paired CSs.
- Learning rate scales with CS salience (αᵢ) and US-specific rate (β).
- Prediction error is `λ − ΣVⱼ` summed over CSs present on that trial.

RW directly predicts:

- **Blocking** (Kamin, 1969) — a fully trained CS A zeros the error for
  the compound AX, so X gains no strength.
- **Overshadowing** (Mackintosh, 1976; Pavlov, 1927) — two CSs share a
  single asymptote λ, so each gains less than it would alone.
- **Overexpectation** (Rescorla, 1970) — after separate A+ and B+
  training, compound AB+ starts above λ and drives both toward smaller
  Vs.
- **Super-conditioning** (Rescorla, 1971) — a conditioned inhibitor in
  compound with a novel CS yields negative prediction so the new CS
  overshoots λ.

Tier B productions whose parameters are derived from RW:
`BlockingExpr`, `OvershadowingExpr`, `OverexpectationExpr`,
`SuperConditioningExpr`, `ConditionedInhibitionExpr`,
`SummationRetardationTestExpr`.

---

## 3. Mackintosh (1975) — attentional variation

Mackintosh (1975) modifies RW by allowing αᵢ (CS salience) to grow with
the CS's predictiveness of the US. A relatively better predictor gains
more attention; a worse one loses it.

Mackintosh accommodates:

- **Differential salience across successive phases** — why a redundant
  CS drops in associability rather than merely failing to gain more.
- Individual-cue effects in blocking that RW alone struggles with.

Tier B productions where Mackintosh's α dynamics matter:
`LatentInhibitionExpr`, `OvershadowingExpr`,
`RetrospectiveRevaluationExpr`.

---

## 4. Pearce–Hall (1980) — surprise-driven associability

Pearce & Hall (1980) argue that associability grows with *prediction
error*, not with prediction accuracy. A surprising CS on trial `n` has
high α on trial `n+1`; a well-predicted CS has low α.

Pearce–Hall is the dominant account of:

- **Latent inhibition** (Lubow & Moore, 1959) — repeated preexposure
  without any US drives α to near zero.
- **Continued change in α under extinction and partial reinforcement**.

Tier B productions influenced by PH:
`LatentInhibitionExpr`, `PavlovianPREEExpr`.

---

## 5. SOP / AESOP (Wagner, 1981; Brandon & Wagner, 1991)

Wagner's SOP represents stimuli as elements that cycle through inactive
(I), active primary (A1), and active secondary (A2) memory nodes.
A2-to-A2 co-activation is the substrate of learning; A1-to-A2 produces
excitation; A2-to-A1 produces inhibition.

SOP is the cleanest account of:

- **Mediated conditioning** (Holland, 1981) — a CS retrieves a US
  representation in A2, which is then associable with a new outcome.
- **Second-order and sensory preconditioning** — chain learning via A2
  representations.

Tier B productions derived from SOP: `HigherOrderConditioningExpr`,
`SensoryPreconditioningExpr`, `MediatedConditioningExpr`.

---

## 6. Bouton (1993, 2004) — retrieval and context

Bouton (1993, 2004) argues that extinction is **new learning**, not
unlearning, and that the original excitatory memory remains available
and retrievable in contexts that differ from the extinction context.

Bouton's retrieval theory is the primary account of:

- **Renewal** (Bouton & Bolles, 1979) — ABA / ABC / AAB designs;
  context change at test restores the excitatory memory.
- **Reinstatement** (Rescorla & Heth, 1975) — US-alone presentations
  restore responding by restoring the extinction-blocked retrieval
  context.
- **Spontaneous recovery** (Rescorla, 2004) — passage of time plays the
  role of context change.
- **Contextual extinction** — extinction learning is context-specific.

Tier B productions derived from Bouton: `RenewalExpr`,
`ReinstatementExpr`, `SpontaneousRecoveryExpr`,
`ContextualExtinctionExpr`.

---

## 7. Timing models (Gibbon & Balsam, 1981; Gallistel & Gibbon, 2000)

Scalar expectancy theory and its rate-estimation successor treat trial
duration and ITI as structural variables (the I/T ratio). These models
are the primary account of the peak procedure (Roberts, 1981) and of
the timing-dependent parameters of several other procedures.

Tier B production derived from timing theory: `PeakProcedureExpr`;
parameters of `InhibitionOfDelayExpr`.

---

## 8. What this package does not take a position on

- The choice among RW, Mackintosh, Pearce–Hall, SOP, and retrieval
  theory. Each Tier B primitive is a **procedure**, not a model; which
  model explains its outcome is up to the researcher.
- The neural substrate (Fanselow 1990's contextual fear depends on
  hippocampus–amygdala circuitry; the procedure specification here is
  paradigm-neutral in that regard).
- Molar vs. molecular analysis of respondent data.

Annotations that *do* commit to a specific model live in Core
(`annotations/extensions/learning-models.md`), not here.

---

## 9. References — pointers, not derivations

- Bouton, M. E. (1993). Context, time, and memory retrieval in the
  interference paradigms of Pavlovian learning. *Psychological Bulletin*,
  114(1), 80–99. https://doi.org/10.1037/0033-2909.114.1.80
- Bouton, M. E. (2004). Context and behavioral processes in extinction.
  *Learning & Memory*, 11(5), 485–494. https://doi.org/10.1101/lm.78804
- Bouton, M. E. (2016). *Learning and behavior: A contemporary synthesis*
  (2nd ed.). Sinauer.
- Brandon, S. E., & Wagner, A. R. (1991). Modulation of a discrete
  Pavlovian conditioned reflex by a putative emotive Pavlovian
  conditioned stimulus. *Journal of Experimental Psychology: Animal
  Behavior Processes*, 17(3), 299–311.
  https://doi.org/10.1037/0097-7403.17.3.299
- Gallistel, C. R., & Gibbon, J. (2000). Time, rate, and conditioning.
  *Psychological Review*, 107(2), 289–344.
  https://doi.org/10.1037/0033-295X.107.2.289
- Gibbon, J., & Balsam, P. (1981). Spreading association in time. In
  C. M. Locurto, H. S. Terrace, & J. Gibbon (Eds.), *Autoshaping and
  conditioning theory* (pp. 219–253). Academic Press.
- Mackintosh, N. J. (1974). *The psychology of animal learning*.
  Academic Press.
- Mackintosh, N. J. (1975). A theory of attention. *Psychological
  Review*, 82(4), 276–298. https://doi.org/10.1037/h0076778
- Pearce, J. M. (2013). *Animal learning and cognition* (3rd ed.).
  Psychology Press.
- Pearce, J. M., & Hall, G. (1980). A model for Pavlovian learning.
  *Psychological Review*, 87(6), 532–552.
  https://doi.org/10.1037/0033-295X.87.6.532
- Rescorla, R. A., & Wagner, A. R. (1972). A theory of Pavlovian
  conditioning. In A. H. Black & W. F. Prokasy (Eds.), *Classical
  conditioning II* (pp. 64–99). Appleton-Century-Crofts.
- Wagner, A. R. (1981). SOP: A model of automatic memory processing in
  animal behavior. In N. E. Spear & R. R. Miller (Eds.), *Information
  processing in animals: Memory mechanisms* (pp. 5–47). Erlbaum.

