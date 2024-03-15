import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Make sure to change the [file_path] with your actual path.
df = pd.read_csv('[file_path]\\1_top_paying_roles.csv')

top_skills = df['job_title']
avg_salaries = df['salary_year_avg']

sns.set(style="darkgrid")
plt.style.use("dark_background")
plt.rcParams.update({"grid.linewidth":0.5, "grid.alpha":0.5})

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_salaries, y=top_skills, palette='Blues_r', edgecolor='none')
plt.xticks(rotation=45)  
plt.xlabel('Average Yearly Salary ($)')
plt.ylabel('')
plt.title('Average Salary Distribution For Top 10 Paying Data Analyst Jobs In 2023')
plt.tight_layout()
plt.show()
