import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Data
control_group_size = 1000
control_group_conversions = 200
treatment_group_size = 1000
treatment_group_conversions = 250

# Conversion rates
conversion_rate_A = control_group_conversions / control_group_size
conversion_rate_B = treatment_group_conversions / treatment_group_size

# Proportion of success for both groups
p_A = conversion_rate_A
p_B = conversion_rate_B

# Combined proportion for pooled standard error
p_combined = (control_group_conversions + treatment_group_conversions) / (control_group_size + treatment_group_size)

# Standard error
standard_error = np.sqrt(p_combined * (1 - p_combined) * (1 / control_group_size + 1 / treatment_group_size))

# Z-score calculation
z_score = (p_B - p_A) / standard_error

# p-value
p_value = stats.norm.sf(abs(z_score)) * 2  # two-tailed test

# Print results
print(f"Conversion rate (Control Group A): {conversion_rate_A:.2%}")
print(f"Conversion rate (Treatment Group B): {conversion_rate_B:.2%}")
print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.4f}")

# Determine if we can reject the null hypothesis
alpha = 0.05  # significance level
if p_value < alpha:
    print("\nConclusion: We reject the null hypothesis. The change is statistically significant.")
else:
    print("\nConclusion: We fail to reject the null hypothesis. The change is not statistically significant.")

# Visualizing conversion rates
groups = ['Control Group (A)', 'Treatment Group (B)']
conversion_rates = [conversion_rate_A, conversion_rate_B]

plt.bar(groups, conversion_rates, color=['blue', 'green'])
plt.ylabel('Conversion Rate')
plt.title('A/B Test Conversion Rate Comparison')
plt.ylim([0, max(conversion_rates) * 1.2])
plt.show()
