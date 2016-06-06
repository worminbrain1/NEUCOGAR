from func import *

logger = logging.getLogger('neuromodulation')
startbuild = datetime.datetime.now()


# Connect the volume transmitter to the parts
vt_dopa_ex = nest.Create('volume_transmitter')
vt_dopa_in = nest.Create('volume_transmitter')
vt_sero_ex = nest.Create('volume_transmitter')
vt_sero_in = nest.Create('volume_transmitter')
DOPA_synparams_ex['vt'] = vt_dopa_ex[0]
DOPA_synparams_in['vt'] = vt_dopa_in[0]
SERO_synparams_ex['vt'] = vt_sero_ex[0]
SERO_synparams_in['vt'] = vt_sero_in[0]


nest.CopyModel('stdp_dopamine_synapse', dopa_model_ex, DOPA_synparams_ex)
nest.CopyModel('stdp_dopamine_synapse', dopa_model_in, DOPA_synparams_in)
nest.CopyModel('stdp_serotonine_synapse', sero_model_in, SERO_synparams_in)
nest.CopyModel('stdp_serotonine_synapse', sero_model_ex, SERO_synparams_ex)

nest.Connect(LC[LC_NA[0]][k_IDs], vt_dopa_ex)
nest.Connect(LC[LC_D1][k_IDs], vt_dopa_ex)
nest.Connect(LC[LC_D2][k_IDs], vt_dopa_ex)
nest.Connect(LC[LC_NA[1]][k_IDs], vt_dopa_ex)
nest.Connect(PGI[PGI_Glu][k_IDs], vt_dopa_ex)
nest.Connect(Amy[Amy_Glu][k_IDs], vt_dopa_ex)
nest.Connect(RN[RN_5-HT][k_IDs], vt_dopa_ex)
nest.Connect(RN[RN_a1][k_IDs], vt_dopa_ex)
nest.Connect(RN[RN_a2][k_IDs], vt_dopa_ex)
nest.Connect(Prefrontalcortex[Prefrontalcortex_Glu[1]][k_IDs], vt_dopa_ex)
nest.Connect(Prefrontalcortex[Prefrontalcortex_Glu[0]][k_IDs], vt_dopa_ex)
nest.Connect(VTA[VTA_DA[0]][k_IDs], vt_dopa_ex)
nest.Connect(VTA[VTA_a1][k_IDs], vt_dopa_ex)
nest.Connect(VTA[VTA_DA[1]][k_IDs], vt_dopa_ex)
nest.Connect(Motorcortex[Motorcortex_Glu][k_IDs], vt_dopa_ex)


