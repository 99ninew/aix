#!/bin/bash
TRAFFICS=("uniform_random" "shuffle" "transpose" "tornado" "neighbor")
RATES=(0.01 0.05 0.1 0.2 0.3 0.4 0.45 0.5)
for traffic in "${TRAFFICS[@]}"; do
  for rate in "${RATES[@]}"; do
    outdir="../lab2_results/${traffic}_${rate}"
    mkdir -p $outdir
    ../build/NULL/gem5.opt \
    ../configs/example/garnet_synth_traffic.py \
    --network=garnet --num-cpus=64 --num-dirs=64 \
    --topology=Mesh_XY --mesh-rows=8 \
    --inj-vnet=0 --synthetic=$traffic \
    --sim-cycles=10000 --injectionrate=$rate 
    echo > $outdir/network_stats.txt 
    grep "average_packet_latency" m5out/stats.txt | sed 's/system.ruby.network.average_packet_latency\s*/average_packet_latency = /' >> $outdir/network_stats.txt
    grep "reception_rate" m5out/stats.txt | sed 's/system.ruby.network.reception_rate\s*/reception_rate = /' >> $outdir/network_stats.txt
    grep "average_hops" m5out/stats.txt | sed 's/system.ruby.network.average_hops\s*/average_hops = /' >> $outdir/network_stats.txt
  done
done