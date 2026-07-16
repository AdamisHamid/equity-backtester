import matplotlib.pyplot as plt
import os
 
 
def plot_performance(cum_benchmark, cum_strategy = None, cum_wf = None, strategy_label = 'Strategy', title = 'Strategy vs Benchmark Cumulative Performance', filename = 'performance.png'):
    fig, ax = plt.subplots(figsize = (10, 6))
 
    ax.plot(cum_benchmark, label = 'Benchmark', linewidth = 1.8)
 
    if cum_strategy is not None:
        ax.plot(cum_strategy, label = strategy_label, linewidth = 1.8)
 
    if cum_wf is not None:
        ax.plot(cum_wf, label = 'Walk-Forward', linewidth = 1.8)
 
    ax.set_title(title, fontsize = 14)
    ax.set_xlabel('Date', fontsize = 12)
    ax.set_ylabel('Cumulative Return', fontsize = 12)
 
    ax.legend(fontsize = 10)
    ax.grid(True, alpha = 0.3)
 
    plt.tight_layout()
 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plt.savefig(os.path.join(script_dir, filename))
    plt.show()
 