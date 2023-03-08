import mesa
from box_agent import *
from pallet_model import *

# init
current_boxes = 0

class RobotAgent(mesa.Agent):
    # A model-based agent with has_box property set to False

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.has_box = False

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore = True,
            include_center = False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    def get_box(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            for cellmate in cellmates:
                if cellmate.__class__.__name__ == "BoxAgent":
                    self.model.grid.remove_agent(cellmate)
                    self.has_box = True
                    break

    def drop_box(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            for cellmate in cellmates:
                if cellmate.__class__.__name__ == "PalletAgent":

                    global current_boxes
                    current_boxes += 1

                    cellmate.box_counter += 1
                    self.has_box = False
                    break

    def step(self):
        self.move()
        if self.has_box:
            self.drop_box()
        else:
            self.get_box()

class RobotModel (mesa.Model):
    def __init__(self, box_num_agt, rob_num_agt, pall_num_agt, width, height):
        self.box_num_agents = box_num_agt
        self.rob_num_agents = rob_num_agt
        self.pall_num_agents = pall_num_agt

        # Define grid (with toroidal true)
        self.grid = mesa.space.MultiGrid(width, height, True)
        # Set a random scheduler
        self.schedule = mesa.time.RandomActivation(self)

        for i in range(self.box_num_agents):
            a = BoxAgent(i, self)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        # Create RobotAgent
        for i in range(self.rob_num_agents):
            a = RobotAgent(i, self)
            self.schedule.add(a)

            # Add agent to a random grid cell (in the multi grid)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

        for i in range(self.pall_num_agents):
            a = PalletAgent(i, self)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
    
    def step(self):
        if current_boxes < self.box_num_agents:
            self.schedule.step()
        else:
            print("All boxes have been placed on the pallets")
            self.running = False
