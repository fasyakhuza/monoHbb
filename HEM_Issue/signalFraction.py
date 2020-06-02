import os
from os import sys

import ROOT
from ROOT import TFile, TCanvas, TH1F, TLegend, gStyle, gPad, TPaveText

sys.path.append('../../yieldratio/')
import PlotTemplates
from PlotTemplates import *



path_preCut = "analysis_histogram/2018_2016Sig_old/"

sig1_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma1000_MChi1_MA1200_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102911.root")
sig2_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma100_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102834.root")
sig3_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma10_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102620.root")

nMET1_SR1_preCut = (sig1_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET2_SR1_preCut = (sig2_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET3_SR1_preCut = (sig3_preCut.Get("h_reg_SR_1b_MET")).Integral()

nMET1_SR2_preCut = (sig1_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET2_SR2_preCut = (sig2_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET3_SR2_preCut = (sig3_preCut.Get("h_reg_SR_2b_MET")).Integral()



path_postCut = "analysis_histogram/2018_2016Sig_afterCut_v2/"

sig1_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma1000_MChi1_MA1200_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102911_0000_0_0.root")
sig2_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma100_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102834_0000_0_0.root")
sig3_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma10_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102620_0000_0_0.root")

nMET1_SR1_postCut = (sig1_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET2_SR1_postCut = (sig2_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET3_SR1_postCut = (sig3_postCut.Get("h_reg_SR_1b_MET")).Integral()

nMET1_SR2_postCut = (sig1_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET2_SR2_postCut = (sig2_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET3_SR2_postCut = (sig3_postCut.Get("h_reg_SR_2b_MET")).Integral()



sig1frac_SR1 = (nMET1_SR1_preCut - nMET1_SR1_postCut)/nMET1_SR1_preCut*100
sig2frac_SR1 = (nMET2_SR1_preCut - nMET2_SR1_postCut)/nMET2_SR1_preCut*100
sig3frac_SR1 = (nMET3_SR1_preCut - nMET3_SR1_postCut)/nMET3_SR1_preCut*100

sig1frac_SR2 = (nMET1_SR2_preCut - nMET1_SR2_postCut)/nMET1_SR2_preCut*100
sig2frac_SR2 = (nMET2_SR2_preCut - nMET2_SR2_postCut)/nMET2_SR2_preCut*100
sig3frac_SR2 = (nMET3_SR2_preCut - nMET3_SR2_postCut)/nMET3_SR2_preCut*100


print "Fraction value of signal sample 1 in SR1 :", sig1frac_SR1, "%"
print " "
print "Fraction value of signal sample 2 in SR1 :", sig2frac_SR1, "%"
print " "
print "Fraction value of signal sample 3 in SR1 :", sig3frac_SR1, "%"
print " "
print " "
print "Fraction value of signal sample 1 in SR2 :", sig1frac_SR2, "%"
print " "
print "Fraction value of signal sample 2 in SR2 :", sig2frac_SR2, "%"
print " "
print "Fraction value of signal sample 3 in SR2 :", sig3frac_SR2, "%"
print " "
