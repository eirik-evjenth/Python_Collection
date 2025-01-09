import matplotlib.pyplot as plt

# Data for the graph
reasons = ['Automate Boring Stuff', 'Solve Problems', 'Get a Job', 'Impress Friends', 'Fun']
importance = [8, 9, 10, 7, 10]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(reasons, importance, color=['blue', 'green', 'red', 'purple', 'orange'])

# Add titles and labels
plt.title('Why You Should Learn Basic Programming')
plt.xlabel('Reasons')
plt.ylabel('Importance (1-10)')

# Add text annotations
for i, value in enumerate(importance):
    plt.text(i, value + 0.2, str(value), ha='center')

# Show the graph
plt.show()