import plotly.express as px
from data.download import download_data

def plt_line_i(ticker:str):
    """Plot a interactive plot using plotly.

    Args:
        ticker (str): The ticker of financial asset.

    Returns:
        plotly: A ticker plot.
    """

    data = download_data(ticker)

    fig = px.line(
        data.reset_index(),
        x="Date", y="Close", title=ticker,
        labels={"Close": 'Fechamento', "Date": "Data"}
    )

    return fig 