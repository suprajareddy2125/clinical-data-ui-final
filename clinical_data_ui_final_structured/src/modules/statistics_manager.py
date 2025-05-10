import pandas as pd
import matplotlib.pyplot as plt

class StatisticsManager:
    def generate_key_statistics(self):
        data = pd.read_csv('data/Patient_data.csv')
        visit_counts = data['Visit_time'].value_counts().sort_index()
        plt.figure(figsize=(10, 6))
        visit_counts.plot(kind='bar', color='skyblue')
        plt.title('Visits per date')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('statistics.png')
        return 'statistics.png'
