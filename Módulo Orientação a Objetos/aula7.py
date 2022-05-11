import matplotlib.pyplot as plt
import numpy as np

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.bar(meses, vendas,)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, len(meses), 0, max(vendas)+500])

plt.subplot(1, 3, 3)
plt.scatter(meses, vendas)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, len(meses), 0, max(vendas)+500])

plt.show()
