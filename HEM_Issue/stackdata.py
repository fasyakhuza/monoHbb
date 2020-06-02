import os
from os import sys

import ROOT
from ROOT import TFile, TCanvas, TH1F, TLegend, gStyle, gPad, TPaveText

from datetime import datetime

sys.path.append('../../yieldratio/')
import PlotTemplates
from PlotTemplates import *


def drawhist(isMET, reg, dirPath):
    path_before = "analysis_histogram/2018_old/"
    path_after = "analysis_histogram/2018_combined_afterCut_v2/"
    
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
        
        #h_jet2phi_1b = []
        #jet2phi_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_Jet2Phi")
        #h_jet2phi_1b.append(jet2phi_comb_top1b)
        #jet2phi_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_Jet2Phi")
        #h_jet2phi_1b.append(jet2phi_AB_top1b)
        #jet2phi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopmunuCR_1b_Jet2Phi")
        #h_jet2phi_1b.append(jet2phi_CD_bfr_top1b)
        #jet2phi_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_Jet2Phi")
        #h_jet2phi_1b.append(jet2phi_CD_top1b)
        
        h_jet1eta_1b = []
        jet1eta_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_comb_top1b)
        jet1eta_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_AB_top1b)
        jet1eta_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopmunuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_CD_bfr_top1b)
        jet1eta_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_CD_top1b)
        
        #h_jet2eta_1b = []
        #jet2eta_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_Jet2Eta")
        #h_jet2eta_1b.append(jet2eta_comb_top1b)
        #jet2eta_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_Jet2Eta")
        #h_jet2eta_1b.append(jet2eta_AB_top1b)
        #jet2eta_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopmunuCR_1b_Jet2Eta")
        #h_jet2eta_1b.append(jet2eta_CD_bfr_top1b)
        #jet2eta_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_Jet2Eta")
        #h_jet2eta_1b.append(jet2eta_CD_top1b)
        
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
        
        #h_RecoilPhi_1b = []
        #RecoilPhi_comb_top1b = openfcomb.Get("h_reg_TopmunuCR_1b_RecoilPhi")
        #h_RecoilPhi_1b.append(RecoilPhi_comb_top1b)
        #RecoilPhi_AB_top1b = openfAB.Get("h_reg_TopmunuCR_1b_RecoilPhi")
        #h_RecoilPhi_1b.append(RecoilPhi_AB_top1b)
        #RecoilPhi_CD_top1b = openfCD.Get("h_reg_TopmunuCR_1b_RecoilPhi")
        #h_RecoilPhi_1b.append(RecoilPhi_CD_top1b)
    
    
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
        #alllist.append(h_RecoilPhi_1b)
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
        openfAB = TFile(path_before+"combined_data_SE_AB.root")
        openfCD_bfr = TFile(path_before+"combined_data_SE_CD.root")
        openfCD = TFile(path_after+"combined_data_SE_CD.root")

        h_jet1phi_1b = []
        jet1phi_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_comb_top1b)
        jet1phi_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_AB_top1b)
        jet1phi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_CD_bfr_top1b)
        jet1phi_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_Jet1Phi")
        h_jet1phi_1b.append(jet1phi_CD_top1b)
        
        #h_jet2phi_1b = []
        #jet2phi_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_Jet2Phi")
        #h_jet2phi_1b.append(jet2phi_comb_top1b)
        #jet2phi_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_Jet2Phi")
        #h_jet2phi_1b.append(jet2phi_AB_top1b)
        #jet2phi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_Jet2Phi")
        #h_jet2phi_1b.append(jet2phi_CD_bfr_top1b)
        #jet2phi_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_Jet2Phi")
        #h_jet2phi_1b.append(jet2phi_CD_top1b)
        
        h_jet1eta_1b = []
        jet1eta_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_comb_top1b)
        jet1eta_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_AB_top1b)
        jet1eta_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_CD_bfr_top1b)
        jet1eta_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_Jet1Eta")
        h_jet1eta_1b.append(jet1eta_CD_top1b)
        
        #h_jet2eta_1b = []
        #jet2eta_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_Jet2Eta")
        #h_jet2eta_1b.append(jet2eta_comb_top1b)
        #jet2eta_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_Jet2Eta")
        #h_jet2eta_1b.append(jet2eta_AB_top1b)
        #jet2eta_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_Jet2Eta")
        #h_jet2eta_1b.append(jet2eta_CD_bfr_top1b)
        #jet2eta_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_Jet2Eta")
        #h_jet2eta_1b.append(jet2eta_CD_top1b)
        
        #h_MET_1b = []
        #MET_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_MET")
        #h_MET_1b.append(MET_comb_top1b)
        #MET_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_MET")
        #h_MET_1b.append(MET_AB_top1b)
        #MET_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_MET")
        #h_MET_1b.append(MET_CD_top1b)
        
        h_METphi_1b = []
        METphi_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_comb_top1b)
        METphi_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_AB_top1b)
        METphi_CD_bfr_top1b = openfCD_bfr.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_CD_bfr_top1b)
        METphi_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_METPhi")
        h_METphi_1b.append(METphi_CD_top1b)
        
        #h_RecoilPhi_1b = []
        #RecoilPhi_comb_top1b = openfcomb.Get("h_reg_TopenuCR_1b_RecoilPhi")
        #h_RecoilPhi_1b.append(RecoilPhi_comb_top1b)
        #RecoilPhi_AB_top1b = openfAB.Get("h_reg_TopenuCR_1b_RecoilPhi")
        #h_RecoilPhi_1b.append(RecoilPhi_AB_top1b)
        #RecoilPhi_CD_top1b = openfCD.Get("h_reg_TopenuCR_1b_RecoilPhi")
        #h_RecoilPhi_1b.append(RecoilPhi_CD_top1b)
        
        
        h_jet1phi_2b = []
        jet1phi_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_comb_top2b)
        jet1phi_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_AB_top2b)
        jet1phi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_CD_bfr_top2b)
        jet1phi_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Jet1Phi")
        h_jet1phi_2b.append(jet1phi_CD_top2b)
        
        h_jet2phi_2b = []
        jet2phi_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_comb_top2b)
        jet2phi_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_AB_top2b)
        jet2phi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_CD_bfr_top2b)
        jet2phi_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Jet2Phi")
        h_jet2phi_2b.append(jet2phi_CD_top2b)
        
        h_jet1eta_2b = []
        jet1eta_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_comb_top2b)
        jet1eta_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_AB_top2b)
        jet1eta_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_CD_bfr_top2b)
        jet1eta_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Jet1Eta")
        h_jet1eta_2b.append(jet1eta_CD_top2b)
        
        h_jet2eta_2b = []
        jet2eta_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_comb_top2b)
        jet2eta_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_AB_top2b)
        jet2eta_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_CD_bfr_top2b)
        jet2eta_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_Jet2Eta")
        h_jet2eta_2b.append(jet2eta_CD_top2b)
        
        #h_MET_2b = []
        #MET_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_MET")
        #h_MET_2b.append(MET_comb_top2b)
        #MET_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_MET")
        #h_MET_2b.append(MET_AB_top2b)
        #MET_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_MET")
        #h_MET_2b.append(MET_CD_top2b)
        
        h_METphi_2b = []
        METphi_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_comb_top2b)
        METphi_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_AB_top2b)
        METphi_CD_bfr_top2b = openfCD_bfr.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_CD_bfr_top2b)
        METphi_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_METPhi")
        h_METphi_2b.append(METphi_CD_top2b)
        
        #h_RecoilPhi_2b = []
        #RecoilPhi_comb_top2b = openfcomb.Get("h_reg_TopenuCR_2b_RecoilPhi")
        #h_RecoilPhi_2b.append(RecoilPhi_comb_top2b)
        #RecoilPhi_AB_top2b = openfAB.Get("h_reg_TopenuCR_2b_RecoilPhi")
        #h_RecoilPhi_2b.append(RecoilPhi_AB_top2b)
        #RecoilPhi_CD_top2b = openfCD.Get("h_reg_TopenuCR_2b_RecoilPhi")
        #h_RecoilPhi_2b.append(RecoilPhi_CD_top2b)
        
        alllist = []
        alllist.append(h_jet1phi_1b)
        #alllist.append(h_jet2phi_1b)
        alllist.append(h_jet1eta_1b)
        #alllist.append(h_jet2eta_1b)
        #alllist.append(h_MET_1b)
        alllist.append(h_METphi_1b)
        #alllist.append(h_RecoilPhi_1b)
        alllist.append(h_jet1phi_2b)
        alllist.append(h_jet2phi_2b)
        alllist.append(h_jet1eta_2b)
        alllist.append(h_jet2eta_2b)
        #alllist.append(h_MET_2b)
        alllist.append(h_METphi_2b)
        #alllist.append(h_RecoilPhi_2b)
        
        #print "2", alllist, len(alllist)

            
        

    
    c = PlotTemplates.myCanvas()
    gPad.GetUymax()
    gPad.SetLogy()
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)
        
    leg = PlotTemplates.SetLegend(coordinate_=[.47,.73,.79,.88])

    #xAxisName = ["Jet1 #phi", "Jet1 #eta", "MET", "MET #phi", "Recoil #phi", "Jet1 #phi", "Jet2 #phi", "Jet1 #eta", "Jet2 #eta", "MET", "MET #phi", "Recoil #phi"]

    xAxisName = ["Jet1 #phi", "Jet1 #eta", "MET #phi", "Jet1 #phi", "Jet2 #phi", "Jet1 #eta", "Jet2 #eta", "MET #phi"]
        
    for i in range(len(alllist)):
        leg.Clear()
        h = alllist[i]
        
        h[0].Scale(1/h[0].Integral())
        h[0].SetLineWidth(3)
        h[0].SetMarkerStyle(20)
        h[0].SetMarkerSize(0.5)
        h[0].SetLineColor(1)
        h[0].SetMarkerColor(1)
        h[0].GetXaxis().SetTitle(xAxisName[i])
        h[0].GetYaxis().SetTitle("Events/Bin")
        leg.AddEntry(h[0], "Total (Before Cut)")
            
        h[1].Scale(1/h[1].Integral())
        h[1].SetLineWidth(3)
        h[1].SetMarkerStyle(21)
        h[1].SetMarkerSize(0.5)
        h[1].SetLineColor(2)
        h[1].SetMarkerColor(2)
        h[1].GetXaxis().SetTitle(xAxisName[i])
        leg.AddEntry(h[1], "AB (Before Cut)")
        
        h[2].Scale(1/h[2].Integral())
        h[2].SetLineWidth(3)
        h[2].SetMarkerStyle(22)
        h[2].SetMarkerSize(0.5)
        h[2].SetLineColor(4)
        h[2].SetMarkerColor(4)
        h[2].GetXaxis().SetTitle(xAxisName[i])
        leg.AddEntry(h[2], "CD (Before Cut)")
        
        h[3].Scale(1/h[3].Integral())
        h[3].SetLineWidth(3)
        h[3].SetMarkerStyle(23)
        h[3].SetMarkerSize(0.5)
        h[3].SetLineColor(3)
        h[3].SetMarkerColor(3)
        h[3].GetXaxis().SetTitle(xAxisName[i])
        leg.AddEntry(h[3], "CD (After Cut)")
            
        h[0].Draw("hist")
        h[1].Draw("histsame")
        h[2].Draw("histsame")
        h[3].Draw("histsame")
        leg.Draw()
            
        energy = PlotTemplates.drawenergy(is2017 = False)
        for k in energy:
            k.Draw()
        
        pavetxt = ["Top (e#nu) + 1b CR", "Top (e#nu) + 1b CR", "Top (e#nu) + 1b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR", "Top (e#nu) + 2b CR"]
    
        pt = TPaveText(0.1577181,0.815,0.3580537,0.875,"brNDC")
        pt.SetBorderSize(0)
        pt.SetTextAlign(12)
        pt.SetFillStyle(0)
        pt.SetTextFont(52)
        pt.AddText(pavetxt[i])
        pt.Draw()
        
        #name = ["_1b_jet1phi", "_1b_jet1eta", "_1b_MET", "_1b_METphi", "_1b_RecoilPhi", "_2b_jet1phi", "_2b_jet2phi", "_2b_jet1eta", "_2b_jet2eta", "_2b_MET", "_2b_METphi", "_2b_RecoilPhi"]

        name = ["_1b_jet1phi", "_1b_jet1eta", "_1b_METphi", "_2b_jet1phi", "_2b_jet2phi", "_2b_jet1eta", "_2b_jet2eta", "_2b_METphi"]
            
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



