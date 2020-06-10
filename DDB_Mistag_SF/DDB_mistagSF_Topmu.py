#created by Fasya Khuzaimah on 2020.04.17

import ROOT
from ROOT import TFile, TTree, TH1F, TCanvas, TLegend, TAxis, TLatex, TPad, TPaveText, gStyle, gPad
import array as arr

print "Top Muon Region"
print " "

L = 41500.0 #/pb ; integrated luminosity
nbins = 14
totalmax = 1550.0
ttmax = 850.0
edges = arr.array('f', [0.0, 0.08, 0.16, 0.23, 0.30, 0.37, 0.44, 0.51, 0.58, 0.65, 0.72, 0.79, 0.86, 0.93, 1.0])
dirpath = "monohbb.v06.00.00.2017_NCU/combined/"

#---------------------------------#
#         TTtoSemileptonic        #
#---------------------------------#

Top_path = dirpath+"combined_crab_TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root"

xsTop = 300.9498

h_TopMatch = TH1F("h_TopMatch", "", nbins, edges)
h_Wmatch = TH1F("h_Wmatch", "", nbins, edges)
h_unmatch = TH1F("h_unmatch", "", nbins, edges)
h_ttFailed = TH1F("h_ttFailed", "", nbins, edges)
h_ttPassed = TH1F("h_ttPassed", "", nbins, edges)
h_ttPassed_Match = TH1F("h_ttPassed_Match", "", nbins, edges)
h_ttPassed_Wmatch = TH1F("h_ttPassed_Wmatch", "", nbins, edges)
h_ttPassed_unmatch = TH1F("h_ttPassed_unmatch", "", nbins, edges)
h_pfMC = TH1F("h_pfMC", "", 2, 0, 2)
h_pfMCpassf = TH1F("h_pfMCpassf", "", 2, 0, 2)
h_pfMCpassp = TH1F("h_pfMCpassp", "", 2, 0, 2)
h_pfMCfailf = TH1F("h_pfMCfailf", "", 2, 0, 2)
h_pfMCfailp = TH1F("h_pfMCfailp", "", 2, 0, 2)

openTop = TFile(Top_path, "read")
h_total_mcweight_Top = openTop.Get("h_total_mcweight")
totalEventsTop = h_total_mcweight_Top.Integral()
treeTop = openTop.Get("monoHbb_Topmu_boosted")
EventsTop = treeTop.GetEntries()

for i in range(EventsTop):
    treeTop.GetEntry(i)
    st_TopMatching = getattr(treeTop, 'st_TopMatching')
    CSV_Top = getattr(treeTop, 'FJetCSV')
    SD_Top = getattr(treeTop, 'FJetMass')
    dPhi_Top = getattr(treeTop, 'min_dPhi')
    if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4):
        h_TopMatch.Fill(CSV_Top)
    if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4):
        h_Wmatch.Fill(CSV_Top)
    if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4):
        h_unmatch.Fill(CSV_Top)
    if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top <= 0.86):
        h_ttFailed.Fill(CSV_Top)
        h_pfMC.Fill(0.5)
        h_pfMCfailf.Fill(0.5)
        h_pfMCpassf.Fill(1.5)
    if (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86):
        h_ttPassed.Fill(CSV_Top)
        h_pfMC.Fill(1.5)
        h_pfMCfailp.Fill(0.5)
        h_pfMCpassp.Fill(1.5)
    if (st_TopMatching == 2) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86):
        h_ttPassed_Match.Fill(CSV_Top)
    if (st_TopMatching == 3) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86):
        h_ttPassed_Wmatch.Fill(CSV_Top)
    if (st_TopMatching == 4) and (SD_Top > 100.0) and (SD_Top < 150.0) and (dPhi_Top > 0.4) and (CSV_Top > 0.86):
        h_ttPassed_unmatch.Fill(CSV_Top)

h_TopMatch = h_TopMatch*(L*xsTop/totalEventsTop)
h_Wmatch = h_Wmatch*(L*xsTop/totalEventsTop)
h_unmatch = h_unmatch*(L*xsTop/totalEventsTop)
h_ttFailed = h_ttFailed*(L*xsTop/totalEventsTop)
h_ttPassed = h_ttPassed*(L*xsTop/totalEventsTop)
h_ttPassed_Match = h_ttPassed_Match*(L*xsTop/totalEventsTop)
h_ttPassed_Wmatch = h_ttPassed_Wmatch*(L*xsTop/totalEventsTop)
h_ttPassed_unmatch = h_ttPassed_unmatch*(L*xsTop/totalEventsTop)
h_pfMC = h_pfMC*(L*xsTop/totalEventsTop)
h_pfMCfailf = h_pfMCfailf*(L*xsTop/totalEventsTop)
h_pfMCfailp = h_pfMCfailp*(L*xsTop/totalEventsTop)
h_pfMCpassf = h_pfMCpassf*(L*xsTop/totalEventsTop)
h_pfMCpassp = h_pfMCpassp*(L*xsTop/totalEventsTop)

