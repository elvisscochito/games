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

final_wealth = []

def training():

    # Run the model 100 times, each model executing 10 steps
    for j in range(100):
        # Create the model
        model = MoneyModel(10)

        # Print the model's current wealth
        for agent in model.schedule.agents:
            print(f"Agent {agent.unique_id} starts with wealth {agent.wealth}")

        # Advance the model by 10 steps
        for i in range(10):
            # Run the model
            model.step()

        for agent in model.schedule.agents:
            # print the final wealth
            print(f"Agent {agent.unique_id} ends with wealth {agent.wealth}")
            # Store the model's wealth
            final_wealth.append(agent.wealth)

    plot_model(model)

def plot_model(model):
    # Plot the number of agents in the model
    """ agent_wealth = [agent.wealth for agent in model.schedule.agents]
    plt.hist(agent_wealth)
    plt.title("Wealth distribution")
    plt.xlabel("Wealth")
    plt.ylabel("Number of agents")
    plt.show() """

    # Plot the model's final wealth distribution
    plt.hist(final_wealth, bins=range(max(final_wealth)+1))
    plt.title("Wealth distribution")
    plt.xlabel("Wealth")
    plt.ylabel("Number of agents")
    plt.show()

if __name__ == "__main__":
    # Run the model
    training()
