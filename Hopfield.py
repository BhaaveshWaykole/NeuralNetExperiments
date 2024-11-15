import numpy as np

# Initial pattern and target pattern
x = np.array([1, 1, 1, 0])  # Stored pattern
tx = np.array([0, 0, 1, 0])  # Test pattern 

# Initialize weight matrix with zeros
w = np.zeros((4, 4))

# Initial state of the network 
y = np.array([0, 0, 1, 0])

# Convergence flag
con = True

# Update order
up = [0, 1, 2, 3]  # A custom order for updating nodes, as in original

# Local multiplication update rule for weights 
for i in range(4):
    for j in range(4):
        if i != j:
            w[i, j] = x[i] * x[j]

#Display weight matrix
print(w)

# Start iterative update
while con:
    yin = np.zeros(4)  # Yin will store the net input for each neuron
    for i in up:  # Update the neurons in the specified order
        yin[i] = tx[i] + np.dot(y, w[:, i])  
        
        # Activation function: Threshold at 0
        if yin[i] > 0:
            y[i] = 1
        else:
            y[i] = 0

    # Check for convergence: if current state y matches the stored pattern x
    if np.array_equal(y, x):
        print('Convergence has been obtained')
        print('The converged output:')
        print(y)
        con = False  # End the loop if convergence is reached