h_tt = h_ttFailed.Clone("h_tt")
h_tt = h_tt + h_ttPassed
frac_match = (h_TopMatch.Integral())/(h_tt.Integral())*100
frac_Wmatch = (h_Wmatch.Integral())/(h_tt.Integral())*100
frac_unmatch = (h_unmatch.Integral())/(h_tt.Integral())*100
frac_Passed = (h_ttPassed.Integral())/(h_tt.Integral())*100
frac_Failed = (h_ttFailed.Integral())/(h_tt.Integral())*100
frac_ttPassedMatch = (h_ttPassed_Match.Integral())/(h_tt.Integral())*100
frac_ttPassedWmatch = (h_ttPassed_Wmatch.Integral())/(h_tt.Integral())*100
frac_ttPassedUnmatch = (h_ttPassed_unmatch.Integral())/(h_tt.Integral())*100

print "match fraction :", frac_match
print "W-match fraction :", frac_Wmatch
print "unmatch fraction :", frac_unmatch
print " "
print "Mistagged tt MC fraction :", frac_Passed
print "Failed tt MC fraction :", frac_Failed
print " "
print "Mistagged tt (Top Match) MC fraction :", frac_ttPassedMatch
print "Mistagged tt (W-Match) MC fraction :", frac_ttPassedWmatch
print "Mistagged tt (Unmatch) MC fraction :", frac_ttPassedUnmatch
print " "


Cloned_frac_ttFailed = h_ttFailed.Clone("Cloned_frac_ttFailed")
Cloned_frac_ttPassed = h_ttPassed.Clone("Cloned_frac_ttPassed")
Cloned_frac_tt = h_tt.Clone("Cloned_frac_tt")

h_pfMCtotal = h_pfMCfailf.Clone("h_pfMCtotal")
h_pfMCtotal = h_pfMCtotal + h_pfMCfailp + h_pfMCpassf + h_pfMCpassp

h_pfMCtopMu = h_pfMC.Clone("h_pfMCtopMu")



#---------------------------------#
#          Hadronic tt            #
#---------------------------------#

ttHad_path = dirpath+"combined_crab_TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root"#_forTopMu.root

xs_ttHad = 314.0047

h_ttHad = TH1F("h_ttHad", "", nbins, edges)
h_ttHadFailed = TH1F("h_ttHadFailed", "", nbins, edges)
h_ttHadPassed = TH1F("h_ttHadPassed", "", nbins, edges)
h_pfttHad = TH1F("h_pfttHad", "", 2, 0, 2)

open_ttHad = TFile(ttHad_path, "read")
h_total_mcweight_ttHad = open_ttHad.Get("h_total_mcweight")
totalEvents_ttHad = h_total_mcweight_ttHad.Integral()
tree_ttHad = open_ttHad.Get("monoHbb_Topmu_boosted")
Events_ttHad = tree_ttHad.GetEntries()

for i in range(Events_ttHad):
    tree_ttHad.GetEntry(i)
    CSV_ttHad = getattr(tree_ttHad, 'FJetCSV')
    SD_ttHad = getattr(tree_ttHad, 'FJetMass')
    dPhi_ttHad = getattr(tree_ttHad, 'min_dPhi')
    if (SD_ttHad > 100.0) and (SD_ttHad < 150.0) and (dPhi_ttHad > 0.4):
        h_ttHad.Fill(CSV_ttHad)
    if (SD_ttHad > 100.0) and (SD_ttHad < 150.0) and (dPhi_ttHad > 0.4) and (CSV_ttHad <= 0.86):
        h_ttHadFailed.Fill(CSV_ttHad)
        h_pfttHad.Fill(0.5)
    if (SD_ttHad > 100.0) and (SD_ttHad < 150.0) and (dPhi_ttHad > 0.4) and (CSV_ttHad > 0.86):
        h_ttHadPassed.Fill(CSV_ttHad)
        h_pfttHad.Fill(1.5)

#print "ttHad", h_ttHad.Integral()

h_ttHad = h_ttHad*(L*xs_ttHad/totalEvents_ttHad)
h_ttHadFailed = h_ttHadFailed*(L*xs_ttHad/totalEvents_ttHad)
h_ttHadPassed = h_ttHadPassed*(L*xs_ttHad/totalEvents_ttHad)
h_pfttHad = h_pfttHad*(L*xs_ttHad/totalEvents_ttHad)



