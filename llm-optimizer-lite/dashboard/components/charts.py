import pandas as pd
import plotly.express as px


def cost_timeseries_chart(points: list[dict]):
    frame = pd.DataFrame(points)
    if frame.empty:
        return None
    return px.line(frame, x="ts", y="estimated_cost_usd", title="Estimated Cost Over Time")
