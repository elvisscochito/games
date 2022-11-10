import mesa

class MoneyAgent(mesa.Agent):
    # A model-based agent with fixed initial wealth

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

class MoneyModel (mesa.Model):
    # A model with some number of agents
    def __init__(self, N):
        self.num_agents = N
        """ self.schedule = mesa.RandomActivation(self) """
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            """ self.schedule.add(a) """
