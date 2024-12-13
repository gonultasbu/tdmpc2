class Trainer:
    """Base trainer class for TD-MPC2."""

    def __init__(self, cfg, env, agent, buffer):
        self.cfg = cfg
        self.env = env
        self.agent = agent
        self.buffer = buffer
        print("Architecture:", self.agent.model)

    def eval(self):
        """Evaluate a TD-MPC2 agent."""
        raise NotImplementedError

    def train(self):
        """Train a TD-MPC2 agent."""
        raise NotImplementedError