#---------------------------------#
#          Leptonic tt            #
#---------------------------------#

ttLep_path = dirpath+"combined_crab_TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root"

xs_ttLep = 72.1455

h_ttLep = TH1F("h_ttLep", "", nbins, edges)
h_ttLepPassed = TH1F("h_ttLepPassed", "", nbins, edges)
h_ttLepFailed = TH1F("h_ttLepFailed", "", nbins, edges)
h_pfttLep = TH1F("h_pfttLep", "", 2, 0, 2)

open_ttLep = TFile(ttLep_path, "read")
h_total_mcweight_ttLep = open_ttLep.Get("h_total_mcweight")
totalEvents_ttLep = h_total_mcweight_ttLep.Integral()
tree_ttLep = open_ttLep.Get("monoHbb_Topmu_boosted")
Events_ttLep = tree_ttLep.GetEntries()

for i in range(Events_ttLep):
    tree_ttLep.GetEntry(i)
    CSV_ttLep = getattr(tree_ttLep, 'FJetCSV')
    SD_ttLep = getattr(tree_ttLep, 'FJetMass')
    dPhi_ttLep = getattr(tree_ttLep, 'min_dPhi')
    if (SD_ttLep > 100.0) and (SD_ttLep < 150.0) and (dPhi_ttLep > 0.4):
        h_ttLep.Fill(CSV_ttLep)
    if (SD_ttLep > 100.0) and (SD_ttLep < 150.0) and (dPhi_ttLep > 0.4) and (CSV_ttLep <= 0.86):
        h_ttLepFailed.Fill(CSV_ttLep)
        h_pfttLep.Fill(0.5)
    if (SD_ttLep > 100.0) and (SD_ttLep < 150.0) and (dPhi_ttLep > 0.4) and (CSV_ttLep > 0.86):
        h_ttLepPassed.Fill(CSV_ttLep)
        h_pfttLep.Fill(1.5)

h_ttLep = h_ttLep*(L*xs_ttLep/totalEvents_ttLep)
h_ttLepFailed = h_ttLepFailed*(L*xs_ttLep/totalEvents_ttLep)
h_ttLepPassed = h_ttLepPassed*(L*xs_ttLep/totalEvents_ttLep)
h_pfttLep = h_pfttLep*(L*xs_ttLep/totalEvents_ttLep)



#---------------------------------#
#              W+Jets             #
#---------------------------------#

WJets_files = [dirpath+"combined_crab_WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8_forTopMu.root",dirpath+"combined_crab_WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8.root",dirpath+"combined_crab_WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8.root",dirpath+"combined_crab_WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8.root",dirpath+"combined_crab_WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8.root",dirpath+"combined_crab_WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8.root",dirpath+"combined_crab_WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8.root"]

xsWJets = [1395.0, 407.9, 57.48, 12.87, 5.366, 1.074, 0.008001]

h_WJets = TH1F("h_WJets", "", nbins, edges)
h_WJetsPassed = TH1F("h_WJetsPassed", "", nbins, edges)
h_WJetsFailed = TH1F("h_WJetsFailed", "", nbins, edges)
h_pfWjets = TH1F("h_pfWjets", "", 2, 0, 2)
h_pfWjetsfailf = TH1F("h_pfWjetsfailf", "", 2, 0, 2)
h_pfWjetsfailp = TH1F("h_pfWjetsfailp", "", 2, 0, 2)
h_pfWjetspassf = TH1F("h_pfWjetspassf", "", 2, 0, 2)
h_pfWjetspassp = TH1F("h_pfWjetspassp", "", 2, 0, 2)

h_sumWJets = TH1F("h_sumWJets", "", nbins, edges)
h_sumWJetsPassed = TH1F("h_sumWJetsPassed", "", nbins, edges)
h_sumWJetsFailed = TH1F("h_sumWJetsFailed", "", nbins, edges)
h_sumpfWjets = TH1F("h_sumpfWjets", "", 2, 0, 2)
h_sumpfWjetsfailf = TH1F("h_sumpfWjetsfailf", "", 2, 0, 2)
h_sumpfWjetsfailp = TH1F("h_sumpfWjetsfailp", "", 2, 0, 2)
h_sumpfWjetspassf = TH1F("h_sumpfWjetspassf", "", 2, 0, 2)
h_sumpfWjetspassp = TH1F("h_sumpfWjetspassp", "", 2, 0, 2)

