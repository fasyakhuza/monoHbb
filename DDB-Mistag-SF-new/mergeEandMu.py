#created by Fasya Khuzaimah on 2020.04.17

import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TLegend, TAxis, TLatex, TPad, TPaveText, THStack, TMath, TGraphErrors, TMultiGraph, gStyle, gPad
import array as arr
import numpy as np
import argparse
import DDB_mistagSF


def myCanvas(c, size = [800, 700]):
    c = TCanvas(c, "", size[0], size[1])
    c.SetTopMargin(0.1)
    c.SetBottomMargin(0.15)
    c.SetRightMargin(0.1)
    c.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)
    return c
    
def myLegend(coordinate=[0.45,0.6,0.65,0.75], ncol=1):
    co = coordinate
    leg = TLegend(co[0], co[1], co[2], co[3])
    leg.SetNColumns(ncol)
    leg.SetBorderSize(0)
    leg.SetLineColor(1)
    leg.SetLineStyle(1)
    leg.SetLineWidth(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.03)
    return leg

def myStack(colorlist_, backgroundlist_, legendname_):
    hs = THStack("hs", "")
    leg1 = myLegend()
    for j in range(len(colorlist_)):
        h = backgroundlist_[j]
        h.SetFillColor(colorlist_[j])
        h.SetLineColor(colorlist_[j])
        hs.Add(h, "")
        leg1.AddEntry(h,legendname_[j],"f")
    return [hs, leg1]

def dataPredRatio(data_, totalBkg_):
    dataPredRatio_ = data_ - totalBkg_
    dataPredRatio_.Divide(totalBkg_)
    return dataPredRatio_

