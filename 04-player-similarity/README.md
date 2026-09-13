# Stage 4: Player Similarity Engine

**Goal:** Build a scouting-style tool that finds players with statistically 
similar playing profiles — mimicking a real recruitment workflow (find 
alternatives to a target player).

**Data:** FBref (via `soccerdata`) — 2024-25 Premier League season, 322 
players with 10+ full matches played, combining standard, shooting, and 
miscellaneous stat categories.

**Method:** 10 per-90 features (goals, shots, shot accuracy, conversion 
rate, assists, crosses, tackles, interceptions, fouls) were standardized 
and compared using cosine similarity via k-nearest-neighbors.

**Results:** the model performs strongly for attacking players. Bukayo 
Saka's top matches (Trossard, Sávio, Eze, Traoré, Doku) are all wide 
attacker/dribbler profiles; Erling Haaland's matches (Isak, Mateta, Wood, 
Wissa, Welbeck) are all efficient penalty-box finishers.

**Limitation:** defensive midfielder comparisons are less reliable due to 
a thinner defensive feature set — only tackles won and interceptions were 
available. Confirmed via the library's documentation that `soccerdata`'s 
FBref wrapper does not expose richer passing/defensive stat categories at 
the player-season level.

**Tools:** `soccerdata`, `scikit-learn`, `pandas`