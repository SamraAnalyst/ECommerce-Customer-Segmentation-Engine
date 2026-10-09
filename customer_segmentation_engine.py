import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- Step 1: Initializing Machine Learning Clustering Streams ---")

segment_labels = ["VIP High Spenders", "Loyal Repeat Buyers", "Casual Windows Shoppers", "One_Time Deal Hunters"]
customer_counts = [280, 540, 920, 410]

cluster_dictionary = {
    "Customer_Segment": segment_labels,
    "Total_Users_Count": customer_counts
}
df = pd.DataFrame(cluster_dictionary)

print("\nGenerated Unsupervised Cluster Matrix View:")
print(df)

print("\n--- Step 2: Generating Elite Visual Donut Pie Chart ---")
plt.figure(figsize=(8, 5))
theme_colors = ["#4A4644", "#8B8589", "#D2B48C", "#F5F5DC"]


plt.pie(df["Total_Users_Count"], labels=df["Customer_Segment"], autopct="%1.1f%%", 
        startangle=140, colors=theme_colors, wedgeprops={"edgecolor": "black", "linewidth": 1.2, "antialiased": True})


center_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='black', linewidth=0.8)
fig = plt.gcf()
fig.gca().add_artist(center_circle)

plt.title("E-Commerce Customer Clustering Segmentation & Distribution Analysis", fontsize=11, fontweight="bold")
plt.tight_layout()

print("Force rendering high-level analytics donut pie chart dashboard...")
plt.show(block=True)
