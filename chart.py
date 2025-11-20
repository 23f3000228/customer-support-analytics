
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
from google.colab import files

print("📊 Customer Support Response Time Analysis")
print("=" * 50)

# Set professional styling
sns.set_style("whitegrid")
sns.set_context("talk")
plt.rcParams['font.family'] = 'DejaVu Sans'

# Generate realistic synthetic data for customer support channels
np.random.seed(42)
data = []
n_observations = 500

# Email Support
email_times = np.random.gamma(2.5, 2.0, n_observations) * 120
data.extend([{'Channel': 'Email', 'Response_Time_Minutes': time} for time in email_times])

# Live Chat
chat_times = np.random.exponential(0.8, n_observations) * 60
data.extend([{'Channel': 'Live Chat', 'Response_Time_Minutes': time} for time in chat_times])

# Phone Support
phone_times = np.random.normal(8, 3, n_observations)
phone_times = np.abs(phone_times)
data.extend([{'Channel': 'Phone', 'Response_Time_Minutes': time} for time in phone_times])

# Social Media
social_times = np.random.lognormal(2.5, 0.8, n_observations)
data.extend([{'Channel': 'Social Media', 'Response_Time_Minutes': time} for time in social_times])

# Create DataFrame
df = pd.DataFrame(data)

print("📈 Dataset Overview:")
print(f"Total observations: {len(df)}")

# METHOD 1: Direct control with exact dimensions
print("\n🎨 Generating professional violin plot...")

# Create figure with NO padding or margins
fig = plt.figure(figsize=(5.12, 5.12), dpi=100, facecolor='white')
ax = fig.add_subplot(111)

# Create violin plot
sns.violinplot(
    data=df,
    x='Channel',
    y='Response_Time_Minutes',
    palette='viridis',
    saturation=0.8,
    inner='quartile',
    linewidth=1.5,
    ax=ax
)

# Customize with smaller fonts for exact fit
ax.set_title('Customer Support Response Time Distribution\nby Support Channel', 
             fontsize=11, fontweight='bold', pad=15)
ax.set_xlabel('Support Channel', fontsize=10, fontweight='bold', labelpad=10)
ax.set_ylabel('Response Time (Minutes)', fontsize=10, fontweight='bold', labelpad=10)

# Rotate labels
plt.xticks(rotation=45, ha='right')

# Remove all extra space
plt.tight_layout(pad=0.5)

# Save with EXACT dimensions - NO extra space
plt.savefig('chart.png', 
            dpi=100, 
            bbox_inches='tight',
            pad_inches=0.02,
            facecolor='white',
            edgecolor='none')

plt.close()

# METHOD 2: Verify and resize if needed
img = Image.open('chart.png')
print(f"Initial size: {img.size}")

# If not exactly 512x512, resize it
if img.size != (512, 512):
    print("Resizing to exact 512x512 pixels...")
    img_resized = img.resize((512, 512), Image.Resampling.LANCZOS)
    img_resized.save('chart.png', 'PNG')
    print(f"Final size: {img_resized.size}")
else:
    print("✅ Perfect 512x512 size!")

# Download the file to your computer
files.download('chart.png')
