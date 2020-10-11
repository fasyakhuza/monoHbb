#created by Fasya Khuzaimah on 2020.07.08

import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TLegend, TAxis, TLatex, TPad, TPaveText, TMath, gStyle, gPad
import array as arr
import argparse


nbins = 14
edges = arr.array('f', [0.0, 0.08, 0.16, 0.23, 0.30, 0.37, 0.44, 0.51, 0.58, 0.65, 0.72, 0.79, 0.86, 0.93, 1.0])

def fixed_length(text, length):
    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " "*length)[:length]
    return text

def makeTable(header, row1, XSuncertainties, LumiUncertaintiesList, TotalSysList):
    hashtaglength = 176
    length = 20
    
    #print header
    print "#"*hashtaglength
    print "# ",
    for column in header:
        print fixed_length(column,length), " # ",
    print ""
    print "#"*hashtaglength

    #print row 1 = header 2
    print "# ",
    for column in row1:
        print fixed_length(column,length), " # ",
    print ""
    print "#"*hashtaglength
    
    #print Cross Section Uncertainties
    print "# ",
    for column in XSuncertainties:
        print fixed_length(column,length), " # ",
    print ""
    print "#"*hashtaglength

    #print Luminosity Uncertainties
    print "# ",
    for column in LumiUncertaintiesList:
        print fixed_length(column,length), " # ",
    print ""
    print "#"*hashtaglength

    #print the Total Systematic Uncertainties
    print "# ",
    for column in TotalSysList:
        print fixed_length(column,length), " # ",
    print ""
    print "#"*hashtaglength

ttDataEfficiencyList = []
tthistoUpTopE = []
tthistoUpTopMu = []
tthistoDownTopE = []
tthistoDownTopMu = []
dataPassUpTopE = []
dataPassUpTopMu = []
dataPassDownTopE = []
dataPassDownTopMu = []
dataTotalUpTopE = []
dataTotalUpTopMu = []
dataTotalDownTopE = []
dataTotalDownTopMu = []

def priorSFlists(year_):
    if year_ == 2017:
        '''
        #monohbb.v06.00.01.2017_NCU
        numberpriorSFinclusive = [0.880, 0.817, 0.842]
        numberpriorSFpt200_350 = [0.959, 0.781, 0.852]
        numberpriorSFpt350_500 = [0.828, 0.901, 0.871]
        numberpriorSFpt500_inf = [0.807, 0.417, 0.565]
        numberpriorSFmet200_270 = [0.834, 0.720, 0.762]
        numberpriorSFmet270_345 = [0.582, 0.747, 0.687]
        numberpriorSFmet345_1000 = [1.567, 0.747, 0.940]
        '''
        
        #monohbb.v06.00.05.2017_NCU
        numberpriorSFinclusive = [0.846, 0.833, 0.838]
        numberpriorSFpt200_350 = [0.856, 0.817, 0.832]
        numberpriorSFpt350_500 = [0.844, 0.862, 0.856]
        numberpriorSFpt500_inf = [0.722, 0.657, 0.682]
        numberpriorSFmet200_270 = [0.88, 0.789, 0.822]
        numberpriorSFmet270_345 = [0.661, 0.774, 0.740]
        numberpriorSFmet345_1000 = [1.096, 0.762, 0.855]
    

    if year_ == 2018:
        numberpriorSFinclusive = [0.852, 0.881, 0.869]
        numberpriorSFpt200_350 = [0.806, 0.862, 0.839]
        numberpriorSFpt350_500 = [0.882, 0.895, 0.889]
        numberpriorSFpt500_inf = [0.967, 0.909, 0.937]
        numberpriorSFmet200_270 = [0.878, 0.766, 0.811]
        numberpriorSFmet270_345 = [0.857, 0.967, 0.93]
        numberpriorSFmet345_1000 = [0.627, 0.945, 0.799]

    return [numberpriorSFinclusive, numberpriorSFpt200_350, numberpriorSFpt350_500, numberpriorSFpt500_inf, numberpriorSFmet200_270, numberpriorSFmet270_345, numberpriorSFmet345_1000]


