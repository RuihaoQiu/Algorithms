## Model and visulization

from sklearn.datasets.samples_generator import make_blobs, make_moons
import matplotlib.pyplot as plt
import numpy as np
import random
plt.style.use('ggplot')

def plot_class(clf):
    #X_train, y_train = make_blobs(n_samples=200, centers=2,
    #              random_state=2, cluster_std=2.50)
    X_train, y_train = make_moons(200, noise=0.20)
    
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_xlabel('feature 1', color='gray')
    ax.set_ylabel('feature 2', color='gray')
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, s=100, cmap='Paired', zorder=3)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()        
    x = np.linspace(xlim[0], xlim[1], 50)
    y = np.linspace(ylim[0], ylim[1], 50)
    yy, xx = np.meshgrid(y, x)
    X_test = np.vstack([xx.ravel(), yy.ravel()]).T

    clf.fit(X_train, y_train)
    zz = clf.predict(X_test)
    zz = zz.reshape(xx.shape)
    ax.contourf(xx, yy, zz, cmap='Paired', alpha=0.4, zorder=1)
    plt.show()


def plot_regressor(reg):
    y = np.array([[i**2 + random.uniform(0, 1)*20**2 for i in range(50)]]).T
    X = np.array([[i for i in range(50)]]).T
    X_test = np.array([[i for i in range(50)]]).T

    reg.fit(X, y)
    y_pred = reg.predict(X_test)

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_xlabel('feature 1', color='gray')
    ax.plot(X, y, 'o', markersize=8, label="y_train")
    ax.plot(X, y_pred, lw=3, label="y_pred")
    ax.legend()
    plt.show()