for k in range(len(WJets_files)):
    openWJets = TFile(WJets_files[k], "read")
    h_total_mcweight_WJets = openWJets.Get("h_total_mcweight")
    totalEventsWJets = h_total_mcweight_WJets.Integral()
    treeWJets = openWJets.Get("monoHbb_Topmu_boosted")
    EventsWJets = treeWJets.GetEntries()

    for i in range(EventsWJets):
        treeWJets.GetEntry(i)
        CSV_WJets = getattr(treeWJets, 'FJetCSV')
        SD_WJets = getattr(treeWJets, 'FJetMass')
        dPhi_WJets = getattr(treeWJets, 'min_dPhi')
        if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4):
            h_WJets.Fill(CSV_WJets)
        if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (CSV_WJets <= 0.86):
            h_WJetsFailed.Fill(CSV_WJets)
            h_pfWjets.Fill(0.5)
            h_pfWjetsfailf.Fill(0.5)
            h_pfWjetspassf.Fill(1.5)
        if (SD_WJets > 100.0) and (SD_WJets < 150.0) and (dPhi_WJets > 0.4) and (CSV_WJets > 0.86):
            h_WJetsPassed.Fill(CSV_WJets)
            h_pfWjets.Fill(1.5)
            h_pfWjetsfailp.Fill(0.5)
            h_pfWjetspassp.Fill(1.5)

    h_WJets = h_WJets*(L*xsWJets[k]/totalEventsWJets)
    h_WJetsPassed = h_WJetsPassed*(L*xsWJets[k]/totalEventsWJets)
    h_WJetsFailed = h_WJetsFailed*(L*xsWJets[k]/totalEventsWJets)
    h_pfWjets = h_pfWjets*(L*xsWJets[k]/totalEventsWJets)
    h_pfWjetsfailf = h_pfWjetsfailf*(L*xsWJets[k]/totalEventsWJets)
    h_pfWjetsfailp = h_pfWjetsfailp*(L*xsWJets[k]/totalEventsWJets)
    h_pfWjetspassf = h_pfWjetspassf*(L*xsWJets[k]/totalEventsWJets)
    h_pfWjetspassp = h_pfWjetspassp*(L*xsWJets[k]/totalEventsWJets)

    h_sumWJets += h_WJets
    h_sumWJetsPassed += h_WJetsPassed
    h_sumWJetsFailed += h_WJetsFailed
    h_sumpfWjets += h_pfWjets
    h_sumpfWjetsfailf += h_pfWjetsfailf
    h_sumpfWjetsfailp += h_pfWjetsfailp
    h_sumpfWjetspassf + h_pfWjetspassf
    h_sumpfWjetspassp += h_pfWjetspassp


#---------------------------------#
#              Diboson             #
#---------------------------------#

Diboson_files = [dirpath+"combined_crab_ZZ_TuneCP5_13TeV-pythia8.root",dirpath+"combined_crab_WW_TuneCP5_13TeV-pythia8.root",dirpath+"combined_crab_WZ_TuneCP5_13TeV-pythia8.root"]

xsDiboson = [12.14, 75.8, 27.6]

h_Diboson = TH1F("h_Diboson", "", nbins, edges)
h_DibosonPassed = TH1F("h_DibosonPassed", "", nbins, edges)
h_DibosonFailed = TH1F("h_DibosonFailed", "", nbins, edges)
h_pfdiboson = TH1F("h_pfdiboson", "", 2, 0, 2)
h_pfdibosonfailf = TH1F("h_pfdibosonfailf", "", 2, 0, 2)
h_pfdibosonfailp = TH1F("h_pfdibosonfailp", "", 2, 0, 2)
h_pfdibosonpassf = TH1F("h_pfdibosonpassf", "", 2, 0, 2)
h_pfdibosonpassp = TH1F("h_pfdibosonpassp", "", 2, 0, 2)

h_sumDiboson = TH1F("h_sumDiboson", "", nbins, edges)
h_sumDibosonPassed = TH1F("h_sumDibosonPassed", "", nbins, edges)
h_sumDibosonFailed = TH1F("h_sumDibosonFailed", "", nbins, edges)
h_sumpfdiboson = TH1F("h_sumpfdiboson", "", 2, 0, 2)
h_sumpfdibosonfailf = TH1F("h_sumpfdibosonfailf", "", 2, 0, 2)
h_sumpfdibosonfailp = TH1F("h_sumpfdibosonfailp", "", 2, 0, 2)
h_sumpfdibosonpassf = TH1F("h_sumpfdibosonpassf", "", 2, 0, 2)
h_sumpfdibosonpassp = TH1F("h_sumpfdibosonpassp", "", 2, 0, 2)

