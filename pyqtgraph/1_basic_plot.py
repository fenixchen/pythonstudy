import numpy as np

import pyqtgraph as pg

data = np.random.normal(size=1000)
pg.plot(data, title="Simplest possible plotting example")

if __name__ == "__main__":
    pg.exec()
