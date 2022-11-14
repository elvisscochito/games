import mesa
from money_model import *

# set visual properties for agents
def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5}
    if agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5 + 0.5 * agent.wealth
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.2
    return portrayal

# grid visualization of the model
grid = mesa.visualization.CanvasGrid(
    agent_portrayal,
    10, 10, 500, 500
)

# set up server and create the model at the same time (instead of creating model separately)
server = mesa.visualization.ModularServer(
    MoneyModel,
    [grid],
    "Money Model",
    {"N": 100, "width": 10, "height": 10}
)

server.port = 8521 # The default
server.launch()
