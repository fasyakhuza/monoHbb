import os
from os import sys

import ROOT
from ROOT import TFile, TCanvas, TH1F, TLegend, gStyle, gPad, TPaveText, TMath

from datetime import datetime

sys.path.append('../../yieldratio/')
import PlotTemplates
from PlotTemplates import *

#import MathUtils
#from MathUtils import *

path_before = "analysis_output/2018_combined_data/"
#path_after = "analysis_output/2018_combined_afterCut_v2/"

ABCD = "combined_data_SE.root"
AB = "combined_data_SE_AB.root"
CD = "combined_data_SE_CD.root"

nbins = 28
cmin = -1.0
cmax = 7.0

h_dR_jet1_ele_1b_ABCD_bfr = TH1F("h_dR_jet1_ele_1b_ABCD_bfr", "", nbins, cmin, cmax)
h_dR_jet1_ele_2b_ABCD_bfr = TH1F("h_dR_jet1_ele_2b_ABCD_bfr", "", nbins, cmin, cmax)

h_dR_jet1_ele_1b_AB_bfr = TH1F("h_dR_jet1_ele_1b_AB_bfr", "", nbins, cmin, cmax)
h_dR_jet1_ele_2b_AB_bfr = TH1F("h_dR_jet1_ele_2b_AB_bfr", "", nbins, cmin, cmax)

h_dR_jet1_ele_1b_CD_bfr = TH1F("h_dR_jet1_ele_1b_CD_bfr", "", nbins, cmin, cmax)
h_dR_jet1_ele_2b_CD_bfr = TH1F("h_dR_jet1_ele_2b_CD_bfr", "", nbins, cmin, cmax)

#h_dR_jet1_ele_1b_CD_aftr = TH1F("h_dR_jet1_ele_1b_CD_aftr", "", 20, cmin, cmax)
#h_dR_jet1_ele_2b_CD_aftr = TH1F("h_dR_jet1_ele_2b_CD_aftr", "", 20, cmin, cmax)

def Phi_mpi_pi(x):
    kPI = 3.14159265358979323846
    kTWOPI = 2 * kPI
    
    while (x >= kPI): x = x - kTWOPI;
    while (x < -kPI): x = x + kTWOPI;
    return x;

def DeltaPhi(phi1,phi2):
    phi = Phi_mpi_pi(phi1-phi2)
    return abs(phi)

def Delta_R(eta1, eta2, phi1,phi2):
    deltaeta = eta1-eta2
    deltaphi = DeltaPhi(phi1,phi2)
    DR = TMath.Sqrt ( deltaeta**2 + deltaphi**2 )
    return DR

def dR_jet_ele(path, ifile, h_dR_1b, h_dR_2b):
    print path+ifile
    openf = TFile(path+ifile, "read")
    tree_1b = openf.Get("bbDM_TopenuCR_1b")
    tree_2b = openf.Get("bbDM_TopenuCR_2b")
    nEvents_1b = tree_1b.GetEntries()
    nEvents_2b = tree_2b.GetEntries()
    for i in range(nEvents_1b):
        tree_1b.GetEntry(i)
        eleEta_1b = getattr(tree_1b, 'leadingLepEta')
        elePhi_1b = getattr(tree_1b, 'leadingLepPhi')
        jet1Eta_1b = getattr(tree_1b, 'Jet1Eta')
        jet1Phi_1b = getattr(tree_1b, 'Jet1Phi')
        dR_jet1_ele_1b = Delta_R(jet1Eta_1b, eleEta_1b, jet1Phi_1b, elePhi_1b)
        h_dR_1b.Fill(dR_jet1_ele_1b)

    for j in range(nEvents_2b):
        tree_2b.GetEntry(j)
        eleEta_2b = getattr(tree_2b, 'leadingLepEta')
        elePhi_2b = getattr(tree_2b, 'leadingLepPhi')
        jet1Eta_2b = getattr(tree_2b, 'Jet1Eta')
        jet1Phi_2b = getattr(tree_2b, 'Jet1Phi')
        dR_jet1_ele_2b = Delta_R(jet1Eta_2b, eleEta_2b, jet1Phi_2b, elePhi_2b)
        h_dR_2b.Fill(dR_jet1_ele_2b)

    return [h_dR_1b, h_dR_2b]