connect(LC[LC_NA[0]], Prefrontalcortex[Prefrontalcortex_Glu[1]], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_NA[0]], Prefrontalcortex[Prefrontalcortex_Glu[0]], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_NA[0]], Motorcortex[Motorcortex_Glu], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_NA[0]], VTA[VTA_a1], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_NA[0]], LTD[LTD_a1], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_NA[0]], LTD[LTD_a2], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_Ach], LC[LC_NA[0]], syn_type=Ach, weight_coef=1.000000000)
connect(LC[LC_Ach], LC[LC_GABA], syn_type=Ach, weight_coef=1.000000000)
connect(LC[LC_Ach], LC[LC_NA[1]], syn_type=Ach, weight_coef=1.000000000)
connect(LC[LC_GABA], LC[LC_NA[0]], syn_type=GABA, weight_coef=1.000000000)
connect(LC[LC_D1], LC[LC_NA[0]], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_D2], LC[LC_NA[1]], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_NA[1]], RN[RN_a2], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_NA[1]], RN[RN_a1], syn_type=DA_ex, weight_coef=1.000000000)
connect(LC[LC_NA[1]], AcbShell[AcbShell_GABA[1]], syn_type=DA_ex, weight_coef=1.000000000)
connect(PGI[PGI_GABA], LC[LC_GABA], syn_type=GABA, weight_coef=1.000000000)
connect(PGI[PGI_Glu], LC[LC_NA[0]], syn_type=DA_ex, weight_coef=1.000000000)
connect(PGI[PGI_Glu], LC[LC_NA[1]], syn_type=DA_ex, weight_coef=1.000000000)
connect(BNST[BNST_Glu], BNST[BNST_GABA], syn_type=Glu, weight_coef=1.000000000)
connect(BNST[BNST_GABA], PVN[PVN_GABA], syn_type=GABA, weight_coef=1.000000000)
connect(BNST[BNST_Ach], Amy[Amy_Ach], syn_type=Ach, weight_coef=1.000000000)
connect(Amy[Amy_Glu], AcbShell[AcbShell_GABA[1]], syn_type=DA_ex, weight_coef=1.000000000)
connect(Amy[Amy_Glu], AcbCore[AcbCore_Ach], syn_type=DA_ex, weight_coef=1.000000000)
connect(Amy[Amy_Glu], AcbCore[AcbCore_GABA[0]], syn_type=DA_ex, weight_coef=1.000000000)
connect(Amy[Amy_Ach], LC[LC_NA[0]], syn_type=Ach, weight_coef=1.000000000)
connect(Amy[Amy_Ach], LC[LC_Ach], syn_type=Ach, weight_coef=1.000000000)
connect(Amy[Amy_Ach], LC[LC_GABA], syn_type=Ach, weight_coef=1.000000000)
connect(Amy[Amy_Ach], LC[LC_D1], syn_type=Ach, weight_coef=1.000000000)
connect(Amy[Amy_Ach], LC[LC_D2], syn_type=Ach, weight_coef=1.000000000)
connect(Amy[Amy_Ach], LC[LC_NA[1]], syn_type=Ach, weight_coef=1.000000000)
connect(Amy[Amy_GABA], BNST[BNST_GABA], syn_type=GABA, weight_coef=1.000000000)
connect(RN[RN_5-HT], LC[LC_NA[0]], syn_type=DA_ex, weight_coef=1.000000000)
connect(RN[RN_a1], RN[RN_5-HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(RN[RN_a2], RN[RN_5-HT], syn_type=DA_ex, weight_coef=1.000000000)
connect(Thalamus[Thalamus_Glu], Motorcortex[Motorcortex_Glu], syn_type=Glu, weight_coef=1.000000000)
connect(PVN[PVN_GABA], Motorcortex[Motorcortex_Glu], syn_type=GABA, weight_coef=1.000000000)
connect(LTD[LTD_Ach], BNST[BNST_Ach], syn_type=Ach, weight_coef=1.000000000)
connect(LTD[LTD_Ach], LC[LC_NA[0]], syn_type=Ach, weight_coef=1.000000000)
connect(LTD[LTD_Ach], Thalamus[Thalamus_Glu], syn_type=Ach, weight_coef=1.000000000)
connect(LTD[LTD_Ach], Prefrontalcortex[Prefrontalcortex_Glu[1]], syn_type=Ach, weight_coef=1.000000000)
connect(LTD[LTD_Ach], Prefrontalcortex[Prefrontalcortex_Glu[0]], syn_type=Ach, weight_coef=1.000000000)
connect(PrH[PrH_GABA], LC[LC_GABA], syn_type=GABA, weight_coef=1.000000000)
connect(AcbCore[AcbCore_Ach], AcbShell[AcbShell_GABA[1]], syn_type=Ach, weight_coef=1.000000000)
connect(AcbCore[AcbCore_GABA[0]], AcbShell[AcbShell_GABA[1]], syn_type=GABA, weight_coef=1.000000000)
connect(Prefrontalcortex[Prefrontalcortex_Glu[1]], LC[LC_NA[0]], syn_type=DA_ex, weight_coef=1.000000000)
connect(Prefrontalcortex[Prefrontalcortex_Glu[0]], BNST[BNST_Glu], syn_type=DA_ex, weight_coef=1.000000000)
connect(VTA[VTA_DA[0]], LC[LC_D1], syn_type=DA_ex, weight_coef=1.000000000)
connect(VTA[VTA_DA[0]], LC[LC_D2], syn_type=DA_ex, weight_coef=1.000000000)
connect(VTA[VTA_DA[0]], Prefrontalcortex[Prefrontalcortex_Glu[1]], syn_type=DA_ex, weight_coef=1.000000000)
connect(VTA[VTA_DA[0]], Prefrontalcortex[Prefrontalcortex_Glu[0]], syn_type=DA_ex, weight_coef=1.000000000)
connect(VTA[VTA_a1], VTA[VTA_DA[1]], syn_type=DA_ex, weight_coef=1.000000000)
connect(VTA[VTA_DA[1]], AcbShell[AcbShell_GABA[1]], syn_type=DA_ex, weight_coef=1.000000000)
connect(AcbShell[AcbShell_GABA[1]], LC[LC_NA[0]], syn_type=GABA, weight_coef=1.000000000)
connect(AcbShell[AcbShell_GABA[1]], LC[LC_Ach], syn_type=GABA, weight_coef=1.000000000)
connect(AcbShell[AcbShell_GABA[1]], LC[LC_GABA], syn_type=GABA, weight_coef=1.000000000)
connect(AcbShell[AcbShell_GABA[1]], LC[LC_D1], syn_type=GABA, weight_coef=1.000000000)
connect(AcbShell[AcbShell_GABA[1]], LC[LC_D2], syn_type=GABA, weight_coef=1.000000000)
connect(AcbShell[AcbShell_GABA[1]], LC[LC_NA[1]], syn_type=GABA, weight_coef=1.000000000)
connect(Motorcortex[Motorcortex_Glu], LC[LC_NA[0]], syn_type=DA_ex, weight_coef=1.000000000)


logger.debug("* * * Creating spike generators...")
  

logger.debug("* * * Attaching spikes detector")
logger.debug("* * * Attaching multimeters")
connect_detector(LC[LC_NA[0]])
connect_multimeter(LC[LC_NA[0]])
connect_detector(LC[LC_Ach])
connect_multimeter(LC[LC_Ach])
connect_detector(LC[LC_GABA])
connect_multimeter(LC[LC_GABA])
connect_detector(LC[LC_D1])
connect_multimeter(LC[LC_D1])
connect_detector(LC[LC_D2])
connect_multimeter(LC[LC_D2])
connect_detector(LC[LC_NA[1]])
connect_multimeter(LC[LC_NA[1]])
connect_detector(PGI[PGI_GABA])
connect_multimeter(PGI[PGI_GABA])
connect_detector(PGI[PGI_Glu])
connect_multimeter(PGI[PGI_Glu])
connect_detector(BNST[BNST_Glu])
connect_multimeter(BNST[BNST_Glu])
connect_detector(BNST[BNST_GABA])
connect_multimeter(BNST[BNST_GABA])
connect_detector(BNST[BNST_Ach])
connect_multimeter(BNST[BNST_Ach])
connect_detector(Amy[Amy_Glu])
connect_multimeter(Amy[Amy_Glu])
connect_detector(Amy[Amy_Ach])
connect_multimeter(Amy[Amy_Ach])
connect_detector(Amy[Amy_GABA])
connect_multimeter(Amy[Amy_GABA])
connect_detector(RN[RN_5-HT])
connect_multimeter(RN[RN_5-HT])
connect_detector(RN[RN_a1])
connect_multimeter(RN[RN_a1])
connect_detector(RN[RN_a2])
connect_multimeter(RN[RN_a2])
connect_detector(Thalamus[Thalamus_Glu])
connect_multimeter(Thalamus[Thalamus_Glu])
connect_detector(PVN[PVN_GABA])
connect_multimeter(PVN[PVN_GABA])
connect_detector(LTD[LTD_a1])
connect_multimeter(LTD[LTD_a1])
connect_detector(LTD[LTD_a2])
connect_multimeter(LTD[LTD_a2])
connect_detector(LTD[LTD_Ach])
connect_multimeter(LTD[LTD_Ach])
connect_detector(PrH[PrH_GABA])
connect_multimeter(PrH[PrH_GABA])
connect_detector(AcbCore[AcbCore_Ach])
connect_multimeter(AcbCore[AcbCore_Ach])
connect_detector(AcbCore[AcbCore_GABA[0]])
connect_multimeter(AcbCore[AcbCore_GABA[0]])
connect_detector(Prefrontalcortex[Prefrontalcortex_Glu[1]])
connect_multimeter(Prefrontalcortex[Prefrontalcortex_Glu[1]])
connect_detector(Prefrontalcortex[Prefrontalcortex_Glu[0]])
connect_multimeter(Prefrontalcortex[Prefrontalcortex_Glu[0]])
connect_detector(Ab[Ab_NA])
connect_multimeter(Ab[Ab_NA])
connect_detector(VTA[VTA_DA[0]])
connect_multimeter(VTA[VTA_DA[0]])
connect_detector(VTA[VTA_a1])
connect_multimeter(VTA[VTA_a1])
connect_detector(VTA[VTA_DA[1]])
connect_multimeter(VTA[VTA_DA[1]])
connect_detector(Aa[Aa_NA])
connect_multimeter(Aa[Aa_NA])
connect_detector(AcbShell[AcbShell_GABA[1]])
connect_multimeter(AcbShell[AcbShell_GABA[1]])
connect_detector(Motorcortex[Motorcortex_Glu])
connect_multimeter(Motorcortex[Motorcortex_Glu])


endbuild = datetime.datetime.now()

simulate()
get_log(startbuild, endbuild)
save(GUI=statusGUI)