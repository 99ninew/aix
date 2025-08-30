import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../noc_results_2.csv")
for traffic in df['traffic'].unique():
    sub = df[df['traffic'] == traffic]
    plt.plot(sub['throughput'], sub['latency'], marker='o', label=traffic)
    for i, row in sub.iterrows():
        plt.text(row['throughput'], row['latency'], f"width={row['width']:.2f}", fontsize=8, ha='right')
plt.xlabel('Throughput-reception rate (packets/node/cycle)')
plt.ylabel('average packet latency (Tick)')
plt.title('Latency-Throughput Curve (8x8 Mesh, 10000 cycles)')
plt.legend()
plt.grid(True)
plt.savefig('../noc_latency_throughput_width_rate0.1.png')
plt.show()