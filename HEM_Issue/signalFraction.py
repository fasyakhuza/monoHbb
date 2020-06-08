import os
from os import sys

import ROOT
from ROOT import TFile, TCanvas, TH1F, TLegend, gStyle, gPad, TPaveText

sys.path.append('../../yieldratio/')
import PlotTemplates
from PlotTemplates import *



path_preCut = "analysis_histogram/2018_2016Sig_old/"

sig1_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma150_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102403.root")
sig2_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma200_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102202.root")
sig3_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma250_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102052.root")
sig4_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma300_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102014.root")
sig5_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma350_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_101903.root")
sig6_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma400_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_101746.root")
sig7_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma450_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_101546.root")
sig8_preCut = TFile(path_preCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma500_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_101429.root")

nMET1_SR1_preCut = (sig1_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET2_SR1_preCut = (sig2_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET3_SR1_preCut = (sig3_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET4_SR1_preCut = (sig4_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET5_SR1_preCut = (sig5_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET6_SR1_preCut = (sig6_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET7_SR1_preCut = (sig7_preCut.Get("h_reg_SR_1b_MET")).Integral()
nMET8_SR1_preCut = (sig8_preCut.Get("h_reg_SR_1b_MET")).Integral()

nMET1_SR2_preCut = (sig1_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET2_SR2_preCut = (sig2_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET3_SR2_preCut = (sig3_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET4_SR2_preCut = (sig4_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET5_SR2_preCut = (sig5_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET6_SR2_preCut = (sig6_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET7_SR2_preCut = (sig7_preCut.Get("h_reg_SR_2b_MET")).Integral()
nMET8_SR2_preCut = (sig8_preCut.Get("h_reg_SR_2b_MET")).Integral()



path_postCut = "analysis_histogram/2018_hem_cut_updated_signal/"

sig1_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma150_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102403_0000_0_0.root")
sig2_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma200_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102202_0000_0_0.root")
sig3_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma250_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102052_0000_0_0.root")
sig4_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma300_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_102014_0000_0_0.root")
sig5_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma350_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_101903_0000_0_0.root")
sig6_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma400_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_101746_0000_0_0.root")
sig7_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma450_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_101546_0000_0_0.root")
sig8_postCut = TFile(path_postCut+"Output_crab_bbDM_2HDMa_LO_5f_Ma500_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV-madgraph-pythia8_200523_101429_0000_0_0.root")


nMET1_SR1_postCut = (sig1_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET2_SR1_postCut = (sig2_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET3_SR1_postCut = (sig3_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET4_SR1_postCut = (sig4_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET5_SR1_postCut = (sig5_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET6_SR1_postCut = (sig6_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET7_SR1_postCut = (sig7_postCut.Get("h_reg_SR_1b_MET")).Integral()
nMET8_SR1_postCut = (sig8_postCut.Get("h_reg_SR_1b_MET")).Integral()

nMET1_SR2_postCut = (sig1_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET2_SR2_postCut = (sig2_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET3_SR2_postCut = (sig3_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET4_SR2_postCut = (sig4_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET5_SR2_postCut = (sig5_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET6_SR2_postCut = (sig6_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET7_SR2_postCut = (sig7_postCut.Get("h_reg_SR_2b_MET")).Integral()
nMET8_SR2_postCut = (sig8_postCut.Get("h_reg_SR_2b_MET")).Integral()



sig1frac_SR1 = (nMET1_SR1_preCut - nMET1_SR1_postCut)/nMET1_SR1_preCut*100
sig2frac_SR1 = (nMET2_SR1_preCut - nMET2_SR1_postCut)/nMET2_SR1_preCut*100
sig3frac_SR1 = (nMET3_SR1_preCut - nMET3_SR1_postCut)/nMET3_SR1_preCut*100
sig4frac_SR1 = (nMET4_SR1_preCut - nMET4_SR1_postCut)/nMET4_SR1_preCut*100
sig5frac_SR1 = (nMET5_SR1_preCut - nMET5_SR1_postCut)/nMET5_SR1_preCut*100
sig6frac_SR1 = (nMET6_SR1_preCut - nMET6_SR1_postCut)/nMET6_SR1_preCut*100
sig7frac_SR1 = (nMET7_SR1_preCut - nMET7_SR1_postCut)/nMET7_SR1_preCut*100
sig8frac_SR1 = (nMET8_SR1_preCut - nMET8_SR1_postCut)/nMET8_SR1_preCut*100

sig1frac_SR2 = (nMET1_SR2_preCut - nMET1_SR2_postCut)/nMET1_SR2_preCut*100
sig2frac_SR2 = (nMET2_SR2_preCut - nMET2_SR2_postCut)/nMET2_SR2_preCut*100
sig3frac_SR2 = (nMET3_SR2_preCut - nMET3_SR2_postCut)/nMET3_SR2_preCut*100
sig4frac_SR2 = (nMET4_SR2_preCut - nMET4_SR2_postCut)/nMET4_SR2_preCut*100
sig5frac_SR2 = (nMET5_SR2_preCut - nMET5_SR2_postCut)/nMET5_SR2_preCut*100
sig6frac_SR2 = (nMET6_SR2_preCut - nMET6_SR2_postCut)/nMET6_SR2_preCut*100
sig7frac_SR2 = (nMET7_SR2_preCut - nMET7_SR2_postCut)/nMET7_SR2_preCut*100
sig8frac_SR2 = (nMET8_SR2_preCut - nMET8_SR2_postCut)/nMET8_SR2_preCut*100



print "Fraction value of signal sample 1 in SR1 :", sig1frac_SR1, "%"
print " "
print "Fraction value of signal sample 2 in SR1 :", sig2frac_SR1, "%"
print " "
print "Fraction value of signal sample 3 in SR1 :", sig3frac_SR1, "%"
print " "
print "Fraction value of signal sample 4 in SR1 :", sig4frac_SR1, "%"
print " "
print "Fraction value of signal sample 5 in SR1 :", sig5frac_SR1, "%"
print " "
print "Fraction value of signal sample 6 in SR1 :", sig6frac_SR1, "%"
print " "
print "Fraction value of signal sample 7 in SR1 :", sig7frac_SR1, "%"
print " "
print "Fraction value of signal sample 8 in SR1 :", sig8frac_SR1, "%"
print " "

print " "

print "Fraction value of signal sample 1 in SR2 :", sig1frac_SR2, "%"
print " "
print "Fraction value of signal sample 2 in SR2 :", sig2frac_SR2, "%"
print " "
print "Fraction value of signal sample 3 in SR2 :", sig3frac_SR2, "%"
print " "
print "Fraction value of signal sample 4 in SR2 :", sig4frac_SR2, "%"
print " "
print "Fraction value of signal sample 5 in SR2 :", sig5frac_SR2, "%"
print " "
print "Fraction value of signal sample 6 in SR2 :", sig6frac_SR2, "%"
print " "
print "Fraction value of signal sample 7 in SR2 :", sig7frac_SR2, "%"
print " "
print "Fraction value of signal sample 8 in SR2 :", sig8frac_SR2, "%"
print " "
