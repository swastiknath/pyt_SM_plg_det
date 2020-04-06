# torch imports
import torch.nn.functional as F
import torch.nn as nn


## TODO: Complete this classifier
class MulticlassClassifier(nn.Module):
   

    ## TODO: Define the init function, the input params are required (for loading code in train.py to work)
    def __init__(self, input_features, hidden_dim, output_dim):
        """
        Initialize the model by setting up linear layers.
        Use the input parameters to help define the layers of your model.
        :param input_features: the number of input features in your training/test data
        :param hidden_dim: helps define the number of nodes in the hidden layer(s)
        :param output_dim: the number of outputs you want to produce
        """
        super(MulticlassClassifier, self).__init__()

        # define any initial layers, here
        self.linear1 = nn.Linear(in_features = input_features, out_features = hidden_dim)
        self.relu =  nn.ReLU(inplace=True)
        self.linear2 = nn.Linear(in_features = hidden_dim, out_features = output_dim)
        self.sof = nn.Softmax()
    ## TODO: Define the feedforward behavior of the network
    def forward(self, x):
        """
        Perform a forward pass of our model on input features, x.
        :param x: A batch of input features of size (batch_size, input_features)
        :return: A single, sigmoid-activated value as output
        """
        
        # define the feedforward behavior
        x = self.linear1(x.float())
        x = self.relu(x.float())
        x = self.linear2(x.float())
        x = self.sof(x)
        return x
 