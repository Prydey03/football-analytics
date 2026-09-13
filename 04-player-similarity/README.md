# Stage 4: Player Similarity Engine

**Goal:** Build a scouting-style tool that finds players with statistically 
similar playing profiles — mimicking a real recruitment workflow (find 
alternatives to a target player at a different age or cost bracket).

**Data:** FBref (via `soccerdata`) — 2024-25 Premier League season, 322 
players with 10+ full matches played, combining standard, shooting, and 
miscellaneous stat categories.

## Method

Ten per-90 features were engineered from raw season stats, covering 
attacking output, shot quality, and defensive contribution: goals, shots, 
shot accuracy, goals-per-shot, assists, crosses, tackles won, 
interceptions, fouls committed, and fouls drawn — all standardized 
(z-scores) so no single stat dominates due to scale differences. Player 
similarity was then calculated using cosine similarity via 
k-nearest-neighbors, returning the 5 closest statistical matches to any 
given player.

## Results

The model performs strongly for attacking players. Bukayo Saka's closest 
matches (Trossard, Sávio, Eze, Traoré, Doku) are all recognizable wide 
attacker/dribbler profiles. Erling Haaland's matches (Isak, Mateta, Wood, 
Wissa, Welbeck) are all high-efficiency penalty-box finishers. Both 
results align closely with genuine football intuition.

Defenders also cluster sensibly — Aaron Wan-Bissaka's closest matches 
(Justin, Huijsen, Martínez) are predominantly other defenders, with only 
two midfielders appearing in the top 5.

## Limitation

Defensive **midfielder** comparisons specifically are less reliable. 
Declan Rice's closest matches skewed toward creative attacking midfielders 
rather than genuine ball-winners. This is likely because only two 
defensive metrics (tackles won, interceptions per 90) were available 
through FBref's data via `soccerdata`, and a deep-lying midfielder's style 
is harder to distinguish numerically from an attacking midfielder's when 
defensive signal is this limited — whereas a fullback's overall stat 
profile (low goals, moderate crossing, some defensive actions) is more 
numerically distinct regardless. I confirmed this is a genuine data 
ceiling by checking `soccerdata`'s own documentation: the FBref wrapper 
does not expose a dedicated passing or richer defensive stat category at 
the player-season level, only `standard`, `shooting`, `playing_time`, 
`keeper`, and `misc`.

## Interactive App

This project includes a live Streamlit app where you can select any 
Premier League player and see their 5 most statistically similar players.

**To run locally:**
pip install -r requirements.txt
streamlit run app.py

**Live app: [football-analytics-mrbbroanuyjpffm3ksutjb.streamlit.app)**

This project includes a live Streamlit app...

![app screenshot](app_screenshot.png)

**Tools:** `soccerdata`, `scikit-learn`, `pandas`, `streamlit`