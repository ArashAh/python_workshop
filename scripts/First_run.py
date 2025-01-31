import numpy as np
import matplotlib.pyplot as plt
random_numbers = np.random.rand(100)
mean_value = np.mean(random_numbers)
print("Random numbers:", random_numbers)
print("Mean value:", mean_value)

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(random_numbers, marker='o', linestyle='-', color='b', label='Random Numbers')
plt.axhline(y=mean_value, color='r', linestyle='--', label=f'Mean Value: {mean_value:.2f}')
plt.title('Plot of 100 Random Numbers')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()