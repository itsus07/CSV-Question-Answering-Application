import matplotlib.pyplot as plt
import seaborn as sns

def plot_graph(df, x_col, y_col, graph_type):
    plt.figure(figsize=(8, 5)) 
    
    if graph_type == "Line":
        sns.lineplot(x=df[x_col], y=df[y_col])
    elif graph_type == "Bar":
        sns.barplot(x=df[x_col], y=df[y_col])
    elif graph_type == "Scatter":
        sns.scatterplot(x=df[x_col], y=df[y_col])
        
    plt.title(f"{graph_type} Plot: {x_col} vs {y_col}")
    return plt.gcf()  
