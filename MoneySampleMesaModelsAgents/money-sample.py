import mesa
import matplotlib.pyplot as plt

class MoneyAgent(mesa.Agent):
    # A model-based agent with fixed initial wealth

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        # The agent's step will go here.
        # For demostration purposes, we just print a message.
        print(f"Hi, I'm the agent: {self.unique_id}")

        # Exchange wealth with random neighbor
        if self.wealth > 0:
            neighbor = self.random.choice(self.model.schedule.agents)
            neighbor.wealth += 1
            self.wealth -= 1
            print(f"And I exchange wealth with neighbor: {neighbor.unique_id}")
class MoneyModel (mesa.Model):
    # A model with some number of agents
    def __init__(self, N):
        self.num_agents = N
        # Set a random scheduler
        self.schedule = mesa.time.RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            agent = MoneyAgent(i, self)
            self.schedule.add(agent)
    
    def step(self):
        # Advance the model by one step (method build in scheduler)
        self.schedule.step()

def plot_model(model):
    # Plot the number of agents in the model
    agent_wealth = [agent.wealth for agent in model.schedule.agents]
    plt.hist(agent_wealth)
    plt.title("Wealth distribution")
    plt.xlabel("Wealth")
    plt.ylabel("Number of agents")
    plt.show()

if __name__ == "__main__":
    # Create a model
    empty_model = MoneyModel(10)
    # Run the model
    empty_model.step()
    # Plot the model
    plot_model(empty_model)
