import matplotlib.pyplot as plt
import os

def plot_performance(cum_strategy, cum_benchmark):
    fig, ax = plt.subplots(figsize = (10, 6))
    
    ax.plot(cum_strategy, label = 'Strategy', linewidth = 1.8)
    ax.plot(cum_benchmark, label = 'Benchmark', linewidth = 1.8)

    ax.set_title('Strategy vs Benchmark Cumulative Performance', fontsize = 14)
    ax.set_xlabel('Date', fontsize = 12)
    ax.set_ylabel('Cumulative Return', fontsize = 12)
    
    ax.legend(fontsize = 10)
    ax.grid(True, alpha = 0.3)
    
    plt.tight_layout()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plt.savefig(os.path.join(script_dir, 'performance.png'))
    plt.show()