import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def relu(z):
    return np.maximum(0, z)


def dRelu(x):
    x[x <= 0] = 0
    x[x > 0] = 1
    return x


def dSigmoid(x):
    s = 1 / (1 + np.exp(-x))
    dX = s * (1-s)
    return dX


class dlnet:
    def __init__(self, x, y):
        self.X = x  # Inputs to network
        self.Y = y  # Desired output of network
        self.Yh = np.zeros((1, self.Y.shape[1]))  # Network output

        self.L = 2  # Number of layers in network
        self.dims = [9, 15, 1]  # The number of neurons in each layer

        self.param = {}  # Dictionary to hold W and b params of network
        self.ch = {}  # Cache variable to hold temporary calculations
        self.grad = {}  # Gradient

        self.loss = []  # Stores the loss value of the network every x iterations
        self.lr = 0.003  # Learning rate
        self.sam = self.Y.shape[1]  # Number of training samples

    def nInit(self):
        np.random.seed(1)
        self.param['W1'] = np.random.randn(self.dims[1], self.dims[0]) / np.sqrt(self.dims[0])
        self.param['b1'] = np.zeros((self.dims[1], 1))
        self.param['W2'] = np.random.randn(self.dims[2], self.dims[1]) / np.sqrt(self.dims[1])
        self.param['b2'] = np.zeros((self.dims[2], 1))
        return

    def forward(self):
        Z1 = self.param['W1'].dot(self.X) + self.param['b1']
        A1 = relu(Z1)
        self.ch['Z1'], self.ch['A1'] = Z1, A1

        Z2 = self.param['W2'].dot(A1) + self.param['b2']
        A2 = sigmoid(Z2)
        self.ch['Z2'], self.ch['A2'] = Z2, A2

        self.Yh = A2
        loss = self.nloss(A2)
        return self.Yh, loss

    def nloss(self, Yh):
        loss = (1. / self.sam) * (-np.dot(self.Y, np.log(Yh).T) - np.dot((1 - self.Y), np.log(1 - Yh).T))
        return loss

    def backward(self):
        dLoss_Yh = - (np.divide(self.Y, self.Yh) - np.divide(1 - self.Y, 1 - self.Yh))
        dLoss_Z2 = dLoss_Yh * dSigmoid(self.ch['Z2'])
        dLoss_A1 = np.dot(self.param['W2'].T, dLoss_Z2)
        dLoss_W2 = 1. / self.ch['A1'].shape[1] * np.dot(dLoss_Z2, self.ch['A1'].T)
        dLoss_b2 = 1. / self.ch['A1'].shape[1] * np.dot(dLoss_Z2, np.ones([dLoss_Z2.shape[1], 1]))

        dLoss_Z1 = dLoss_A1 * dRelu(self.ch['Z1'])
        dLoss_A0 = np.dot(self.param['W1'].T, dLoss_Z1)
        dLoss_W1 = 1. / self.X.shape[1] * np.dot(dLoss_Z1, self.X.T)
        dLoss_b1 = 1. / self.X.shape[1] * np.dot(dLoss_Z1, np.ones([dLoss_Z1.shape[1], 1]))

        self.param['W1'] -= self.lr * dLoss_W1
        self.param['b1'] -= self.lr * dLoss_b1
        self.param['W2'] -= self.lr * dLoss_W2
        self.param['b2'] -= self.lr * dLoss_b2

    def gd(self, x, y, iter=3000):
        np.random.seed(1)

        self.nInit()

        for i in range(0, iter):
            Yh, loss = self.forward()
            self.backward()

            if i % 500 == 0:
                print('Cost after iteration %i: %f' % (i, loss))
                self.loss.append(loss)

        return

    def pred(self, x, y):
        self.confidence = 0.99
        self.X = x
        self.Y = y
        comp = np.zeros((1, x.shape[1]))
        pred, loss = self.forward()

        for i in range(0, pred.shape[1]):
            if pred[0, i] > self.confidence: comp[0, i] = 1
            else: comp[0, 1] = 0

        print('Acc: ' + str(np.sum((comp == y)/x.shape[1])))
        return comp
