import mesa
import matplotlib.pyplot as plt
import numpy as np

class MoneyAgent(mesa.Agent):
    # A model-based agent with fixed initial wealth

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore = True,
            include_center = False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1
            print(f"And I exchange wealth with neighbor: {other.unique_id}")

    def step(self):
        print(f"Hi, I'm the agent: {self.unique_id} and I'm at position {self.pos} with wealth {self.wealth}")
        self.move()
        if self.wealth > 0:
            self.give_money()

class MoneyModel (mesa.Model):
    # A model with some number of agents
    def __init__(self, N, width, height):
        self.num_agents = N

        # Define grid (with toroidal true)
        self.grid = mesa.space.MultiGrid(width, height, True)
        # Set a random scheduler
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            agent = MoneyAgent(i, self)
            self.schedule.add(agent)

            # Add agent to a random grid cell (in the multi grid)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y)) 
    
    def step(self):
        # Advance the model by one step (method build in scheduler)
        self.schedule.step()

def training_steps():
    # create the model and the grid
    model = MoneyModel(50, 10, 10)

    # Every agent move by 20 steps
    for i in range(20):
        model.step()

    agent_counts = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        agent_count = len(cell_content)
        agent_counts[x][y] = agent_count
    
    plot_model(agent_counts)

def training_money():
    # create the model and the grid
    model = MoneyModel(50, 10, 10)

    # Every agent move by 20 steps
    for i in range(20):
        model.step()
    
    # Get the wealth of all agents in each cell
    agent_counts = np.zeros((model.grid.width, model.grid.height))
    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        sum = 0
        for agent in cell_content:
            sum += agent.wealth
        agent_counts[x][y] = sum
    plot_model(agent_counts)

def plot_model(model):
    agent_counts = model
    plt.imshow(agent_counts, interpolation = 'nearest')
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    # Run the model
    training_money()
