import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    cols = len(players.axes[1])
    rows = len(players.axes[0])
    return [rows, cols]
    