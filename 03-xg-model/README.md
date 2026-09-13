# Stage 3: Expected Goals (xG) Model Built From Scratch

**Goal:** Move beyond single-variable correlation (Stage 1) to a proper 
multi-feature xG model, and validate it against a professional benchmark 
— demonstrating not just that a relationship exists, but understanding 
which specific factors drive scoring probability and why.

**Data:** StatsBomb open data — 790 shots from the 2024 Copa América 
(32 matches)

**Method:** Logistic regression using five features: distance to goal, 
shot angle, body part (header vs. other), shot type (open play vs. set 
piece), and defensive pressure.

## Key Findings

**Distance, body part, and shot type all mattered — angle and pressure did not.**
Distance to goal, whether a shot was a header, and whether it came from 
open play versus a set piece were all statistically significant predictors 
of scoring (p < 0.01). Shot angle and defensive pressure were not 
significant in this model (p = 0.619 and p = 0.193 respectively). This 
isn't a failure of the model — angle is naturally correlated with distance 
(very wide-angle shots also tend to be further out), so once distance is 
already accounted for, angle adds little additional independent 
information. A model without distance included might show angle as far 
more significant on its own.

**A simple model still closely tracks a professional one.**
Despite using only five features and no defender or goalkeeper positioning 
data, this model's predicted probabilities correlated strongly with 
StatsBomb's own professional xG values (**r = 0.91**). This suggests that 
a small number of well-chosen, interpretable features can capture most of 
the signal in shot quality — the remaining gap is likely explained by 
finer-grained spatial context (how many defenders were between the shooter 
and goal, whether the goalkeeper was positioned well) that isn't present 
in this simpler feature set.

**The model correctly separates penalty kicks as a distinct shot category.**
All five penalties in the dataset clustered tightly around ~60% predicted 
conversion — visible as the distinct point cluster in the comparison chart 
below, sitting apart from the main distribution of open-play shots. This 
is a meaningful sanity check: a well-built xG model should recognize that 
penalties behave fundamentally differently from open-play attempts, and 
this one does, without penalties being explicitly hard-coded as a special 
case.

## Limitation

Where this model diverges most from StatsBomb's xG — for example, one 
shot StatsBomb rated at 0.46 that this model rated at only 0.17 — the gap 
likely reflects StatsBomb's access to defender and goalkeeper positioning 
data via freeze-frame tracking, information this simpler model has no way 
to account for. A shot with a clear sight of an open goal and StatsBomb 
recognizes that; this model can only infer shot difficulty from distance, 
angle, and shot type, and has no visibility into how the defense was set 
up at the moment of the shot. This is the natural ceiling of a model built 
without spatial/positional data, and would be the next area to address 
with a more advanced approach (e.g. incorporating freeze-frame features 
directly).

**Tools:** `statsmodels`, `statsbombpy`, `pandas`, `numpy`, `matplotlib`

![xG comparison](xg_comparison.png)