for k in range(len(Diboson_files)):
    openDiboson = TFile(Diboson_files[k], "read")
    h_total_mcweight_Diboson = openDiboson.Get("h_total_mcweight")
    totalEventsDiboson = h_total_mcweight_Diboson.Integral()
    treeDiboson = openDiboson.Get("monoHbb_Topmu_boosted")
    EventsDiboson = treeDiboson.GetEntries()
    
    for i in range(EventsDiboson):
        treeDiboson.GetEntry(i)
        CSV_Diboson = getattr(treeDiboson, 'FJetCSV')
        SD_Diboson = getattr(treeDiboson, 'FJetMass')
        dPhi_Diboson = getattr(treeDiboson, 'min_dPhi')
        if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4):
            h_Diboson.Fill(CSV_Diboson)
        if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (CSV_Diboson <= 0.86):
            h_DibosonFailed.Fill(CSV_Diboson)
            h_pfdiboson.Fill(0.5)
            h_pfdibosonfailf.Fill(0.5)
            h_pfdibosonpassf.Fill(1.5)
        if (SD_Diboson > 100.0) and (SD_Diboson < 150.0) and (dPhi_Diboson > 0.4) and (CSV_Diboson > 0.86):
            h_DibosonPassed.Fill(CSV_Diboson)
            h_pfdiboson.Fill(1.5)
            h_pfdibosonfailp.Fill(0.5)
            h_pfdibosonpassp.Fill(1.5)

    h_Diboson = h_Diboson*(L*xsDiboson[k]/totalEventsDiboson)
    h_DibosonPassed = h_DibosonPassed*(L*xsDiboson[k]/totalEventsDiboson)
    h_DibosonFailed = h_DibosonFailed*(L*xsDiboson[k]/totalEventsDiboson)
    h_pfdiboson = h_pfdiboson*(L*xsDiboson[k]/totalEventsDiboson)
    h_pfdibosonfailf = h_pfdibosonfailf*(L*xsDiboson[k]/totalEventsDiboson)
    h_pfdibosonfailp = h_pfdibosonfailp*(L*xsDiboson[k]/totalEventsDiboson)
    h_pfdibosonpassf = h_pfdibosonpassf*(L*xsDiboson[k]/totalEventsDiboson)
    h_pfdibosonpassp = h_pfdibosonpassp*(L*xsDiboson[k]/totalEventsDiboson)

    h_sumDiboson += h_Diboson
    h_sumDibosonPassed += h_DibosonPassed
    h_sumDibosonFailed += h_DibosonFailed
    h_sumpfdiboson += h_pfdiboson
    h_sumpfdibosonfailf += h_pfdibosonfailf
    h_sumpfdibosonfailp += h_pfdibosonfailp
    h_sumpfdibosonpassf += h_pfdibosonpassf
    h_sumpfdibosonpassp += h_pfdibosonfailp



#---------------------------------#
#               DATA              #
#---------------------------------#
##               MET             ##
#---------------------------------#

MET_path = dirpath+"combined_data_MET.root"

h_MET = TH1F("h_MET", "", nbins, edges)
h_MET_Failed = TH1F("h_MET_Failed", "", nbins, edges)
h_MET_Passed = TH1F("h_MET_Passed", "", nbins, edges)
h_pfdata = TH1F("h_pfdata", "", 2, 0, 2)
h_pfdatapassp = TH1F("h_pfdatapassp", "", 2, 0, 2)
h_pfdatapassf = TH1F("h_pfdatapassf", "", 2, 0, 2)
h_pfdatafailp = TH1F("h_pfdatafailp", "", 2, 0, 2)
h_pfdatafailf = TH1F("h_pfdatafailf", "", 2, 0, 2)

openMET = TFile(MET_path, "read")
h_total_mcweight_MET = openMET.Get("h_total_mcweight")
totalEventsMET = h_total_mcweight_MET.Integral()
treeMET = openMET.Get("monoHbb_Topmu_boosted")
EventsMET = treeMET.GetEntries()

for i in range(EventsMET):
    treeMET.GetEntry(i)
    CSV_MET = getattr(treeMET, 'FJetCSV')
    SD_MET = getattr(treeMET, 'FJetMass')
    dPhi_MET = getattr(treeMET, 'min_dPhi')
    if (SD_MET > 100.0) and (SD_MET < 150.0) and (dPhi_MET > 0.4):
        h_MET.Fill(CSV_MET)
    if (SD_MET > 100.0) and (SD_MET < 150.0) and (dPhi_MET > 0.4) and (CSV_MET <= 0.86):
        h_MET_Failed.Fill(CSV_MET)
        h_pfdata.Fill(0.5)
        h_pfdatafailf.Fill(0.5)
        h_pfdatapassf.Fill(1.5)
    if (SD_MET > 100.0) and (SD_MET < 150.0) and (dPhi_MET > 0.4) and (CSV_MET > 0.86):
        h_MET_Passed.Fill(CSV_MET)
        h_pfdata.Fill(1.5)
        h_pfdatafailp.Fill(0.5)
        h_pfdatapassp.Fill(1.5)