def overlayhisto(dR_histo1, dR_histo2, dR_histo3, is1b, dirPath = "plots"):
    c = PlotTemplates.myCanvas()
    gPad.GetUymax()
    #gPad.SetLogy()
    gStyle.SetOptStat(0)
    gStyle.SetOptTitle(0)
    
    leg = PlotTemplates.SetLegend(coordinate_=[.47,.73,.79,.88])
    
    dR_histo1.SetLineWidth(3)
    dR_histo1.SetMarkerStyle(20)
    dR_histo1.SetMarkerSize(0.5)
    dR_histo1.SetLineColor(1)
    dR_histo1.SetMarkerColor(1)
    dR_histo1.GetXaxis().SetTitle("Delta R")
    dR_histo1.GetYaxis().SetTitle("Events/Bin")
    leg.AddEntry(dR_histo1, "Total (Before Cut)")

    dR_histo2.SetLineWidth(3)
    dR_histo2.SetMarkerStyle(21)
    dR_histo2.SetMarkerSize(0.5)
    dR_histo2.SetLineColor(2)
    dR_histo2.SetMarkerColor(2)
    leg.AddEntry(dR_histo2, "AB (Before Cut)")
    
    dR_histo3.SetLineWidth(3)
    dR_histo3.SetMarkerStyle(22)
    dR_histo3.SetMarkerSize(0.5)
    dR_histo3.SetLineColor(4)
    dR_histo3.SetMarkerColor(4)
    leg.AddEntry(dR_histo3, "CD (Before Cut)")
        
    #dR_histo4.SetLineWidth(3)
    #dR_histo4.SetMarkerStyle(23)
    #dR_histo4.SetMarkerSize(0.5)
    #dR_histo4.SetLineColor(3)
    #dR_histo4.SetMarkerColor(3)
    #dR_histo4.GetXaxis().SetTitle(xAxisName[i])
    #leg.AddEntry(dR_histo4, "CD (After Cut)")
        
    dR_histo1.Draw("hist")
    dR_histo2.Draw("histsame")
    dR_histo3.Draw("histsame")
    #dR_histo4.Draw("histsame")
    leg.Draw()
        
    energy = PlotTemplates.drawenergy(is2017 = False)
    for e in energy:
        e.Draw()
    
    if is1b:
        nb = "1b"
        nb_ext = "1b_dR_jet1_ele"
    if not is1b:
        nb = "2b"
        nb_ext = "2b_dR_jet1_ele"

    pt = TPaveText(0.1577181,0.815,0.3580537,0.875,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(52)
    pt.AddText("Top (e#nu) + "+nb+" CR")
    pt.Draw()

    dt = datetime.now()
    dt_str = dt.strftime("%Y%m%d_%H%M")

    subdirPath = dirPath+"/deltaR"
    subsubdirPath = subdirPath+"/TopenuCR_"+dt_str
    dirPDF = subsubdirPath+"/pdf"
    dirPNG = subsubdirPath+"/png"
    if not (os.path.exists(subdirPath)):
        os.mkdir(subdirPath)
    if not (os.path.exists(subsubdirPath)):
        os.mkdir(subsubdirPath)
    if not (os.path.exists(dirPDF)):
        os.mkdir(dirPDF)
    if not (os.path.exists(dirPNG)):
        os.mkdir(dirPNG)

    c.Update()
    c.Modified()
    c.SaveAs(dirPDF+"/TopenuCR_"+nb_ext+".pdf")
    c.SaveAs(dirPNG+"/TopenuCR_"+nb_ext+".png")


dR_histo_ABCD_bfr = dR_jet_ele(path = path_before, ifile = ABCD, h_dR_1b = h_dR_jet1_ele_1b_ABCD_bfr, h_dR_2b = h_dR_jet1_ele_2b_ABCD_bfr)
dR_histo_AB_bfr = dR_jet_ele(path = path_before, ifile = AB, h_dR_1b = h_dR_jet1_ele_1b_AB_bfr, h_dR_2b = h_dR_jet1_ele_2b_AB_bfr)
dR_histo_CD_bfr = dR_jet_ele(path = path_before, ifile = CD, h_dR_1b = h_dR_jet1_ele_1b_CD_bfr, h_dR_2b = h_dR_jet1_ele_2b_CD_bfr)
#dR_histo_CD_aftr = dR_jet_ele(path = path_after, ifile = CD, h_dR_1b = h_dR_jet1_ele_1b_CD_aftr, h_dR_2b = h_dR_jet1_ele_2b_CD_aftr)

h_1b = overlayhisto(dR_histo1 = dR_histo_ABCD_bfr[0], dR_histo2 = dR_histo_AB_bfr[0], dR_histo3 = dR_histo_CD_bfr[0], is1b = True)
h_2b = overlayhisto(dR_histo1 = dR_histo_ABCD_bfr[1], dR_histo2 = dR_histo_AB_bfr[1], dR_histo3 = dR_histo_CD_bfr[1], is1b = False)
