#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.7.13.4
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self, address0='serial=3136C69', address1='serial=3136C6D', freq=2.45e9, freq_offset=0, samp_rate=500e3):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Parameters
        ##################################################
        self.address0 = address0
        self.address1 = address1
        self.freq = freq
        self.freq_offset = freq_offset
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.tun_tx_gain = tun_tx_gain = 0
        self.tun_rx_gain = tun_rx_gain = 62.6
        self.tun_freq = tun_freq = 2.45e9
        self.tone_ampl = tone_ampl = 1
        self.tone2 = tone2 = samp_rate/4
        self.tone1 = tone1 = samp_rate/4

        ##################################################
        # Blocks
        ##################################################
        _tun_rx_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tun_rx_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tun_rx_gain_sizer,
        	value=self.tun_rx_gain,
        	callback=self.set_tun_rx_gain,
        	label='UHD Rx Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tun_rx_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tun_rx_gain_sizer,
        	value=self.tun_rx_gain,
        	callback=self.set_tun_rx_gain,
        	minimum=0,
        	maximum=70,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tun_rx_gain_sizer, 3, 4, 1, 4)
        _tun_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tun_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tun_freq_sizer,
        	value=self.tun_freq,
        	callback=self.set_tun_freq,
        	label='UHD Freq (Hz)',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tun_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tun_freq_sizer,
        	value=self.tun_freq,
        	callback=self.set_tun_freq,
        	minimum=2.4e9,
        	maximum=2.5e9,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tun_freq_sizer, 2, 0, 1, 8)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Receiving',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.GridAdd(self.wxgui_scopesink2_0.win, 4, 4, 4, 4)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(('address2', "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(tun_freq, 0)
        self.uhd_usrp_source_0_0.set_gain(tun_rx_gain, 0)
        self.uhd_usrp_source_0_0.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_0_0.set_auto_iq_balance(True, 0)
        _tun_tx_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tun_tx_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tun_tx_gain_sizer,
        	value=self.tun_tx_gain,
        	callback=self.set_tun_tx_gain,
        	label='UHD Tx Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tun_tx_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tun_tx_gain_sizer,
        	value=self.tun_tx_gain,
        	callback=self.set_tun_tx_gain,
        	minimum=0,
        	maximum=35,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tun_tx_gain_sizer, 3, 0, 1, 4)
        _tone_ampl_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tone_ampl_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tone_ampl_sizer,
        	value=self.tone_ampl,
        	callback=self.set_tone_ampl,
        	label='Tone Amplitude',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tone_ampl_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tone_ampl_sizer,
        	value=self.tone_ampl,
        	callback=self.set_tone_ampl,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tone_ampl_sizer, 1, 0, 1, 8)
        _tone2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tone2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tone2_sizer,
        	value=self.tone2,
        	callback=self.set_tone2,
        	label='Tone 2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tone2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tone2_sizer,
        	value=self.tone2,
        	callback=self.set_tone2,
        	minimum=-samp_rate/2,
        	maximum=samp_rate/2,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tone2_sizer, 0, 4, 1, 4)
        _tone1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tone1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tone1_sizer,
        	value=self.tone1,
        	callback=self.set_tone1,
        	label='Tone 1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tone1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tone1_sizer,
        	value=self.tone1,
        	callback=self.set_tone1,
        	minimum=-samp_rate/2,
        	maximum=samp_rate/2,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_tone1_sizer, 0, 0, 1, 4)
        self.digital_gmsk_demod_0 = digital.gmsk_demod(
        	samples_per_symbol=4,
        	gain_mu=0.175,
        	mu=0.5,
        	omega_relative_limit=0.005,
        	freq_error=0.0,
        	verbose=False,
        	log=False,
        )
        self.blks2_packet_decoder_0 = grc_blks2.packet_demod_f(grc_blks2.packet_decoder(
        		access_code='',
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0.recv_pkt(ok, payload),
        	),
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.digital_gmsk_demod_0, 0), (self.blks2_packet_decoder_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.digital_gmsk_demod_0, 0))

    def get_address0(self):
        return self.address0

    def set_address0(self, address0):
        self.address0 = address0

    def get_address1(self):
        return self.address1

    def set_address1(self, address1):
        self.address1 = address1

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.set_tone2(self.samp_rate/4)
        self.set_tone1(self.samp_rate/4)

    def get_tun_tx_gain(self):
        return self.tun_tx_gain

    def set_tun_tx_gain(self, tun_tx_gain):
        self.tun_tx_gain = tun_tx_gain
        self._tun_tx_gain_slider.set_value(self.tun_tx_gain)
        self._tun_tx_gain_text_box.set_value(self.tun_tx_gain)

    def get_tun_rx_gain(self):
        return self.tun_rx_gain

    def set_tun_rx_gain(self, tun_rx_gain):
        self.tun_rx_gain = tun_rx_gain
        self._tun_rx_gain_slider.set_value(self.tun_rx_gain)
        self._tun_rx_gain_text_box.set_value(self.tun_rx_gain)
        self.uhd_usrp_source_0_0.set_gain(self.tun_rx_gain, 0)


    def get_tun_freq(self):
        return self.tun_freq

    def set_tun_freq(self, tun_freq):
        self.tun_freq = tun_freq
        self._tun_freq_slider.set_value(self.tun_freq)
        self._tun_freq_text_box.set_value(self.tun_freq)
        self.uhd_usrp_source_0_0.set_center_freq(self.tun_freq, 0)

    def get_tone_ampl(self):
        return self.tone_ampl

    def set_tone_ampl(self, tone_ampl):
        self.tone_ampl = tone_ampl
        self._tone_ampl_slider.set_value(self.tone_ampl)
        self._tone_ampl_text_box.set_value(self.tone_ampl)

    def get_tone2(self):
        return self.tone2

    def set_tone2(self, tone2):
        self.tone2 = tone2
        self._tone2_slider.set_value(self.tone2)
        self._tone2_text_box.set_value(self.tone2)

    def get_tone1(self):
        return self.tone1

    def set_tone1(self, tone1):
        self.tone1 = tone1
        self._tone1_slider.set_value(self.tone1)
        self._tone1_text_box.set_value(self.tone1)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--address0", dest="address0", type="string", default='serial=3136C69',
        help="Set IP Address, Dev 0 [default=%default]")
    parser.add_option(
        "", "--address1", dest="address1", type="string", default='serial=3136C6D',
        help="Set IP Address, Dev 1 [default=%default]")
    parser.add_option(
        "-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(2.45e9),
        help="Set Default Frequency [default=%default]")
    parser.add_option(
        "-o", "--freq-offset", dest="freq_offset", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Rx Frequency Offset [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(500e3),
        help="Set Sample Rate [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(address0=options.address0, address1=options.address1, freq=options.freq, freq_offset=options.freq_offset, samp_rate=options.samp_rate)
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()