SubtractedData = h_MET.Clone("SubtractedData")
SubtractedData = SubtractedData - (h_sumWJets + h_sumDiboson)# + h_ttHad + h_ttLep)
SubtractedDataPassed = h_MET_Passed.Clone("SubtractedDataPassed")
SubtractedDataPassed = SubtractedDataPassed - (h_sumWJetsPassed + h_sumDibosonPassed)# + h_ttHadPassed + h_ttLepPassed)
SubtractedDataFailed = h_MET_Failed.Clone("SubtractedDataFailed")
SubtractedDataFailed = SubtractedDataFailed - (h_sumWJetsFailed + h_sumDibosonFailed)# + h_ttHadFailed + h_ttLepFailed)

h_pfdata = h_pfdata - (h_sumpfWjets + h_sumpfdiboson)# + h_pfttHad + h_pfttLep)
h_pfdatafailf = h_pfdatafailf - (h_sumpfWjetsfailf + h_sumpfdibosonfailf)
h_pfdatafailp = h_pfdatafailp - (h_sumpfWjetsfailp + h_sumpfdibosonfailp)
h_pfdatapassf = h_pfdatapassf - (h_sumpfWjetspassf + h_sumpfdibosonpassf)
h_pfdatapassp = h_pfdatapassp - (h_sumpfWjetspassp + h_sumpfdibosonpassp)
h_pfdatatotal = h_pfdatafailf.Clone("h_pfdatatotal")
h_pfdatatotal = h_pfdatatotal + h_pfdatafailp + h_pfdatapassf + h_pfdatapassp

h_totaldata = SubtractedDataPassed.Clone("h_totaldata")
h_totaldata = h_totaldata + SubtractedDataFailed
frac_tt_data_passed = (SubtractedDataPassed.Integral())/(h_totaldata.Integral())*100
frac_tt_data_failed = (SubtractedDataFailed.Integral())/(h_totaldata.Integral())*100

print "Mistagged tt Data fraction :", frac_tt_data_passed
print "Failed tt Data fraction :", frac_tt_data_failed
print " "


Cloned_frac_tt_data_failed = SubtractedDataFailed.Clone("Cloned_frac_tt_data_failed")
Cloned_frac_tt_data_passed = SubtractedDataPassed.Clone("Cloned_frac_tt_data_passed")
Cloned_frac_tt_data_total = h_totaldata.Clone("Cloned_frac_tt_data_total")

h_pfdataTopMu = h_pfdata.Clone("h_pfdataTopMu")



#** MISTAG SCALE FACTOR **#

SF = frac_tt_data_passed / frac_Passed
print " "
print "DDB Mistag SF :", SF
print " "



def dataPredRatio(data_, totalBkg_):
    dataPredRatio_ = data_ - totalBkg_
    dataPredRatio_.Divide(totalBkg_)
    return dataPredRatio_

#------------Overlap histograms in Full Canvas-------------#

frac_match_text = str(round(frac_match, 2))
frac_Wmatch_text = str(round(frac_Wmatch, 2))
frac_unmatch_text = str(round(frac_unmatch, 2))


h_TopMatchFinal = h_TopMatch.Clone("h_TopMatchFinal")
h_WmatchFinal = h_Wmatch.Clone("h_WmatchFinal")
h_unmatchFinal = h_unmatch.Clone("h_unmatchFinal")
h_ttHadFinal = h_ttHad.Clone("h_ttHadFinal")
h_ttLepFinal = h_ttLep.Clone("h_ttLepFinal")
h_sumWJetsFinal = h_sumWJets.Clone("h_sumWJetsFinal")


h_sumWJetsFinal = h_sumWJetsFinal + h_sumDiboson
h_ttLepFinal = h_sumWJetsFinal# + h_ttLepFinal
h_ttHadFinal = h_ttLepFinal# + h_ttHadFinal
h_unmatchFinal = h_unmatchFinal + h_ttHadFinal
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

padMain.cd()

h_TopMatchFinal.SetFillColor(821)
h_TopMatchFinal.SetLineColor(821)#923
h_TopMatchFinal.GetXaxis().SetTitle("Double b score")
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


'''
h_ttHadFinal.SetFillColor(800)
h_ttHadFinal.SetLineColor(800)
leg.AddEntry(h_ttHadFinal, "tt Hadronic","f")


h_ttLepFinal.SetFillColor(809)
h_ttLepFinal.SetLineColor(809)
leg.AddEntry(h_ttLepFinal, "tt Leptonic","f")
'''

h_sumWJetsFinal.SetFillColor(854)
h_sumWJetsFinal.SetLineColor(854)
leg.AddEntry(h_sumWJetsFinal, "W+Jets","f")

