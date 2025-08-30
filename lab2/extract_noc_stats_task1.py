import os
import re
import pandas as pd

traffics = ["uniform_random", "shuffle", "transpose", "tornado", "neighbor"]
rates = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5]
rows = []

for traffic in traffics:
    for rate in rates:
        stat_path = f"../lab2_results/{traffic}_{rate}/network_stats.txt"
        if not os.path.exists(stat_path):
            continue
        with open(stat_path) as f:
            stats = f.read()
        latency = re.search(r"average_packet_latency\s*=\s*([\d\.Ee+-]+)", stats)
        throughput = re.search(r"reception_rate\s*=\s*([\d\.Ee+-]+)", stats)
        hop = re.search(r"average_hops\s*=\s*([\d\.Ee+-]+)", stats)
        rows.append({
            "traffic": traffic,
            "rate": rate,
            "latency": float(latency.group(1)) if latency else None,
            "throughput": float(throughput.group(1)) if throughput else None,
            "hop": float(hop.group(1)) if hop else None
        })

df = pd.DataFrame(rows)
df.to_csv("../noc_results.csv", index=False)