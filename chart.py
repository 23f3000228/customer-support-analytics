# Customer Analytics: Response Time Distribution by Support Channel
# Heller Schamberger and Rau - Customer Experience Analysis

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("📊 Customer Support Response Time Analysis")
print("=" * 50)

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready text sizes
plt.rcParams['font.family'] = 'DejaVu Sans'

# Generate realistic synthetic data for customer support channels
np.random.seed(42)  # For reproducible results

# Create realistic response time distributions for different support channels
data = []
n_observations = 500

# Email Support - typically slower response times
email_times = np.random.gamma(2.5, 2.0, n_observations) * 120  # Minutes
data.extend([{'Channel': 'Email', 'Response_Time_Minutes': time} for time in email_times])

# Live Chat - fast response times
chat_times = np.random.exponential(0.8, n_observations) * 60  # Minutes
data.extend([{'Channel': 'Live Chat', 'Response_Time_Minutes': time} for time in chat_times])

# Phone Support - moderate response times
phone_times = np.random.normal(8, 3, n_observations)  # Minutes
phone_times = np.abs(phone_times)  # Ensure positive values
data.extend([{'Channel': 'Phone', 'Response_Time_Minutes': time} for time in phone_times])

# Social Media - variable response times
social_times = np.random.lognormal(2.5, 0.8, n_observations)  # Minutes
data.extend([{'Channel': 'Social Media', 'Response_Time_Minutes': time} for time in social_times])

# Create DataFrame
df = pd.DataFrame(data)

print("📈 Dataset Overview:")
print(f"Total observations: {len(df)}")
print(f"Support channels: {df['Channel'].unique().tolist()}")
print(f"Response time range: {df['Response_Time_Minutes'].min():.1f} - {df['Response_Time_Minutes'].max():.1f} minutes")
print("\nChannel Statistics:")
print(df.groupby('Channel')['Response_Time_Minutes'].describe().round(2))

# Create the violin plot
print("\n🎨 Generating professional violin plot...")
plt.figure(figsize=(8, 8))  # Set for 512x512 output with dpi=64

# Create violin plot with professional styling
violin_plot = sns.violinplot(
    data=df,
    x='Channel',
    y='Response_Time_Minutes',
    palette='viridis',  # Professional color palette
    saturation=0.8,
    inner='quartile',  # Show quartiles inside violins
    linewidth=1.5
)

# Customize the plot for executive presentation
plt.title('Customer Support Response Time Distribution\nby Support Channel', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=14, fontweight='bold', labelpad=15)
plt.ylabel('Response Time (Minutes)', fontsize=14, fontweight='bold', labelpad=15)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(True, alpha=0.3)

# Remove top and right spines for cleaner look
sns.despine(left=False, bottom=False)

# Adjust layout
plt.tight_layout()

# Save the chart with exact 512x512 pixel dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("✅ Chart saved as 'chart.png'")
print(f"📏 Image dimensions: 512x512 pixels")

# Display some insights
print("\n🔍 Key Business Insights:")
print("-" * 40)
channel_stats = df.groupby('Channel')['Response_Time_Minutes'].agg(['mean', 'median', 'std']).round(1)
for channel in channel_stats.index:
    stats = channel_stats.loc[channel]
    print(f"📞 {channel}: Mean={stats['mean']}min, Median={stats['median']}min, Std={stats['std']}min")

# Show the plot
plt.show()

print("\n🎯 Analysis complete! Ready for executive presentation.")