h_sumDiboson.SetFillColor(627)
h_sumDiboson.SetLineColor(627)
leg.AddEntry(h_sumDiboson, "Diboson","f")

h_MET.SetLineColor(1)
h_MET.SetMarkerStyle(20)
h_MET.SetMarkerSize(1.5)
leg.AddEntry(h_MET, "Data", "lep")

#-------Draw Histogram in Full Canvas---------#

h_TopMatchFinal.Draw("hist")
h_WmatchFinal.Draw("histsame")
h_unmatchFinal.Draw("histsame")
#h_ttHadFinal.Draw("histsame")
#h_ttLepFinal.Draw("histsame")
h_sumWJetsFinal.Draw("histsame")
h_sumDiboson.Draw("histsame")
h_MET.Draw("e1same")
leg.Draw()

lt = TLatex()
lt.DrawLatexNDC(0.24,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
lt.DrawLatexNDC(0.24,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
lt.DrawLatexNDC(0.24,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")


padRatio.cd()

gPad.GetUymax()

ratio = dataPredRatio(data_ = h_MET, totalBkg_ = h_TopMatchFinal)
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

#full.cd()
#full.Modified()
full.Update()
full.SaveAs("new_output/Topmu_unsubtracted.pdf")


#------------Overlap histograms in Subtract Canvas-------------#

frac_Passed_text = str(round(frac_Passed, 2))

subtract = TCanvas("subtract","subtract",900,700) #width-height
subtract.SetLeftMargin(0.15)
gStyle.SetOptStat(0)

leg2 = TLegend(0.4,0.5,0.6,0.6)
leg2.SetBorderSize(0)
leg2.SetTextSize(0.027)

#h_ttFailed.Rebin(2)
h_ttFailed.SetFillColor(821)
h_ttFailed.SetLineColor(821)#933
h_ttFailed.GetXaxis().SetTitle("Double b score")
h_ttFailed.GetYaxis().SetTitle("Events/Bin")
h_ttFailed.SetMaximum(ttmax)
leg2.AddEntry(h_ttFailed, "t#bar{t}", "f")

#h_ttPassed.Rebin(2)
h_ttPassed.SetFillColor(622)
h_ttPassed.SetLineColor(622)
h_ttPassed.GetXaxis().SetTitle("Double b score")
h_ttPassed.GetYaxis().SetTitle("Events/Bin")
h_ttPassed.SetMaximum(ttmax)
leg2.AddEntry(h_ttPassed, "t#bar{t} mistag ("+frac_Passed_text+"%)", "f")

#SubtractedData.Rebin(2)
SubtractedData.SetLineColor(1)
SubtractedData.SetMarkerStyle(20)
SubtractedData.SetMarkerSize(1.5)
SubtractedData.GetXaxis().SetTitle("Double b score")
SubtractedData.GetYaxis().SetTitle("Events/Bin")
leg2.AddEntry(SubtractedData, "Data-Bkg.", "lep")

#-------Draw Histogram in Subtract Canvas---------#

h_ttFailed.Draw("hist")
h_ttPassed.Draw("histsame")
SubtractedData.Draw("e1same")
leg2.Draw()

lt2 = TLatex()
lt2.DrawLatexNDC(0.23,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
lt2.DrawLatexNDC(0.23,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
lt2.DrawLatexNDC(0.23,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt2.DrawLatexNDC(0.71,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")

#subtract.cd()
#subtract.Modified()
subtract.Update()
subtract.SaveAs("new_output/Topmu_subtracted.pdf")


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

#pfdatatotal = h_totaldata.Integral()
#h_pfdata = h_pfdata*(1/pfdatatotal)
h_pfdata.Sumw2()
h_pfdata.Divide(h_pfdatatotal)
h_pfdata.SetLineColor(1)
h_pfdata.SetMarkerStyle(20)
h_pfdata.SetLineWidth(2)
h_pfdata.SetMaximum(1.5)
h_pfdata.GetYaxis().SetTitle("Fraction")
h_pfdata.GetXaxis().SetTickLength(0.03)
h_pfdata.GetXaxis().SetNdivisions(104)
h_pfdata.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Fail")
h_pfdata.GetXaxis().ChangeLabel(1,-1,0)
h_pfdata.GetXaxis().ChangeLabel(3,-1,0)
h_pfdata.GetXaxis().ChangeLabel(-1,-1,0)
h_pfdata.GetXaxis().ChangeLabel(-2,-1,-1,-1,-1,-1,"Pass")
leg3.AddEntry(h_pfdata, "Subtracted Data", "lep")

#pfMCtotal = h_tt.Integral()
#h_pfMC = h_pfMC*(1/pfMCtotal)
h_pfMC.Sumw2()
h_pfMC.Divide(h_pfMCtotal)
h_pfMC.SetLineColor(870)
h_pfMC.SetMarkerColor(870)
h_pfMC.SetLineWidth(3)
leg3.AddEntry(h_pfMC, "tt", "lep")

h_pfdata.Draw("e1")
h_pfMC.Draw("e1histsame")
leg3.Draw()

lt3 = TLatex()
lt3.DrawLatexNDC(0.21,0.85,"#scale[0.8]{CMS} #scale[0.65]{#bf{#it{Internal}}}")
lt3.DrawLatexNDC(0.21,0.8,"#scale[0.7]{#bf{t#bar{t} CR (#mu)}}")
lt3.DrawLatexNDC(0.21,0.75,"#scale[0.5]{#bf{2-prong (bq) enriched}}")
lt3.DrawLatexNDC(0.67,0.92,"#scale[0.7]{#bf{41.5 fb^{-1} (13 TeV)}}")
lt3.Draw()

#** Pad2 **#
pad2.cd()

Cloned_frac_tt_data_passed.Rebin(14)
Cloned_frac_tt_data_total.Rebin(14)
Cloned_frac_tt_data_passed.Sumw2()
Cloned_frac_tt_data_passed.Divide(Cloned_frac_tt_data_total)

Cloned_frac_ttPassed.Rebin(14)
Cloned_frac_tt.Rebin(14)
Cloned_frac_ttPassed.Sumw2()
Cloned_frac_ttPassed.Divide(Cloned_frac_tt)

Cloned_frac_tt_data_passed.SetLineColor(1)
Cloned_frac_tt_data_passed.SetLineWidth(2)
Cloned_frac_tt_data_passed.SetMarkerStyle(20)
Cloned_frac_tt_data_passed.GetYaxis().SetTitle("Fraction")
Cloned_frac_tt_data_passed.GetYaxis().SetTitleSize(0.09)
Cloned_frac_tt_data_passed.GetYaxis().SetNdivisions(204)
Cloned_frac_tt_data_passed.GetYaxis().SetLabelSize(0.1)
Cloned_frac_tt_data_passed.SetMaximum(0.2)
Cloned_frac_tt_data_passed.SetMinimum(0.0)
Cloned_frac_tt_data_passed.GetXaxis().SetTitle("")
Cloned_frac_tt_data_passed.GetXaxis().SetLabelSize(0.09)
Cloned_frac_tt_data_passed.GetXaxis().SetLabelOffset(0.02)
Cloned_frac_tt_data_passed.GetXaxis().SetNdivisions(104)
Cloned_frac_tt_data_passed.GetXaxis().ChangeLabel(2,-1,-1,-1,-1,-1,"Pass")
Cloned_frac_tt_data_passed.GetXaxis().ChangeLabel(1,-1,0)
Cloned_frac_tt_data_passed.GetXaxis().ChangeLabel(-1,-1,0)

Cloned_frac_ttPassed.SetLineColor(870)
Cloned_frac_ttPassed.SetMarkerColor(870)
Cloned_frac_ttPassed.SetLineWidth(3)

Cloned_frac_tt_data_passed.Draw("e1")
Cloned_frac_ttPassed.Draw("e1histsame")

#** Pad3 **#
pad3.cd()

mistagSF = Cloned_frac_tt_data_passed.Clone("mistagSF")
mistagSF.Sumw2()
mistagSF.Divide(Cloned_frac_ttPassed)

print "******"
print "mistag SF:", mistagSF.Integral()

SFfinal = round(SF, 2)
SFtext = "SF = "+str(SFfinal)

mistagSF.SetLineColor(797)
mistagSF.SetMarkerColor(797)
mistagSF.SetLineWidth(3)
mistagSF.SetMaximum(1.2)
mistagSF.SetMinimum(0.6)
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
scalefactor.SaveAs("new_output/Topmu_SF.pdf")



# Save the canvases in root file #

print " "
print "Generating TopMu.root"

outfile = TFile("TopMu.root", "RECREATE")
h_TopMatch.Write()
h_Wmatch.Write()
h_unmatch.Write()
h_sumWJets.Write()
h_sumDiboson.Write()
h_MET.Write()

h_ttFailed.Write()
h_ttPassed.Write()
SubtractedData.Write()

h_pfdataTopMu.Write()
h_pfdatatotal.Write()
h_pfMCtopMu.Write()
h_pfMCtotal.Write()

SubtractedDataPassed.Write()
h_totaldata.Write()
#h_ttPassed.Write()
h_tt.Write()

outfile.Close()
print "Finish generating TopMu.root"
