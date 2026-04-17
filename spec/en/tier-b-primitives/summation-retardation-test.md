# Summation / Retardation Test

## DSL spelling

`SummationRetardationTest(inhibitor=<StimulusRef>, excitor=<StimulusRef>,
                         us=<StimulusRef>,
                         mode=("Summation" | "Retardation"))`

## Operational definition

A **test primitive** — not an acquisition procedure. It takes a
previously trained `inhibitor` I and tests whether I has acquired
negative associative strength. **Summation test:** the compound of I
with a separately trained `excitor` E is tested; if the CR to IE is
smaller than to E alone, I is inhibitory. **Retardation test:** I is
now paired with the US; if acquisition to I is slower than to a
novel control CS, I's negative starting value retarded acquisition
and I is inhibitory. Rescorla (1969) argued that *both* tests must
succeed to establish conditioned inhibition.

## Parameters

| Name | Type | Description |
|---|---|---|
| `inhibitor` | `StimulusRef` | Candidate inhibitor (typically trained via `ConditionedInhibition` or `OccasionSetting`). |
| `excitor` | `StimulusRef` | Separately trained excitatory CS (summation) or the US used for retardation training. |
| `us` | `StimulusRef` | The US. |
| `mode` | `"Summation"` \| `"Retardation"` | Which of the two canonical tests to perform. |

## Example

```
SummationRetardationTest(
    inhibitor = i,
    excitor   = e,
    us        = shock,
    mode      = Summation
)

SummationRetardationTest(
    inhibitor = i,
    excitor   = e,
    us        = shock,
    mode      = Retardation
)
```

## Primary citation

- Rescorla, R. A. (1969). Pavlovian conditioned inhibition.
  *Psychological Bulletin*, 72(2), 77–94. https://doi.org/10.1037/h0027760

## Related primitives

Verification primitive for `ConditionedInhibition` and (partially)
`OccasionSetting`. Does not itself train any CS; presupposes that
`inhibitor` has been trained by a prior preparation in the enclosing
program.