def getXSuncertainties(Data_path, treeName, year_, ana, isEle, isUp):
    #print "\nGetting Systematic Uncertainty from Cross Section"
    
    if year_ == 2017:
        L = 41500.0#/pb ; integrated luminosity
        version = "monohbb.v06.00.05.2017_NCU/"
        #print "\nProcessing 2017 data, ", version, " version"
    if year_ == 2018:
        L = 58827.0#/pb ; integrated luminosity
        version = "monohbb.v06.00.05.2018_NCU/"
        #print "\nProcessing 2018 data, ", version, " version"
    
    dirpath = "/afs/cern.ch/work/f/fkhuzaim/DDB_MistagSF/"+version+"combined/"

    if ana == "Inclusive":
        numberpriorSF = numberpriorSFinclusive
    if ana == "PT-200-350":
        numberpriorSF = numberpriorSFpt200_350
    if ana == "PT-350-500":
        numberpriorSF = numberpriorSFpt350_500
    if ana == "PT-500-2000":
        numberpriorSF = numberpriorSFpt500_inf
    if ana == "MET-200-270":
        numberpriorSF = numberpriorSFmet200_270
    if ana == "MET-270-345":
        numberpriorSF = numberpriorSFmet270_345
    if ana == "MET-345-1000":
        numberpriorSF = numberpriorSFmet345_1000

    
    if year_ == 2017:
        Top_path = "combined_crab_TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root"
    if year_ == 2018:
        Top_path = "combined_crab_TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8.root"
    xsTop = 300.9498
    
    
    #---------------------------------#
    #           Background            #
    #---------------------------------#
    
    if year_ == 2017:
        Bkg_files = ["combined_crab_WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_ZZ_TuneCP5_13TeV-pythia8.root", "combined_crab_WW_TuneCP5_13TeV-pythia8.root", "combined_crab_WZ_TuneCP5_13TeV-pythia8.root", "combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]
    if year_ == 2018:
        Bkg_files = ["combined_crab_WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_ZZ_TuneCP5_13TeV-pythia8.root", "combined_crab_WW_TuneCP5_13TeV-pythia8.root", "combined_crab_WZ_TuneCP5_13TeV-pythia8.root", "combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]
    
    xsBkg = [1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 12.14, 75.8, 27.6, 3.74, 67.91, 113.3, 34.97, 34.91]
    sigmaXSbkgUp = [53.63775, 15.68376, 2.21011, 0.49485, 0.20632, 0.0413, 0.000308, 0.67984, 4.169, 1.794, 0.1450, 2.8292, 4.7202, 0.8779, 0.8764]
    sigmaXSbkgDown = [52.7868, 15.43494, 2.17504, 0.487, 0.20305, 0.04064, 0.0003028, 0.67984, 4.169, 1.794, 0.1305, 2.4130, 4.0258, 0.8779, 0.8764]

    '''
    print " "
    print "Processing tt To Semilepronic MC"
    print " "
    '''
    
    h_ttFailed = TH1F("h_ttFailed", "", nbins, edges)
    h_ttPassed = TH1F("h_ttPassed", "", nbins, edges)

    openTop = TFile(dirpath+Top_path, "read")
    h_total_mcweight_Top = openTop.Get("h_total_mcweight")
    totalEventsTop = h_total_mcweight_Top.Integral()
    treeTop = openTop.Get(treeName)
    EventsTop = treeTop.GetEntries()

    for i in range(EventsTop):
        treeTop.GetEntry(i)
        st_TopMatching = getattr(treeTop, 'st_TopMatching')
        CSV_Top = getattr(treeTop, 'FJetCSV')
        SD_Top = getattr(treeTop, 'FJetMass')
        dPhi_Top = getattr(treeTop, 'min_dPhi')
        N2DDT_Top = getattr(treeTop, 'N2DDT')
        nJets_Top = getattr(treeTop, 'nJets')
        pt_Top = getattr(treeTop, 'FJetPt')
        met_Top = getattr(treeTop, 'MET')
        if ana == "Inclusive":
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top <= 0.86) and (nJets_Top <= 2):
                h_ttFailed.Fill(CSV_Top)
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86) and (nJets_Top <= 2):
                h_ttPassed.Fill(CSV_Top)
        if ana == "MET-200-270" or ana == "MET-270-345" or ana == "MET-345-1000":
            metbins = ana.split("-")
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top <= 0.86) and (nJets_Top <= 2) and (met_Top > int(metbins[1])) and (met_Top <= int(metbins[2])):
                h_ttFailed.Fill(CSV_Top)
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86) and (nJets_Top <= 2) and (met_Top > int(metbins[1])) and (met_Top <= int(metbins[2])):
                h_ttPassed.Fill(CSV_Top)
        if ana == "PT-200-350" or ana == "PT-350-500" or ana == "PT-500-2000":
            ptbins = ana.split("-")
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top <= 0.86) and (nJets_Top <= 2) and (pt_Top > int(ptbins[1])) and (pt_Top <= int(ptbins[2])):
                h_ttFailed.Fill(CSV_Top)
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86) and (nJets_Top <= 2) and (pt_Top > int(ptbins[1])) and (pt_Top <= int(ptbins[2])):
                h_ttPassed.Fill(CSV_Top)

    h_ttFailed = h_ttFailed*(L*xsTop/totalEventsTop)
    h_ttPassed = h_ttPassed*(L*xsTop/totalEventsTop)
    h_tt = h_ttFailed.Clone("h_tt")
    h_tt = h_tt + h_ttPassed

    if isUp and isEle:
        tthistoUpTopE.append(h_ttPassed)
        tthistoUpTopE.append(h_tt)
    if isUp and not isEle:
        tthistoUpTopMu.append(h_ttPassed)
        tthistoUpTopMu.append(h_tt)
    if not isUp and isEle:
        tthistoDownTopE.append(h_ttPassed)
        tthistoDownTopE.append(h_tt)
    if not isUp and not isEle:
        tthistoDownTopMu.append(h_ttPassed)
        tthistoDownTopMu.append(h_tt)

    ttMCefficiency = (h_ttPassed.Integral())/(h_tt.Integral())
    #print "Efficiency of tt MC:", ttMCefficiency
    

    #print "\nProcessing Data and Background"

    SFlist = []
    UncList = []
    UncInPercentageList = []
    
    del SFlist[:]
    del UncList[:]
    del UncInPercentageList[:]
    del ttDataEfficiencyList[:]
    
    h_Data = TH1F("h_Data", "", nbins, edges)
    h_Data_Failed = TH1F("h_Data_Failed", "", nbins, edges)
    h_Data_Passed = TH1F("h_Data_Passed", "", nbins, edges)
    
    h_Bkg = TH1F("h_Bkg", "", nbins, edges)
    h_BkgPass = TH1F("h_BkgPass", "", nbins, edges)
    h_BkgFail = TH1F("h_BkgFail", "", nbins, edges)

    h_sumBkg = TH1F("h_sumBkg", "", nbins, edges)
    h_sumBkgPass = TH1F("h_sumBkgPass", "", nbins, edges)
    h_sumBkgFail = TH1F("h_sumBkgFail", "", nbins, edges)


    for j in range(len(xsBkg)):
        
        h_Data.Reset()
        h_Data_Passed.Reset()
        h_Data_Failed.Reset()
        h_sumBkg.Reset()
        h_sumBkgPass.Reset()
        h_sumBkgFail.Reset()
        
        openData = TFile(dirpath+Data_path, "read")
        h_total_mcweight_Data = openData.Get("h_total_mcweight")
        totalEventsData = h_total_mcweight_Data.Integral()
        treeData = openData.Get(treeName)
        EventsData = treeData.GetEntries()

        for y in range(EventsData):
            treeData.GetEntry(y)
            CSV_Data = getattr(treeData, 'FJetCSV')
            SD_Data = getattr(treeData, 'FJetMass')
            dPhi_Data = getattr(treeData, 'min_dPhi')
            N2DDT_Data = getattr(treeData, 'N2DDT')
            nJets_Data = getattr(treeData, 'nJets')
            pt_Data = getattr(treeData, 'FJetPt')
            met_Data = getattr(treeData, 'MET')
            if ana == "Inclusive":
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2):
                    h_Data.Fill(CSV_Data)
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data <= 0.86) and (nJets_Data <= 2):
                    h_Data_Failed.Fill(CSV_Data)
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data > 0.86) and (nJets_Data <= 2):
                    h_Data_Passed.Fill(CSV_Data)
            if ana == "MET-200-270" or ana == "MET-270-345" or ana == "MET-345-1000":
                metbins = ana.split("-")
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2) and (met_Data > int(metbins[1])) and (met_Data <= int(metbins[2])):
                    h_Data.Fill(CSV_Data)
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data <= 0.86) and (nJets_Data <= 2) and (met_Data > int(metbins[1])) and (met_Data <= int(metbins[2])):
                    h_Data_Failed.Fill(CSV_Data)
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data > 0.86) and (nJets_Data <= 2) and (met_Data > int(metbins[1])) and (met_Data <= int(metbins[2])):
                    h_Data_Passed.Fill(CSV_Data)
            if ana == "PT-200-350" or ana == "PT-350-500" or ana == "PT-500-2000":
                ptbins = ana.split("-")
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2) and (pt_Data > int(ptbins[1])) and (pt_Data <= int(ptbins[2])):
                    h_Data.Fill(CSV_Data)
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data <= 0.86) and (nJets_Data <= 2) and (pt_Data > int(ptbins[1])) and (pt_Data <= int(ptbins[2])):
                    h_Data_Failed.Fill(CSV_Data)
                if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data > 0.86) and (nJets_Data <= 2) and (pt_Data > int(ptbins[1])) and (pt_Data <= int(ptbins[2])):
                    h_Data_Passed.Fill(CSV_Data)

        for k in range(len(Bkg_files)):
            h_Bkg.Reset()
            h_BkgPass.Reset()
            h_BkgFail.Reset()
    
            openkBkg = TFile(dirpath+Bkg_files[k], "read")
            h_total_mcweight_kBkg = openkBkg.Get("h_total_mcweight")
            totalEventskBkg = h_total_mcweight_kBkg.Integral()
            treekBkg = openkBkg.Get(treeName)
            EventskBkg = treekBkg.GetEntries()
    
            for i in range(EventskBkg):
                treekBkg.GetEntry(i)
                CSV_iBkgEvent = getattr(treekBkg, 'FJetCSV')
                SD_iBkgEvent = getattr(treekBkg, 'FJetMass')
                dPhi_iBkgEvent = getattr(treekBkg, 'min_dPhi')
                N2DDT_iBkgEvent = getattr(treekBkg, 'N2DDT')
                nJets_iBkgEvent = getattr(treekBkg, 'nJets')
                pt_iBkgEvent = getattr(treekBkg, 'FJetPt')
                met_iBkgEvent = getattr(treekBkg, 'MET')
                if ana == "Inclusive":
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (nJets_iBkgEvent <= 2):
                        h_Bkg.Fill(CSV_iBkgEvent)
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent <= 0.86) and (nJets_iBkgEvent <= 2):
                        h_BkgFail.Fill(CSV_iBkgEvent)
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent > 0.86) and (nJets_iBkgEvent <= 2):
                        h_BkgPass.Fill(CSV_iBkgEvent)
                if ana == "MET-200-270" or ana == "MET-270-345" or ana == "MET-345-1000":
                    metbins = ana.split("-")
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (nJets_iBkgEvent <= 2) and (met_iBkgEvent > int(metbins[1])) and (met_iBkgEvent <= int(metbins[2])):
                        h_Bkg.Fill(CSV_iBkgEvent)
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent <= 0.86) and (nJets_iBkgEvent <= 2) and (met_iBkgEvent > int(metbins[1])) and (met_iBkgEvent <= int(metbins[2])):
                        h_BkgFail.Fill(CSV_iBkgEvent)
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent > 0.86) and (nJets_iBkgEvent <= 2) and (met_iBkgEvent > int(metbins[1])) and (met_iBkgEvent <= int(metbins[2])):
                        h_BkgPass.Fill(CSV_iBkgEvent)
                if ana == "PT-200-350" or ana == "PT-350-500" or ana == "PT-500-2000":
                    ptbins = ana.split("-")
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (nJets_iBkgEvent <= 2) and (pt_iBkgEvent > int(ptbins[1])) and (pt_iBkgEvent <= int(ptbins[2])):
                        h_Bkg.Fill(CSV_iBkgEvent)
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent <= 0.86) and (nJets_iBkgEvent <= 2) and (pt_iBkgEvent > int(ptbins[1])) and (pt_iBkgEvent <= int(ptbins[2])):
                        h_BkgFail.Fill(CSV_iBkgEvent)
                    if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent > 0.86) and (nJets_iBkgEvent <= 2) and (pt_iBkgEvent > int(ptbins[1])) and (pt_iBkgEvent <= int(ptbins[2])):
                        h_BkgPass.Fill(CSV_iBkgEvent)


            if (k == j):
                if not isUp:
                    XS = (xsBkg[k]-sigmaXSbkgDown[j])
                if isUp:
                    XS = (xsBkg[k]+sigmaXSbkgUp[j])
                #print "k:", k, "j:", j, "XS:", XS
                h_Bkg = h_Bkg*(L*XS/totalEventskBkg)
                h_BkgPass = h_BkgPass*(L*XS/totalEventskBkg)
                h_BkgFail = h_BkgFail*(L*XS/totalEventskBkg)

                h_sumBkg += h_Bkg
                h_sumBkgPass += h_BkgPass
                h_sumBkgFail += h_BkgFail

            else:
                XS = xsBkg[k]
                #print "k:", k, "j:", j, "XS:", XS
                h_Bkg = h_Bkg*(L*XS/totalEventskBkg)
                h_BkgPass = h_BkgPass*(L*XS/totalEventskBkg)
                h_BkgFail = h_BkgFail*(L*XS/totalEventskBkg)
        
                h_sumBkg += h_Bkg
                h_sumBkgPass += h_BkgPass
                h_sumBkgFail += h_BkgFail


        h_Data = h_Data - h_sumBkg
        h_Data_Passed = h_Data_Passed - h_sumBkgPass
        Data_Passed = h_Data_Passed.Integral()
        h_Data_Failed = h_Data_Failed - h_sumBkgFail
        h_subtractedData = h_Data_Passed.Clone("h_subtractedData")
        h_subtractedData = h_subtractedData + h_Data_Failed
        subtractedData = h_subtractedData.Integral()

        if isUp and isEle:
            dataPassUpTopE.append(Data_Passed)
            dataTotalUpTopE.append(subtractedData)
        if isUp and not isEle:
            dataPassUpTopMu.append(Data_Passed)
            dataTotalUpTopMu.append(subtractedData)
        if not isUp and isEle:
            dataPassDownTopE.append(Data_Passed)
            dataTotalDownTopE.append(subtractedData)
        if not isUp and not isEle:
            dataPassDownTopMu.append(Data_Passed)
            dataTotalDownTopMu.append(subtractedData)


        ttDataefficiency = (h_Data_Passed.Integral())/(h_subtractedData.Integral())
        ttDataEfficiencyList.append(ttDataefficiency)
        #print " "
        #print "Efficiency of tt Data:", ttDataefficiency

        SF = ttDataefficiency/ttMCefficiency
        #print " "
        #print "j:", j, "SF", SF

        SFlist.append(SF)
    
    
    
    #print " "
    #print "dataTotalhistoUpTopE 0", dataTotalhistoUpTopE[0].Integral()
    #print " "

    if isEle:
        priorSF = numberpriorSF[0]
    if not isEle:
        priorSF = numberpriorSF[1]
    for z in range(len(SFlist)):
        uncertainty = SFlist[z] - priorSF
        UncList.append(uncertainty)
        UncInPercentage = uncertainty/priorSF*100
        UncInPercentageList.append(UncInPercentage)

    #get the total uncertainty (up/down)
    sumUncPercen = 0.0
    for u in range(len(UncInPercentageList)):
        sumUncPercen += UncInPercentageList[u]**2
    totalUnc = TMath.Sqrt(sumUncPercen)

    return [SFlist, UncList, UncInPercentageList, totalUnc, ttDataEfficiencyList, priorSF]



