# import requests
import plotly.graph_objects as go

# Fetch data from API (Replace API URL & Key)
# API_URL = "https://api.cryptometer.io/volume-flow/?timeframe=1d&api_key=YOUR_API_KEY"
# response = requests.get(API_URL)
# data = response.json()

# Sample structured data for visualization
flows = [
    {"source": "USD", "target": "USDT", "value": 50000000},
    {"source": "USDT", "target": "ETH", "value": 30000000},
    {"source": "USDT", "target": "BTC", "value": 20000000},
    {"source": "BTC", "target": "SOL", "value": 5000000},
    {"source": "ETH", "target": "BNB", "value": 10000000}
]

# Extract unique nodes
nodes = list(set([item["source"] for item in flows] + [item["target"] for item in flows]))

# Map nodes to indices
node_indices = {node: idx for idx, node in enumerate(nodes)}

# Create Sankey diagram
fig = go.Figure(go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=nodes,
    ),
    link=dict(
        source=[node_indices[item["source"]] for item in flows],
        target=[node_indices[item["target"]] for item in flows],
        value=[item["value"] for item in flows],
    ),
))

fig.update_layout(title_text="Crypto Liquidity Flow", font_size=10)
fig.show()