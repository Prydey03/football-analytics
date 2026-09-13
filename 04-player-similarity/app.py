import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

st.title("Premier League Player Similarity Finder")
st.write("Enter a player name to find statistically similar players based on 2024-25 Premier League stats.")
st.caption("Note: comparisons are strongest for attacking players. Defensive midfielder matches may be less reliable due to limited defensive metrics available in the underlying data.")

@st.cache_data
def load_data():
    model_data = pd.read_csv('player_data.csv')
    
    final_features = ['Standard_Gls_p90', 'Standard_Sh_p90', 'Standard_SoT%', 'Standard_G/Sh',
                       'Performance_Ast_p90', 'Performance_Crs_p90', 'Performance_TklW_p90',
                       'Performance_Int_p90', 'Performance_Fls_p90', 'Performance_Fld_p90']
    
    X = model_data[final_features].fillna(0)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    nn_model = NearestNeighbors(n_neighbors=6, metric='cosine')
    nn_model.fit(X_scaled)
    
    return model_data, X_scaled, nn_model, final_features

model_data, X_scaled, nn_model, final_features = load_data()

player_list = sorted(model_data['player'].unique())
selected_player = st.selectbox("Select a player:", player_list)

if selected_player:
    idx = model_data[model_data['player'] == selected_player].index[0]
    row_position = model_data.index.get_loc(idx)
    
    distances, indices = nn_model.kneighbors([X_scaled[row_position]])
    similar_players = model_data.iloc[indices[0][1:6]][['player', 'team', 'pos'] + final_features]
    
    st.subheader(f"Players similar to {selected_player}:")
    st.dataframe(similar_players)