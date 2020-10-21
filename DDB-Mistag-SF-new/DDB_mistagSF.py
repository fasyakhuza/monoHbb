#created by Fasya Khuzaimah on 2020.04.17

import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TLegend, TAxis, TLatex, TPad, TPaveText, TMath, TGraphErrors, TMultiGraph, gStyle, gPad, gROOT
import array as arr
import numpy as np
import argparse
import os


def dataPredRatio(data_, totalBkg_):
    dataPredRatio_ = data_ - totalBkg_
    dataPredRatio_.Divide(totalBkg_)
    return dataPredRatio_

def fixed_length(text, length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " "*length)[:length]
    return text

def makeTable(header, row1, inforMC, inforDATA, inforBKG):
    hashtaglength = 91
    length = 25
    
    #print header
    print "#"*hashtaglength
    print "# ",
    for column in header:
        print fixed_length(column,length), " # ",
    print ""
    print "#"*hashtaglength
        
    #print scale factor
    print "# ",
    for column in row1:
        print fixed_length(column,length), " # ",
    print ""
    print "#"*hashtaglength
        
    #print tt MC
    for row in inforMC:
        print "# ",
        for column in row:
            print fixed_length(column,length), " # ",
        print ""
    print "#"*hashtaglength
        
    #print tt DATA
    for row in inforDATA:
        print "# ",
        for column in row:
            print fixed_length(column,length), " # ",
        print ""
    print "#"*hashtaglength
    
    #print Background
    for row in inforBKG:
        print "# ",
        for column in row:
            print fixed_length(column,length), " # ",
        print ""
    print "#"*hashtaglength

def yearandversion(year_):
    if year_ == 2017:
        L = 41500.0#/pb ; integrated luminosity
        version = "monohbb.v06.00.05.2017_NCU/"
        inputdirpath = "/afs/cern.ch/work/f/fkhuzaim/DDB_MistagSF/"+version+"combined/"
    if year_ == 2018:
        L = 58827.0#/pb ; integrated luminosity
        version = "monohbb.v06.00.05.2018_NCU/"
        inputdirpath = "/afs/cern.ch/work/f/fkhuzaim/DDB_MistagSF/"+version+"combined/"
    outdir ="/afs/cern.ch/work/f/fkhuzaim/DDB_MistagSF/new_output/"+version
    return [L, inputdirpath, outdir]

#print "Top Electron Region"
#print " "

nbins = 14
edges = arr.array('f', [0.0, 0.08, 0.16, 0.23, 0.30, 0.37, 0.44, 0.51, 0.58, 0.65, 0.72, 0.79, 0.86, 0.93, 1.0])

ttMC_fraction = arr.array('d')
ttMC_error = arr.array('d')
ttData_fraction = arr.array('d')
ttData_error = arr.array('d')



