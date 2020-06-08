import os
from os import sys

import ROOT
from ROOT import TFile, TCanvas, TH1F, TH2F, TLegend, gStyle, gPad, TPaveText

from datetime import datetime

sys.path.append('../../yieldratio/')
import PlotTemplates
from PlotTemplates import *


def effect(h_Pre, h_Post):
    nPre = h_Pre.Integral()
    nPost = h_Post.Integral()
    effectPrecentage = (nPre - nPost)/nPre*100
    return effectPrecentage


def drawhist(isMET, reg, dirPath):
    path_before = "analysis_histogram/2018_old/"
    path_after = "analysis_histogram/2018_hem_cut_updated/"
    
    if isMET:
        openfcomb = TFile(path_before+"combined_data_MET.root")
        openfAB = TFile(path_before+"combined_data_MET_AB.root")
        openfCD_bfr = TFile(path_before+"combined_data_MET_CD.root")
        openfCD = TFile(path_after+"combined_data_MET_CD.root")

        h_jet1phi_1b = []
        jet1phi_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_comb_top1b)
        jet1phi_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_AB_top1b)
        jet1phi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopmunuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_CD_bfr_top1b)
        jet1phi_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_CD_top1b)
        
        
        h_jet1eta_1b = []
        jet1eta_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_comb_top1b)
        jet1eta_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_AB_top1b)
        jet1eta_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopmunuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_CD_bfr_top1b)
        jet1eta_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_CD_top1b)

        
        #h_MET_1b = []
        #MET_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_MET")
        #h_MET_1b.append(MET_comb_top1b)
        #MET_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_MET")
        #h_MET_1b.append(MET_AB_top1b)
        #MET_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_MET")
        #h_MET_1b.append(MET_CD_top1b)
    
        h_METphi_1b = []
        METphi_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_METPhi")
        h_METphi_1b.append(METphi_comb_top1b)
        METphi_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_METPhi")
        h_METphi_1b.append(METphi_AB_top1b)
        METphi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopmunuCR_1b_METPhi")
        h_METphi_1b.append(METphi_CD_bfr_top1b)
        METphi_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_METPhi")
        h_METphi_1b.append(METphi_CD_top1b)
        
        h_RecoilPhi_1b = []
        RecoilPhi_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_comb_top1b)
        RecoilPhi_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_AB_top1b)
        RecoilPhi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopmunuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_CD_bfr_top1b)
        RecoilPhi_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_CD_top1b)
    
    
        h_jet1phi_2b = []
        jet1phi_comb_top2b = openfcomb.Get("h_reg_TopmunuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_comb_top2b)
        jet1phi_AB_top2b = openfAB.Get("h_reg_TopmunuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_AB_top2b)
        jet1phi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopmunuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_CD_bfr_top2b)
        jet1phi_CD_top2b = openfCD.Get("h_reg_TopmunuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_CD_top2b)
        
        h_jet2phi_2b = []
        jet2phi_comb_top2b = openfcomb.Get("h_reg_TopmunuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_comb_top2b)
        jet2phi_AB_top2b = openfAB.Get("h_reg_TopmunuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_AB_top2b)
        jet2phi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopmunuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_CD_bfr_top2b)
        jet2phi_CD_top2b = openfCD.Get("h_reg_TopmunuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_CD_top2b)
        
        h_jet1eta_2b = []
        jet1eta_comb_top2b = openfcomb.Get("h_reg_TopmunuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_comb_top2b)
        jet1eta_AB_top2b = openfAB.Get("h_reg_TopmunuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_AB_top2b)
        jet1eta_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopmunuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_CD_bfr_top2b)
        jet1eta_CD_top2b = openfCD.Get("h_reg_TopmunuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_CD_top2b)
        
        h_jet2eta_2b = []
        jet2eta_comb_top2b = openfcomb.Get("h_reg_TopmunuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_comb_top2b)
        jet2eta_AB_top2b = openfAB.Get("h_reg_TopmunuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_AB_top2b)
        jet2eta_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopmunuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_CD_bfr_top2b)
        jet2eta_CD_top2b = openfCD.Get("h_reg_TopmunuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_CD_top2b)
        
        #h_MET_2b = []
        #MET_comb_top2b = openfcomb.Get("h_reg_TopmunuCR_2b_MET")
        #h_MET_2b.append(MET_comb_top2b)
        #MET_AB_top2b = openfAB.Get("h_reg_TopmunuCR_2b_MET")
        #h_MET_2b.append(MET_AB_top2b)
        #MET_CD_top2b = openfCD.Get("h_reg_TopmunuCR_2b_MET")
        #h_MET_2b.append(MET_CD_top2b)
        
        h_METphi_2b = []
        METphi_comb_top2b = openfcomb.Get("h_reg_TopmunuCR_2b_METPhi")
        h_METphi_2b.append(METphi_comb_top2b)
        METphi_AB_top2b = openfAB.Get("h_reg_TopmunuCR_2b_METPhi")
        h_METphi_2b.append(METphi_AB_top2b)
        METphi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopmunuCR_2b_METPhi")
        h_METphi_2b.append(METphi_CD_bfr_top2b)
        METphi_CD_top2b = openfCD.Get("h_reg_TopmunuCR_2b_METPhi")
        h_METphi_2b.append(METphi_CD_top2b)
        
        #h_RecoilPhi_2b = []
        #RecoilPhi_comb_top2b = openfcomb.Get("h_reg_TopmunuCR_2b_RecoilPhi")
        #h_RecoilPhi_2b.append(RecoilPhi_comb_top2b)
        #RecoilPhi_AB_top2b = openfAB.Get("h_reg_TopmunuCR_2b_RecoilPhi")
        #h_RecoilPhi_2b.append(RecoilPhi_AB_top2b)
        #RecoilPhi_CD_top2b = openfCD.Get("h_reg_TopmunuCR_2b_RecoilPhi")
        #h_RecoilPhi_2b.append(RecoilPhi_CD_top2b)
        
        alllist = []
        alllist.append(h_jet1phi_1b)
        #alllist.append(h_jet2phi_1b)
        alllist.append(h_jet1eta_1b)
        #alllist.append(h_jet2eta_1b)
        #alllist.append(h_MET_1b)
        alllist.append(h_METphi_1b)
        alllist.append(h_RecoilPhi_1b)
        alllist.append(h_jet1phi_2b)
        alllist.append(h_jet2phi_2b)
        alllist.append(h_jet1eta_2b)
        alllist.append(h_jet2eta_2b)
        #alllist.append(h_MET_2b)
        alllist.append(h_METphi_2b)
        #alllist.append(h_RecoilPhi_2b)
        
        #print "1", alllist, len(alllist)

    if not isMET:
        openfcomb = TFile(path_before+"combined_data_SE.root")
        openfcomb_aftr = TFile(path_after+"combined_data_SE.root")
        openfAB = TFile(path_before+"combined_data_SE_AB.root")
        openfAB_aftr = TFile(path_after+"combined_data_SE_AB.root")
        openfCD_bfr = TFile(path_before+"combined_data_SE_CD.root")
        openfCD = TFile(path_after+"combined_data_SE_CD.root")

        
        h_jet1phi_1b = []
        jet1phi_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_comb_top1b)
        
        jet1phi_comb_aftr_top1b = openfcomb_aftr.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_comb_aftr_top1b)
        
        jet1phi_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_AB_top1b)
        
        jet1phi_AB_aftr_top1b = openfAB_aftr.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_AB_aftr_top1b)
        
        jet1phi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_CD_bfr_top1b)
        
        jet1phi_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_CD_top1b)
        
        
        
        h_jet1eta_1b = []
        jet1eta_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_comb_top1b)
        
        jet1eta_comb_aftr_top1b = openfcomb_aftr.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_comb_aftr_top1b)
        
        jet1eta_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_AB_top1b)
        
        jet1eta_AB_aftr_top1b = openfAB_aftr.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_AB_aftr_top1b)
        
        jet1eta_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_CD_bfr_top1b)
        
        jet1eta_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_CD_top1b)
        
        
        
        h_MET_1b = []
        MET_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_MET")
        h_MET_1b.append(MET_comb_top1b)
        
        MET_comb_aftr_top1b = openfcomb_aftr.Get("h_reg_TopenuCR_1b_MET")
        h_MET_1b.append(MET_comb_aftr_top1b)
        
        MET_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_MET")
        h_MET_1b.append(MET_AB_top1b)
        
        MET_AB_aftr_top1b = openfAB_aftr.Get("h_reg_TopenuCR_1b_MET")
        h_MET_1b.append(MET_AB_aftr_top1b)
        
        MET_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_MET")
        h_MET_1b.append(MET_CD_bfr_top1b)
        
        MET_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_MET")
        h_MET_1b.append(MET_CD_top1b)
        
        
        
        h_METphi_1b = []
        METphi_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_comb_top1b)
        
        METphi_comb_aftr_top1b = openfcomb_aftr.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_comb_aftr_top1b)
        
        METphi_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_AB_top1b)
        
        METphi_AB_aftr_top1b = openfAB_aftr.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_AB_aftr_top1b)
        
        METphi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_CD_bfr_top1b)
        
        METphi_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_CD_top1b)
        
        
        
        h_Recoil_1b = []
        Recoil_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_Recoil")
        h_Recoil_1b.append(Recoil_comb_top1b)
        
        Recoil_comb_aftr_top1b = openfcomb_aftr.Get("h_reg_TopenuCR_1b_Recoil")
        h_Recoil_1b.append(Recoil_comb_aftr_top1b)
        
        Recoil_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_Recoil")
        h_Recoil_1b.append(Recoil_AB_top1b)
        
        Recoil_AB_aftr_top1b = openfAB_aftr.Get("h_reg_TopenuCR_1b_Recoil")
        h_Recoil_1b.append(Recoil_AB_aftr_top1b)
        
        Recoil_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_Recoil")
        h_Recoil_1b.append(Recoil_CD_bfr_top1b)
        
        Recoil_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_Recoil")
        h_Recoil_1b.append(Recoil_CD_top1b)
        
        

        h_RecoilPhi_1b = []
        RecoilPhi_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_comb_top1b)
        
        RecoilPhi_comb_aftr_top1b = openfcomb_aftr.Get("h_reg_TopenuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_comb_aftr_top1b)
        
        RecoilPhi_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_AB_top1b)
        
        RecoilPhi_AB_aftr_top1b = openfAB_aftr.Get("h_reg_TopenuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_AB_aftr_top1b)
        
        RecoilPhi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_CD_bfr_top1b)
        
        RecoilPhi_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_RecoilPhi")
        h_RecoilPhi_1b.append(RecoilPhi_CD_top1b)
        
        
        
        
        h_jet1phi_2b = []
        jet1phi_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_comb_top2b)
        
        jet1phi_comb_aftr_top2b = openfcomb_aftr.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_comb_aftr_top2b)
        
        jet1phi_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_AB_top2b)
        
        jet1phi_AB_aftr_top2b = openfAB_aftr.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_AB_aftr_top2b)
        
        jet1phi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_CD_bfr_top2b)
        
        jet1phi_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_CD_top2b)
        
        
        
        h_jet2phi_2b = []
        jet2phi_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_comb_top2b)
        
        jet2phi_comb_aftr_top2b = openfcomb_aftr.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_comb_aftr_top2b)
        
        jet2phi_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_AB_top2b)
        
        jet2phi_AB_aftr_top2b = openfAB_aftr.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_AB_aftr_top2b)
        
        jet2phi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_CD_bfr_top2b)
        
        jet2phi_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_CD_top2b)
        
        
        
        h_jet1eta_2b = []
        jet1eta_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_comb_top2b)
        
        jet1eta_comb_aftr_top2b = openfcomb_aftr.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_comb_aftr_top2b)
        
        jet1eta_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_AB_top2b)
        
        jet1eta_AB_aftr_top2b = openfAB_aftr.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_AB_aftr_top2b)
        
        jet1eta_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_CD_bfr_top2b)
        
        jet1eta_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_CD_top2b)
        
        
        
        h_jet2eta_2b = []
        jet2eta_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_comb_top2b)
        
        jet2eta_comb_aftr_top2b = openfcomb_aftr.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_comb_aftr_top2b)
        
        jet2eta_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_AB_top2b)
        
        jet2eta_AB_aftr_top2b = openfAB_aftr.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_AB_aftr_top2b)
        
        jet2eta_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_CD_bfr_top2b)
        
        jet2eta_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_CD_top2b)
        
        
        
        h_MET_2b = []
        MET_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_MET")
        h_MET_2b.append(MET_comb_top2b)
        
        MET_comb_aftr_top2b = openfcomb_aftr.Get("h_reg_TopenuCR_2b_MET")
        h_MET_2b.append(MET_comb_aftr_top2b)
        
        MET_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_MET")
        h_MET_2b.append(MET_AB_top2b)
        
        MET_AB_aftr_top2b = openfAB_aftr.Get("h_reg_TopenuCR_2b_MET")
        h_MET_2b.append(MET_AB_aftr_top2b)
        
        MET_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_MET")
        h_MET_2b.append(MET_CD_bfr_top2b)
        
        MET_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_MET")
        h_MET_2b.append(MET_CD_top2b)
        
        
        
        h_METphi_2b = []
        METphi_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_comb_top2b)
        
        METphi_comb_aftr_top2b = openfcomb_aftr.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_comb_aftr_top2b)
        
        METphi_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_AB_top2b)
        
        METphi_AB_aftr_top2b = openfAB_aftr.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_AB_aftr_top2b)
        
        METphi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_CD_bfr_top2b)
        
        METphi_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_CD_top2b)
        
        
        
        h_Recoil_2b = []
        Recoil_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Recoil")
        h_Recoil_2b.append(Recoil_comb_top2b)
        
        Recoil_comb_aftr_top2b = openfcomb_aftr.Get("h_reg_TopenuCR_2b_Recoil")
        h_Recoil_2b.append(Recoil_comb_aftr_top2b)
        
        Recoil_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Recoil")
        h_Recoil_2b.append(Recoil_AB_top2b)
        
        Recoil_AB_aftr_top2b = openfAB_aftr.Get("h_reg_TopenuCR_2b_Recoil")
        h_Recoil_2b.append(Recoil_AB_aftr_top2b)
        
        Recoil_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Recoil")
        h_Recoil_2b.append(Recoil_CD_bfr_top2b)
        
        Recoil_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Recoil")
        h_Recoil_2b.append(Recoil_CD_top2b)
        
        
        
        h_RecoilPhi_2b = []
        RecoilPhi_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_RecoilPhi")
        h_RecoilPhi_2b.append(RecoilPhi_comb_top2b)
        
        RecoilPhi_comb_aftr_top2b = openfcomb_aftr.Get("h_reg_TopenuCR_2b_RecoilPhi")
        h_RecoilPhi_2b.append(RecoilPhi_comb_aftr_top2b)
        
        RecoilPhi_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_RecoilPhi")
        h_RecoilPhi_2b.append(RecoilPhi_AB_top2b)
        
        RecoilPhi_AB_aftr_top2b = openfAB_aftr.Get("h_reg_TopenuCR_2b_RecoilPhi")
        h_RecoilPhi_2b.append(RecoilPhi_AB_aftr_top2b)
        
        RecoilPhi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_RecoilPhi")
        h_RecoilPhi_2b.append(RecoilPhi_CD_bfr_top2b)
        
        RecoilPhi_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_RecoilPhi")
        h_RecoilPhi_2b.append(RecoilPhi_CD_top2b)
        
        
        
        alllist = []
        alllist.append(h_jet1phi_1b)
        alllist.append(h_jet1eta_1b)
        alllist.append(h_MET_1b)
        alllist.append(h_METphi_1b)
        alllist.append(h_Recoil_1b)
        alllist.append(h_RecoilPhi_1b)
        alllist.append(h_jet1phi_2b)
        alllist.append(h_jet2phi_2b)
        alllist.append(h_jet1eta_2b)
        alllist.append(h_jet2eta_2b)
        alllist.append(h_MET_2b)
        alllist.append(h_METphi_2b)
        alllist.append(h_Recoil_2b)
        alllist.append(h_RecoilPhi_2b)
        
        #print "2", alllist, len(alllist)

            
        


    effectMET_ABCD_1b = effect(h_Pre = MET_comb_top1b, h_Post = MET_comb_aftr_top1b)
    print "HEM effect on MET of Topenu 1b ABCD:", effectMET_ABCD_1b, "%"
    print " "
    effectMET_AB_1b = effect(h_Pre = MET_AB_top1b, h_Post = MET_AB_aftr_top1b)
    print "HEM effect on MET of Topenu 1b AB:", effectMET_AB_1b, "%"
    print " "
    effectMET_CD_1b = effect(h_Pre = MET_CD_bfr_top1b, h_Post = MET_CD_top1b)
    print "HEM effect on MET of Topenu 1b CD:", effectMET_CD_1b, "%"
    print " "
    
    
    
    c = PlotTemplates.myCanvas()
    gPad.GetUymax()
    gPad.SetLogy()
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)
        
    leg = PlotTemplates.SetLegend(coordinate_=[.37,.76,.78,.9], ncol=2)
    leg.SetTextSize(0.017)


    xAxisName = ["Jet1 #phi", "Jet1 #eta", "MET (GeV)", "MET #phi", "Recoil (GeV)", "Recoil #phi", "Jet1 #phi", "Jet2 #phi", "Jet1 #eta", "Jet2 #eta", "MET (GeV)", "MET #phi", "Recoil (GeV)", "Recoil #phi"]
    
    color = [1,2,4,3,6,28]
    color_bfr = [1,4,6]
    legendName = ["2018 ABCD (Before HEM Veto)", "2018 ABCD (After HEM Veto)", "2018 AB (Before HEM Veto)", "2018 AB (After HEM Veto)", "2018 CD (Before HEM Veto)", "2018 CD (After HEM Veto)"]
    legendName_bfr = ["2018 ABCD", "2018 AB", "2018 CD"]

    for i in range(len(alllist)):
        leg.Clear()
        if (i == 2) or (i == 4) or (i == 10) or (i == 12):
            h = alllist[i]
            
            for j in range(len(h)):
                h[j].SetLineWidth(3)
                #h[j].SetMarkerStyle(20)
                #h[j].SetMarkerSize(0.5)
                h[j].SetLineColor(color[j])
                #h[j].SetMarkerColor(color[j])
                h[j].GetXaxis().SetTitle(xAxisName[i])
                h[j].GetYaxis().SetTitle("Events/Bin")
                leg.AddEntry(h[j], legendName[j])
                #h[j].Draw("histsame")
                #leg.Draw()

        else:
            h = alllist[i]
            
            #print i, "x-axis :", h[0].GetNbinsX(), h[0].GetXaxis().GetBinLowEdge(1)
            
            for j in range(len(h)):
                h[j].Scale(1/h[j].Integral())
                h[j].SetLineWidth(3)
                #h[j].SetMarkerStyle(20)
                #h[j].SetMarkerSize(0.5)
                h[j].SetLineColor(color[j])
                #h[j].SetMarkerColor(color[j])
                h[j].GetXaxis().SetTitle(xAxisName[i])
                h[j].GetYaxis().SetTitle("Events/Bin")
                leg.AddEntry(h[j], legendName[j])
                #h[j].Draw("histsame")
                #leg.Draw()


        h[0].Draw("hist")
        h[1].Draw("histsame")
        h[2].Draw("histsame")
        h[3].Draw("histsame")
        h[4].Draw("histsame")
        h[5].Draw("histsame")
        leg.Draw()

        energy = PlotTemplates.drawenergy(is2017 = False)
        for k in energy:
            k.Draw()
        
        pavetxt = ["Top (e#nu) + 1b CR", "Top (e#nu) + 1b CR", "Top (e#nu) + 1b CR", "Top (e#nu) + 1b CR", "Top (e#nu) + 1b CR", "Top (e#nu) + 1b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR"]
    
        pt = TPaveText(0.2177181,0.855,0.4540537,0.885,"brNDC")
        pt.SetBorderSize(0)
        pt.SetTextAlign(12)
        pt.SetFillStyle(0)
        pt.SetTextFont(52)
        pt.AddText(pavetxt[i])
        pt.Draw()


        name = ["_1b_jet1phi", "_1b_jet1eta", "_1b_MET", "_1b_METphi", "_1b_Recoil", "_1b_Recoilphi", "_2b_jet1phi", "_2b_jet2phi", "_2b_jet1eta", "_2b_jet2eta", "_2b_MET", "_2b_METphi", "_2b_Recoil", "_2b_RecoilPhi"]
            
        c.Update()

        dt = datetime.now()
        dt_str = dt.strftime("%Y%m%d_%H%M")


        subdirPath = dirPath+"/"+reg+"_"+dt_str
        if not (os.path.exists(subdirPath)):
            os.mkdir(subdirPath)
        dirPDF = subdirPath+"/pdf"
        dirPNG = subdirPath+"/png"
        if not (os.path.exists(dirPDF)):
            os.mkdir(dirPDF)
        if not (os.path.exists(dirPNG)):
            os.mkdir(dirPNG)
        
        c.SaveAs(dirPDF+"/"+reg+name[i]+"_new.pdf")
        c.SaveAs(dirPNG+"/"+reg+name[i]+"_new.png")


#drawMET = drawhist(isMET = True, dirPath = "plots", reg = "TopmunuCR")
drawSE = drawhist(isMET = False, dirPath = "plots", reg = "TopenuCR")

