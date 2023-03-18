from nfstream import NFStreamer
my_streamer = NFStreamer(source="facebook.pcap",
                         # We disable l7 dissection for readability purpose.
                         n_dissections=0,
                         splt_analysis=10)
for flow in my_streamer:
    print(flow)