def mistagSFtopEMu(year_, isWithST, ana_):
    if isWithST == "True":
        dir = "withSingleTop/"+ana_+"/"
    else:
        dir = "withoutSingleTop/"+ana_+"/"

    print "Top Electron Region"
    print " "

    openfile1 = TFile(dir+"TopE.root")#

    topmatchTopE = openfile1.Get("h_TopMatch")
    WmatchTopE = openfile1.Get("h_Wmatch")
    unmatchTopE = openfile1.Get("h_unmatch")
    wjetsTopE = openfile1.Get("h_sumWJets")
    dibosonTopE = openfile1.Get("h_sumDiboson")
    unsubtractedDataTopE = openfile1.Get("h_Data")

    failMCsubtractTopE = openfile1.Get("h_ttFailed")
    passMCsubtractTopE = openfile1.Get("h_ttPassed")
    subtractedDataTopE = openfile1.Get("SubtractedData")

    datafailTopE = openfile1.Get("SubtractedDataFailed")
    datapassTopE = openfile1.Get("SubtractedDataPassed")#
    totaldataTopE = openfile1.Get("h_totaldata")
    totalMCtopE = openfile1.Get("h_tt")

    passedTopEdataBfrSubtract = openfile1.Get("h_Data_Passed")
    wjetsTopEpassed = openfile1.Get("h_sumWJetsPassed")
    dibosonTopEpassed = openfile1.Get("h_sumDibosonPassed")

    failedTopEdataBfrSubtract = openfile1.Get("h_Data_Failed")
    wjetsTopEfailed = openfile1.Get("h_sumWJetsFailed")
    dibosonTopEfailed = openfile1.Get("h_sumDibosonFailed")

    if isWithST == "True":
        stTopE = openfile1.Get("h_sumST")
        stTopEpassed = openfile1.Get("h_sumSTPassed")
        stTopEfailed = openfile1.Get("h_sumSTFailed")

    print "Top Muon Region"
    print " "

    openfile2 = TFile(dir+"TopMu.root")#

    topmatchTopMu = openfile2.Get("h_TopMatch")
    WmatchTopMu = openfile2.Get("h_Wmatch")
    unmatchTopMu = openfile2.Get("h_unmatch")
    wjetsTopMu = openfile2.Get("h_sumWJets")
    dibosonTopMu = openfile2.Get("h_sumDiboson")
    unsubtractedDataTopMu = openfile2.Get("h_Data")

    failMCsubtractTopMu = openfile2.Get("h_ttFailed")
    passMCsubtractTopMu = openfile2.Get("h_ttPassed")
    subtractedDataTopMu = openfile2.Get("SubtractedData")

    datafailTopMu = openfile2.Get("SubtractedDataFailed")
    datapassTopMu = openfile2.Get("SubtractedDataPassed")#
    totaldataTopMu = openfile2.Get("h_totaldata")
    totalMCtopMu = openfile2.Get("h_tt")

    passedTopMudataBfrSubtract = openfile2.Get("h_Data_Passed")
    wjetsTopMupassed = openfile2.Get("h_sumWJetsPassed")
    dibosonTopMupassed = openfile2.Get("h_sumDibosonPassed")

    failedTopMudataBfrSubtract = openfile2.Get("h_Data_Failed")
    wjetsTopMufailed = openfile2.Get("h_sumWJetsFailed")
    dibosonTopMufailed = openfile2.Get("h_sumDibosonFailed")

    if isWithST == "True":
        stTopMu = openfile2.Get("h_sumST")
        stTopMupassed = openfile2.Get("h_sumSTPassed")
        stTopMufailed = openfile2.Get("h_sumSTFailed")

    print "get histograms from root files: done"
    print " "


    SubtractedDataPassedTopE = datapassTopE.Clone("SubtractedDataPassedTopE")
    SubtractedDataPassedTopMu = datapassTopMu.Clone("SubtractedDataPassedTopMu")


    #merge histogram"
    print "merge histograms"
    print " "


    topmatchMerge = topmatchTopE + topmatchTopMu
    WmatchMerge = WmatchTopE + WmatchTopMu
    unmatchMerge = unmatchTopE + unmatchTopMu
    wjetsMerge = wjetsTopE + wjetsTopMu
    stMerge = stTopE + stTopMu
    dibosonMerge = dibosonTopE + dibosonTopMu
    unsubtractedDataMerge = unsubtractedDataTopE + unsubtractedDataTopMu

    failMCsubtractMerge = failMCsubtractTopE.Clone("failMCsubtractMerge")
    failMCsubtractMerge = failMCsubtractMerge + failMCsubtractTopMu
    passMCsubtractMerge = passMCsubtractTopE.Clone("passMCsubtractMerge")
    passMCsubtractMerge = passMCsubtractMerge + passMCsubtractTopMu
    subtractedDataMerge = subtractedDataTopE + subtractedDataTopMu


    ttData_fraction = arr.array('d')
    ttData_error = arr.array('d')

    totaldataMerge = totaldataTopE + totaldataTopMu
    totaldata = totaldataMerge.Integral()
    totaldataMerge.Rebin(14)

    datafailMerge = datafailTopE + datafailTopMu
    faildata = datafailMerge.Integral()
    datafailMerge.Rebin(14)
    datafailMerge.Sumw2()
    datafailMerge.Divide(totaldataMerge)
    frac_ttData_fail = datafailMerge.Integral()
    ttData_fraction.append(frac_ttData_fail)
    ttData_error.append(datafailMerge.GetBinError(1))

    datapassMerge = datapassTopE + datapassTopMu
    passdata = datapassMerge.Integral()
    datapassMerge.Rebin(14)
    datapassMerge.Sumw2()
    datapassMerge.Divide(totaldataMerge)
    frac_ttData_pass = datapassMerge.Integral()
    ttData_fraction.append(frac_ttData_pass)
    ttData_error.append(datapassMerge.GetBinError(1))



    ttMC_fraction = arr.array('d')
    ttMC_error = arr.array('d')

    totalMCmerge = totalMCtopE + totalMCtopMu
    totalMCmerge.Rebin(14)

    MCfailTopE = failMCsubtractTopE.Clone("MCfailTopE")
    MCfailTopMu = failMCsubtractTopMu.Clone("MCfailTopMu")
    MCfailMerge = MCfailTopE + MCfailTopMu
    MCfailMerge.Rebin(14)
    MCfailMerge.Sumw2()
    MCfailMerge.Divide(totalMCmerge)
    frac_Failed_fin = MCfailMerge.Integral()
    ttMC_fraction.append(frac_Failed_fin)
    ttMC_error.append(MCfailMerge.GetBinError(1))

    MCpassTopE = passMCsubtractTopE.Clone("MCpassTopE")
    MCpassTopMu = passMCsubtractTopMu.Clone("MCpassTopMu")
    MCpassMerge = MCpassTopE + MCpassTopMu
    MCpassMerge.Rebin(14)
    MCpassMerge.Sumw2()
    MCpassMerge.Divide(totalMCmerge)
    frac_Passed_fin = MCpassMerge.Integral()
    ttMC_fraction.append(frac_Passed_fin)
    ttMC_error.append(MCpassMerge.GetBinError(1))

    #print "\nttMC_fraction:", ttMC_fraction
    #print "ttMC_error:", ttMC_error


    sfMerge = datapassMerge.Clone("sfMerge")
    sfMerge.Sumw2()
    sfMerge.Divide(MCpassMerge)

    stacklist = []
    stacklist.append(dibosonMerge)
    if isWithST == "True":
        stacklist.append(stMerge)
    stacklist.append(wjetsMerge)
    stacklist.append(unmatchMerge)
    stacklist.append(WmatchMerge)
    stacklist.append(topmatchMerge)

    print "merge histograms: done"
    print " "


    print "draw histograms"
    print " "
    #----------------------- canvas 1 -----------------------#

    c1 = TCanvas("c1","",800,900) #width-height
    c1.SetTopMargin(0.4)
    c1.SetBottomMargin(0.05)
    c1.SetRightMargin(0.1)
    c1.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)

    padMain = TPad("padMain", "", 0.0, 0.25, 1.0, 0.97)
    padMain.SetTopMargin(0.4)
    padMain.SetRightMargin(0.05)
    padMain.SetLeftMargin(0.17)
    padMain.SetBottomMargin(0.03)
    padMain.SetTopMargin(0.1)

    padRatio = TPad("padRatio", "", 0.0, 0.0, 1.0, 0.25)
    padRatio.SetRightMargin(0.05)
    padRatio.SetLeftMargin(0.17)
    padRatio.SetTopMargin(0.05)
    padRatio.SetBottomMargin(0.3)
    padMain.Draw()
    padRatio.Draw()

    padMain.cd()

    gPad.GetUymax()
    leg1 = myLegend(coordinate=[0.45,0.57,0.65,0.6])

    #unsubtractedDataMerge.SetMaximum(40)#17000
    unsubtractedDataMerge.SetLineColor(1)
    unsubtractedDataMerge.SetMarkerStyle(20)
    unsubtractedDataMerge.SetMarkerSize(1.5)
    unsubtractedDataMerge.GetXaxis().SetLabelSize(0)
    unsubtractedDataMerge.GetXaxis().SetTitleSize(0)
    unsubtractedDataMerge.GetXaxis().SetTitle("Double b score")
    unsubtractedDataMerge.GetYaxis().SetTitle("Events/Bin")
    leg1.AddEntry(unsubtractedDataMerge, "Data", "lep")
    unsubtractedDataMerge.Draw("e1")

    if isWithST == "True":
        stackhisto = myStack(colorlist_ = [627, 800, 854, 813, 822, 821],  backgroundlist_ = stacklist, legendname_ = ["Diboson", "Single Top", "W+Jets", "Top (unmtch.)", "Top (W-mtch.)", "Top (mtch.)"])
    else:
        stackhisto = myStack(colorlist_ = [627, 854, 813, 822, 821],  backgroundlist_ = stacklist, legendname_ = ["Diboson", "W+Jets", "Top (unmtch.)", "Top (W-mtch.)", "Top (mtch.)"])
    stackhisto[0].Draw("histsame")
    unsubtractedDataMerge.Draw("e1same")
    stackhisto[1].Draw()
    leg1.Draw()

    lt = TLatex()
    lt.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    lt.DrawLatexNDC(0.23,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e+#mu)}}")
    lt.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")


    padRatio.cd()

    gPad.GetUymax()

    h_totalBkg = topmatchMerge.Clone("h_totalBkg")
    h_totalBkg = h_totalBkg + WmatchMerge + unmatchMerge + wjetsMerge + dibosonMerge
    ratio = dataPredRatio(data_ = unsubtractedDataMerge, totalBkg_ = h_totalBkg)
    ratio.SetLineColor(1)
    ratio.SetLineWidth(3)
    ratio.SetMarkerSize(1.5)
    ratio.GetXaxis().SetLabelSize(0.13)
    ratio.GetXaxis().SetTitleOffset(1)
    ratio.GetXaxis().SetTitleSize(0.13)
    ratio.GetXaxis().SetTickLength(0.1)
    ratio.GetYaxis().SetLabelSize(0.12)
    ratio.GetYaxis().SetTitleOffset(0.5)
    ratio.GetYaxis().SetTitleSize(0.13)
    ratio.GetYaxis().SetNdivisions(405)
    ratio.GetYaxis().SetTitle("#frac{Data-Pred}{Pred}")
    ratio.GetXaxis().SetTitle("Double b score")
    ratio.Draw("e1")

    c1.SaveAs(dir+"Merge_all.pdf")#


    #----------------------- canvas 2 -----------------------#

    c2 = myCanvas(c = "c2")
    gPad.GetUymax()
    leg2 = myLegend()

    #failMCsubtractMerge.SetMaximum(1800)#1200
    failMCsubtractMerge.SetFillColor(821)
    failMCsubtractMerge.SetLineColor(821)#922
    failMCsubtractMerge.GetXaxis().SetTitle("Double b score")
    failMCsubtractMerge.GetYaxis().SetTitle("Events/Bin")
    leg2.AddEntry(failMCsubtractMerge, "t#bar{t}", "f")

    passMCsubtractMerge.SetFillColor(622)
    passMCsubtractMerge.SetLineColor(622)
    #passMCsubtractMerge.GetXaxis().SetTitle("Double b score")
    #passMCsubtractMerge.GetYaxis().SetTitle("Events/Bin")
    leg2.AddEntry(passMCsubtractMerge, "t#bar{t} mistag", "f")

    subtractedDataMerge.SetLineColor(1)
    subtractedDataMerge.SetMarkerStyle(20)
    subtractedDataMerge.SetMarkerSize(1.5)
    #subtractedDataMerge.GetXaxis().SetTitle("Double b score")
    #subtractedDataMerge.GetYaxis().SetTitle("Events/Bin")
    leg2.AddEntry(subtractedDataMerge, "Subtracted Data", "lep")

    failMCsubtractMerge.Draw("hist")
    passMCsubtractMerge.Draw("histsame")
    subtractedDataMerge.Draw("e1same")
    leg2.Draw()

    lt2 = TLatex()
    lt2.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    lt2.DrawLatexNDC(0.23,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e+#mu)}}")
    lt2.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")

    c2.SaveAs(dir+"Merged_subtrac.pdf")#


    #----------------------- canvas 3 -----------------------#

    c3 = myCanvas(c = "c3", size = [700, 900])

    pad1 = TPad("pad1", "", 0.01, 0.25, 0.93, 1.0)
    pad1.SetTopMargin(0.1)
    pad1.SetRightMargin(0.05)
    pad1.SetLeftMargin(0.17)
    pad1.SetBottomMargin(0.05)

    pad2 = TPad("pad2", "", 0.0, 0.0, 0.375, 0.24)
    pad2.SetTopMargin(0.0)
    pad2.SetRightMargin(0.0)
    pad2.SetLeftMargin(0.0)
    pad2.SetBottomMargin(0.0)

    pad3 = TPad("pad3", "", 0.38, 0.025, 0.94, 0.25)
    pad2.SetTopMargin(0.05)
    pad2.SetRightMargin(0.0)
    pad2.SetLeftMargin(0.45)
    pad2.SetBottomMargin(0.2)

    pad1.Draw()
    pad2.Draw()
    pad3.Draw()

    #* Pad 1 *#
    pad1.cd()
    leg3 = myLegend(coordinate=[0.65,0.4,0.75,0.5])

    xaxisname = arr.array('d', [1, 2])
    zero1 = np.zeros(2)

    gPad.Modified()
    gPad.SetGridy()

    gr1 = TGraphErrors(2, xaxisname, ttMC_fraction, zero1, ttMC_error)
    gr1.SetTitle("t#bar{t}")
    gr1.SetLineColor(870)
    gr1.SetLineWidth(3)
    gr1.SetMarkerStyle(20)
    gr1.SetMarkerColor(870)
    leg3.AddEntry(gr1, "t#bar{t}", "lep")

    gr2 = TGraphErrors(2, xaxisname, ttData_fraction, zero1, ttData_error)
    gr2.SetTitle("t#bar{t} Data")
    gr2.SetLineColor(1)
    gr2.SetLineWidth(2)
    gr2.SetMarkerStyle(20)
    gr2.SetMarkerColor(1)
    leg3.AddEntry(gr2, "t#bar{t} Data", "lep")

    mg = TMultiGraph("mg","")
    mg.Add(gr1)
    mg.Add(gr2)
    mg.GetHistogram().SetMaximum(1.5)
    mg.GetHistogram().SetMinimum(0)
    mg.GetYaxis().SetTitle("Fraction")
    mg.GetXaxis().SetLimits(0,3)
    mg.GetXaxis().SetTickLength(0.03)
    mg.GetXaxis().SetNdivisions(103)
    mg.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Fail")
    mg.GetXaxis().ChangeLabel(1,-1,0)
    mg.GetXaxis().ChangeLabel(-1,-1,0)
    mg.GetXaxis().ChangeLabel(3,-1,-1,-1,-1,-1,"Pass")
    mg.Draw("AP")
    leg3.Draw()

    lt3 = TLatex()
    lt3.DrawLatexNDC(0.19,0.855,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    lt3.DrawLatexNDC(0.19,0.805,"#scale[0.7]{#bf{t#bar{t} CR (e+#mu)}}")
    lt3.DrawLatexNDC(0.19,0.755,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")
    lt3.Draw()

    pad1.Update()

    #* Pad 2 *#
    pad2.cd()

    MCpassMerge.SetFillColor(0)
    MCpassMerge.SetLineColor(870)
    MCpassMerge.SetLineWidth(3)
    MCpassMerge.SetMarkerColor(870)
    MCpassMerge.SetMarkerStyle(20)
    MCpassMerge.GetYaxis().SetTitle("Fraction")
    MCpassMerge.GetYaxis().SetTitleSize(0.09)
    MCpassMerge.GetYaxis().SetLabelSize(0.1)
    MCpassMerge.GetYaxis().SetNdivisions(404)
    MCpassMerge.SetMaximum(0.3)
    MCpassMerge.SetMinimum(0.0)
    MCpassMerge.GetXaxis().SetTitle("")
    MCpassMerge.GetXaxis().SetLabelOffset(0.02)
    MCpassMerge.GetXaxis().SetLabelSize(0.09)
    MCpassMerge.GetXaxis().SetNdivisions(104)
    MCpassMerge.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Pass")
    MCpassMerge.GetXaxis().ChangeLabel(1,-1,0)
    MCpassMerge.GetXaxis().ChangeLabel(-1,-1,0)

    datapassMerge.SetFillColor(0)
    datapassMerge.SetLineColor(1)
    datapassMerge.SetLineWidth(2)
    datapassMerge.SetMarkerColor(1)
    datapassMerge.SetMarkerStyle(20)

    MCpassMerge.Draw("e1")
    datapassMerge.Draw("e1histsame")

    '''
    lt4 = TLatex()
    lt4.DrawLatexNDC(0.4,0.5,"#scale[2.0]{Eff.}")
    lt4.Draw()
    '''

    #* Pad 3 *#
    pad3.cd()

    SF = sfMerge.Integral()
    print "******"
    print "mistag SF:", SF

    SFfinal = round(SF, 3)
    SFtext = "SF = "+str(SFfinal)

    mistagSFmax = SF + 0.2
    mistagSFmin = SF - 0.2

    sfMerge.SetLineColor(797)
    sfMerge.SetMarkerColor(797)
    sfMerge.SetLineWidth(3)
    sfMerge.SetMaximum(mistagSFmax)
    sfMerge.SetMinimum(mistagSFmin)
    sfMerge.GetXaxis().SetTitle(" ")
    sfMerge.GetXaxis().SetLabelOffset(999)
    sfMerge.GetXaxis().SetLabelSize(0)
    sfMerge.GetXaxis().SetTickLength(0)
    sfMerge.GetYaxis().SetLabelSize(0.1)
    sfMerge.GetYaxis().SetNdivisions(404)
    sfMerge.GetYaxis().SetTitle(" ")

    sfMerge.Draw("e1hist")

    pt = TPaveText(0.21, 0.72, 0.31, 0.8, "brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(42)
    pt.SetTextSize(0.1)
    pt.AddText(SFtext)
    pt.Draw()

    c3.SaveAs(dir+"Merge_SF.pdf")#

    passedBfrSubtactDataMerge = (passedTopEdataBfrSubtract + passedTopMudataBfrSubtract).Integral()
    failedBfrSubtractDataMerge = (failedTopEdataBfrSubtract + failedTopMudataBfrSubtract).Integral()

    if isWithST == "True":
        passbackground = (wjetsTopEpassed + wjetsTopMupassed + dibosonTopEpassed + dibosonTopMupassed + stTopEpassed + stTopMupassed).Integral()
        failbackground = (wjetsTopEfailed + wjetsTopMufailed + dibosonTopEfailed + dibosonTopMufailed + stTopEfailed + stTopMufailed).Integral()
        totalbackground = (wjetsMerge + dibosonMerge + stMerge).Integral()
    else:
        passbackground = (wjetsTopEpassed + wjetsTopMupassed + dibosonTopEpassed + dibosonTopMupassed).Integral()
        failbackground = (wjetsTopEfailed + wjetsTopMufailed + dibosonTopEfailed + dibosonTopMufailed).Integral()
        totalbackground = (wjetsMerge+dibosonMerge).Integral()


    #get the statistical uncertainty#

    dx = ttData_error[1]
    print "data efficiency error", dx

    dy = ttMC_error[1]
    print "MC efficiency error", dy

    x = datapassMerge.Integral()
    y = MCpassMerge.Integral()

    statUnc = TMath.Sqrt(( (dx**2)/(y**2) ) + ( (x**2)*(dy**2)/(y**4) ) )
    #print "statistical Uncertainty in Top (e+muon) CR", statUnc
    #print " "
    print "relative statistical Uncertainty in Top (e+muon) CR", statUnc/SF*100, " %"
    print " "

    print "DDB Mistag SF and stat: ", round(SF,3), " +- ", round(statUnc,3), " (stat)"
    #print "theoretical statistical uncertainty of data efficiency", TMath.Sqrt((x*(1-x))/(subtractedDataMerge.Integral()))
    #print "theoretical statistical uncertainty of MC efficiency", TMath.Sqrt((y*(1-y))/(totalMCmerge.Integral()))
    #print " "

    header = ["Process", "Number of Events", "Top (e+muon)"]
    row1 = [" ", "DDB mistag SF", str(SFfinal) + " +- " + str(round(statUnc,3)) + " (stat)"]
    row2 = ["tt MC", "Pass (not normalized)", ""]
    row3 = [" ", "Pass (normalized)", str(round(passMCsubtractMerge.Integral(),2))]
    row4 = [" ", "Fail (not normalized)", ""]
    row5 = [" ", "Fail (normalized)", str(round(failMCsubtractMerge.Integral(),2))]
    row6 = [" ", "Total (not normalized)", ""]
    row7 = [" ", "Total (normalized)", str(round(totalMCmerge.Integral(),2))]
    
    inforMC = [row2, row3, row4, row5, row6, row7]
    
    row8 = ["tt DATA", "Pass (before subtraction)", str(round(passedBfrSubtactDataMerge,2))]
    row9 = [" ", "Pass (after subtraction)", str(round(passdata,2))]
    row10 = [" ", "Fail (before subtraction)", str(round(failedBfrSubtractDataMerge,2))]
    row11 = [" ", "Fail (after subtraction)", str(round(faildata,2))]
    row12 = [" ", "Total (before subtraction)", str(round(unsubtractedDataMerge.Integral(),2))]
    row13 = [" ", "Total (after subtraction)", str(round(totaldata,2))]
    
    inforDATA = [row8, row9, row10, row11, row12, row13]
    
    row14 = ["Background", "Pass (normalized)", str(round(passbackground,2))]
    row15 = [" ", "Fail (normalized)", str(round(failbackground,2))]
    row16 = [" ", "Total (normalized)", str(round(totalbackground,2))]
    
    inforBKG = [row14, row15, row16]
    
    DDB_mistagSF.makeTable(header, row1, inforMC, inforDATA, inforBKG)
                                      

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate and draw plots of DDB mistag scale factor for Top (e+muon) CR')
    
    #add command
    parser.add_argument('-Y', dest='discrepancy', help='Add the year of the data set')
    parser.add_argument('-isWithST', help='Analyze whether Top (e) or Top (mu) region')
    parser.add_argument('-a', help='Write the analysis range you want to calculate')
    
    #Get arguments from the user
    args = parser.parse_args()
    
    if args.discrepancy:
        if args.isWithST:
            if args.a:
                mistagSFtopEMu(int(args.discrepancy), args.isWithST, args.a)




'''
#get the SFnew = SFold = SF

Ndp = (passedTopEdata + passedTopMudata).Integral()
Nsdt = subtractedDataMerge.Integral()
Nbp = (wjetsTopEpassed + wjetsTopMupassed + dibosonTopEpassed + dibosonTopMupassed).Integral()
frac_Passed = MCpassMerge.Integral()

SFno = Ndp/(frac_Passed*Nsdt+Nbp)
print "SFnew = SFold = SF =", SFno
'''