def withSingleTopAndInclusive(x, year_, isTope):
    if isTope == "True":
        print "Top (e) Control Region"
    else:
        print "Top (mu) Control Region"
    print "Running With Single Top for Inclusive Analysis of " + str(year_) + " Data"
    print ""
    
    vers = yearandversion(year_)
    
    outdirtype = "withSingleTop/"
    outputpath = vers[2]+outdirtype+x+"/"
    if not os.path.exists(vers[2]):
        os.mkdir(vers[2])
    if not os.path.exists(vers[2]+outdirtype):
        os.mkdir(vers[2]+outdirtype)
    if not os.path.exists(outputpath):
        os.mkdir(outputpath)
    
    #totalmax = 1500
    #ttmax = 800


    #---------------------------------#
    #         TTtoSemileptonic        #
    #---------------------------------#
    
    if year_ == 2017:
        Top_path = vers[1]+"combined_crab_TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root"
    if year_ == 2018:
        Top_path = vers[1]+"combined_crab_TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8.root"
    
    xsTop = 300.9498
    
    h_TopMatch = TH1F("h_TopMatch", "", nbins, edges)
    h_Wmatch = TH1F("h_Wmatch", "", nbins, edges)
    h_unmatch = TH1F("h_unmatch", "", nbins, edges)
    h_ttFailed = TH1F("h_ttFailed", "", nbins, edges)
    h_ttPassed = TH1F("h_ttPassed", "", nbins, edges)
    h_ttPassed_Match = TH1F("h_ttPassed_Match", "", nbins, edges)
    h_ttPassed_Wmatch = TH1F("h_ttPassed_Wmatch", "", nbins, edges)
    h_ttPassed_unmatch = TH1F("h_ttPassed_unmatch", "", nbins, edges)
    
    openTop = TFile(Top_path, "read")
    h_total_mcweight_Top = openTop.Get("h_total_mcweight")
    totalEventsTop = h_total_mcweight_Top.Integral()
    if isTope == "True":
        treeTop = openTop.Get("monoHbb_Tope_boosted")
    else:
        treeTop = openTop.Get("monoHbb_Topmu_boosted")
    EventsTop = treeTop.GetEntries()
    
    for i in range(EventsTop):
        treeTop.GetEntry(i)
        st_TopMatching = getattr(treeTop, 'st_TopMatching')
        CSV_Top = getattr(treeTop, 'FJetCSV')
        SD_Top = getattr(treeTop, 'FJetMass')
        dPhi_Top = getattr(treeTop, 'min_dPhi')
        nJets_Top = getattr(treeTop, 'nJets')
        pt_Top = getattr(treeTop, 'FJetPt')
        met_Top = getattr(treeTop, 'MET')
        if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0):
            h_TopMatch.Fill(CSV_Top)
        if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0):
            h_Wmatch.Fill(CSV_Top)
        if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0):
            h_unmatch.Fill(CSV_Top)
        if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86):
            h_ttPassed.Fill(CSV_Top)
        if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top <= 0.86):
            h_ttFailed.Fill(CSV_Top)
        if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86):
            h_ttPassed_Match.Fill(CSV_Top)
        if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86):
            h_ttPassed_Wmatch.Fill(CSV_Top)
        if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86):
            h_ttPassed_unmatch.Fill(CSV_Top)

    ttMCpassNotNormalized = h_ttPassed.Integral()
    ttMCfailNotNormalized = h_ttFailed.Integral()
    ttMCtotalNotNormalized = ttMCpassNotNormalized + ttMCfailNotNormalized
    
    h_TopMatch = h_TopMatch*(vers[0]*xsTop/totalEventsTop)
    h_Wmatch = h_Wmatch*(vers[0]*xsTop/totalEventsTop)
    h_unmatch = h_unmatch*(vers[0]*xsTop/totalEventsTop)
    h_ttFailed = h_ttFailed*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed = h_ttPassed*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_Match = h_ttPassed_Match*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_Wmatch = h_ttPassed_Wmatch*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_unmatch = h_ttPassed_unmatch*(vers[0]*xsTop/totalEventsTop)
    
    h_tt = h_ttFailed.Clone("h_tt")
    h_tt = h_tt + h_ttPassed
    frac_match = (h_TopMatch.Integral())/(h_tt.Integral())*100
    frac_Wmatch = (h_Wmatch.Integral())/(h_tt.Integral())*100
    frac_unmatch = (h_unmatch.Integral())/(h_tt.Integral())*100
    frac_ttPassedMatch = (h_ttPassed_Match.Integral())/(h_tt.Integral())*100
    frac_ttPassedWmatch = (h_ttPassed_Wmatch.Integral())/(h_tt.Integral())*100
    frac_ttPassedUnmatch = (h_ttPassed_unmatch.Integral())/(h_tt.Integral())*100
    
    
    
    #---------------------------------#
    #              W+Jets             #
    #---------------------------------#
    
    WJets_files = ["combined_crab_WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root"]
    
    xsWJets = [1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001]
    
    h_WJets = TH1F("h_WJets", "", nbins, edges)
    h_WJetsPassed = TH1F("h_WJetsPassed", "", nbins, edges)
    h_WJetsFailed = TH1F("h_WJetsFailed", "", nbins, edges)
    
    h_sumWJets = TH1F("h_sumWJets", "", nbins, edges)
    h_sumWJetsPassed = TH1F("h_sumWJetsPassed", "", nbins, edges)
    h_sumWJetsFailed = TH1F("h_sumWJetsFailed", "", nbins, edges)

    
    for k in range(len(WJets_files)):
        h_WJets.Reset()
        h_WJetsPassed.Reset()
        h_WJetsFailed.Reset()
        
        openWJets = TFile(vers[1]+WJets_files[k], "read")
        h_total_mcweight_WJets = openWJets.Get("h_total_mcweight")
        totalEventsWJets = h_total_mcweight_WJets.Integral()
        if isTope == "True":
            treeWJets = openWJets.Get("monoHbb_Tope_boosted")
        else:
            treeWJets = openWJets.Get("monoHbb_Topmu_boosted")
        EventsWJets = treeWJets.GetEntries()
        
        for i in range(EventsWJets):
            treeWJets.GetEntry(i)
            CSV_WJets = getattr(treeWJets, 'FJetCSV')
            SD_WJets = getattr(treeWJets, 'FJetMass')
            dPhi_WJets = getattr(treeWJets, 'min_dPhi')
            nJets_WJets = getattr(treeWJets, 'nJets')
            pt_WJets = getattr(treeWJets, 'FJetPt')
            met_WJets = getattr(treeWJets, 'MET')
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0):
                h_WJets.Fill(CSV_WJets)
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0) and (CSV_WJets > 0.86):
                h_WJetsPassed.Fill(CSV_WJets)
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0) and (CSV_WJets <= 0.86):
                h_WJetsFailed.Fill(CSV_WJets)
    
        h_WJets = h_WJets*(vers[0]*xsWJets[k]/totalEventsWJets)
        h_WJetsPassed = h_WJetsPassed*(vers[0]*xsWJets[k]/totalEventsWJets)
        h_WJetsFailed = h_WJetsFailed*(vers[0]*xsWJets[k]/totalEventsWJets)
        
        h_sumWJets += h_WJets
        h_sumWJetsPassed += h_WJetsPassed
        h_sumWJetsFailed += h_WJetsFailed



    #---------------------------------#
    #              Diboson             #
    #---------------------------------#

    Diboson_files = ["combined_crab_ZZ_TuneCP5_13TeV-pythia8.root", "combined_crab_WW_TuneCP5_13TeV-pythia8.root", "combined_crab_WZ_TuneCP5_13TeV-pythia8.root"]

    xsDiboson = [12.14, 75.8, 27.6]

    h_Diboson = TH1F("h_Diboson", "", nbins, edges)
    h_DibosonPassed = TH1F("h_DibosonPassed", "", nbins, edges)
    h_DibosonFailed = TH1F("h_DibosonFailed", "", nbins, edges)

    h_sumDiboson = TH1F("h_sumDiboson", "", nbins, edges)
    h_sumDibosonPassed = TH1F("h_sumDibosonPassed", "", nbins, edges)
    h_sumDibosonFailed = TH1F("h_sumDibosonFailed", "", nbins, edges)

    
    for k in range(len(Diboson_files)):
        h_Diboson.Reset()
        h_DibosonPassed.Reset()
        h_DibosonFailed.Reset()
        
        openDiboson = TFile(vers[1]+Diboson_files[k], "read")
        h_total_mcweight_Diboson = openDiboson.Get("h_total_mcweight")
        totalEventsDiboson = h_total_mcweight_Diboson.Integral()
        if isTope == "True":
            treeDiboson = openDiboson.Get("monoHbb_Tope_boosted")
        else:
            treeDiboson = openDiboson.Get("monoHbb_Topmu_boosted")
        EventsDiboson = treeDiboson.GetEntries()
        
        for i in range(EventsDiboson):
            treeDiboson.GetEntry(i)
            CSV_Diboson = getattr(treeDiboson, 'FJetCSV')
            SD_Diboson = getattr(treeDiboson, 'FJetMass')
            dPhi_Diboson = getattr(treeDiboson, 'min_dPhi')
            nJets_Diboson = getattr(treeDiboson, 'nJets')
            pt_Diboson = getattr(treeDiboson, 'FJetPt')
            met_Diboson = getattr(treeDiboson, 'MET')
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0):
                h_Diboson.Fill(CSV_Diboson)
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0) and (CSV_Diboson > 0.86):
                h_DibosonPassed.Fill(CSV_Diboson)
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0) and (CSV_Diboson <= 0.86):
                h_DibosonFailed.Fill(CSV_Diboson)
    
        h_Diboson = h_Diboson*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        h_DibosonPassed = h_DibosonPassed*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        h_DibosonFailed = h_DibosonFailed*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        
        h_sumDiboson += h_Diboson
        h_sumDibosonPassed += h_DibosonPassed
        h_sumDibosonFailed += h_DibosonFailed




    #---------------------------------#
    #              Single t           #
    #---------------------------------#
    
    if year_ == 2017:
        ST_files = ["combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]
    if year_ == 2018:
        ST_files = ["combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]

    xsST = [3.74, 67.91, 113.3, 34.97, 34.91]

    h_ST = TH1F("h_ST", "", nbins, edges)
    h_STPassed = TH1F("h_STPassed", "", nbins, edges)
    h_STFailed = TH1F("h_STFailed", "", nbins, edges)

    h_sumST = TH1F("h_sumST", "", nbins, edges)
    h_sumSTPassed = TH1F("h_sumSTPassed", "", nbins, edges)
    h_sumSTFailed = TH1F("h_sumSTFailed", "", nbins, edges)

    for k in range(len(ST_files)):
        h_ST.Reset()
        h_STPassed.Reset()
        h_STFailed.Reset()
        
        openST = TFile(vers[1]+ST_files[k], "read")
        h_total_mcweight_ST = openST.Get("h_total_mcweight")
        totalEventsST = h_total_mcweight_ST.Integral()
        if isTope == "True":
            treeST = openST.Get("monoHbb_Tope_boosted")
        else:
            treeST = openST.Get("monoHbb_Topmu_boosted")
        EventsST = treeST.GetEntries()
        
        for i in range(EventsST):
            treeST.GetEntry(i)
            CSV_ST = getattr(treeST, 'FJetCSV')
            SD_ST = getattr(treeST, 'FJetMass')
            dPhi_ST = getattr(treeST, 'min_dPhi')
            nJets_ST = getattr(treeST, 'nJets')
            pt_ST = getattr(treeST, 'FJetPt')
            met_ST = getattr(treeST, 'MET')
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (nJets_ST <= 2):
                h_ST.Fill(CSV_ST)
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (CSV_ST > 0.86) and (nJets_ST <= 2):
                h_STPassed.Fill(CSV_ST)
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (CSV_ST <= 0.86) and (nJets_ST <= 2):
                h_STFailed.Fill(CSV_ST)

        h_ST = h_ST*(vers[0]*xsST[k]/totalEventsST)
        h_STPassed = h_STPassed*(vers[0]*xsST[k]/totalEventsST)
        h_STFailed = h_STFailed*(vers[0]*xsST[k]/totalEventsST)
        
        h_sumST += h_ST
        h_sumSTPassed += h_STPassed
        h_sumSTFailed += h_STFailed


    #---------------------------------#
    #               DATA              #
    #---------------------------------#

    if isTope == "True":
        Data_path = vers[1]+"combined_data_SE.root"
    else:
        Data_path = vers[1]+"combined_data_MET.root"

    h_Data = TH1F("h_Data", "", nbins, edges)
    h_Data_Failed = TH1F("h_Data_Failed", "", nbins, edges)
    h_Data_Passed = TH1F("h_Data_Passed", "", nbins, edges)

    openData = TFile(Data_path, "read")
    h_total_mcweight_Data = openData.Get("h_total_mcweight")
    totalEventsData = h_total_mcweight_Data.Integral()
    if isTope == "True":
        treeData = openData.Get("monoHbb_Tope_boosted")
    else:
        treeData = openData.Get("monoHbb_Topmu_boosted")
    EventsData = treeData.GetEntries()

    for i in range(EventsData):
        treeData.GetEntry(i)
        CSV_Data = getattr(treeData, 'FJetCSV')
        SD_Data = getattr(treeData, 'FJetMass')
        dPhi_Data = getattr(treeData, 'min_dPhi')
        nJets_Data = getattr(treeData, 'nJets')
        pt_Data = getattr(treeData, 'FJetPt')
        met_Data = getattr(treeData, 'MET')
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0):
            h_Data.Fill(CSV_Data)
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0) and (CSV_Data > 0.86):
            h_Data_Passed.Fill(CSV_Data)
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0) and (CSV_Data <= 0.86):
            h_Data_Failed.Fill(CSV_Data)

    SubtractedData = h_Data.Clone("SubtractedData")
    SubtractedData = SubtractedData - (h_sumWJets + h_sumDiboson + h_sumST)
    SubtractedDataPassed = h_Data_Passed.Clone("SubtractedDataPassed")
    SubtractedDataPassed = SubtractedDataPassed - (h_sumWJetsPassed + h_sumDibosonPassed + h_sumSTPassed)
    SubtractedDataFailed = h_Data_Failed.Clone("SubtractedDataFailed")
    SubtractedDataFailed = SubtractedDataFailed - (h_sumWJetsFailed + h_sumDibosonFailed + h_sumSTFailed)

    h_totaldata = SubtractedDataPassed.Clone("h_totaldata")
    h_totaldata = h_totaldata + SubtractedDataFailed
    frac_tt_data_passed = (SubtractedDataPassed.Integral())/(h_totaldata.Integral())
    frac_tt_data_failed = (SubtractedDataFailed.Integral())/(h_totaldata.Integral())*100

            
    
    #------------Overlap histograms in Full Canvas-------------#
    
    frac_match_text = str(round(frac_match, 2))
    frac_Wmatch_text = str(round(frac_Wmatch, 2))
    frac_unmatch_text = str(round(frac_unmatch, 2))
    
    
    h_TopMatchFinal = h_TopMatch.Clone("h_TopMatchFinal")
    h_WmatchFinal = h_Wmatch.Clone("h_WmatchFinal")
    h_unmatchFinal = h_unmatch.Clone("h_unmatchFinal")
    h_sumWJetsFinal = h_sumWJets.Clone("h_sumWJetsFinal")
    h_sumSTFinal = h_sumST.Clone("h_sumSTFinal")
    
    h_sumSTFinal = h_sumSTFinal + h_sumDiboson
    h_sumWJetsFinal = h_sumWJetsFinal + h_sumSTFinal
    h_unmatchFinal = h_unmatchFinal + h_sumWJetsFinal
    h_WmatchFinal = h_WmatchFinal + h_unmatchFinal
    h_TopMatchFinal = h_TopMatchFinal + h_WmatchFinal
    
    
    full = TCanvas("full","",800,900) #width-height
    full.SetTopMargin(0.4)
    full.SetBottomMargin(0.05)
    full.SetRightMargin(0.1)
    full.SetLeftMargin(0.15)
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
    
    leg = TLegend(0.65,0.7,0.85,0.87)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.027)
    
    binvalues1 = []
    for i in range(nbins):
        binvalue = h_Data.GetBinContent(i)
        binvalues1.append(binvalue)
    totalmax = max(binvalues1) + 100
    
    padMain.cd()
    
    h_TopMatchFinal.SetFillColor(821)
    h_TopMatchFinal.SetLineColor(821)#923
    h_TopMatchFinal.GetXaxis().SetTitle("DDB")
    h_TopMatchFinal.GetXaxis().SetLabelSize(0)
    h_TopMatchFinal.GetYaxis().SetTitle("Events/Bin")
    h_TopMatchFinal.GetYaxis().SetTitleSize(0.05)
    h_TopMatchFinal.GetYaxis().SetLabelSize(0.05)
    h_TopMatchFinal.SetMaximum(totalmax)
    leg.AddEntry(h_TopMatchFinal, "Top (mtch.) ("+frac_match_text+"%)", "f")
    
    h_WmatchFinal.SetFillColor(822)
    h_WmatchFinal.SetLineColor(822)
    leg.AddEntry(h_WmatchFinal, "Top (W-mtch.) ("+frac_Wmatch_text+"%)","f")
    
    h_unmatchFinal.SetFillColor(813)
    h_unmatchFinal.SetLineColor(813)
    leg.AddEntry(h_unmatchFinal, "Top (unmtch.) ("+frac_unmatch_text+"%)","f")
    
    h_sumWJetsFinal.SetFillColor(854)
    h_sumWJetsFinal.SetLineColor(854)
    leg.AddEntry(h_sumWJetsFinal, "W+Jets","f")
    
    h_sumSTFinal.SetFillColor(800)
    h_sumSTFinal.SetLineColor(800)
    leg.AddEntry(h_sumSTFinal, "Single Top","f")
    
    h_sumDiboson.SetFillColor(627)
    h_sumDiboson.SetLineColor(627)
    leg.AddEntry(h_sumDiboson, "Diboson","f")
    
    h_Data.SetLineColor(1)
    h_Data.SetMarkerStyle(20)
    h_Data.SetMarkerSize(1.5)
    leg.AddEntry(h_Data, "Data", "lep")
    
    #-------Draw Histogram in Full Canvas---------#
    
    h_TopMatchFinal.Draw("hist")
    h_WmatchFinal.Draw("histsame")
    h_unmatchFinal.Draw("histsame")
    h_sumWJetsFinal.Draw("histsame")
    h_sumSTFinal.Draw("histsame")
    h_sumDiboson.Draw("histsame")
    h_Data.Draw("e1same")
    leg.Draw()
    
    lt = TLatex()
    lt.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{Inclusive}}")
    lt.DrawLatexNDC(0.24,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt.DrawLatexNDC(0.24,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")
    
    
    padRatio.cd()
    
    gPad.GetUymax()
    
    totalData = h_Data.Clone("totalData")
    ratio = dataPredRatio(data_ = totalData, totalBkg_ = h_TopMatchFinal)
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
    ratio.GetXaxis().SetTitle("DDB")
    ratio.Draw("e1")
    
    #full.cd()
    full.Modified()
    full.Update()
    if isTope == "True":
        full.SaveAs(outputpath+"Tope_unsubtracted.pdf")
    else:
        full.SaveAs(outputpath+"Topmu_unsubtracted.pdf")


    #------------Overlap histograms in Subtract Canvas-------------#

    Cloned_frac_tt = h_tt.Clone("Cloned_frac_tt")
    Cloned_frac_tt.Rebin(14)
    Cloned_frac_ttFailed = h_ttFailed.Clone("Cloned_frac_ttFailed")
    Cloned_frac_ttFailed.Rebin(14)
    Cloned_frac_ttFailed.Sumw2()
    Cloned_frac_ttFailed.Divide(Cloned_frac_tt)
    frac_Failed_fin = Cloned_frac_ttFailed.Integral()
    ttMC_fraction.append(frac_Failed_fin)
    ttMC_error.append(Cloned_frac_ttFailed.GetBinError(1))


    Cloned_frac_ttPassed = h_ttPassed.Clone("Cloned_frac_ttPassed")
    Cloned_frac_ttPassed.Rebin(14)
    Cloned_frac_ttPassed.Sumw2()
    Cloned_frac_ttPassed.Divide(Cloned_frac_tt)
    frac_Passed_fin = Cloned_frac_ttPassed.Integral()
    ttMC_fraction.append(frac_Passed_fin)
    ttMC_error.append(Cloned_frac_ttPassed.GetBinError(1))


    Cloned_frac_tt_data_total = h_totaldata.Clone("Cloned_frac_tt_data_total")
    Cloned_frac_tt_data_total.Rebin(14)
    Cloned_frac_tt_data_failed = SubtractedDataFailed.Clone("Cloned_frac_tt_data_failed")
    Cloned_frac_tt_data_failed.Rebin(14)
    Cloned_frac_tt_data_failed.Sumw2()
    Cloned_frac_tt_data_failed.Divide(Cloned_frac_tt_data_total)
    frac_ttData_fail = Cloned_frac_tt_data_failed.Integral()
    ttData_fraction.append(frac_ttData_fail)
    ttData_error.append(Cloned_frac_tt_data_failed.GetBinError(1))


    Cloned_frac_tt_data_passed = SubtractedDataPassed.Clone("Cloned_frac_tt_data_passed")
    Cloned_frac_tt_data_passed.Rebin(14)
    Cloned_frac_tt_data_passed.Sumw2()
    Cloned_frac_tt_data_passed.Divide(Cloned_frac_tt_data_total)
    frac_ttData_pass = Cloned_frac_tt_data_passed.Integral()
    ttData_fraction.append(frac_ttData_pass)
    ttData_error.append(Cloned_frac_tt_data_passed.GetBinError(1))

    frac_Passed_text = str(round(frac_Passed_fin*100, 2))

    subtract = TCanvas("subtract","",900,700) #width-height
    subtract.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)

    leg2 = TLegend(0.4,0.5,0.6,0.6)
    leg2.SetBorderSize(0)
    leg2.SetTextSize(0.027)

    binvalues2 = []
    for i in range(nbins):
        binvalue = SubtractedData.GetBinContent(i)
        binvalues2.append(binvalue)
    ttmax = max(binvalues2) + 50

    #h_ttFailed.Rebin(2)
    h_ttFailed.SetFillColor(821)
    h_ttFailed.SetLineColor(821)#922
    h_ttFailed.GetXaxis().SetTitle("DDB")
    h_ttFailed.GetYaxis().SetTitle("Events/Bin")
    h_ttFailed.SetMaximum(ttmax)
    leg2.AddEntry(h_ttFailed, "t#bar{t}", "f")

    #h_ttPassed.Rebin(2)
    h_ttPassed.SetFillColor(622)
    h_ttPassed.SetLineColor(622)
    h_ttPassed.GetXaxis().SetTitle("DDB")
    h_ttPassed.GetYaxis().SetTitle("Events/Bin")
    h_ttPassed.SetMaximum(ttmax)
    leg2.AddEntry(h_ttPassed, "t#bar{t} mistag ("+frac_Passed_text+"%)", "f")

    #SubtractedData.Rebin(2)
    SubtractedData.SetLineColor(1)
    SubtractedData.SetMarkerStyle(20)
    SubtractedData.SetMarkerSize(1.5)
    SubtractedData.GetXaxis().SetTitle("DDB")
    SubtractedData.GetYaxis().SetTitle("Events/Bin")
    leg2.AddEntry(SubtractedData, "Subtracted Data", "lep")

    #-------Draw Histogram in Subtract Canvas---------#

    h_ttFailed.Draw("hist")
    h_ttPassed.Draw("histsame")
    SubtractedData.Draw("e1same")
    leg2.Draw()

    lt2 = TLatex()
    lt2.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{Inclusive}}")
    lt2.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt2.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt2.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt2.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")

    #subtract.cd()
    subtract.Modified()
    subtract.Update()
    if isTope == "True":
        subtract.SaveAs(outputpath+"Tope_subtracted.pdf")
    else:
        subtract.SaveAs(outputpath+"Topmu_subtracted.pdf")



    #** MISTAG SCALE FACTOR **#

    SF = frac_tt_data_passed / frac_Passed_fin
    print " "
    print "DDB Mistag SF :", SF
    print " "



    #------------Overlap histograms in Scalefactor Canvas-------------#
    
    scalefactor = TCanvas("scalefactor","", 700, 900)
    scalefactor.SetTopMargin(0.1)
    scalefactor.SetBottomMargin(0.15)
    scalefactor.SetRightMargin(0.1)
    scalefactor.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)

    pad1 = TPad("pad1", "", 0.01, 0.25, 0.93, 1.0)
    pad1.SetTopMargin(0.1)
    pad1.SetRightMargin(0.05)
    pad1.SetLeftMargin(0.17)
    pad1.SetBottomMargin(0.05)

    pad2 = TPad("pad2", "", 0.0, 0.0, 0.375, 0.24)
    pad2.SetTopMargin(0.0)
    pad2.SetRightMargin(0.1)
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

    #** Pad1 **#
    pad1.cd()

    leg3 = TLegend(0.5,0.55,0.7,0.65)
    leg3.SetBorderSize(0)
    leg3.SetTextSize(0.027)

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
    mg.Draw("AP")
    mg.GetHistogram().SetMaximum(1.5)
    mg.GetHistogram().SetMinimum(0)
    mg.GetHistogram().GetYaxis().SetTitle("Fraction")
    gPad.Modified()
    mg.GetXaxis().SetLimits(0,3)
    mg.GetXaxis().SetTickLength(0.03)
    mg.GetXaxis().SetNdivisions(103)
    mg.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Fail")
    mg.GetXaxis().ChangeLabel(1,-1,0)
    mg.GetXaxis().ChangeLabel(-1,-1,0)
    mg.GetXaxis().ChangeLabel(3,-1,-1,-1,-1,-1,"Pass")
    leg3.Draw()

    lt3 = TLatex()
    lt3.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{Inclusive}}")
    lt3.DrawLatexNDC(0.19,0.855,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt3.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt3.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt3.DrawLatexNDC(0.19,0.755,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")
    lt3.Draw()

    pad1.Update()

    #** Pad2 **#
    pad2.cd()

    Cloned_frac_ttPassed.SetLineColor(870)
    Cloned_frac_ttPassed.SetLineWidth(3)
    Cloned_frac_ttPassed.SetMarkerColor(870)
    Cloned_frac_ttPassed.SetMarkerStyle(20)
    Cloned_frac_ttPassed.GetYaxis().SetTitle("Fraction")
    Cloned_frac_ttPassed.GetYaxis().SetTitleSize(0.09)
    Cloned_frac_ttPassed.GetYaxis().SetLabelSize(0.1)
    Cloned_frac_ttPassed.GetYaxis().SetNdivisions(404)
    Cloned_frac_ttPassed.SetMaximum(0.3)#0.3
    Cloned_frac_ttPassed.SetMinimum(0.0)#0.0
    Cloned_frac_ttPassed.GetXaxis().SetTitle("")
    Cloned_frac_ttPassed.GetXaxis().SetLabelSize(0.09)
    Cloned_frac_ttPassed.GetXaxis().SetLabelOffset(0.02)
    Cloned_frac_ttPassed.GetXaxis().SetNdivisions(104)
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Pass")
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(1,-1,0)
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(-1,-1,0)

    Cloned_frac_tt_data_passed.SetLineColor(1)
    Cloned_frac_tt_data_passed.SetLineWidth(2)
    Cloned_frac_tt_data_passed.SetMarkerColor(1)
    Cloned_frac_tt_data_passed.SetMarkerStyle(20)

    Cloned_frac_ttPassed.Draw("e1")
    Cloned_frac_tt_data_passed.Draw("e1histsame")


    #** Pad3 **#
    pad3.cd()

    mistagSF = Cloned_frac_tt_data_passed.Clone("mistagSF")
    mistagSF.Sumw2()
    mistagSF.Divide(Cloned_frac_ttPassed)

    #print "******"
    #print "mistag SF:", mistagSF.Integral()

    SFfinal = round(SF, 3)
    SFtext = "SF = "+str(SFfinal)

    mistagSFmax = SF + 0.2
    mistagSFmin = SF - 0.2

    mistagSF.SetLineColor(797)
    mistagSF.SetMarkerColor(797)
    mistagSF.SetLineWidth(3)
    mistagSF.SetMaximum(mistagSFmax)
    mistagSF.SetMinimum(mistagSFmin)
    mistagSF.GetXaxis().SetTitle(" ")
    mistagSF.GetXaxis().SetLabelOffset(999)
    mistagSF.GetXaxis().SetLabelSize(0)
    mistagSF.GetXaxis().SetTickLength(0)
    mistagSF.GetYaxis().SetLabelSize(0.1)
    mistagSF.GetYaxis().SetNdivisions(404)
    mistagSF.GetYaxis().SetTitle(" ")

    mistagSF.Draw("e1hist")

    pt = TPaveText(0.21, 0.72, 0.31, 0.8, "brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(42)
    pt.SetTextSize(0.1)
    pt.AddText(SFtext)
    pt.Draw()

    scalefactor.Modified()
    scalefactor.Update()
    if isTope == "True":
        scalefactor.SaveAs(outputpath+"Tope_SF.pdf")
    else:
        scalefactor.SaveAs(outputpath+"Topmu_SF.pdf")

    
    
    # Save the canvases in root file #

    if isTope == "True":
        print "\nGenerating TopE.root"

        outfile = TFile(outputpath+"TopE.root", "RECREATE")
    else:
        print "\nGenerating TopMu.root"
        
        outfile = TFile(outputpath+"TopMu.root", "RECREATE")
    h_TopMatch.Write()
    h_Wmatch.Write()
    h_unmatch.Write()
    h_sumWJets.Write()
    h_sumDiboson.Write()
    h_sumST.Write()
    h_Data.Write()

    h_ttFailed.Write()
    h_ttPassed.Write()
    SubtractedData.Write()

    SubtractedDataFailed.Write()
    SubtractedDataPassed.Write()
    h_totaldata.Write()
    h_tt.Write()

    h_Data_Passed.Write()
    h_sumWJetsPassed.Write()
    h_sumDibosonPassed.Write()
    h_sumSTPassed.Write()
    
    h_Data_Failed.Write()
    h_sumWJetsFailed.Write()
    h_sumDibosonFailed.Write()
    h_sumSTFailed.Write()

    outfile.Close()
    if isTope == "True":
        print "Finish generating TopE.root"
    else:
        print "Finish generating TopMu.root"



    #get the statistical uncertainty#

    dx = ttData_error[1]
    #print "data efficiency error", dx

    dy = ttMC_error[1]
    #print "MC efficiency error", dy

    x = frac_tt_data_passed
    y = frac_Passed_fin

    statUnc = TMath.Sqrt(( (dx**2)/(y**2) ) + ( (x**2)*(dy**2)/(y**4) ) )
    #print "statistical Uncertainty in Top (e) CR", statUnc
    #print " "
    if isTope == "True":
        print "\nrelative statistical Uncertainty in Top (e) CR", statUnc/SF*100, " %"
    else:
        print "\nrelative statistical Uncertainty in Top (mu) CR", statUnc/SF*100, " %"
    print ""

    if isTope == "True":
        header = ["Process", "Number of Events", "Top (e)"]
    else:
        header = ["Process", "Number of Events", "Top (mu)"]
    row1 = [" ", "DDB mistag SF", str(round(SF, 3)) + " +- " + str(round(statUnc,3)) + " (stat)"]
    row2 = ["tt MC", "Pass (not normalized)", str(ttMCpassNotNormalized)]
    row3 = [" ", "Pass (normalized)", str(round(h_ttPassed.Integral(),2))]
    row4 = [" ", "Fail (not normalized)", str(ttMCfailNotNormalized)]
    row5 = [" ", "Fail (normalized)", str(round(h_ttFailed.Integral(),2))]
    row6 = [" ", "Total (not normalized)", str(ttMCtotalNotNormalized)]
    row7 = [" ", "Total (normalized)", str(round(h_tt.Integral(),2))]

    inforMC = [row2, row3, row4, row5, row6, row7]

    row8 = ["tt DATA", "Pass (before subtraction)", str(round(h_Data_Passed.Integral(),2))]
    row9 = [" ", "Pass (after subtraction)", str(round(SubtractedDataPassed.Integral(),2))]
    row10 = [" ", "Fail (before subtraction)", str(round(h_Data_Failed.Integral(),2))]
    row11 = [" ", "Fail (after subtraction)", str(round(SubtractedDataFailed.Integral(),2))]
    row12 = [" ", "Total (before subtraction)", str(round(h_Data.Integral(),2))]
    row13 = [" ", "Total (after subtraction)", str(round(h_totaldata.Integral(),2))]

    inforDATA = [row8, row9, row10, row11, row12, row13]

    row14 = ["Background", "Pass (normalized)", str(round((h_sumWJetsPassed + h_sumDibosonPassed + h_sumSTPassed).Integral(),2))]
    row15 = [" ", "Fail (normalized)", str(round((h_sumWJetsFailed + h_sumDibosonFailed + h_sumSTFailed).Integral(),2))]
    row16 = [" ", "Total (normalized)", str(round((h_sumWJets + h_sumDiboson + h_sumST).Integral(),2))]

    inforBKG = [row14, row15, row16]

    makeTable(header, row1, inforMC, inforDATA, inforBKG)



def withSingleTopAndMETbins(lowerMET, upperMET, year_, isTope):
    if isTope == "True":
        print "Top (e) Control Region"
    else:
        print "Top (mu) Control Region"
    print "Running With Single Top for MET " + str(lowerMET) + "-" + str(upperMET) + " GeV Analysis of " + str(year_) + " Data"
    print ""
    
    vers = yearandversion(year_)
    
    outdirtype = "withSingleTop/MET-"
    outputpath = vers[2]+outdirtype+str(lowerMET)+"-"+str(upperMET)+"/"
    if not os.path.exists(vers[2]):
        os.mkdir(vers[2])
    if not os.path.exists(vers[2]+outdirtype):
        os.mkdir(vers[2]+outdirtype)
    if not os.path.exists(outputpath):
        os.mkdir(outputpath)
    
    #totalmax = 300
    #ttmax = 200
    
    #---------------------------------#
    #         TTtoSemileptonic        #
    #---------------------------------#

    if year_ == 2017:
        Top_path = vers[1]+"combined_crab_TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root"
    if year_ == 2018:
        Top_path = vers[1]+"combined_crab_TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8.root"

    xsTop = 300.9498

    h_TopMatch = TH1F("h_TopMatch", "", nbins, edges)
    h_Wmatch = TH1F("h_Wmatch", "", nbins, edges)
    h_unmatch = TH1F("h_unmatch", "", nbins, edges)
    h_ttFailed = TH1F("h_ttFailed", "", nbins, edges)
    h_ttPassed = TH1F("h_ttPassed", "", nbins, edges)
    h_ttPassed_Match = TH1F("h_ttPassed_Match", "", nbins, edges)
    h_ttPassed_Wmatch = TH1F("h_ttPassed_Wmatch", "", nbins, edges)
    h_ttPassed_unmatch = TH1F("h_ttPassed_unmatch", "", nbins, edges)

    openTop = TFile(Top_path, "read")
    h_total_mcweight_Top = openTop.Get("h_total_mcweight")
    totalEventsTop = h_total_mcweight_Top.Integral()
    if isTope == "True":
        treeTop = openTop.Get("monoHbb_Tope_boosted")
    else:
        treeTop = openTop.Get("monoHbb_Topmu_boosted")
    EventsTop = treeTop.GetEntries()

    for i in range(EventsTop):
        treeTop.GetEntry(i)
        st_TopMatching = getattr(treeTop, 'st_TopMatching')
        CSV_Top = getattr(treeTop, 'FJetCSV')
        SD_Top = getattr(treeTop, 'FJetMass')
        dPhi_Top = getattr(treeTop, 'min_dPhi')
        nJets_Top = getattr(treeTop, 'nJets')
        pt_Top = getattr(treeTop, 'FJetPt')
        met_Top = getattr(treeTop, 'MET')
        if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (met_Top > lowerMET) and (met_Top <= upperMET):
            h_TopMatch.Fill(CSV_Top)
        if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (met_Top > lowerMET) and (met_Top <= upperMET):
            h_Wmatch.Fill(CSV_Top)
        if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (met_Top > lowerMET) and (met_Top <= upperMET):
            h_unmatch.Fill(CSV_Top)
        if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86) and (met_Top > lowerMET) and (met_Top <= upperMET):
            h_ttPassed.Fill(CSV_Top)
        if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top <= 0.86) and (met_Top > lowerMET) and (met_Top <= upperMET):
            h_ttFailed.Fill(CSV_Top)
        if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86) and (met_Top > lowerMET) and (met_Top <= upperMET):
            h_ttPassed_Match.Fill(CSV_Top)
        if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86) and (met_Top > lowerMET) and (met_Top <= upperMET):
            h_ttPassed_Wmatch.Fill(CSV_Top)
        if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86) and (met_Top > lowerMET) and (met_Top <= upperMET):
            h_ttPassed_unmatch.Fill(CSV_Top)

    ttMCpassNotNormalized = h_ttPassed.Integral()
    ttMCfailNotNormalized = h_ttFailed.Integral()
    ttMCtotalNotNormalized = ttMCpassNotNormalized + ttMCfailNotNormalized

    h_TopMatch = h_TopMatch*(vers[0]*xsTop/totalEventsTop)
    h_Wmatch = h_Wmatch*(vers[0]*xsTop/totalEventsTop)
    h_unmatch = h_unmatch*(vers[0]*xsTop/totalEventsTop)
    h_ttFailed = h_ttFailed*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed = h_ttPassed*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_Match = h_ttPassed_Match*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_Wmatch = h_ttPassed_Wmatch*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_unmatch = h_ttPassed_unmatch*(vers[0]*xsTop/totalEventsTop)

    h_tt = h_ttFailed.Clone("h_tt")
    h_tt = h_tt + h_ttPassed
    frac_match = (h_TopMatch.Integral())/(h_tt.Integral())*100
    frac_Wmatch = (h_Wmatch.Integral())/(h_tt.Integral())*100
    frac_unmatch = (h_unmatch.Integral())/(h_tt.Integral())*100
    frac_ttPassedMatch = (h_ttPassed_Match.Integral())/(h_tt.Integral())*100
    frac_ttPassedWmatch = (h_ttPassed_Wmatch.Integral())/(h_tt.Integral())*100
    frac_ttPassedUnmatch = (h_ttPassed_unmatch.Integral())/(h_tt.Integral())*100



    #---------------------------------#
    #              W+Jets             #
    #---------------------------------#

    WJets_files = ["combined_crab_WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root"]

    xsWJets = [1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001]

    h_WJets = TH1F("h_WJets", "", nbins, edges)
    h_WJetsPassed = TH1F("h_WJetsPassed", "", nbins, edges)
    h_WJetsFailed = TH1F("h_WJetsFailed", "", nbins, edges)

    h_sumWJets = TH1F("h_sumWJets", "", nbins, edges)
    h_sumWJetsPassed = TH1F("h_sumWJetsPassed", "", nbins, edges)
    h_sumWJetsFailed = TH1F("h_sumWJetsFailed", "", nbins, edges)

    for k in range(len(WJets_files)):
        h_WJets.Reset()
        h_WJetsPassed.Reset()
        h_WJetsFailed.Reset()
        
        openWJets = TFile(vers[1]+WJets_files[k], "read")
        h_total_mcweight_WJets = openWJets.Get("h_total_mcweight")
        totalEventsWJets = h_total_mcweight_WJets.Integral()
        if isTope == "True":
            treeWJets = openWJets.Get("monoHbb_Tope_boosted")
        else:
            treeWJets = openWJets.Get("monoHbb_Topmu_boosted")
        EventsWJets = treeWJets.GetEntries()
        
        for i in range(EventsWJets):
            treeWJets.GetEntry(i)
            CSV_WJets = getattr(treeWJets, 'FJetCSV')
            SD_WJets = getattr(treeWJets, 'FJetMass')
            dPhi_WJets = getattr(treeWJets, 'min_dPhi')
            nJets_WJets = getattr(treeWJets, 'nJets')
            pt_WJets = getattr(treeWJets, 'FJetPt')
            met_WJets = getattr(treeWJets, 'MET')
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0) and (met_WJets > lowerMET) and (met_WJets <= upperMET):
                h_WJets.Fill(CSV_WJets)
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0) and (CSV_WJets > 0.86) and (met_WJets > lowerMET) and (met_WJets <= upperMET):
                h_WJetsPassed.Fill(CSV_WJets)
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0) and (CSV_WJets <= 0.86) and (met_WJets > lowerMET) and (met_WJets <= upperMET):
                h_WJetsFailed.Fill(CSV_WJets)

        h_WJets = h_WJets*(vers[0]*xsWJets[k]/totalEventsWJets)
        h_WJetsPassed = h_WJetsPassed*(vers[0]*xsWJets[k]/totalEventsWJets)
        h_WJetsFailed = h_WJetsFailed*(vers[0]*xsWJets[k]/totalEventsWJets)
        
        h_sumWJets += h_WJets
        h_sumWJetsPassed += h_WJetsPassed
        h_sumWJetsFailed += h_WJetsFailed


    #---------------------------------#
    #              Diboson             #
    #---------------------------------#

    Diboson_files = ["combined_crab_ZZ_TuneCP5_13TeV-pythia8.root", "combined_crab_WW_TuneCP5_13TeV-pythia8.root", "combined_crab_WZ_TuneCP5_13TeV-pythia8.root"]

    xsDiboson = [12.14, 75.8, 27.6]

    h_Diboson = TH1F("h_Diboson", "", nbins, edges)
    h_DibosonPassed = TH1F("h_DibosonPassed", "", nbins, edges)
    h_DibosonFailed = TH1F("h_DibosonFailed", "", nbins, edges)

    h_sumDiboson = TH1F("h_sumDiboson", "", nbins, edges)
    h_sumDibosonPassed = TH1F("h_sumDibosonPassed", "", nbins, edges)
    h_sumDibosonFailed = TH1F("h_sumDibosonFailed", "", nbins, edges)

    for k in range(len(Diboson_files)):
        h_Diboson.Reset()
        h_DibosonPassed.Reset()
        h_DibosonFailed.Reset()
        
        openDiboson = TFile(vers[1]+Diboson_files[k], "read")
        h_total_mcweight_Diboson = openDiboson.Get("h_total_mcweight")
        totalEventsDiboson = h_total_mcweight_Diboson.Integral()
        if isTope == "True":
            treeDiboson = openDiboson.Get("monoHbb_Tope_boosted")
        else:
            treeDiboson = openDiboson.Get("monoHbb_Topmu_boosted")
        EventsDiboson = treeDiboson.GetEntries()
        
        for i in range(EventsDiboson):
            treeDiboson.GetEntry(i)
            CSV_Diboson = getattr(treeDiboson, 'FJetCSV')
            SD_Diboson = getattr(treeDiboson, 'FJetMass')
            dPhi_Diboson = getattr(treeDiboson, 'min_dPhi')
            nJets_Diboson = getattr(treeDiboson, 'nJets')
            pt_Diboson = getattr(treeDiboson, 'FJetPt')
            met_Diboson = getattr(treeDiboson, 'MET')
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0) and (met_Diboson > lowerMET) and (met_Diboson <= upperMET):
                h_Diboson.Fill(CSV_Diboson)
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0) and (CSV_Diboson > 0.86) and (met_Diboson > lowerMET) and (met_Diboson <= upperMET):
                h_DibosonPassed.Fill(CSV_Diboson)
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0) and (CSV_Diboson <= 0.86) and (met_Diboson > lowerMET) and (met_Diboson <= upperMET):
                h_DibosonFailed.Fill(CSV_Diboson)

        h_Diboson = h_Diboson*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        h_DibosonPassed = h_DibosonPassed*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        h_DibosonFailed = h_DibosonFailed*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        
        h_sumDiboson += h_Diboson
        h_sumDibosonPassed += h_DibosonPassed
        h_sumDibosonFailed += h_DibosonFailed


    #---------------------------------#
    #              Single t           #
    #---------------------------------#

    if year_ == 2017:
        ST_files = ["combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]
    if year_ == 2018:
        ST_files = ["combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]

    xsST = [3.74, 67.91, 113.3, 34.97, 34.91]

    h_ST = TH1F("h_ST", "", nbins, edges)
    h_STPassed = TH1F("h_STPassed", "", nbins, edges)
    h_STFailed = TH1F("h_STFailed", "", nbins, edges)

    h_sumST = TH1F("h_sumST", "", nbins, edges)
    h_sumSTPassed = TH1F("h_sumSTPassed", "", nbins, edges)
    h_sumSTFailed = TH1F("h_sumSTFailed", "", nbins, edges)

    for k in range(len(ST_files)):
        h_ST.Reset()
        h_STPassed.Reset()
        h_STFailed.Reset()
        
        openST = TFile(vers[1]+ST_files[k], "read")
        h_total_mcweight_ST = openST.Get("h_total_mcweight")
        totalEventsST = h_total_mcweight_ST.Integral()
        if isTope == "True":
            treeST = openST.Get("monoHbb_Tope_boosted")
        else:
            treeST = openST.Get("monoHbb_Topmu_boosted")
        EventsST = treeST.GetEntries()
        
        for i in range(EventsST):
            treeST.GetEntry(i)
            CSV_ST = getattr(treeST, 'FJetCSV')
            SD_ST = getattr(treeST, 'FJetMass')
            dPhi_ST = getattr(treeST, 'min_dPhi')
            nJets_ST = getattr(treeST, 'nJets')
            pt_ST = getattr(treeST, 'FJetPt')
            met_ST = getattr(treeST, 'MET')
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (nJets_ST <= 2) and (met_ST > lowerMET) and (met_ST <= upperMET):
                h_ST.Fill(CSV_ST)
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (CSV_ST > 0.86) and (nJets_ST <= 2) and (met_ST > lowerMET) and (met_ST <= upperMET):
                h_STPassed.Fill(CSV_ST)
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (CSV_ST <= 0.86) and (nJets_ST <= 2) and (met_ST > lowerMET) and (met_ST <= upperMET):
                h_STFailed.Fill(CSV_ST)

        h_ST = h_ST*(vers[0]*xsST[k]/totalEventsST)
        h_STPassed = h_STPassed*(vers[0]*xsST[k]/totalEventsST)
        h_STFailed = h_STFailed*(vers[0]*xsST[k]/totalEventsST)

        h_sumST += h_ST
        h_sumSTPassed += h_STPassed
        h_sumSTFailed += h_STFailed



    #---------------------------------#
    #               DATA              #
    #---------------------------------#

    if isTope == "True":
        Data_path = vers[1]+"combined_data_SE.root"
    else:
        Data_path = vers[1]+"combined_data_MET.root"

    h_Data = TH1F("h_Data", "", nbins, edges)
    h_Data_Failed = TH1F("h_Data_Failed", "", nbins, edges)
    h_Data_Passed = TH1F("h_Data_Passed", "", nbins, edges)

    openData = TFile(Data_path, "read")
    h_total_mcweight_Data = openData.Get("h_total_mcweight")
    totalEventsData = h_total_mcweight_Data.Integral()
    if isTope == "True":
        treeData = openData.Get("monoHbb_Tope_boosted")
    else:
        treeData = openData.Get("monoHbb_Topmu_boosted")
    EventsData = treeData.GetEntries()

    for i in range(EventsData):
        treeData.GetEntry(i)
        CSV_Data = getattr(treeData, 'FJetCSV')
        SD_Data = getattr(treeData, 'FJetMass')
        dPhi_Data = getattr(treeData, 'min_dPhi')
        nJets_Data = getattr(treeData, 'nJets')
        pt_Data = getattr(treeData, 'FJetPt')
        met_Data = getattr(treeData, 'MET')
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0) and (met_Data > lowerMET) and (met_Data <= upperMET):
            h_Data.Fill(CSV_Data)
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0) and (CSV_Data > 0.86) and (met_Data > lowerMET) and (met_Data <= upperMET):
            h_Data_Passed.Fill(CSV_Data)
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0) and (CSV_Data <= 0.86) and (met_Data > lowerMET) and (met_Data <= upperMET):
            h_Data_Failed.Fill(CSV_Data)

    SubtractedData = h_Data.Clone("SubtractedData")
    SubtractedData = SubtractedData - (h_sumWJets + h_sumDiboson + h_sumST)
    SubtractedDataPassed = h_Data_Passed.Clone("SubtractedDataPassed")
    SubtractedDataPassed = SubtractedDataPassed - (h_sumWJetsPassed + h_sumDibosonPassed + h_sumSTPassed)
    SubtractedDataFailed = h_Data_Failed.Clone("SubtractedDataFailed")
    SubtractedDataFailed = SubtractedDataFailed - (h_sumWJetsFailed + h_sumDibosonFailed + h_sumSTFailed)


    h_totaldata = SubtractedDataPassed.Clone("h_totaldata")
    h_totaldata = h_totaldata + SubtractedDataFailed
    frac_tt_data_passed = (SubtractedDataPassed.Integral())/(h_totaldata.Integral())
    frac_tt_data_failed = (SubtractedDataFailed.Integral())/(h_totaldata.Integral())*100


    #------------Overlap histograms in Full Canvas-------------#

    frac_match_text = str(round(frac_match, 2))
    frac_Wmatch_text = str(round(frac_Wmatch, 2))
    frac_unmatch_text = str(round(frac_unmatch, 2))


    h_TopMatchFinal = h_TopMatch.Clone("h_TopMatchFinal")
    h_WmatchFinal = h_Wmatch.Clone("h_WmatchFinal")
    h_unmatchFinal = h_unmatch.Clone("h_unmatchFinal")
    h_sumWJetsFinal = h_sumWJets.Clone("h_sumWJetsFinal")
    h_sumSTFinal = h_sumST.Clone("h_sumSTFinal")

    h_sumSTFinal = h_sumSTFinal + h_sumDiboson
    h_sumWJetsFinal = h_sumWJetsFinal + h_sumSTFinal
    h_unmatchFinal = h_unmatchFinal + h_sumWJetsFinal
    h_WmatchFinal = h_WmatchFinal + h_unmatchFinal
    h_TopMatchFinal = h_TopMatchFinal + h_WmatchFinal

    full = TCanvas("full","",800,900) #width-height
    full.SetTopMargin(0.4)
    full.SetBottomMargin(0.05)
    full.SetRightMargin(0.1)
    full.SetLeftMargin(0.15)
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

    leg = TLegend(0.65,0.7,0.85,0.87)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.027)
    
    binvalues1 = []
    for i in range(nbins):
        binvalue = h_Data.GetBinContent(i)
        binvalues1.append(binvalue)
    totalmax = max(binvalues1) + 100
    
    padMain.cd()

    h_TopMatchFinal.SetFillColor(821)
    h_TopMatchFinal.SetLineColor(821)#923
    h_TopMatchFinal.GetXaxis().SetTitle("DDB")
    h_TopMatchFinal.GetXaxis().SetLabelSize(0)
    h_TopMatchFinal.GetYaxis().SetTitle("Events/Bin")
    h_TopMatchFinal.GetYaxis().SetTitleSize(0.05)
    h_TopMatchFinal.GetYaxis().SetLabelSize(0.05)
    h_TopMatchFinal.SetMaximum(totalmax)
    leg.AddEntry(h_TopMatchFinal, "Top (mtch.) ("+frac_match_text+"%)", "f")

    h_WmatchFinal.SetFillColor(822)
    h_WmatchFinal.SetLineColor(822)
    leg.AddEntry(h_WmatchFinal, "Top (W-mtch.) ("+frac_Wmatch_text+"%)","f")

    h_unmatchFinal.SetFillColor(813)
    h_unmatchFinal.SetLineColor(813)
    leg.AddEntry(h_unmatchFinal, "Top (unmtch.) ("+frac_unmatch_text+"%)","f")

    h_sumWJetsFinal.SetFillColor(854)
    h_sumWJetsFinal.SetLineColor(854)
    leg.AddEntry(h_sumWJetsFinal, "W+Jets","f")
    
    h_sumSTFinal.SetFillColor(800)
    h_sumSTFinal.SetLineColor(800)
    leg.AddEntry(h_sumSTFinal, "Single Top","f")

    h_sumDiboson.SetFillColor(627)
    h_sumDiboson.SetLineColor(627)
    leg.AddEntry(h_sumDiboson, "Diboson","f")

    h_Data.SetLineColor(1)
    h_Data.SetMarkerStyle(20)
    h_Data.SetMarkerSize(1.5)
    leg.AddEntry(h_Data, "Data", "lep")

    #-------Draw Histogram in Full Canvas---------#

    h_TopMatchFinal.Draw("hist")
    h_WmatchFinal.Draw("histsame")
    h_unmatchFinal.Draw("histsame")
    h_sumWJetsFinal.Draw("histsame")
    h_sumSTFinal.Draw("histsame")
    h_sumDiboson.Draw("histsame")
    h_Data.Draw("e1same")
    leg.Draw()

    lt = TLatex()
    lt.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{MET "+str(lowerMET)+"-"+str(upperMET)+" GeV}}")
    lt.DrawLatexNDC(0.24,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt.DrawLatexNDC(0.24,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")


    padRatio.cd()

    gPad.GetUymax()

    totalData = h_Data.Clone("totalData")
    ratio = dataPredRatio(data_ = totalData, totalBkg_ = h_TopMatchFinal)
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
    ratio.GetXaxis().SetTitle("DDB")
    ratio.Draw("e1")

    #full.cd()
    full.Modified()
    full.Update()
    if isTope == "True":
        full.SaveAs(outputpath+"Tope_unsubtracted.pdf")
    else:
        full.SaveAs(outputpath+"Topmu_unsubtracted.pdf")


    #------------Overlap histograms in Subtract Canvas-------------#
    
    Cloned_frac_tt = h_tt.Clone("Cloned_frac_tt")
    Cloned_frac_tt.Rebin(14)
    Cloned_frac_ttFailed = h_ttFailed.Clone("Cloned_frac_ttFailed")
    Cloned_frac_ttFailed.Rebin(14)
    Cloned_frac_ttFailed.Sumw2()
    Cloned_frac_ttFailed.Divide(Cloned_frac_tt)
    frac_Failed_fin = Cloned_frac_ttFailed.Integral()
    ttMC_fraction.append(frac_Failed_fin)
    ttMC_error.append(Cloned_frac_ttFailed.GetBinError(1))
    
    
    Cloned_frac_ttPassed = h_ttPassed.Clone("Cloned_frac_ttPassed")
    Cloned_frac_ttPassed.Rebin(14)
    Cloned_frac_ttPassed.Sumw2()
    Cloned_frac_ttPassed.Divide(Cloned_frac_tt)
    frac_Passed_fin = Cloned_frac_ttPassed.Integral()
    ttMC_fraction.append(frac_Passed_fin)
    ttMC_error.append(Cloned_frac_ttPassed.GetBinError(1))
    
    
    Cloned_frac_tt_data_total = h_totaldata.Clone("Cloned_frac_tt_data_total")
    Cloned_frac_tt_data_total.Rebin(14)
    Cloned_frac_tt_data_failed = SubtractedDataFailed.Clone("Cloned_frac_tt_data_failed")
    Cloned_frac_tt_data_failed.Rebin(14)
    Cloned_frac_tt_data_failed.Sumw2()
    Cloned_frac_tt_data_failed.Divide(Cloned_frac_tt_data_total)
    frac_ttData_fail = Cloned_frac_tt_data_failed.Integral()
    ttData_fraction.append(frac_ttData_fail)
    ttData_error.append(Cloned_frac_tt_data_failed.GetBinError(1))
    
    
    Cloned_frac_tt_data_passed = SubtractedDataPassed.Clone("Cloned_frac_tt_data_passed")
    Cloned_frac_tt_data_passed.Rebin(14)
    Cloned_frac_tt_data_passed.Sumw2()
    Cloned_frac_tt_data_passed.Divide(Cloned_frac_tt_data_total)
    frac_ttData_pass = Cloned_frac_tt_data_passed.Integral()
    ttData_fraction.append(frac_ttData_pass)
    ttData_error.append(Cloned_frac_tt_data_passed.GetBinError(1))
    
    frac_Passed_text = str(round(frac_Passed_fin*100, 2))
    
    subtract = TCanvas("subtract","",900,700) #width-height
    subtract.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)
    
    leg2 = TLegend(0.4,0.5,0.6,0.6)
    leg2.SetBorderSize(0)
    leg2.SetTextSize(0.027)

    binvalues2 = []
    for i in range(nbins):
        binvalue = SubtractedData.GetBinContent(i)
        binvalues2.append(binvalue)
    ttmax = max(binvalues2) + 50
    
    #h_ttFailed.Rebin(2)
    h_ttFailed.SetFillColor(821)
    h_ttFailed.SetLineColor(821)#922
    h_ttFailed.GetXaxis().SetTitle("DDB")
    h_ttFailed.GetYaxis().SetTitle("Events/Bin")
    h_ttFailed.SetMaximum(ttmax)
    leg2.AddEntry(h_ttFailed, "t#bar{t}", "f")
    
    #h_ttPassed.Rebin(2)
    h_ttPassed.SetFillColor(622)
    h_ttPassed.SetLineColor(622)
    h_ttPassed.GetXaxis().SetTitle("DDB")
    h_ttPassed.GetYaxis().SetTitle("Events/Bin")
    h_ttPassed.SetMaximum(ttmax)
    leg2.AddEntry(h_ttPassed, "t#bar{t} mistag ("+frac_Passed_text+"%)", "f")
    
    #SubtractedData.Rebin(2)
    SubtractedData.SetLineColor(1)
    SubtractedData.SetMarkerStyle(20)
    SubtractedData.SetMarkerSize(1.5)
    SubtractedData.GetXaxis().SetTitle("DDB")
    SubtractedData.GetYaxis().SetTitle("Events/Bin")
    leg2.AddEntry(SubtractedData, "Subtracted Data", "lep")
    
    #-------Draw Histogram in Subtract Canvas---------#
    
    h_ttFailed.Draw("hist")
    h_ttPassed.Draw("histsame")
    SubtractedData.Draw("e1same")
    leg2.Draw()
    
    lt2 = TLatex()
    lt2.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{MET "+str(lowerMET)+"-"+str(upperMET)+" GeV}}")
    lt2.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt2.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt2.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt2.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")
    
    #subtract.cd()
    subtract.Modified()
    subtract.Update()
    if isTope == "True":
        subtract.SaveAs(outputpath+"Tope_subtracted.pdf")
    else:
        subtract.SaveAs(outputpath+"Topmu_subtracted.pdf")
    
    
    #------------Overlap histograms in Scalefactor Canvas-------------#

    #** MISTAG SCALE FACTOR **#

    SF = frac_tt_data_passed / frac_Passed_fin
    print " "
    print "DDB Mistag SF :", SF
    print " "

    scalefactor = TCanvas("scalefactor","", 700, 900)
    scalefactor.SetTopMargin(0.1)
    scalefactor.SetBottomMargin(0.15)
    scalefactor.SetRightMargin(0.1)
    scalefactor.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)
    
    pad1 = TPad("pad1", "", 0.01, 0.25, 0.93, 1.0)
    pad1.SetTopMargin(0.1)
    pad1.SetRightMargin(0.05)
    pad1.SetLeftMargin(0.17)
    pad1.SetBottomMargin(0.05)
    
    pad2 = TPad("pad2", "", 0.0, 0.0, 0.375, 0.24)
    pad2.SetTopMargin(0.0)
    pad2.SetRightMargin(0.1)
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
    
    #** Pad1 **#
    pad1.cd()
    
    leg3 = TLegend(0.5,0.55,0.7,0.65)
    leg3.SetBorderSize(0)
    leg3.SetTextSize(0.027)
    
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
    mg.Draw("AP")
    mg.GetHistogram().SetMaximum(1.5)
    mg.GetHistogram().SetMinimum(0)
    mg.GetHistogram().GetYaxis().SetTitle("Fraction")
    gPad.Modified()
    mg.GetXaxis().SetLimits(0,3)
    mg.GetXaxis().SetTickLength(0.03)
    mg.GetXaxis().SetNdivisions(103)
    mg.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Fail")
    mg.GetXaxis().ChangeLabel(1,-1,0)
    mg.GetXaxis().ChangeLabel(-1,-1,0)
    mg.GetXaxis().ChangeLabel(3,-1,-1,-1,-1,-1,"Pass")
    leg3.Draw()
    
    lt3 = TLatex()
    lt3.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{MET "+str(lowerMET)+"-"+str(upperMET)+" GeV}}")
    lt3.DrawLatexNDC(0.19,0.855,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt3.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt3.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt3.DrawLatexNDC(0.19,0.755,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")
    lt3.Draw()
    
    pad1.Update()
    
    #** Pad2 **#
    pad2.cd()
    
    Cloned_frac_ttPassed.SetLineColor(870)
    Cloned_frac_ttPassed.SetLineWidth(3)
    Cloned_frac_ttPassed.SetMarkerColor(870)
    Cloned_frac_ttPassed.SetMarkerStyle(20)
    Cloned_frac_ttPassed.GetYaxis().SetTitle("Fraction")
    Cloned_frac_ttPassed.GetYaxis().SetTitleSize(0.09)
    Cloned_frac_ttPassed.GetYaxis().SetLabelSize(0.1)
    Cloned_frac_ttPassed.GetYaxis().SetNdivisions(404)
    Cloned_frac_ttPassed.SetMaximum(0.3)#0.3
    Cloned_frac_ttPassed.SetMinimum(0.0)#0.0
    Cloned_frac_ttPassed.GetXaxis().SetTitle("")
    Cloned_frac_ttPassed.GetXaxis().SetLabelSize(0.09)
    Cloned_frac_ttPassed.GetXaxis().SetLabelOffset(0.02)
    Cloned_frac_ttPassed.GetXaxis().SetNdivisions(104)
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Pass")
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(1,-1,0)
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(-1,-1,0)
    
    Cloned_frac_tt_data_passed.SetLineColor(1)
    Cloned_frac_tt_data_passed.SetLineWidth(2)
    Cloned_frac_tt_data_passed.SetMarkerColor(1)
    Cloned_frac_tt_data_passed.SetMarkerStyle(20)
    
    Cloned_frac_ttPassed.Draw("e1")
    Cloned_frac_tt_data_passed.Draw("e1histsame")
    
    
    #** Pad3 **#
    pad3.cd()
    
    mistagSF = Cloned_frac_tt_data_passed.Clone("mistagSF")
    mistagSF.Sumw2()
    mistagSF.Divide(Cloned_frac_ttPassed)
    
    #print "******"
    #print "mistag SF:", mistagSF.Integral()
    
    SFfinal = round(SF, 3)
    SFtext = "SF = "+str(SFfinal)
    
    mistagSFmax = SF + 0.2
    mistagSFmin = SF - 0.2
    
    mistagSF.SetLineColor(797)
    mistagSF.SetMarkerColor(797)
    mistagSF.SetLineWidth(3)
    mistagSF.SetMaximum(mistagSFmax)
    mistagSF.SetMinimum(mistagSFmin)
    mistagSF.GetXaxis().SetTitle(" ")
    mistagSF.GetXaxis().SetLabelOffset(999)
    mistagSF.GetXaxis().SetLabelSize(0)
    mistagSF.GetXaxis().SetTickLength(0)
    mistagSF.GetYaxis().SetLabelSize(0.1)
    mistagSF.GetYaxis().SetNdivisions(404)
    mistagSF.GetYaxis().SetTitle(" ")
    
    mistagSF.Draw("e1hist")
    
    pt = TPaveText(0.21, 0.72, 0.31, 0.8, "brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(42)
    pt.SetTextSize(0.1)
    pt.AddText(SFtext)
    pt.Draw()
    
    scalefactor.Modified()
    scalefactor.Update()
    if isTope == "True":
        scalefactor.SaveAs(outputpath+"Tope_SF.pdf")
    else:
        scalefactor.SaveAs(outputpath+"Topmu_SF.pdf")
    
    
    # Save the canvases in root file #
    if isTope == "True":
        print "\nGenerating TopE.root"
    
        outfile = TFile(outputpath+"TopE.root", "RECREATE")
    else:
        print "\nGenerating TopMu.root"
        
        outfile = TFile(outputpath+"TopMu.root", "RECREATE")
    h_TopMatch.Write()
    h_Wmatch.Write()
    h_unmatch.Write()
    h_sumWJets.Write()
    h_sumDiboson.Write()
    h_sumST.Write()
    h_Data.Write()
    
    h_ttFailed.Write()
    h_ttPassed.Write()
    SubtractedData.Write()
    
    SubtractedDataFailed.Write()
    SubtractedDataPassed.Write()
    h_totaldata.Write()
    h_tt.Write()
    
    h_Data_Passed.Write()
    h_sumWJetsPassed.Write()
    h_sumDibosonPassed.Write()
    h_sumSTPassed.Write()
    
    h_Data_Failed.Write()
    h_sumWJetsFailed.Write()
    h_sumDibosonFailed.Write()
    h_sumSTFailed.Write()
    
    outfile.Close()
    if isTope == "True":
        print "Finish generating TopE.root"
    else:
        print "Finish generating TopMu.root"
    
    
    
    #get the statistical uncertainty#
    
    dx = ttData_error[1]
    #print "data efficiency error", dx
    
    dy = ttMC_error[1]
    #print "MC efficiency error", dy
    
    x = frac_tt_data_passed
    y = frac_Passed_fin
    
    statUnc = TMath.Sqrt(( (dx**2)/(y**2) ) + ( (x**2)*(dy**2)/(y**4) ) )
    #print "statistical Uncertainty in Top (e) CR", statUnc
    #print " "
    if isTope == "True":
        print "\nrelative statistical Uncertainty in Top (e) CR", statUnc/SF*100, " %"
    else:
        print "\nrelative statistical Uncertainty in Top (mu) CR", statUnc/SF*100, " %"
    print ""

    if isTope == "True":
        header = ["Process", "Number of Events", "Top (e)"]
    else:
        header = ["Process", "Number of Events", "Top (mu)"]
    row1 = [" ", "DDB mistag SF", str(round(SF, 3)) + " +- " + str(round(statUnc,3)) + " (stat)"]
    row2 = ["tt MC", "Pass (not normalized)", str(ttMCpassNotNormalized)]
    row3 = [" ", "Pass (normalized)", str(round(h_ttPassed.Integral(),2))]
    row4 = [" ", "Fail (not normalized)", str(ttMCfailNotNormalized)]
    row5 = [" ", "Fail (normalized)", str(round(h_ttFailed.Integral(),2))]
    row6 = [" ", "Total (not normalized)", str(ttMCtotalNotNormalized)]
    row7 = [" ", "Total (normalized)", str(round(h_tt.Integral(),2))]

    inforMC = [row2, row3, row4, row5, row6, row7]

    row8 = ["tt DATA", "Pass (before subtraction)", str(round(h_Data_Passed.Integral(),2))]
    row9 = [" ", "Pass (after subtraction)", str(round(SubtractedDataPassed.Integral(),2))]
    row10 = [" ", "Fail (before subtraction)", str(round(h_Data_Failed.Integral(),2))]
    row11 = [" ", "Fail (after subtraction)", str(round(SubtractedDataFailed.Integral(),2))]
    row12 = [" ", "Total (before subtraction)", str(round(h_Data.Integral(),2))]
    row13 = [" ", "Total (after subtraction)", str(round(h_totaldata.Integral(),2))]

    inforDATA = [row8, row9, row10, row11, row12, row13]

    row14 = ["Background", "Pass (normalized)", str(round((h_sumWJetsPassed + h_sumDibosonPassed + h_sumSTPassed).Integral(),2))]
    row15 = [" ", "Fail (normalized)", str(round((h_sumWJetsFailed + h_sumDibosonFailed + h_sumSTFailed).Integral(),2))]
    row16 = [" ", "Total (normalized)", str(round((h_sumWJets + h_sumDiboson + h_sumST).Integral(),2))]

    inforBKG = [row14, row15, row16]

    makeTable(header, row1, inforMC, inforDATA, inforBKG)



def withSingleTopAndpTbins(lowerpT, upperpT, year_, isTope):
    if isTope == "True":
        print "Top (e) Control Region"
    else:
        print "Top (mu) Control Region"
    print "Running With Single Top for pT " + str(lowerpT) + "-" + str(upperpT) + " GeV Analysis of " + str(year_) + " Data"
    print ""
    
    vers = yearandversion(year_)
    
    outdirtype = "withSingleTop/PT-"
    outputpath = vers[2]+outdirtype+str(lowerpT)+"-"+str(upperpT)+"/"
    if not os.path.exists(vers[2]):
        os.mkdir(vers[2])
    if not os.path.exists(vers[2]+outdirtype):
        os.mkdir(vers[2]+outdirtype)
    if not os.path.exists(outputpath):
        os.mkdir(outputpath)
    
    #totalmax = 500
    #ttmax = 300
    
    #---------------------------------#
    #         TTtoSemileptonic        #
    #---------------------------------#
    
    if year_ == 2017:
        Top_path = vers[1]+"combined_crab_TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root"
    if year_ == 2018:
        Top_path = vers[1]+"combined_crab_TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8.root"
    
    xsTop = 300.9498
    
    h_TopMatch = TH1F("h_TopMatch", "", nbins, edges)
    h_Wmatch = TH1F("h_Wmatch", "", nbins, edges)
    h_unmatch = TH1F("h_unmatch", "", nbins, edges)
    h_ttFailed = TH1F("h_ttFailed", "", nbins, edges)
    h_ttPassed = TH1F("h_ttPassed", "", nbins, edges)
    h_ttPassed_Match = TH1F("h_ttPassed_Match", "", nbins, edges)
    h_ttPassed_Wmatch = TH1F("h_ttPassed_Wmatch", "", nbins, edges)
    h_ttPassed_unmatch = TH1F("h_ttPassed_unmatch", "", nbins, edges)
    
    openTop = TFile(Top_path, "read")
    h_total_mcweight_Top = openTop.Get("h_total_mcweight")
    totalEventsTop = h_total_mcweight_Top.Integral()
    if isTope == "True":
        treeTop = openTop.Get("monoHbb_Tope_boosted")
    else:
        treeTop = openTop.Get("monoHbb_Topmu_boosted")
    EventsTop = treeTop.GetEntries()
    
    for i in range(EventsTop):
        treeTop.GetEntry(i)
        st_TopMatching = getattr(treeTop, 'st_TopMatching')
        CSV_Top = getattr(treeTop, 'FJetCSV')
        SD_Top = getattr(treeTop, 'FJetMass')
        dPhi_Top = getattr(treeTop, 'min_dPhi')
        nJets_Top = getattr(treeTop, 'nJets')
        pt_Top = getattr(treeTop, 'FJetPt')
        met_Top = getattr(treeTop, 'MET')
        if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (pt_Top > lowerpT) and (pt_Top <= upperpT):
            h_TopMatch.Fill(CSV_Top)
        if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (pt_Top > lowerpT) and (pt_Top <= upperpT):
            h_Wmatch.Fill(CSV_Top)
        if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (pt_Top > lowerpT) and (pt_Top <= upperpT):
            h_unmatch.Fill(CSV_Top)
        if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86) and (pt_Top > lowerpT) and (pt_Top <= upperpT):
            h_ttPassed.Fill(CSV_Top)
        if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top <= 0.86) and (pt_Top > lowerpT) and (pt_Top <= upperpT):
            h_ttFailed.Fill(CSV_Top)
        if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86) and (pt_Top > lowerpT) and (pt_Top <= upperpT):
            h_ttPassed_Match.Fill(CSV_Top)
        if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86) and (pt_Top > lowerpT) and (pt_Top <= upperpT):
            h_ttPassed_Wmatch.Fill(CSV_Top)
        if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (nJets_Top <= 2.0) and (CSV_Top > 0.86) and (pt_Top > lowerpT) and (pt_Top <= upperpT):
            h_ttPassed_unmatch.Fill(CSV_Top)

    ttMCpassNotNormalized = h_ttPassed.Integral()
    ttMCfailNotNormalized = h_ttFailed.Integral()
    ttMCtotalNotNormalized = ttMCpassNotNormalized + ttMCfailNotNormalized
    
    h_TopMatch = h_TopMatch*(vers[0]*xsTop/totalEventsTop)
    h_Wmatch = h_Wmatch*(vers[0]*xsTop/totalEventsTop)
    h_unmatch = h_unmatch*(vers[0]*xsTop/totalEventsTop)
    h_ttFailed = h_ttFailed*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed = h_ttPassed*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_Match = h_ttPassed_Match*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_Wmatch = h_ttPassed_Wmatch*(vers[0]*xsTop/totalEventsTop)
    h_ttPassed_unmatch = h_ttPassed_unmatch*(vers[0]*xsTop/totalEventsTop)
    
    h_tt = h_ttFailed.Clone("h_tt")
    h_tt = h_tt + h_ttPassed
    frac_match = (h_TopMatch.Integral())/(h_tt.Integral())*100
    frac_Wmatch = (h_Wmatch.Integral())/(h_tt.Integral())*100
    frac_unmatch = (h_unmatch.Integral())/(h_tt.Integral())*100
    frac_ttPassedMatch = (h_ttPassed_Match.Integral())/(h_tt.Integral())*100
    frac_ttPassedWmatch = (h_ttPassed_Wmatch.Integral())/(h_tt.Integral())*100
    frac_ttPassedUnmatch = (h_ttPassed_unmatch.Integral())/(h_tt.Integral())*100
    
    
    
    #---------------------------------#
    #              W+Jets             #
    #---------------------------------#
    
    WJets_files = ["combined_crab_WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root"]
    
    xsWJets = [1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001]
    
    h_WJets = TH1F("h_WJets", "", nbins, edges)
    h_WJetsPassed = TH1F("h_WJetsPassed", "", nbins, edges)
    h_WJetsFailed = TH1F("h_WJetsFailed", "", nbins, edges)
    
    h_sumWJets = TH1F("h_sumWJets", "", nbins, edges)
    h_sumWJetsPassed = TH1F("h_sumWJetsPassed", "", nbins, edges)
    h_sumWJetsFailed = TH1F("h_sumWJetsFailed", "", nbins, edges)
    
    for k in range(len(WJets_files)):
        h_WJets.Reset()
        h_WJetsPassed.Reset()
        h_WJetsFailed.Reset()
        
        openWJets = TFile(vers[1]+WJets_files[k], "read")
        h_total_mcweight_WJets = openWJets.Get("h_total_mcweight")
        totalEventsWJets = h_total_mcweight_WJets.Integral()
        if isTope == "True":
            treeWJets = openWJets.Get("monoHbb_Tope_boosted")
        else:
            treeWJets = openWJets.Get("monoHbb_Topmu_boosted")
        EventsWJets = treeWJets.GetEntries()
        
        for i in range(EventsWJets):
            treeWJets.GetEntry(i)
            CSV_WJets = getattr(treeWJets, 'FJetCSV')
            SD_WJets = getattr(treeWJets, 'FJetMass')
            dPhi_WJets = getattr(treeWJets, 'min_dPhi')
            nJets_WJets = getattr(treeWJets, 'nJets')
            pt_WJets = getattr(treeWJets, 'FJetPt')
            met_WJets = getattr(treeWJets, 'MET')
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0) and (pt_WJets > lowerpT) and (pt_WJets <= upperpT):
                h_WJets.Fill(CSV_WJets)
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0) and (CSV_WJets > 0.86) and (pt_WJets > lowerpT) and (pt_WJets <= upperpT):
                h_WJetsPassed.Fill(CSV_WJets)
            if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (nJets_WJets <= 2.0) and (CSV_WJets <= 0.86) and (pt_WJets > lowerpT) and (pt_WJets <= upperpT):
                h_WJetsFailed.Fill(CSV_WJets)
    
        h_WJets = h_WJets*(vers[0]*xsWJets[k]/totalEventsWJets)
        h_WJetsPassed = h_WJetsPassed*(vers[0]*xsWJets[k]/totalEventsWJets)
        h_WJetsFailed = h_WJetsFailed*(vers[0]*xsWJets[k]/totalEventsWJets)
        
        h_sumWJets += h_WJets
        h_sumWJetsPassed += h_WJetsPassed
        h_sumWJetsFailed += h_WJetsFailed


    #---------------------------------#
    #              Diboson             #
    #---------------------------------#

    Diboson_files = ["combined_crab_ZZ_TuneCP5_13TeV-pythia8.root", "combined_crab_WW_TuneCP5_13TeV-pythia8.root", "combined_crab_WZ_TuneCP5_13TeV-pythia8.root"]

    xsDiboson = [12.14, 75.8, 27.6]

    h_Diboson = TH1F("h_Diboson", "", nbins, edges)
    h_DibosonPassed = TH1F("h_DibosonPassed", "", nbins, edges)
    h_DibosonFailed = TH1F("h_DibosonFailed", "", nbins, edges)

    h_sumDiboson = TH1F("h_sumDiboson", "", nbins, edges)
    h_sumDibosonPassed = TH1F("h_sumDibosonPassed", "", nbins, edges)
    h_sumDibosonFailed = TH1F("h_sumDibosonFailed", "", nbins, edges)
    
    for k in range(len(Diboson_files)):
        h_Diboson.Reset()
        h_DibosonPassed.Reset()
        h_DibosonFailed.Reset()
        
        openDiboson = TFile(vers[1]+Diboson_files[k], "read")
        h_total_mcweight_Diboson = openDiboson.Get("h_total_mcweight")
        totalEventsDiboson = h_total_mcweight_Diboson.Integral()
        if isTope == "True":
            treeDiboson = openDiboson.Get("monoHbb_Tope_boosted")
        else:
            treeDiboson = openDiboson.Get("monoHbb_Topmu_boosted")
        EventsDiboson = treeDiboson.GetEntries()
        
        for i in range(EventsDiboson):
            treeDiboson.GetEntry(i)
            CSV_Diboson = getattr(treeDiboson, 'FJetCSV')
            SD_Diboson = getattr(treeDiboson, 'FJetMass')
            dPhi_Diboson = getattr(treeDiboson, 'min_dPhi')
            nJets_Diboson = getattr(treeDiboson, 'nJets')
            pt_Diboson = getattr(treeDiboson, 'FJetPt')
            met_Diboson = getattr(treeDiboson, 'MET')
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0) and (pt_Diboson > lowerpT) and (pt_Diboson <= upperpT):
                h_Diboson.Fill(CSV_Diboson)
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0) and (CSV_Diboson > 0.86) and (pt_Diboson > lowerpT) and (pt_Diboson <= upperpT):
                h_DibosonPassed.Fill(CSV_Diboson)
            if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (nJets_Diboson <= 2.0) and (CSV_Diboson <= 0.86) and (pt_Diboson > lowerpT) and (pt_Diboson <= upperpT):
                h_DibosonFailed.Fill(CSV_Diboson)
    
        h_Diboson = h_Diboson*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        h_DibosonPassed = h_DibosonPassed*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        h_DibosonFailed = h_DibosonFailed*(vers[0]*xsDiboson[k]/totalEventsDiboson)
        
        h_sumDiboson += h_Diboson
        h_sumDibosonPassed += h_DibosonPassed
        h_sumDibosonFailed += h_DibosonFailed


    #---------------------------------#
    #              Single t           #
    #---------------------------------#

    if year_ == 2017:
        ST_files = ["combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]
    if year_ == 2018:
        ST_files = ["combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]

    xsST = [3.74, 67.91, 113.3, 34.97, 34.91]

    h_ST = TH1F("h_ST", "", nbins, edges)
    h_STPassed = TH1F("h_STPassed", "", nbins, edges)
    h_STFailed = TH1F("h_STFailed", "", nbins, edges)

    h_sumST = TH1F("h_sumST", "", nbins, edges)
    h_sumSTPassed = TH1F("h_sumSTPassed", "", nbins, edges)
    h_sumSTFailed = TH1F("h_sumSTFailed", "", nbins, edges)

    for k in range(len(ST_files)):
        h_ST.Reset()
        h_STPassed.Reset()
        h_STFailed.Reset()
        
        openST = TFile(vers[1]+ST_files[k], "read")
        h_total_mcweight_ST = openST.Get("h_total_mcweight")
        totalEventsST = h_total_mcweight_ST.Integral()
        if isTope == "True":
            treeST = openST.Get("monoHbb_Tope_boosted")
        else:
            treeST = openST.Get("monoHbb_Topmu_boosted")
        EventsST = treeST.GetEntries()
        
        for i in range(EventsST):
            treeST.GetEntry(i)
            CSV_ST = getattr(treeST, 'FJetCSV')
            SD_ST = getattr(treeST, 'FJetMass')
            dPhi_ST = getattr(treeST, 'min_dPhi')
            nJets_ST = getattr(treeST, 'nJets')
            pt_ST = getattr(treeST, 'FJetPt')
            met_ST = getattr(treeST, 'MET')
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (nJets_ST <= 2) and (pt_ST > lowerpT) and (pt_ST <= upperpT):
                h_ST.Fill(CSV_ST)
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (CSV_ST > 0.86) and (nJets_ST <= 2) and (pt_ST > lowerpT) and (pt_ST <= upperpT):
                h_STPassed.Fill(CSV_ST)
            if (SD_ST > 100.0) and (SD_ST < 150.0) and (dPhi_ST > 0.4) and (CSV_ST <= 0.86) and (nJets_ST <= 2) and (pt_ST > lowerpT) and (pt_ST <= upperpT):
                h_STFailed.Fill(CSV_ST)

        h_ST = h_ST*(vers[0]*xsST[k]/totalEventsST)
        h_STPassed = h_STPassed*(vers[0]*xsST[k]/totalEventsST)
        h_STFailed = h_STFailed*(vers[0]*xsST[k]/totalEventsST)
        
        h_sumST += h_ST
        h_sumSTPassed += h_STPassed
        h_sumSTFailed += h_STFailed



    #---------------------------------#
    #               DATA              #
    #---------------------------------#

    if isTope == "True":
        Data_path = vers[1]+"combined_data_SE.root"
    else:
        Data_path = vers[1]+"combined_data_MET.root"

    h_Data = TH1F("h_Data", "", nbins, edges)
    h_Data_Failed = TH1F("h_Data_Failed", "", nbins, edges)
    h_Data_Passed = TH1F("h_Data_Passed", "", nbins, edges)

    openData = TFile(Data_path, "read")
    h_total_mcweight_Data = openData.Get("h_total_mcweight")
    totalEventsData = h_total_mcweight_Data.Integral()
    if isTope == "True":
        treeData = openData.Get("monoHbb_Tope_boosted")
    else:
        treeData = openData.Get("monoHbb_Topmu_boosted")
    EventsData = treeData.GetEntries()

    for i in range(EventsData):
        treeData.GetEntry(i)
        CSV_Data = getattr(treeData, 'FJetCSV')
        SD_Data = getattr(treeData, 'FJetMass')
        dPhi_Data = getattr(treeData, 'min_dPhi')
        nJets_Data = getattr(treeData, 'nJets')
        pt_Data = getattr(treeData, 'FJetPt')
        met_Data = getattr(treeData, 'MET')
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0) and (pt_Data > lowerpT) and (pt_Data <= upperpT):
            h_Data.Fill(CSV_Data)
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0) and (CSV_Data > 0.86) and (pt_Data > lowerpT) and (pt_Data <= upperpT):
            h_Data_Passed.Fill(CSV_Data)
        if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2.0) and (CSV_Data <= 0.86) and (pt_Data > lowerpT) and (pt_Data <= upperpT):
            h_Data_Failed.Fill(CSV_Data)

    SubtractedData = h_Data.Clone("SubtractedData")
    SubtractedData = SubtractedData - (h_sumWJets + h_sumDiboson + h_sumST)
    SubtractedDataPassed = h_Data_Passed.Clone("SubtractedDataPassed")
    SubtractedDataPassed = SubtractedDataPassed - (h_sumWJetsPassed + h_sumDibosonPassed + h_sumSTPassed)
    SubtractedDataFailed = h_Data_Failed.Clone("SubtractedDataFailed")
    SubtractedDataFailed = SubtractedDataFailed - (h_sumWJetsFailed + h_sumDibosonFailed + h_sumSTFailed)


    h_totaldata = SubtractedDataPassed.Clone("h_totaldata")
    h_totaldata = h_totaldata + SubtractedDataFailed
    frac_tt_data_passed = (SubtractedDataPassed.Integral())/(h_totaldata.Integral())
    frac_tt_data_failed = (SubtractedDataFailed.Integral())/(h_totaldata.Integral())*100
    
    
    
    #------------Overlap histograms in Full Canvas-------------#
    
    frac_match_text = str(round(frac_match, 2))
    frac_Wmatch_text = str(round(frac_Wmatch, 2))
    frac_unmatch_text = str(round(frac_unmatch, 2))
    
    
    h_TopMatchFinal = h_TopMatch.Clone("h_TopMatchFinal")
    h_WmatchFinal = h_Wmatch.Clone("h_WmatchFinal")
    h_unmatchFinal = h_unmatch.Clone("h_unmatchFinal")
    h_sumWJetsFinal = h_sumWJets.Clone("h_sumWJetsFinal")
    h_sumSTFinal = h_sumST.Clone("h_sumSTFinal")
    
    h_sumSTFinal = h_sumSTFinal + h_sumDiboson
    h_sumWJetsFinal = h_sumWJetsFinal + h_sumSTFinal
    h_unmatchFinal = h_unmatchFinal + h_sumWJetsFinal
    h_WmatchFinal = h_WmatchFinal + h_unmatchFinal
    h_TopMatchFinal = h_TopMatchFinal + h_WmatchFinal
    
    full = TCanvas("full","",800,900) #width-height
    full.SetTopMargin(0.4)
    full.SetBottomMargin(0.05)
    full.SetRightMargin(0.1)
    full.SetLeftMargin(0.15)
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
    
    leg = TLegend(0.65,0.7,0.85,0.87)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.027)
    
    binvalues1 = []
    for i in range(nbins):
        binvalue = h_Data.GetBinContent(i)
        binvalues1.append(binvalue)
    totalmax = max(binvalues1) + 100
    
    padMain.cd()
    
    h_TopMatchFinal.SetFillColor(821)
    h_TopMatchFinal.SetLineColor(821)#923
    h_TopMatchFinal.GetXaxis().SetTitle("DDB")
    h_TopMatchFinal.GetXaxis().SetLabelSize(0)
    h_TopMatchFinal.GetYaxis().SetTitle("Events/Bin")
    h_TopMatchFinal.GetYaxis().SetTitleSize(0.05)
    h_TopMatchFinal.GetYaxis().SetLabelSize(0.05)
    h_TopMatchFinal.SetMaximum(totalmax)
    leg.AddEntry(h_TopMatchFinal, "Top (mtch.) ("+frac_match_text+"%)", "f")
    
    h_WmatchFinal.SetFillColor(822)
    h_WmatchFinal.SetLineColor(822)
    leg.AddEntry(h_WmatchFinal, "Top (W-mtch.) ("+frac_Wmatch_text+"%)","f")
    
    h_unmatchFinal.SetFillColor(813)
    h_unmatchFinal.SetLineColor(813)
    leg.AddEntry(h_unmatchFinal, "Top (unmtch.) ("+frac_unmatch_text+"%)","f")
    
    h_sumWJetsFinal.SetFillColor(854)
    h_sumWJetsFinal.SetLineColor(854)
    leg.AddEntry(h_sumWJetsFinal, "W+Jets","f")
    
    h_sumSTFinal.SetFillColor(800)
    h_sumSTFinal.SetLineColor(800)
    leg.AddEntry(h_sumSTFinal, "Single Top","f")
    
    h_sumDiboson.SetFillColor(627)
    h_sumDiboson.SetLineColor(627)
    leg.AddEntry(h_sumDiboson, "Diboson","f")
    
    h_Data.SetLineColor(1)
    h_Data.SetMarkerStyle(20)
    h_Data.SetMarkerSize(1.5)
    leg.AddEntry(h_Data, "Data", "lep")
    
    #-------Draw Histogram in Full Canvas---------#
    
    h_TopMatchFinal.Draw("hist")
    h_WmatchFinal.Draw("histsame")
    h_unmatchFinal.Draw("histsame")
    h_sumWJetsFinal.Draw("histsame")
    h_sumSTFinal.Draw("histsame")
    h_sumDiboson.Draw("histsame")
    h_Data.Draw("e1same")
    leg.Draw()
    
    lt = TLatex()
    if upperpT == 2000:
        lt.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{p_{T} "+str(lowerpT)+"-Inf GeV}}")
    else:
        lt.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{p_{T} "+str(lowerpT)+"-"+str(upperpT)+" GeV}}")
    lt.DrawLatexNDC(0.24,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt.DrawLatexNDC(0.24,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")
    
    
    padRatio.cd()
    
    gPad.GetUymax()
    
    totalData = h_Data.Clone("totalData")
    ratio = dataPredRatio(data_ = totalData, totalBkg_ = h_TopMatchFinal)
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
    ratio.GetXaxis().SetTitle("DDB")
    ratio.Draw("e1")
    
    #full.cd()
    full.Modified()
    full.Update()
    if isTope == "True":
        full.SaveAs(outputpath+"Tope_unsubtracted.pdf")
    else:
        full.SaveAs(outputpath+"Topmu_unsubtracted.pdf")


    #------------Overlap histograms in Subtract Canvas-------------#
    
    Cloned_frac_tt = h_tt.Clone("Cloned_frac_tt")
    Cloned_frac_tt.Rebin(14)
    Cloned_frac_ttFailed = h_ttFailed.Clone("Cloned_frac_ttFailed")
    Cloned_frac_ttFailed.Rebin(14)
    Cloned_frac_ttFailed.Sumw2()
    Cloned_frac_ttFailed.Divide(Cloned_frac_tt)
    frac_Failed_fin = Cloned_frac_ttFailed.Integral()
    ttMC_fraction.append(frac_Failed_fin)
    ttMC_error.append(Cloned_frac_ttFailed.GetBinError(1))
    
    
    Cloned_frac_ttPassed = h_ttPassed.Clone("Cloned_frac_ttPassed")
    Cloned_frac_ttPassed.Rebin(14)
    Cloned_frac_ttPassed.Sumw2()
    Cloned_frac_ttPassed.Divide(Cloned_frac_tt)
    frac_Passed_fin = Cloned_frac_ttPassed.Integral()
    ttMC_fraction.append(frac_Passed_fin)
    ttMC_error.append(Cloned_frac_ttPassed.GetBinError(1))
    
    
    Cloned_frac_tt_data_total = h_totaldata.Clone("Cloned_frac_tt_data_total")
    Cloned_frac_tt_data_total.Rebin(14)
    Cloned_frac_tt_data_failed = SubtractedDataFailed.Clone("Cloned_frac_tt_data_failed")
    Cloned_frac_tt_data_failed.Rebin(14)
    Cloned_frac_tt_data_failed.Sumw2()
    Cloned_frac_tt_data_failed.Divide(Cloned_frac_tt_data_total)
    frac_ttData_fail = Cloned_frac_tt_data_failed.Integral()
    ttData_fraction.append(frac_ttData_fail)
    ttData_error.append(Cloned_frac_tt_data_failed.GetBinError(1))
    
    
    Cloned_frac_tt_data_passed = SubtractedDataPassed.Clone("Cloned_frac_tt_data_passed")
    Cloned_frac_tt_data_passed.Rebin(14)
    Cloned_frac_tt_data_passed.Sumw2()
    Cloned_frac_tt_data_passed.Divide(Cloned_frac_tt_data_total)
    frac_ttData_pass = Cloned_frac_tt_data_passed.Integral()
    ttData_fraction.append(frac_ttData_pass)
    ttData_error.append(Cloned_frac_tt_data_passed.GetBinError(1))
    
    frac_Passed_text = str(round(frac_Passed_fin*100, 2))
    
    subtract = TCanvas("subtract","",900,700) #width-height
    subtract.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)
    
    leg2 = TLegend(0.4,0.5,0.6,0.6)
    leg2.SetBorderSize(0)
    leg2.SetTextSize(0.027)

    binvalues2 = []
    for i in range(nbins):
        binvalue = SubtractedData.GetBinContent(i)
        binvalues2.append(binvalue)
    ttmax = max(binvalues2) + 50
    
    #h_ttFailed.Rebin(2)
    h_ttFailed.SetFillColor(821)
    h_ttFailed.SetLineColor(821)#922
    h_ttFailed.GetXaxis().SetTitle("DDB")
    h_ttFailed.GetYaxis().SetTitle("Events/Bin")
    h_ttFailed.SetMaximum(ttmax)
    leg2.AddEntry(h_ttFailed, "t#bar{t}", "f")
    
    #h_ttPassed.Rebin(2)
    h_ttPassed.SetFillColor(622)
    h_ttPassed.SetLineColor(622)
    h_ttPassed.GetXaxis().SetTitle("DDB")
    h_ttPassed.GetYaxis().SetTitle("Events/Bin")
    h_ttPassed.SetMaximum(ttmax)
    leg2.AddEntry(h_ttPassed, "t#bar{t} mistag ("+frac_Passed_text+"%)", "f")
    
    #SubtractedData.Rebin(2)
    SubtractedData.SetLineColor(1)
    SubtractedData.SetMarkerStyle(20)
    SubtractedData.SetMarkerSize(1.5)
    SubtractedData.GetXaxis().SetTitle("DDB")
    SubtractedData.GetYaxis().SetTitle("Events/Bin")
    leg2.AddEntry(SubtractedData, "Subtracted Data", "lep")
    
    #-------Draw Histogram in Subtract Canvas---------#
    
    h_ttFailed.Draw("hist")
    h_ttPassed.Draw("histsame")
    SubtractedData.Draw("e1same")
    leg2.Draw()
    
    lt2 = TLatex()
    if upperpT == 2000:
        lt2.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{p_{T} "+str(lowerpT)+"-Inf GeV}}")
    else:
        lt2.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{p_{T} "+str(lowerpT)+"-"+str(upperpT)+" GeV}}")
    lt2.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt2.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt2.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt2.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")
    
    #subtract.cd()
    subtract.Modified()
    subtract.Update()
    if isTope == "True":
        subtract.SaveAs(outputpath+"Tope_subtracted.pdf")
    else:
        subtract.SaveAs(outputpath+"Topmu_subtracted.pdf")
    
    
    #------------Overlap histograms in Scalefactor Canvas-------------#
    
    #** MISTAG SCALE FACTOR **#
    
    SF = frac_tt_data_passed / frac_Passed_fin
    print " "
    print "DDB Mistag SF :", SF
    print " "
    
    scalefactor = TCanvas("scalefactor","", 700, 900)
    scalefactor.SetTopMargin(0.1)
    scalefactor.SetBottomMargin(0.15)
    scalefactor.SetRightMargin(0.1)
    scalefactor.SetLeftMargin(0.15)
    gStyle.SetOptStat(0)
    
    pad1 = TPad("pad1", "", 0.01, 0.25, 0.93, 1.0)
    pad1.SetTopMargin(0.1)
    pad1.SetRightMargin(0.05)
    pad1.SetLeftMargin(0.17)
    pad1.SetBottomMargin(0.05)
    
    pad2 = TPad("pad2", "", 0.0, 0.0, 0.375, 0.24)
    pad2.SetTopMargin(0.0)
    pad2.SetRightMargin(0.1)
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
    
    #** Pad1 **#
    pad1.cd()
    
    leg3 = TLegend(0.5,0.55,0.7,0.65)
    leg3.SetBorderSize(0)
    leg3.SetTextSize(0.027)
    
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
    mg.Draw("AP")
    mg.GetHistogram().SetMaximum(1.5)
    mg.GetHistogram().SetMinimum(0)
    mg.GetHistogram().GetYaxis().SetTitle("Fraction")
    gPad.Modified()
    mg.GetXaxis().SetLimits(0,3)
    mg.GetXaxis().SetTickLength(0.03)
    mg.GetXaxis().SetNdivisions(103)
    mg.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Fail")
    mg.GetXaxis().ChangeLabel(1,-1,0)
    mg.GetXaxis().ChangeLabel(-1,-1,0)
    mg.GetXaxis().ChangeLabel(3,-1,-1,-1,-1,-1,"Pass")
    leg3.Draw()
    
    lt3 = TLatex()
    if upperpT == 2000:
        lt3.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{p_{T} "+str(lowerpT)+"-Inf GeV}}")
    else:
        lt3.DrawLatexNDC(0.17,0.92,"#scale[0.7]{#bf{p_{T} "+str(lowerpT)+"-"+str(upperpT)+" GeV}}")
    lt3.DrawLatexNDC(0.19,0.855,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
    if isTope == "True":
        lt3.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (e)}}")
    else:
        lt3.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
    lt3.DrawLatexNDC(0.19,0.755,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
    if year_ == 2017:
        lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
    if year_ == 2018:
        lt3.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{58.827 fb^{-1} (13 TeV)}}")
    lt3.Draw()
    
    pad1.Update()
    
    #** Pad2 **#
    pad2.cd()
    
    Cloned_frac_ttPassed.SetLineColor(870)
    Cloned_frac_ttPassed.SetLineWidth(3)
    Cloned_frac_ttPassed.SetMarkerColor(870)
    Cloned_frac_ttPassed.SetMarkerStyle(20)
    Cloned_frac_ttPassed.GetYaxis().SetTitle("Fraction")
    Cloned_frac_ttPassed.GetYaxis().SetTitleSize(0.09)
    Cloned_frac_ttPassed.GetYaxis().SetLabelSize(0.1)
    Cloned_frac_ttPassed.GetYaxis().SetNdivisions(404)
    Cloned_frac_ttPassed.SetMaximum(0.3)#0.3
    Cloned_frac_ttPassed.SetMinimum(0.0)#0.0
    Cloned_frac_ttPassed.GetXaxis().SetTitle("")
    Cloned_frac_ttPassed.GetXaxis().SetLabelSize(0.09)
    Cloned_frac_ttPassed.GetXaxis().SetLabelOffset(0.02)
    Cloned_frac_ttPassed.GetXaxis().SetNdivisions(104)
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Pass")
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(1,-1,0)
    Cloned_frac_ttPassed.GetXaxis().ChangeLabel(-1,-1,0)
    
    Cloned_frac_tt_data_passed.SetLineColor(1)
    Cloned_frac_tt_data_passed.SetLineWidth(2)
    Cloned_frac_tt_data_passed.SetMarkerColor(1)
    Cloned_frac_tt_data_passed.SetMarkerStyle(20)
    
    Cloned_frac_ttPassed.Draw("e1")
    Cloned_frac_tt_data_passed.Draw("e1histsame")
    
    
    #** Pad3 **#
    pad3.cd()
    
    mistagSF = Cloned_frac_tt_data_passed.Clone("mistagSF")
    mistagSF.Sumw2()
    mistagSF.Divide(Cloned_frac_ttPassed)
    
    #print "******"
    #print "mistag SF:", mistagSF.Integral()
    
    SFfinal = round(SF, 3)
    SFtext = "SF = "+str(SFfinal)
    
    mistagSFmax = SF + 0.2
    mistagSFmin = SF - 0.2
    
    mistagSF.SetLineColor(797)
    mistagSF.SetMarkerColor(797)
    mistagSF.SetLineWidth(3)
    mistagSF.SetMaximum(mistagSFmax)
    mistagSF.SetMinimum(mistagSFmin)
    mistagSF.GetXaxis().SetTitle(" ")
    mistagSF.GetXaxis().SetLabelOffset(999)
    mistagSF.GetXaxis().SetLabelSize(0)
    mistagSF.GetXaxis().SetTickLength(0)
    mistagSF.GetYaxis().SetLabelSize(0.1)
    mistagSF.GetYaxis().SetNdivisions(404)
    mistagSF.GetYaxis().SetTitle(" ")
    
    mistagSF.Draw("e1hist")
    
    pt = TPaveText(0.21, 0.72, 0.31, 0.8, "brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(42)
    pt.SetTextSize(0.1)
    pt.AddText(SFtext)
    pt.Draw()
    
    scalefactor.Modified()
    scalefactor.Update()
    if isTope == "True":
        scalefactor.SaveAs(outputpath+"Tope_SF.pdf")
    else:
        scalefactor.SaveAs(outputpath+"Topmu_SF.pdf")
    
    
    # Save the canvases in root file #
    if isTope == "True":
        print "\nGenerating TopE.root"
        
        outfile = TFile(outputpath+"TopE.root", "RECREATE")
    else:
        print "\nGenerating TopMu.root"
        
        outfile = TFile(outputpath+"TopMu.root", "RECREATE")
    h_TopMatch.Write()
    h_Wmatch.Write()
    h_unmatch.Write()
    h_sumWJets.Write()
    h_sumDiboson.Write()
    h_sumST.Write()
    h_Data.Write()
    
    h_ttFailed.Write()
    h_ttPassed.Write()
    SubtractedData.Write()
    
    SubtractedDataFailed.Write()
    SubtractedDataPassed.Write()
    h_totaldata.Write()
    h_tt.Write()
    
    h_Data_Passed.Write()
    h_sumWJetsPassed.Write()
    h_sumDibosonPassed.Write()
    h_sumSTPassed.Write()
    
    h_Data_Failed.Write()
    h_sumWJetsFailed.Write()
    h_sumDibosonFailed.Write()
    h_sumSTFailed.Write()
    
    outfile.Close()
    if isTope == "True":
        print "Finish generating TopE.root"
    else:
        print "Finish generating TopMu.root"
    
    
    #get the statistical uncertainty#
    
    dx = ttData_error[1]
    #print "data efficiency error", dx
    
    dy = ttMC_error[1]
    #print "MC efficiency error", dy
    
    x = frac_tt_data_passed
    y = frac_Passed_fin
    
    statUnc = TMath.Sqrt(( (dx**2)/(y**2) ) + ( (x**2)*(dy**2)/(y**4) ) )
    #print "statistical Uncertainty in Top (e) CR", statUnc
    #print " "
    if isTope == "True":
        print "\nrelative statistical Uncertainty in Top (e) CR", statUnc/SF*100, " %"
    else:
        print "\nrelative statistical Uncertainty in Top (mu) CR", statUnc/SF*100, " %"
    print ""

    if isTope == "True":
        header = ["Process", "Number of Events", "Top (e)"]
    else:
        header = ["Process", "Number of Events", "Top (mu)"]
    row1 = [" ", "DDB mistag SF", str(round(SF, 3)) + " +- " + str(round(statUnc,3)) + " (stat)"]
    row2 = ["tt MC", "Pass (not normalized)", str(ttMCpassNotNormalized)]
    row3 = [" ", "Pass (normalized)", str(round(h_ttPassed.Integral(),2))]
    row4 = [" ", "Fail (not normalized)", str(ttMCfailNotNormalized)]
    row5 = [" ", "Fail (normalized)", str(round(h_ttFailed.Integral(),2))]
    row6 = [" ", "Total (not normalized)", str(ttMCtotalNotNormalized)]
    row7 = [" ", "Total (normalized)", str(round(h_tt.Integral(),2))]

    inforMC = [row2, row3, row4, row5, row6, row7]

    row8 = ["tt DATA", "Pass (before subtraction)", str(round(h_Data_Passed.Integral(),2))]
    row9 = [" ", "Pass (after subtraction)", str(round(SubtractedDataPassed.Integral(),2))]
    row10 = [" ", "Fail (before subtraction)", str(round(h_Data_Failed.Integral(),2))]
    row11 = [" ", "Fail (after subtraction)", str(round(SubtractedDataFailed.Integral(),2))]
    row12 = [" ", "Total (before subtraction)", str(round(h_Data.Integral(),2))]
    row13 = [" ", "Total (after subtraction)", str(round(h_totaldata.Integral(),2))]

    inforDATA = [row8, row9, row10, row11, row12, row13]

    row14 = ["Background", "Pass (normalized)", str(round((h_sumWJetsPassed + h_sumDibosonPassed + h_sumSTPassed).Integral(),2))]
    row15 = [" ", "Fail (normalized)", str(round((h_sumWJetsFailed + h_sumDibosonFailed + h_sumSTFailed).Integral(),2))]
    row16 = [" ", "Total (normalized)", str(round((h_sumWJets + h_sumDiboson + h_sumST).Integral(),2))]

    inforBKG = [row14, row15, row16]

    makeTable(header, row1, inforMC, inforDATA, inforBKG)




if __name__ == '__main__':
    gROOT.SetBatch(True)
    
    parser = argparse.ArgumentParser(description='Calculate and draw plots of DDB mistag scale factor')
    
    #add command
    parser.add_argument('-WI', help='Analyze inclusive with single top')
    parser.add_argument('-WMET', help='Analyze MET bin with single top')
    parser.add_argument('-WPT', help='Analyze PT bin with single top')
    parser.add_argument('-Y', dest='discrepancy', help='Add the year of the data set')
    parser.add_argument('-isTope', help='Analyze whether Top (e) or Top (mu) region')
    
    #Get arguments from the user
    args = parser.parse_args()
    
    if args.discrepancy:
        if args.isTope:
            if args.WI:
                withSingleTopAndInclusive(str(args.WI), int(args.discrepancy), args.isTope)
    
            if args.WMET:
                inbins = (args.WMET).split("-")
                withSingleTopAndMETbins(int(inbins[1]), int(inbins[2]), int(args.discrepancy), args.isTope)

            if args.WPT:
                inbins = (args.WPT).split("-")
                withSingleTopAndpTbins(int(inbins[1]), int(inbins[2]), int(args.discrepancy), args.isTope)





#print "theoretical statistical uncertainty of data efficiency", TMath.Sqrt((x*(1-x))/(h_totaldata.Integral()))
#print "theoretical statistical uncertainty of MC efficiency", TMath.Sqrt((y*(1-y))/(h_tt.Integral()))
#print " "



'''
#get the SFnew = SFold = SF

Ndp = h_Data_Passed.Integral()
Nsdt = SubtractedData.Integral()
Nbp = (h_sumWJetsPassed + h_sumDibosonPassed).Integral()

SFno = Ndp/(frac_Passed_fin*Nsdt+Nbp)
print "SFnew = SFold = SF =", SFno
'''


