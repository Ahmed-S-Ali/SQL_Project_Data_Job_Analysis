import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Make sure to change the [file_path] with your actual path.
df = pd.read_csv('[file_path]\\assets\\2_top_paying_skills.csv')

skill_counts = df['skills'].value_counts().head(10)

sns.set(style="darkgrid")
plt.style.use("dark_background")
plt.rcParams.update({"grid.linewidth":0.5, "grid.alpha":0.5})

plt.figure(figsize=(10, 6))
sns.barplot(x=skill_counts.values, y=skill_counts.index, palette='Blues_r', edgecolor='none')
plt.xticks(rotation=45)  
plt.xlabel('Frequency')
plt.ylabel('')
plt.title('Skill Count For Top 10 Paying Data Analyst Jobs In 2023')
plt.tight_layout()
plt.show()
