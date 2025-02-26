import numpy as np

def pinchOne():
    return np.array([[1, 0, 0, 0, 0, 0, 0, 0]])
def pinchTwo():
    return np.array([[0, 1, 0, 0, 0, 0, 0, 0]])
def pinchThree():
    return np.array([[0, 0, 1, 0, 0, 0, 0, 0]])
def pinchFour():
    return np.array([[0, 0, 0, 1, 0, 0, 0, 0]])
def rock():
    return np.array([[0, 0, 0, 0, 1, 0, 0, 0]])
def paper():
    return np.array([[0, 0, 0, 0, 0, 1, 0, 0]])
def scissor():
    return np.array([[0, 0, 0, 0, 0, 0, 1, 0]])    
def none():
    return np.array([[0, 0, 0, 0, 0, 0, 0, 1]])

def labelSwitch(label):
    switch = {
        'Pinch1' : pinchOne,
        'Pinch2' : pinchTwo,
        'Pinch3' : pinchThree,
        'Pinch5' : pinchFour,
        'rock'   : rock,
        'paper'  : paper,
        'scissor': scissor,
        'none'   : none,
    }
    func = switch.get(label, lambda: np.array([[0, 0, 0, 0, 0, 0, 0, 0]]))
    return func()

def lstm(labels, data):
    minVal = 181
    masterData = np.zeros((1,minVal,8))
    masterLabel = np.zeros((1,minVal,8))
    print(masterData.shape)
    labelArray = np.zeros((1, 8))
    i = 1
    print(masterData) 
    max = 0
    min = 0
    smallTest = np.zeros((1,8))
    labelArray = np.append(labelArray, labelSwitch(labels[i-1]), axis=0)  #process the first label bc the loop does not take care of it
    smallTest = np.append(smallTest, [data[i-1]], axis=0)
    counter = 0
    while(i < len(labels)):
        if not(labels[i] == labels[i-1]):
            smallTest = np.delete(smallTest, 0, axis=0)
            labelArray = np.delete(labelArray, 0, axis=0)
            masterLabel = np.append(masterLabel, [labelArray[:minVal]], axis=0)
            masterData = np.append(masterData, [smallTest[:minVal]], axis=0)
            print(masterData.shape)
            print(masterLabel.shape)
            smallTest = np.zeros((1,8))
            labelArray = np.zeros((1,8))
        else:
            #counter += 1
            #print(counter)
            smallTest = np.append(smallTest, [data[i]], axis=0)
            labelArray = np.append(labelArray, labelSwitch(labels[i]), axis=0)
        i+=1
        
        
    #print(flattenedLabels.shape)
    masterLabel = np.delete(masterLabel, 0, axis=0)
    masterData = np.delete(masterData, 0, axis=0)
    np.save('./temp/tripled',masterData)
    np.save('./temp/tripled_label',masterLabel)
    print(max)
    print(min)
    print(masterData)
    print(masterLabel)
    #print(segments)
    #for
    
def plot_decision_boundary(X, y, model, steps=1000, cmap='bwr'):
        # The following allows you to adjust the plot size
        rcParams['figure.figsize'] = 8, 6  # 8 inches by 6 inches
        cmap = plt.get_cmap(cmap)

        # Define region of interest by data limits
        xmin, xmax = X[:,0].min() - 1, X[:,0].max() + 1
        ymin, ymax = X[:,1].min() - 1, X[:,1].max() + 1
        x_span = np.linspace(xmin, xmax, steps)
        y_span = np.linspace(ymin, ymax, steps)
        xx, yy = np.meshgrid(x_span, y_span)

        # Make predictions across region of interest
        labels = model.predict(np.c_[xx.ravel(), yy.ravel()])

        # Plot decision boundary in region of interest
        z = labels.reshape(xx.shape)

        fig, ax = plt.subplots()
        ax.contourf(xx, yy, z, cmap=cmap, alpha=0.5)

        # Get predicted labels on training data and plot
        train_labels = model.predict(X)
        ax.scatter(X[:,0], X[:,1], c=y, cmap=cmap, lw=0)

        return fig, ax 