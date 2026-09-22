import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Set page title
st.set_page_config(page_title="GridFit", layout="wide")
st.title("GridFit: Kerala Solar + Demand Profile")
st.write("This is the foundation model showing typical solar generation vs. evening peak demand in Kerala.")

# Generate 24-hour profile (Placeholder data for now)
hours = np.arange(24)

# Mock solar generation (bell curve, peak at noon)
solar = 100 * np.exp(-((hours - 13)**2) / (2 * 2.5**2))
solar[hours < 6] = 0
solar[hours > 18] = 0

# Mock demand profile (base load + evening peak between 6 PM and 10 PM)
demand = np.full(24, 20) # Base load
demand[17:23] = 80 # Evening peak (6 PM - 10 PM)
demand[12:14] = 40 # Daytime peak (eVTOL charging)

# Create DataFrame
df = pd.DataFrame({'Hour': hours, 'Solar Generation (kW)': solar, 'Demand (kW)': demand})
df.set_index('Hour', inplace=True)

# Create plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Solar Generation (kW)'], mode='lines+markers', name='Solar Generation', fill='tozeroy', line=dict(color='orange')))
fig.add_trace(go.Scatter(x=df.index, y=df['Demand (kW)'], mode='lines+markers', name='Demand', line=dict(color='red')))
fig.update_layout(title='24-Hour Solar vs Demand Profile', xaxis_title='Hour of Day', yaxis_title='Power (kW)', hovermode='x unified')

# Display plot
st.plotly_chart(fig, use_container_width=True)

st.subheader("Data Table")
st.dataframe(df)
