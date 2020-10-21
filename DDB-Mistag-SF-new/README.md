# DDB Mistag Scale Factor

Directory structure: 

DDB-Mistag-SF-new/DDB_mistagSF.py : for plotting Top (e) and Top (muon) CR histograms and calculating the statistical uncertainty
DDB-Mistag-SF-new/mergeEandMu.py : for plotting Top (e + muon) CR histograms and calculating the statistical uncertainty

## Setup framework 
You have to run the python script under CMS environment in lxplus. You can use any CMS environment. If you want to built one, you can follow the following instruction.

```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_3_0
cd CMSSW_10_3_0/src
cmsenv
git clone https://github.com/fasyakhuza/monoHbb.git
rm -r DDB_Mistag_SF
rm -r HEM_Issue
rm -r stackHistoPlots
cd DDB-Mistag-SF-new
```

## Run for Top (e) and Top (muon) CR
The `DDB_mistagSF.py` can be used for plotting DDB mistag scale factor of 2017 and 2018 data, for Top (e) and Top (muon) CR, and for several pT and MET bins, as well.

Change the `inputdirpath` at L70 and L74 to be your inputdirpath.

Change the `outdir` at L75 to be your output directory.

Note: Don't forget to always do `cmsenv` whenever you want to run the python script

There are 3 arguments you have to use for running this python script.
1. The year, 2017 or 2018
```
-Y year [for particular data you want]
```
2. The control region, Top (e) or Top (muon) CR
```
-isTope True [if you want to analyze Top (e) CR]
-isTope False [if you want to analyze Top (muon) CR]
```
3. The range and with/without single top process
```
-WI Inclusive [with single top for inclusive analysis]
-WPT range [This is if you want to analyze in pT bins variation. You can change the "range" to be PT-200-350, PT-350-500, and PT-350-2000.]
-WMET range [This is if you want to analyze in several MET variation. You can change the "range" to be MET-200-270, MET-270-345, and MET-345-1000.]
```

### For example:

1. For Inclusive analysis, for 2017 data and Top (e) CR
```
python DDB_mistagSF.py -Y 2017 -isTope True -WI Inclusive
```
or for 2018 data and Top (muon) CR, you can run using
```
python DDB_mistagSF.py -Y 2018 -isTope False -WI Inclusive
```


2. For PT bin analysis, for 2017 data and Top (e) CR
```
python DDB_mistagSF.py -Y 2017 -isTope True -WPT PT-200-350
```
or for 2018 data and Top (muon) CR, you can run using
```
python DDB_mistagSF.py -Y 2018 -isTope False -WPT PT-350-500
```


3. For MET bin analysis, for 2017 data and Top (e) CR
```
python DDB_mistagSF.py -Y 2017 -isTope True -WMET MET-200-270
```
or for 2018 data and Top (muon) CR, you can run using
```
python DDB_mistagSF.py -Y 2018 -isTope False -WMET MET-345-1000
```

## Run for Top (e+mu)
This `mergeEandMu.py` need TopE.root and TopMu.root which are produced by using previous python script, thus you have to run the previous script before you run this script. They are located in output directory as the results of previous python script.

If you want to add dir path as input and output directory, you can change or add the `dir` at L52 and L54

You can execute this
```
python mergeEandMu.py -Y year -a AnalysisRange
```

For `year`, you can use 2017 or 2018

For `AnalysisRange`, you can change it with:
* Inclusive
* PT-200-350
* PT-250-500
* PT-500-2000
* MET-200-270
* MET-270-345
* MET-345-1000

For example:
```
python mergeEandMu.py -Y 2017 -a MET-345-1000
```

## Calculate Systematic Uncertainty
`XSsysUnc.py` is needed to calculate the systematic uncertainty. This will take a bit long time for running this python script.

You can change the ntuples path at L113 and L117.

For 2017 data, if you want to use `monohbb.v06.00.01.2017_NCU` version, you can uncomment L76-L83 and turn L86-L93 to be comment, and vice versa.

To run this python script, you can follow this command
```
python XSsysUnc.py -Y year -a AnalysisRange
```

You can use 2017 or 2018 for the `year`

For the `AnalysisRange`, you can change it to be:
* Inclusive
* PT-200-350
* PT-350-500
* PT-500-2000
* MET-200-270
* MET-270-345
* MET-345-1000

Thus, for example, if you want to calculate the systematic uncertainty of DDB mistag scale factor of MET-270-345 bin for 2018 data, you can run:
```
python XSsysUnc.py -Y 2018 -a MET-270-345
```




