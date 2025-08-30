#!/bin/bash
TRAFFICS=("uniform_random" "shuffle" "transpose" "tornado" "neighbor")
VCS_PER_CHANNEL=(2 4 8)
ROUTER=(1 2 5)
LINK_WIDTH=(32 64 256)
for traffic in "${TRAFFICS[@]}"; do
  for vcs in "${VCS_PER_CHANNEL[@]}"; do
    for router in "${ROUTER[@]}"; do
      for link_width in "${LINK_WIDTH[@]}"; do
        outdir="../lab2_results_2/${traffic}_${vcs}_${router}_${link_width}"
        mkdir -p $outdir
        ../build/NULL/gem5.opt \
        ../configs/example/garnet_synth_traffic.py \
        --network=garnet --num-cpus=64 --num-dirs=64 \
        --topology=Mesh_XY --mesh-rows=8 \
        --inj-vnet=0 --synthetic=$traffic \
        --sim-cycles=10000 --injectionrate=0.1 \
        --vcs-per-vnet=$vcs --router-latency=$router --link-width-bits=$link_width
        echo > $outdir/network_stats.txt
        grep "average_packet_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_latency\s*/average_packet_latency = /' >> $outdir/network_stats.txt
        grep "reception_rate" m5out/stats.txt | sed 's/system.ruby.network.reception_rate\s*/reception_rate = /' >> $outdir/network_stats.txt
        grep "average_hops" m5out/stats.txt | sed 's/system.ruby.network.average_hops\s*/average_hops = /' >> $outdir/network_stats.txt
      done
    done
  done
done
