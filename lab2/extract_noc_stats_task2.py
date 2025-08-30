import os
import re
import pandas as pd

traffics = ["uniform_random", "shuffle", "transpose", "tornado", "neighbor"]
vcs_per_channel = [2, 4, 8]
router_latency = [1, 2, 5]
link_width = [32, 64, 256]
rows = []

for traffic in traffics:
    # for vcs in vcs_per_channel:
        # router = 1
        # width = 256
    # for router in router_latency:
    #     vcs = 4
    #     width = 256
    for width in link_width:
        vcs = 4
        router = 1
        # stat_path = f"../lab2_results_2/{traffic}_{vcs}_{router}_{width}/network_stats_rate0.01.txt"
        # if not os.path.exists(stat_path):
        #     continue
        # with open(stat_path) as f:
        #     stats = f.read()
        # latency = re.search(r"average_packet_latency\s*=\s*([\d\.Ee+-]+)", stats)
        # throughput = re.search(r"reception_rate\s*=\s*([\d\.Ee+-]+)", stats)
        # rows.append({
        #     "traffic": traffic,
        #     "vcs": vcs,
        #     # "router": router,
        #     # "width": width,
        #     "latency": float(latency.group(1)) if latency else None,
        #     "throughput": float(throughput.group(1)) if throughput else None
        # })
        stat_path_2 = f"../lab2_results_2/{traffic}_{vcs}_{router}_{width}/network_stats.txt"
        if not os.path.exists(stat_path_2):
            continue
        with open(stat_path_2) as f:
            stats2 = f.read()
        latency = re.search(r"average_packet_latency\s*=\s*([\d\.Ee+-]+)", stats2)
        throughput = re.search(r"reception_rate\s*=\s*([\d\.Ee+-]+)", stats2)
        rows.append({
            "traffic": traffic,
            # "vcs": vcs,
            # "router": router,
            "width": width,
            "latency": float(latency.group(1)) if latency else None,
            "throughput": float(throughput.group(1)) if throughput else None
        })
        # stat_path_3 = f"../lab2_results_2/{traffic}_{vcs}_{router}_{width}/network_stats_rate0.5.txt"
        # if not os.path.exists(stat_path_3):
        #     continue
        # with open(stat_path_3) as f:
        #     stats3 = f.read()
        # latency = re.search(r"average_packet_latency\s*=\s*([\d\.Ee+-]+)", stats3)
        # throughput = re.search(r"reception_rate\s*=\s*([\d\.Ee+-]+)", stats3)
        # rows.append({
        #     "traffic": traffic,
        #     "vcs": vcs,
        #     # "router": router,
        #     # "width": width,
        #     "latency": float(latency.group(1)) if latency else None,
        #     "throughput": float(throughput.group(1)) if throughput else None
        # })

df = pd.DataFrame(rows)
df.to_csv("../noc_results_2.csv", index=False)