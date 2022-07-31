import torch
import torch.nn as nn

num_samples = 20
input_size = 10
layer_size = 15
output_size = 5

# First, set up your dataset and model.
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(input_size, layer_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(layer_size, output_size)

    def forward(self, input):
        return self.layer2(self.relu(self.layer1(input)))


# In this example we use a randomly generated dataset.
input = torch.randn(num_samples, input_size)
labels = torch.randn(num_samples, output_size)

# Now define your single-worker PyTorch training function.
import torch.optim as optim


def train_func():
    num_epochs = 3
    model = NeuralNetwork()
    loss_fn = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    for epoch in range(num_epochs):
        output = model(input)
        loss = loss_fn(output, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f"epoch: {epoch}, loss: {loss.item()}")


train_func()
