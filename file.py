import pandas as pd
import matplotlib.pyplot as plt

# Load your Excel file
xlsx = pd.ExcelFile("/home/thrymr/Downloads/LinkedIn_Performance_Report.xlsx")


# Parse the sheets
content_df = xlsx.parse("Content Analysis")
visitor_df = xlsx.parse("Visitor Analysis")
follower_df = xlsx.parse("Follower Analysis")

# Convert 'Date' columns to datetime
content_df['Date'] = pd.to_datetime(content_df['Date'])
visitor_df['Date'] = pd.to_datetime(visitor_df['Date'])
follower_df['Date'] = pd.to_datetime(follower_df['Date'])

# Plot key metrics to visualize spikes
fig, axs = plt.subplots(3, 1, figsize=(14, 12), sharex=True)

# Content engagement (Total Clicks)
axs[0].plot(content_df['Date'], content_df['Clicks (total)'], marker='o', label='Total Clicks')
axs[0].set_title('Content Clicks Over Time')
axs[0].set_ylabel('Clicks')
axs[0].legend()
axs[0].grid(True)

# Visitor activity (Total Page Views)
axs[1].plot(visitor_df['Date'], visitor_df['Total page views (total)'], marker='o', color='orange', label='Total Page Views')
axs[1].set_title('Visitor Page Views Over Time')
axs[1].set_ylabel('Page Views')
axs[1].legend()
axs[1].grid(True)

# Follower growth
axs[2].plot(follower_df['Date'], follower_df['Total followers'], marker='o', color='green', label='Total Followers')
axs[2].set_title('Follower Growth Over Time')
axs[2].set_ylabel('Followers')
axs[2].legend()
axs[2].grid(True)

plt.xlabel('Date')
plt.tight_layout()
plt.show()