##########################################
# Systematic Uncertainty from Luminosity #
##########################################

lumitthistoUpTopE = []
lumitthistoUpTopMu = []
lumitthistoDownTopE = []
lumitthistoDownTopMu = []
lumidataPassUpTopE = []
lumidataPassUpTopMu = []
lumidataPassDownTopE = []
lumidataPassDownTopMu = []
lumidataTotalUpTopE = []
lumidataTotalUpTopMu = []
lumidataTotalDownTopE = []
lumidataTotalDownTopMu = []

def getLumiUncertainties(Data_path, year_, ana, treeName, isUp, isEle):
    #print "\nGetting Systematic Uncertainties from Luminosity Unc"
    #print " "
    
    if year_ == 2017:
        L = 41500.0#/pb ; integrated luminosity
        version = "monohbb.v06.00.05.2017_NCU/"
        #print "\nProcessing 2017 data, ", version, " version"
    if year_ == 2018:
        L = 58827.0#/pb ; integrated luminosity
        version = "monohbb.v06.00.05.2018_NCU/"
        #print "\nProcessing 2018 data, ", version, " version"
    
    dirpath = "/afs/cern.ch/work/f/fkhuzaim/DDB_MistagSF/"+version+"combined/"

    if ana == "Inclusive":
        numberpriorSF = numberpriorSFinclusive
    if ana == "PT-200-350":
        numberpriorSF = numberpriorSFpt200_350
    if ana == "PT-350-500":
        numberpriorSF = numberpriorSFpt350_500
    if ana == "PT-500-2000":
        numberpriorSF = numberpriorSFpt500_inf
    if ana == "MET-200-270":
        numberpriorSF = numberpriorSFmet200_270
    if ana == "MET-270-345":
        numberpriorSF = numberpriorSFmet270_345
    if ana == "MET-345-1000":
        numberpriorSF = numberpriorSFmet345_1000
    
    if isUp:
        lumi = L*1.023
    if not isUp:
        lumi = L*0.977
    #print "luminosity: ", lumi

    if year_ == 2017:
        Top_path = "combined_crab_TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root"
    if year_ == 2018:
        Top_path = "combined_crab_TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8.root"
    xsTop = 300.9498
    
    
    #---------------------------------#
    #           Background            #
    #---------------------------------#
    
    if year_ == 2017:
        Bkg_files = ["combined_crab_WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_ZZ_TuneCP5_13TeV-pythia8.root", "combined_crab_WW_TuneCP5_13TeV-pythia8.root", "combined_crab_WZ_TuneCP5_13TeV-pythia8.root", "combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]
    if year_ == 2018:
        Bkg_files = ["combined_crab_WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root", "combined_crab_ZZ_TuneCP5_13TeV-pythia8.root", "combined_crab_WW_TuneCP5_13TeV-pythia8.root", "combined_crab_WZ_TuneCP5_13TeV-pythia8.root", "combined_crab_ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8.root", "combined_crab_ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root", "combined_crab_ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root", "combined_crab_ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8.root"]
    
    xsBkg = [1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001, 12.14, 75.8, 27.6, 3.74, 67.91, 113.3, 34.97, 34.91]

    
    h_ttFailed = TH1F("h_ttFailed", "", nbins, edges)
    h_ttPassed = TH1F("h_ttPassed", "", nbins, edges)
    
    h_ttFailed.Reset()
    h_ttPassed.Reset()
    
    openTop = TFile(dirpath+Top_path, "read")
    h_total_mcweight_Top = openTop.Get("h_total_mcweight")
    totalEventsTop = h_total_mcweight_Top.Integral()
    treeTop = openTop.Get(treeName)
    EventsTop = treeTop.GetEntries()
    
    for i in range(EventsTop):
        treeTop.GetEntry(i)
        st_TopMatching = getattr(treeTop, 'st_TopMatching')
        CSV_Top = getattr(treeTop, 'FJetCSV')
        SD_Top = getattr(treeTop, 'FJetMass')
        dPhi_Top = getattr(treeTop, 'min_dPhi')
        N2DDT_Top = getattr(treeTop, 'N2DDT')
        nJets_Top = getattr(treeTop, 'nJets')
        pt_Top = getattr(treeTop, 'FJetPt')
        met_Top = getattr(treeTop, 'MET')
        if ana == "Inclusive":
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top <= 0.86) and (nJets_Top <= 2):
                h_ttFailed.Fill(CSV_Top)
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86) and (nJets_Top <= 2):
                h_ttPassed.Fill(CSV_Top)
        if ana == "MET-200-270" or ana == "MET-270-345" or ana == "MET-345-1000":
            metbins = ana.split("-")
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top <= 0.86) and (nJets_Top <= 2) and (met_Top > int(metbins[1])) and (met_Top <= int(metbins[2])):
                h_ttFailed.Fill(CSV_Top)
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86) and (nJets_Top <= 2) and (met_Top > int(metbins[1])) and (met_Top <= int(metbins[2])):
                h_ttPassed.Fill(CSV_Top)
        if ana == "PT-200-350" or ana == "PT-350-500" or ana == "PT-500-2000":
            ptbins = ana.split("-")
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top <= 0.86) and (nJets_Top <= 2) and (pt_Top > int(ptbins[1])) and (pt_Top <= int(ptbins[2])):
                h_ttFailed.Fill(CSV_Top)
            if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86) and (nJets_Top <= 2) and (pt_Top > int(ptbins[1])) and (pt_Top <= int(ptbins[2])):
                h_ttPassed.Fill(CSV_Top)

    h_ttFailed = h_ttFailed*(lumi*xsTop/totalEventsTop)
    h_ttPassed = h_ttPassed*(lumi*xsTop/totalEventsTop)
    h_tt = h_ttFailed.Clone("h_tt")
    h_tt = h_tt + h_ttPassed
    
    if isUp and isEle:
        lumitthistoUpTopE.append(h_ttPassed)
        lumitthistoUpTopE.append(h_tt)
    if isUp and not isEle:
        lumitthistoUpTopMu.append(h_ttPassed)
        lumitthistoUpTopMu.append(h_tt)
    if not isUp and isEle:
        lumitthistoDownTopE.append(h_ttPassed)
        lumitthistoDownTopE.append(h_tt)
    if not isUp and not isEle:
        lumitthistoDownTopMu.append(h_ttPassed)
        lumitthistoDownTopMu.append(h_tt)

    ttMCefficiency = (h_ttPassed.Integral())/(h_tt.Integral())
    #print "\nEfficiency of tt MC:", ttMCefficiency

    
    h_Data = TH1F("h_Data", "", nbins, edges)
    h_Data_Failed = TH1F("h_Data_Failed", "", nbins, edges)
    h_Data_Passed = TH1F("h_Data_Passed", "", nbins, edges)
    
    h_Bkg = TH1F("h_Bkg", "", nbins, edges)
    h_BkgPass = TH1F("h_BkgPass", "", nbins, edges)
    h_BkgFail = TH1F("h_BkgFail", "", nbins, edges)
    
    h_sumBkg = TH1F("h_sumBkg", "", nbins, edges)
    h_sumBkgPass = TH1F("h_sumBkgPass", "", nbins, edges)
    h_sumBkgFail = TH1F("h_sumBkgFail", "", nbins, edges)
    
        
    h_Data.Reset()
    h_Data_Passed.Reset()
    h_Data_Failed.Reset()
    h_sumBkg.Reset()
    h_sumBkgPass.Reset()
    h_sumBkgFail.Reset()

    openData = TFile(dirpath+Data_path, "read")
    h_total_mcweight_Data = openData.Get("h_total_mcweight")
    totalEventsData = h_total_mcweight_Data.Integral()
    treeData = openData.Get(treeName)
    EventsData = treeData.GetEntries()

    for y in range(EventsData):
        treeData.GetEntry(y)
        CSV_Data = getattr(treeData, 'FJetCSV')
        SD_Data = getattr(treeData, 'FJetMass')
        dPhi_Data = getattr(treeData, 'min_dPhi')
        N2DDT_Data = getattr(treeData, 'N2DDT')
        nJets_Data = getattr(treeData, 'nJets')
        pt_Data = getattr(treeData, 'FJetPt')
        met_Data = getattr(treeData, 'MET')
        if ana == "Inclusive":
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2):
                h_Data.Fill(CSV_Data)
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data <= 0.86) and (nJets_Data <= 2):
                h_Data_Failed.Fill(CSV_Data)
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data > 0.86) and (nJets_Data <= 2):
                h_Data_Passed.Fill(CSV_Data)
        if ana == "MET-200-270" or ana == "MET-270-345" or ana == "MET-345-1000":
            metbins = ana.split("-")
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2) and (met_Data > int(metbins[1])) and (met_Data <= int(metbins[2])):
                h_Data.Fill(CSV_Data)
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data <= 0.86) and (nJets_Data <= 2) and (met_Data > int(metbins[1])) and (met_Data <= int(metbins[2])):
                h_Data_Failed.Fill(CSV_Data)
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data > 0.86) and (nJets_Data <= 2) and (met_Data > int(metbins[1])) and (met_Data <= int(metbins[2])):
                h_Data_Passed.Fill(CSV_Data)
        if ana == "PT-200-350" or ana == "PT-350-500" or ana == "PT-500-2000":
            ptbins = ana.split("-")
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (nJets_Data <= 2) and (pt_Data > int(ptbins[1])) and (pt_Data <= int(ptbins[2])):
                h_Data.Fill(CSV_Data)
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data <= 0.86) and (nJets_Data <= 2) and (pt_Data > int(ptbins[1])) and (pt_Data <= int(ptbins[2])):
                h_Data_Failed.Fill(CSV_Data)
            if (SD_Data > 100.0) and (SD_Data < 150.0) and (dPhi_Data > 0.4) and (CSV_Data > 0.86) and (nJets_Data <= 2) and (pt_Data > int(ptbins[1])) and (pt_Data <= int(ptbins[2])):
                h_Data_Passed.Fill(CSV_Data)

    for k in range(len(Bkg_files)):
        h_Bkg.Reset()
        h_BkgPass.Reset()
        h_BkgFail.Reset()
    
        openkBkg = TFile(dirpath+Bkg_files[k], "read")
        h_total_mcweight_kBkg = openkBkg.Get("h_total_mcweight")
        totalEventskBkg = h_total_mcweight_kBkg.Integral()
        treekBkg = openkBkg.Get(treeName)
        EventskBkg = treekBkg.GetEntries()
        
        for i in range(EventskBkg):
            treekBkg.GetEntry(i)
            CSV_iBkgEvent = getattr(treekBkg, 'FJetCSV')
            SD_iBkgEvent = getattr(treekBkg, 'FJetMass')
            dPhi_iBkgEvent = getattr(treekBkg, 'min_dPhi')
            N2DDT_iBkgEvent = getattr(treekBkg, 'N2DDT')
            nJets_iBkgEvent = getattr(treekBkg, 'nJets')
            pt_iBkgEvent = getattr(treekBkg, 'FJetPt')
            met_iBkgEvent = getattr(treekBkg, 'MET')
            if ana == "Inclusive":
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (nJets_iBkgEvent <= 2):
                    h_Bkg.Fill(CSV_iBkgEvent)
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent <= 0.86) and (nJets_iBkgEvent <= 2):
                    h_BkgFail.Fill(CSV_iBkgEvent)
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent > 0.86) and (nJets_iBkgEvent <= 2):
                    h_BkgPass.Fill(CSV_iBkgEvent)
            if ana == "MET-200-270" or ana == "MET-270-345" or ana == "MET-345-1000":
                metbins = ana.split("-")
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (nJets_iBkgEvent <= 2) and (met_iBkgEvent > int(metbins[1])) and (met_iBkgEvent <= int(metbins[2])):
                    h_Bkg.Fill(CSV_iBkgEvent)
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent <= 0.86) and (nJets_iBkgEvent <= 2) and (met_iBkgEvent > int(metbins[1])) and (met_iBkgEvent <= int(metbins[2])):
                    h_BkgFail.Fill(CSV_iBkgEvent)
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent > 0.86) and (nJets_iBkgEvent <= 2) and (met_iBkgEvent > int(metbins[1])) and (met_iBkgEvent <= int(metbins[2])):
                    h_BkgPass.Fill(CSV_iBkgEvent)
            if ana == "PT-200-350" or ana == "PT-350-500" or ana == "PT-500-2000":
                ptbins = ana.split("-")
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (nJets_iBkgEvent <= 2) and (pt_iBkgEvent > int(ptbins[1])) and (pt_iBkgEvent <= int(ptbins[2])):
                    h_Bkg.Fill(CSV_iBkgEvent)
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent <= 0.86) and (nJets_iBkgEvent <= 2) and (pt_iBkgEvent > int(ptbins[1])) and (pt_iBkgEvent <= int(ptbins[2])):
                    h_BkgFail.Fill(CSV_iBkgEvent)
                if (SD_iBkgEvent > 100.0) and (SD_iBkgEvent < 150.0) and (dPhi_iBkgEvent > 0.4) and (CSV_iBkgEvent > 0.86) and (nJets_iBkgEvent <= 2) and (pt_iBkgEvent > int(ptbins[1])) and (pt_iBkgEvent <= int(ptbins[2])):
                    h_BkgPass.Fill(CSV_iBkgEvent)

        h_Bkg = h_Bkg*(lumi*xsBkg[k]/totalEventskBkg)
        h_BkgPass = h_BkgPass*(lumi*xsBkg[k]/totalEventskBkg)
        h_BkgFail = h_BkgFail*(lumi*xsBkg[k]/totalEventskBkg)
            
        h_sumBkg += h_Bkg
        h_sumBkgPass += h_BkgPass
        h_sumBkgFail += h_BkgFail



    h_Data = h_Data - h_sumBkg
    h_Data_Passed = h_Data_Passed - h_sumBkgPass
    Data_Passed = h_Data_Passed.Integral()
    h_Data_Failed = h_Data_Failed - h_sumBkgFail
    h_subtractedData = h_Data_Passed.Clone("h_subtractedData")
    h_subtractedData = h_subtractedData + h_Data_Failed
    subtractedData = h_subtractedData.Integral()
    
    lumidataPass = Data_Passed
    lumisubtractdataTotal = subtractedData

    ttDataefficiency = (h_Data_Passed.Integral())/(h_subtractedData.Integral())
    #print "\nEfficiency of tt Data:", ttDataefficiency

    lumiSF = ttDataefficiency/ttMCefficiency


    if isEle:
        priorSF = numberpriorSF[0]
        #print "priorSF", priorSF
    if not isEle:
        priorSF = numberpriorSF[1]
        #print "priorSF", priorSF

    lumiuncertainty = lumiSF - priorSF
    #print "lumi uncer ", lumiuncertainty
    lumiUncInPercentage = lumiuncertainty/priorSF*100


    return [lumiSF, lumiuncertainty, lumiUncInPercentage, lumidataPass, lumisubtractdataTotal]





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate and draw plots of DDB mistag scale factor')
    
    #add command
    parser.add_argument('-Y', dest='discrepancy', help='Add the year of the data set')
    parser.add_argument('-a', help='Analyze which range do you want to analyze')
    
    #Get arguments from the user
    args = parser.parse_args()
    
    if args.discrepancy:
        priorSFlists_ = priorSFlists(int(args.discrepancy))
        numberpriorSFinclusive = priorSFlists_[0]
        numberpriorSFpt200_350 = priorSFlists_[1]
        numberpriorSFpt350_500 = priorSFlists_[2]
        numberpriorSFpt500_inf = priorSFlists_[3]
        numberpriorSFmet200_270 = priorSFlists_[4]
        numberpriorSFmet270_345 = priorSFlists_[5]
        numberpriorSFmet345_1000 = priorSFlists_[6]
        if args.a:
            
            #---------------------------------#
            #            SE Data              #
            #---------------------------------#
            #       Cross Section (Up)        #
            #---------------------------------#

            print "\nTOP (e) CR REGION for Cross Section Sys"
            print "Up"
            print ""

            SE_path = "combined_data_SE.root"

            getSESFup = getXSuncertainties(Data_path = SE_path, treeName = "monoHbb_Tope_boosted", year_ = int(args.discrepancy), ana = args.a, isUp = True, isEle = True)
            '''
            print "\nSE Data SFup list:", getSESFup[0]
            print "\nSE Data Uncertainty (Up):", getSESFup[1]
            print "\nSE Data Relative Uncertainty in Percentage (Up):", getSESFup[2]
            print "\ntotal Uncertainty Up of SE Data:", getSESFup[3]
            '''

            #---------------------------------#
            #       Cross Section (Down)      #
            #---------------------------------#
            
            print "\nDown"
            print ""
            
            getSESFdown = getXSuncertainties(Data_path = SE_path, treeName = "monoHbb_Tope_boosted", year_ = int(args.discrepancy), ana = args.a, isUp = False, isEle = True)
            '''
            print "\nSE Data SFdown list:", getSESFdown[0]
            print "\nSE Data Uncertainty (Down):", getSESFdown[1]
            print "\nSE Data Relative Uncertainty in Percentage (Down):", getSESFdown[2]
            print "\ntotal Uncertainty Down of SE Data:", getSESFdown[3]
            '''
            
            header = ["Source", "Top (e)", " ", "Top (mu)", " ", "Top (e+mu)", " "]
            row1 = [" ", "Upper Region", "Bottom Region", "Upper Region", "Bottom Region", "Upper Region", "Bottom Region"]
            XSuncertainties = ["Cross Section"]
            XSuncertaintiesFloat = [0]

            newUncTope = 0

            if (abs(getSESFup[3]) > 10.0) or (abs(getSESFdown[3]) > 10.0):
                if abs(getSESFup[3]) > abs(getSESFdown[3]):
                    XSuncertainties.append(str(round((getSESFup[3]/100*getSESFup[5]), 3)))
                    XSuncertaintiesFloat.append(round((getSESFup[3]/100*getSESFup[5]), 3))
                    #print "Top e", round((getSESFup[3]/100*getSESFup[5]), 3)
                else:
                    XSuncertainties.append(str(round((getSESFdown[3]/100*getSESFup[5]), 3)))
                    XSuncertaintiesFloat.append(round((getSESFdown[3]/100*getSESFup[5]), 3))
                    #print "Top e", round((getSESFdown[3]/100*getSESFup[5]), 3)
                XSuncertainties.append(" ")
                XSuncertaintiesFloat.append(0)

            if (abs(getSESFup[3]) < 10.0) and (abs(getSESFdown[3]) < 10.0):
                Up = getSESFup[1]
                Down = getSESFdown[1]
                for i in range(len(Up)):
                    if abs(Up[i]) > abs(Down[i]):
                        newUncTope += Up[i]**2
                    else:
                        newUncTope += Down[i]**2
                newTotalUnc = TMath.Sqrt(newUncTope)
                XSuncertainties.append(str(round(newTotalUnc, 3)))#Upper Region
                XSuncertaintiesFloat.append(round(newTotalUnc, 3))
                #print "Top e", round(newTotalUnc, 3)
                XSuncertainties.append("-"+str(round(newTotalUnc, 3)))#Bottom Region
                XSuncertaintiesFloat.append(round(newTotalUnc, 3))
                #print "Top e", round(newTotalUnc, 3)



            #---------------------------------#
            #           MET Data              #
            #---------------------------------#
            #       Cross Section (Up)        #
            #---------------------------------#

            print "\nTOP (muon) CR REGION for Cross Section Sys"
            print "Up"
            print ""

            MET_path = "combined_data_MET.root"

            getMETSFup = getXSuncertainties(Data_path = MET_path, treeName = "monoHbb_Topmu_boosted", year_ = int(args.discrepancy), ana = args.a, isUp = True, isEle = False)
            '''
            print "\nMET Data SFup list:", getMETSFup[0]
            print "\nMET Data Uncertainty (Up):", getMETSFup[1]
            print "\nMET Data Relative Uncertainty in Percentage (Up):", getMETSFup[2]
            print "\ntotal Uncertainty Up of MET Data:", getMETSFup[3]
            '''
            
            #---------------------------------#
            #       Cross Section (Down)      #
            #---------------------------------#
            
            print "\nDown"
            print ""
            
            getMETSFdown = getXSuncertainties(Data_path = MET_path, treeName = "monoHbb_Topmu_boosted", year_ = int(args.discrepancy), ana = args.a, isUp = False, isEle = False)
            '''
            print "\nMET Data SFdown list:", getMETSFdown[0]
            print "\nMET Data Uncertainty (Down):", getMETSFdown[1]
            print "\nMET Data Relative Uncertainty in Percentage (Down):", getMETSFdown[2]
            print "\ntotal Uncertainty Down of MET Data:", getMETSFdown[3]
            '''

            newUncTopmu = 0

            if (abs(getMETSFup[3]) > 10.0) or (abs(getMETSFdown[3]) > 10.0):
                if abs(getMETSFup[3]) > abs(getMETSFdown[3]):
                    XSuncertainties.append(str(round((getMETSFup[3]/100*getMETSFup[5]), 3)))
                    XSuncertaintiesFloat.append(round((getMETSFup[3]/100*getMETSFup[5]), 3))
                    #print "Top mu", round((getMETSFup[3]/100*getMETSFup[5]), 3)
                else:
                    XSuncertainties.append(str(round((getMETSFdown[3]/100*getMETSFup[5]), 3)))
                    XSuncertaintiesFloat.append(round((getMETSFdown[3]/100*getMETSFup[5]), 3))
                    #print "Top mu", round((getMETSFdown[3]/100*getMETSFup[5]), 3)
                XSuncertainties.append(" ")
                XSuncertaintiesFloat.append(0)

            if (abs(getMETSFup[3]) < 10.0) and (abs(getMETSFdown[3]) < 10.0):
                Up = getMETSFup[1]
                Down = getMETSFdown[1]
                for i in range(len(Up)):
                    if abs(Up[i]) > abs(Down[i]):
                        newUncTopmu += Up[i]**2
                    else:
                        newUncTopmu += Down[i]**2
                newTotalUnc = TMath.Sqrt(newUncTopmu)
                XSuncertainties.append(str(round(newTotalUnc, 3)))#Upper Region
                XSuncertaintiesFloat.append(round(newTotalUnc, 3))
                #print "Top mu", round(newTotalUnc, 3)
                XSuncertainties.append("-"+str(round(newTotalUnc, 3)))#Bottom Region
                XSuncertaintiesFloat.append(round(newTotalUnc, 3))
                #print "Top mu", round(newTotalUnc, 3)



            #---------------------------------#
            #           Top (e+mu)            #
            #---------------------------------#
            #          Cross Section          #
            #---------------------------------#
            
            print "\nTOP (e+mu) CONTROL REGION for Cross Section Sys"
            print ""
            
            if args.a == "Inclusive":
                priorSFmerge = numberpriorSFinclusive[2]
            if args.a == "PT-200-350":
                priorSFmerge = numberpriorSFpt200_350[2]
            if args.a == "PT-350-500":
                priorSFmerge = numberpriorSFpt350_500[2]
            if args.a == "PT-500-2000":
                priorSFmerge = numberpriorSFpt500_inf[2]
            if args.a == "MET-200-270":
                priorSFmerge = numberpriorSFmet200_270[2]
            if args.a == "MET-270-345":
                priorSFmerge = numberpriorSFmet270_345[2]
            if args.a == "MET-345-1000":
                priorSFmerge = numberpriorSFmet345_1000[2]


            print "\nUp"
            print ""
            SFmergeUp = []
            UncMergeUp = []
            RelativeUncMergeUp = []
            ttDataEfficiencyMergeUpList = []


            ttPassUpMerge = tthistoUpTopE[0] + tthistoUpTopMu[0]
            ttTotalUpMerge = tthistoUpTopE[1] + tthistoUpTopMu[1]
            ttMergeUpEfficiency = (ttPassUpMerge.Integral())/(ttTotalUpMerge.Integral())
            #print " "
            #print "tt MC Efficiency Merge Up", ttMergeUpEfficiency

            for i in range(len(dataPassUpTopE)):
                idataPassUpMerge = dataPassUpTopE[i] + dataPassUpTopMu[i]
                idataTotalUpMerge = dataTotalUpTopE[i] + dataTotalUpTopMu[i]
                ittDataEfficiencyMergeUp = idataPassUpMerge/idataTotalUpMerge
                ttDataEfficiencyMergeUpList.append(ittDataEfficiencyMergeUp)
                iSFmergeUp = ittDataEfficiencyMergeUp/ttMergeUpEfficiency
                SFmergeUp.append(iSFmergeUp)

            for j in range(len(SFmergeUp)):
                jUncMergeUp = SFmergeUp[j] - priorSFmerge
                UncMergeUp.append(jUncMergeUp)

            for k in range(len(UncMergeUp)):
                kRelativeUncMergeUp = UncMergeUp[k]/priorSFmerge*100
                RelativeUncMergeUp.append(kRelativeUncMergeUp)

            '''
            print "\nEfficiency of tt Data (Merge Up):", ttDataEfficiencyMergeUpList
            print "\nSF Merge Up:", SFmergeUp
            print "\nUncertainty Merge Up:", UncMergeUp
            print "\nRelative Uncertainty Merge Up in Percen:", RelativeUncMergeUp
            '''

            #get the total uncertainty (up)
            sumUncPercenMergeUp = 0.0
            for u in range(len(RelativeUncMergeUp)):
                sumUncPercenMergeUp += RelativeUncMergeUp[u]**2
            totalUncMergeUp = TMath.Sqrt(sumUncPercenMergeUp)
            #print " "
            #print "Total Relative Uncertainty of Top (e+mu) Up:", totalUncMergeUp



            print "\nDown"
            print ""
            SFmergeDown = []
            UncMergeDown = []
            RelativeUncMergeDown = []
            ttDataEfficiencyMergeDownList = []


            ttPassDownMerge = tthistoDownTopE[0] + tthistoDownTopMu[0]
            ttTotalDownMerge = tthistoDownTopE[1] + tthistoDownTopMu[1]
            ttMergeDownEfficiency = (ttPassDownMerge.Integral())/(ttTotalDownMerge.Integral())
            #print " "
            #print "tt MC Efficiency Merge Down", ttMergeDownEfficiency

            for i in range(len(dataPassDownTopE)):
                idataPassDownMerge = dataPassDownTopE[i] + dataPassDownTopMu[i]
                idataTotalDownMerge = dataTotalDownTopE[i] + dataTotalDownTopMu[i]
                ittDataEfficiencyMergeDown = idataPassDownMerge/idataTotalDownMerge
                ttDataEfficiencyMergeDownList.append(ittDataEfficiencyMergeDown)
                iSFmergeDown = ittDataEfficiencyMergeDown/ttMergeDownEfficiency
                SFmergeDown.append(iSFmergeDown)

            for j in range(len(SFmergeDown)):
                jUncMergeDown = SFmergeDown[j] - priorSFmerge
                UncMergeDown.append(jUncMergeDown)

            for k in range(len(UncMergeDown)):
                kRelativeUncMergeDown = UncMergeDown[k]/priorSFmerge*100
                RelativeUncMergeDown.append(kRelativeUncMergeDown)

            '''
            print "\nEfficiency of tt Data (Merge Down):", ttDataEfficiencyMergeDownList
            print "\nSF Merge Down:", SFmergeDown
            print "\nUncertainty Merge Down:", UncMergeDown
            print "\nRelative Uncertainty Merge Down in Percen:", RelativeUncMergeDown
            '''

            #get the total uncertainty (Down)
            sumUncPercenMergeDown = 0.0
            for u in range(len(RelativeUncMergeDown)):
                sumUncPercenMergeDown += RelativeUncMergeDown[u]**2
            totalUncMergeDown = TMath.Sqrt(sumUncPercenMergeDown)
            #print " "
            #print "Total Relative Uncertainty of Top (e+mu) Down:", totalUncMergeDown


            newUncTopemu = 0

            if (abs(totalUncMergeUp) > 10.0) or (abs(totalUncMergeDown) > 10.0):
                if abs(totalUncMergeUp) > abs(totalUncMergeDown):
                    XSuncertainties.append(str(round((totalUncMergeUp/100*priorSFmerge), 3)))
                    XSuncertaintiesFloat.append(round((totalUncMergeUp/100*priorSFmerge), 3))
                    #print "Top e+mu", round((totalUncMergeUp/100*priorSFmerge), 3)
                else:
                    XSuncertainties.append(str(round((totalUncMergeDown/100*priorSFmerge), 3)))
                    XSuncertaintiesFloat.append(round((totalUncMergeDown/100*priorSFmerge), 3))
                    #print "Top e+mu", round((totalUncMergeDown/100*priorSFmerge), 3)
                XSuncertainties.append(" ")
                XSuncertaintiesFloat.append(0)

            if (abs(totalUncMergeUp) < 10.0) and (abs(totalUncMergeDown) < 10.0):
                Up = UncMergeUp
                Down = UncMergeDown
                for i in range(len(Up)):
                    if abs(Up[i]) > abs(Down[i]):
                        newUncTopemu += Up[i]**2
                    else:
                        newUncTopemu += Down[i]**2
                newTotalUnc = TMath.Sqrt(newUncTopemu)
                XSuncertainties.append(str(round(newTotalUnc, 3)))#Upper Region
                XSuncertaintiesFloat.append(round(newTotalUnc, 3))
                #print "Top e+mu", round(newTotalUnc, 3)
                XSuncertainties.append("-"+str(round(newTotalUnc, 3)))#Bottom Region
                XSuncertaintiesFloat.append(round(newTotalUnc, 3))
                #print "Top e+mu", round(newTotalUnc, 3)

            #print ""
            #print "XSuncertainties", XSuncertainties

            
            
            ################################
            #         Luminosity           #
            ################################
            
            #---------------------------------#
            #            SE Data              #
            #---------------------------------#
            #         Luminosity (Up)         #
            #---------------------------------#
            
            LumiUncertaintiesList = ["Luminosity"]
            LumiUncertaintiesFloat = [0]
            
            print "\nTOP (e) CR REGION for luminosity sys"
            print "Up"
            print ""
            
            getSESFupLumi = getLumiUncertainties(Data_path = SE_path, year_ = int(args.discrepancy), ana = args.a, treeName = "monoHbb_Tope_boosted", isUp = True, isEle = True)
            
            #print "\nSE SFup of Lumi sys:", getSESFupLumi[0]
            '''
            print "\nSE Lumi Uncertainty (Up):", getSESFupLumi[1]
            print "\nSE Lumi Relative Uncertainty in Percentage (Up):", getSESFupLumi[2]
            '''
            LumiUncertaintiesList.append(str(round(getSESFupLumi[1], 3)))
            LumiUncertaintiesFloat.append(round(getSESFupLumi[1], 3))
            
            
            #---------------------------------#
            #         Luminosity (Down)       #
            #---------------------------------#

            print "\nDown"
            print ""

            getSESFdownLumi = getLumiUncertainties(Data_path = SE_path, year_ = int(args.discrepancy), ana = args.a, treeName = "monoHbb_Tope_boosted", isUp = False, isEle = True)
            
            #print "\nSE SFdown of Lumi sys :", getSESFdownLumi[0]
            '''
            print "\nSE Lumi Uncertainty (Down):", getSESFdownLumi[1]
            print "\nSE Lumi Relative Uncertainty in Percentage (Down):", getSESFdownLumi[2]
            '''
            LumiUncertaintiesList.append(str(round(getSESFdownLumi[1], 3)))
            LumiUncertaintiesFloat.append(round(getSESFdownLumi[1], 3))
            
        
            #---------------------------------#
            #           MET Data              #
            #---------------------------------#
            #        Luminosity (Up)          #
            #---------------------------------#
            
            print "\nTOP (muon) CR REGION for luminosity sys"
            print "Up"
            print ""
            
            getMETSFupLumi = getLumiUncertainties(Data_path = MET_path, year_ = int(args.discrepancy), ana = args.a, treeName = "monoHbb_Topmu_boosted", isUp = True, isEle = False)
            
            #print "\nMET SFup of Lumi sys:", getMETSFupLumi[0]
            '''
            print "\nMET Lumi Uncertainty (Up):", getMETSFupLumi[1]
            print "\nMET Lumi Relative Uncertainty in Percentage (Up):", getMETSFupLumi[2]
            '''
            LumiUncertaintiesList.append(str(round(getMETSFupLumi[1], 3)))
            LumiUncertaintiesFloat.append(round(getMETSFupLumi[1], 3))
            
            #---------------------------------#
            #        Luminosity (Down)        #
            #---------------------------------#

            print "\nDown"
            print ""

            getMETSFdownLumi = getLumiUncertainties(Data_path = MET_path, year_ = int(args.discrepancy), ana = args.a, treeName = "monoHbb_Topmu_boosted", isUp = False, isEle = False)
            
            #print "\nMET SFdown of Lumi sys:", getMETSFdownLumi[0]
            '''
            print "\nMET Lumi Uncertainty (Down):", getMETSFdownLumi[1]
            print "\nMET Lumi Relative Uncertainty in Percentage (Down):", getMETSFdownLumi[2]
            '''
            LumiUncertaintiesList.append(str(round(getMETSFdownLumi[1],3)))
            LumiUncertaintiesFloat.append(round(getMETSFdownLumi[1],3))
    
    
            #---------------------------------#
            #           Top (e+mu)            #
            #---------------------------------#
            #           Luminosity            #
            #---------------------------------#

            print "\nTOP (e+mu) CONTROL REGION"
            print "Up"
            print ""

            lumittPassUpMerge = lumitthistoUpTopE[0] + lumitthistoUpTopMu[0]
            lumittTotalUpMerge = lumitthistoUpTopE[1] + lumitthistoUpTopMu[1]
            lumittMergeUpEfficiency = (lumittPassUpMerge.Integral())/(lumittTotalUpMerge.Integral())
            #print " "
            #print "tt MC Efficiency Merge Up of Luminosity", lumittMergeUpEfficiency
            
            
            lumidataPassUpMerge = getSESFupLumi[3] + getMETSFupLumi[3]
            lumidataTotalUpMerge = getSESFupLumi[4] + getMETSFupLumi[4]
            lumittDataEfficiencyMergeUp = lumidataPassUpMerge/lumidataTotalUpMerge
            lumiSFmergeUp = lumittDataEfficiencyMergeUp/lumittMergeUpEfficiency
        
            lumiUncMergeUp = lumiSFmergeUp - priorSFmerge
            LumiUncertaintiesList.append(str(round(lumiUncMergeUp, 3)))
            LumiUncertaintiesFloat.append(round(lumiUncMergeUp, 3))
            
            lumiRelativeUncMergeUp = lumiUncMergeUp/priorSFmerge*100
            
            #print "\nEfficiency of tt Data (Merge Up) of Luminosity:", lumittDataEfficiencyMergeUp
            #print "\nSF Merge Up of Luminosity:", lumiSFmergeUp
            '''
            print "\nUncertainty Merge Up of Luminosity:", lumiUncMergeUp
            print "\nRelative Uncertainty Merge Up in Percen of Luminosity:", lumiRelativeUncMergeUp
            '''


            print "\nDown"
            print ""

            lumittPassDownMerge = lumitthistoDownTopE[0] + lumitthistoDownTopMu[0]
            lumittTotalDownMerge = lumitthistoDownTopE[1] + lumitthistoDownTopMu[1]
            lumittMergeDownEfficiency = (lumittPassDownMerge.Integral())/(lumittTotalDownMerge.Integral())
            #print " "
            #print "tt MC Efficiency Merge Down of Luminosity", lumittMergeDownEfficiency
            
            lumidataPassDownMerge = getSESFdownLumi[3] + getMETSFdownLumi[3]
            lumidataTotalDownMerge = getSESFdownLumi[4] + getMETSFdownLumi[4]
            lumittDataEfficiencyMergeDown = lumidataPassDownMerge/lumidataTotalDownMerge
            lumiSFmergeDown = lumittDataEfficiencyMergeDown/lumittMergeDownEfficiency
            
            lumiUncMergeDown = lumiSFmergeDown - priorSFmerge
            LumiUncertaintiesList.append(str(round(lumiUncMergeDown, 3)))
            LumiUncertaintiesFloat.append(round(lumiUncMergeDown, 3))
            
            lumiRelativeUncMergeDown = lumiUncMergeDown/priorSFmerge*100
            
            #print "\nEfficiency of tt Data (Merge Down) of Luminosity:", lumittDataEfficiencyMergeDown
            #print "\nSF Merge Down of Luminosity:", lumiSFmergeDown
            '''
            print "\nUncertainty Merge Down of Luminosity:", lumiUncMergeDown
            print "\nRelative Uncertainty Merge Down in Percen of Luminosity:", lumiRelativeUncMergeDown
            '''
    
            #print "\nLumiUncertaintiesList", LumiUncertaintiesList
            
            TotalSysList = ["Total Sys. Unc."]
            for i in range(len(XSuncertainties) - 1):
                XSsys = XSuncertaintiesFloat[i+1]
                Lumisys = LumiUncertaintiesFloat[i+1]
                iTotalSys = TMath.Sqrt(XSsys**2 + Lumisys**2)
                if i == 1 or i == 3 or i == 5:
                    TotalSysList.append("-"+str(round(iTotalSys, 3)))
                else:
                    TotalSysList.append(str(round(iTotalSys, 3)))
            
            makeTable(header, row1, XSuncertainties, LumiUncertaintiesList, TotalSysList)

