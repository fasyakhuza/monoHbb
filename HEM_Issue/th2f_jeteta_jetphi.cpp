//
//  th2f_jeteta_jetphi.cpp
//  
//
//  Created by Fasya Khuzaimah on 07.06.20.
//

//#include "TFile.h"
//#include "TTree.h"
//#include "TH2F.h"

void th2f_jeteta_jetphi(){
    TFile *fileAB_before = new TFile("analysis_output/2018_combined_data/combined_data_SE_AB.root");
    TFile *fileCD_before = new TFile("analysis_output/2018_combined_data/combined_data_SE_CD.root");
    TFile *fileTotal_before = new TFile("analysis_output/2018_combined_data/combined_data_SE.root");
    
    TFile *fileAB_after = new TFile("analysis_output/2018_hem_cut_updated_combined/combined_data_SE_AB.root");
    TFile *fileCD_after = new TFile("analysis_output/2018_hem_cut_updated_combined/combined_data_SE_CD.root");
    TFile *fileTotal_after = new TFile("analysis_output/2018_hem_cut_updated_combined/combined_data_SE.root");
    
    TH2F *h_AB_before = new TH2F("h_AB_before", "Top(enu) + 1b; #eta; #phi", 30, -2.5, 2.5, 30, -3.14, 3.14);
    TH2F *h_CD_before = new TH2F("h_CD_before", "Top(enu) + 1b; #eta; #phi", 30, -2.5, 2.5, 30, -3.14, 3.14);
    TH2F *h_Total_before = new TH2F("h_Total_before", "Top(enu) + 1b; #eta; #phi", 30, -2.5, 2.5, 30, -3.14, 3.14);
    
    TH2F *h_AB_after = new TH2F("h_AB_after", "Top(enu) + 1b; #eta; #phi", 30, -2.5, 2.5, 30, -3.14, 3.14);
    TH2F *h_CD_after = new TH2F("h_CD_after", "Top(enu) + 1b; #eta; #phi", 30, -2.5, 2.5, 30, -3.14, 3.14);
    TH2F *h_Total_after = new TH2F("h_Total_after", "Top(enu) + 1b; #eta; #phi", 30, -2.5, 2.5, 30, -3.14, 3.14);
    
    
    TCanvas *c1 = new TCanvas("c1","c1",600,500);
    gStyle->SetOptStat(0);
    
    TTree *treeAB_before = (TTree*)fileAB_before->Get("bbDM_TopenuCR_1b");
    treeAB_before->Draw("Jet1Phi:Jet1Eta>>h_AB_before");
    h_AB_before->Draw("COLZ");
    c1->SaveAs("plots/TH2F/pdf/AB_before.pdf");
    c1->SaveAs("plots/TH2F/png/AB_before.png");
    
    TTree *treeCD_before = (TTree*)fileCD_before->Get("bbDM_TopenuCR_1b");
    treeCD_before->Draw("Jet1Phi:Jet1Eta>>h_CD_before");
    h_CD_before->Draw("COLZ");
    c1->SaveAs("plots/TH2F/pdf/CD_before.pdf");
    c1->SaveAs("plots/TH2F/png/CD_before.png");
    
    TTree *treeTotal_before = (TTree*)fileTotal_before->Get("bbDM_TopenuCR_1b");
    treeTotal_before->Draw("Jet1Phi:Jet1Eta>>h_Total_before");
    h_Total_before->Draw("COLZ");
    c1->SaveAs("plots/TH2F/pdf/Total_before.pdf");
    c1->SaveAs("plots/TH2F/png/Total_before.png");
    
    
    TTree *treeAB_after = (TTree*)fileAB_after->Get("bbDM_TopenuCR_1b");
    treeAB_after->Draw("Jet1Phi:Jet1Eta>>h_AB_after");
    h_AB_after->Draw("COLZ");
    c1->SaveAs("plots/TH2F/pdf/AB_after.pdf");
    c1->SaveAs("plots/TH2F/png/AB_after.png");
    
    TTree *treeCD_after = (TTree*)fileCD_after->Get("bbDM_TopenuCR_1b");
    treeCD_after->Draw("Jet1Phi:Jet1Eta>>h_CD_after");
    h_CD_after->Draw("COLZ");
    c1->SaveAs("plots/TH2F/pdf/CD_after.pdf");
    c1->SaveAs("plots/TH2F/png/CD_after.png");
    
    TTree *treeTotal_after = (TTree*)fileTotal_after->Get("bbDM_TopenuCR_1b");
    treeTotal_after->Draw("Jet1Phi:Jet1Eta>>h_Total_after");
    h_Total_after->Draw("COLZ");
    c1->SaveAs("plots/TH2F/pdf/Total_after.pdf");
    c1->SaveAs("plots/TH2F/png/Total_after.png");
    
}
