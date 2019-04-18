#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Transceiver
# GNU Radio version: 3.7.13.4
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import limesdr
import time

class transceiver(gr.top_block):

    def __init__(self, freq=2.42e9):
        gr.top_block.__init__(self, "Transceiver")

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000
        
        #Queues
        self.sink_queue = gr.msg_queue()
        self.source_queue = gr.msg_queue()

        ##################################################
        # Blocks
        ##################################################
        self.limesdr_source_0 = limesdr.source('', 0, '')
        self.limesdr_source_0.set_sample_rate(samp_rate)
        self.limesdr_source_0.set_center_freq(freq, 0)
        self.limesdr_source_0.set_bandwidth(5e6,0)
        self.limesdr_source_0.set_gain(30,0)
        self.limesdr_source_0.set_antenna(255,0)
        self.limesdr_source_0.calibrate(5e6, 0)

        self.limesdr_sink_0 = limesdr.sink('', 0, '', '')
        self.limesdr_sink_0.set_sample_rate(samp_rate)
        self.limesdr_sink_0.set_center_freq(freq, 0)
        self.limesdr_sink_0.set_bandwidth(5e6,0)
        self.limesdr_sink_0.set_gain(30,0)
        self.limesdr_sink_0.set_antenna(255,0)
        self.limesdr_sink_0.calibrate(5e6, 0)

        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=2,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blocks_probe_signal_x_0 = blocks.probe_signal_f()
        self.blocks_message_source_0 = blocks.message_source(gr.sizeof_char,self.source_queue)
        self.blocks_message_sink_0 = blocks.message_sink(gr.sizeof_char*1, self.sink_queue, False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=1,
        		preamble='',
        		access_code='',
        		pad_for_usrp=True,
        	),
        	payload_length=0,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )
        self.analog_probe_avg_mag_sqrd_x_0 = analog.probe_avg_mag_sqrd_c(0, 1e-3)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.blocks_message_sink_0, 0))
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_probe_signal_x_0, 0))
        self.connect((self.blocks_message_source_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.limesdr_sink_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.analog_probe_avg_mag_sqrd_x_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.limesdr_source_0, 0), (self.digital_gmsk_demod_0, 0))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.limesdr_source_0.set_center_freq(self.freq, 0)
        self.limesdr_sink_0.set_center_freq(self.freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def send_pkt(self, payload):
        self.source_queue.insert_tail(gr.message_from_string(payload))

    def recv_pkt(self):
        pkt = ""

        if self.sink_queue.count():
            pkt = self.sink_queue.delete_head().to_string()

        return pkt


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=transceiver, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = transceiver()
    tb.start()
    print 'i hope this works'
    print 'sink queue count:', tb.sink_queue.count()
    print 'inserting:', 'a'
    #tb.source_queue.insert_tail(gr.message_from_string('a'))
    time.sleep(1)

    #print 'sink queue count:', tb.sink_queue.count()

    #print 'received:', tb.sink_queue.delete_head().to_string()

    print 'operating with fuctions supplied by the top block'
    print 'sending:', 'a'*512
    tb.send_pkt('a'*512)
    time.sleep(1)

    print 'received:', tb.recv_pkt()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
