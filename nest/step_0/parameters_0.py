# -*- coding: utf-8 -*-

'''
It contains:

    Cortex                           = 100 neurons, iaf_psc_exp glutamatergic
    Striatum                         =  10 neurons, iaf_psc_exp GABAergic
    GPe: globus pallidus external    =  10 neurons, iaf_psc_exp GABAergic
    GPi: globus pallidus internal    =  10 neurons, iaf_psc_exp GABAergic
    STN: subthalamic nucleus         =  10 neurons, iaf_psc_exp glutamatergic
    SNr: substantia nigra reticulata =  10 neurons, iaf_psc_exp GABAergic
    SNc: substantia nigra compacta   =  10 neurons, iaf_psc_exp dopaminergic
    Thalamus                         =  10 neurons, iaf_psc_exp glutamatergic

Prefix description:
    MSN_ - Medium Spiny Neurons
    ex_  -  excitory
    inh_ - inhibitory
    STP_ - Short Term Plasticity
'''
# Configure logger
import logging
FORMAT = '%(name)s.%(levelname)s: %(message)s.'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

# general settings
#T = 1000.
T = 100.
dt = 10.
sd_folder_name = "spike_detector_data/"
sd_filename = "spikes-172-0.gdf"
#"spike_detector-cortex-0.gdf"
# dopamine modulation flag
vt_flag = True   #ToDo do that element more visible in code
# dopamine model key
dopa_model = "dopa"

# ========
# NEURONS
# ========

# neurons model without neuromodulation
cortex_neurons_model = striatum_neurons_model = gpe_neurons_model = gpi_neurons_model = stn_neurons_model = snr_neurons_model = thalamus_neurons_model = 'iaf_psc_exp'
# with dopamine
snc_neurons_model = 'iaf_psc_exp' # ToDo iaf_psc_alpha    understand the purpose of alpha for neuromodulation
# Count of neurons in every parts of BS
# table for neuron number: https://docs.google.com/spreadsheets/d/1cAm5uosBoKaaPyC1mvb527nYkVcW2YsAA2ECiCDASzg/edit?usp=sharing
NN_cortex = 150
NN_striatum = NN_gpe = NN_gpi = NN_stn = NN_snc = NN_thalamus = 10
NN_snr = 10

# for a time the neuron model parameters would be setted as STP inhibitory or excitory
# for a time the neuron model parameters would be setted as STP inhibitory or excitory
STP_neuronparams = {'E_L': -55., 'V_th': 30., 'V_reset': -75., 'C_m': 0.05, 't_ref': 2.,
                    'tau_m': 15.}
# ToDO define appropriate params


STP_ex_neuronparams = {'tau_syn_ex': 0.7}
STP_inh_neuronparams = {'tau_syn_inh': 1.13}
# for if_neurons
# dict([{'tau_ref_abs': 3., 'tau_ref_tot': 3.}] +
# dict([{'tau_ref_abs': 2., 'tau_ref_tot': 2.}] +
#'tau_m': 30.,
# 'tau_ex': 3.

# Excitory neurons
cortex_neuronparams = stn_neuronparams = thalamus_neuronparams = STP_neuronparams
# Inhibitory neurons
striatum_neuronparams = gpe_neuronparams = gpi_neuronparams = snr_neuronparams = STP_neuronparams
# Neuromodulation neurons
snc_neuronparams = STP_neuronparams

# =========
# SYNAPSES
# =========

# parameters of synapses
# Glutamate
w_ex = 1.5
# GABA
g = 0.3
w_inh = -w_ex * g

# Volume transmission
stdp_dopamine_synapse_weight = 65.

#--------------------------- ToDo what for?
g_w_ex = 40.
g_w_inh = -20.

K = 10000
f_ex = 0.8
K_ex = f_ex * K
K_inh = (1.0 - f_ex) * K

nu_ex = 10.0  # 2.
nu_inh = 10.0  # 2.
#--------------------------

vt_delay = 1.
delay_inh = 1.
delay_ex = 1.

'''
    ===========
 In SNr neurons according to recent experimental findings [http://www.biomedcentral.com/1471-2202/12/S1/P145#B2]
 has been found short term facilitation in MSN synapses onto SNr neurons from SNc.
'''


# ============
# CONNECTIONS
# ============
conn_dict = {'rule': 'all_to_all', 'multapses': True}
# synapses model are same for test facilitation
bs_synapse_model = 'stdp_synapse'
syn_excitory = "excitatory"
syn_inhibitory = "inhibitory"

'''
==========================|
Medium spiny neurons (MSN) is GABA inhibitory cell. They have dopamine receptors. Dopamine has a dual action on MSNs.
It inhibits the (D2-type) MSNs in the indirect pathway and
excites (D1-type) MSNs in the direct pathway.
Consequently, when dopamine is lost from the striatum, the indirect pathway becomes overactive
and the direct pathway becomes underactive.
'''

