import matplotlib.pyplot as plt

# Sample dataset based on World Bank total population estimate for India (2024)
# Total population: ~1.48 billion
# Assumed gender distribution: Male 51%, Female 49%
gender_labels = ['Male', 'Female']
gender_population = [1.48e9 * 0.51, 1.48e9 * 0.49]  # in absolute numbers

# Create the histogram-style bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(gender_labels, gender_population, color=['steelblue', 'lightcoral'], edgecolor='black')

# Add labels and title
plt.title("India's Gender Distribution (2024 Estimate)", fontsize=16)
plt.xlabel("Gender", fontsize=14)
plt.ylabel("Population Count", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate bars with population values
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1e7, f'{height/1e6:.2f}M', ha='center', va='bottom', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
