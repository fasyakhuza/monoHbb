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
git clone https://github.com/fasyakhuza/monoHbb/tree/master/DDB-Mistag-SF-new
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
-WOI Inclusive [without single top for inclusive analysis]
-WI Inclusive [with single top for inclusive analysis]
-WOPT range [This is if you want analyze WITHOUT single top. You can change the "range" to be 200-350, 350-500, and 350-2000.]
-WPT range [This is if you want analyze WITH single top. You can change the "range" to be 200-350, 350-500, and 350-2000.]
-WOMET range [This is if you want analyze WITHOUT single top. You can change the "range" to be 200-270, 270-345, and 345-1000.]
-WMET range [This is if you want analyze WITH single top. You can change the "range" to be 200-270, 270-345, and 345-1000.]
```

### For example:

1. For Inclusive analysis, Top (e) CR, and without single top process
```
python DDB_mistagSF.py -Y 2017 -isTope True -WOI Inclusive
```
or for 2018 data, Top (muon) CR, and with single top, you can run using
```
python DDB_mistagSF.py -Y 2018 -isTope False -WI Inclusive
```


2. For PT bin analysis, Top (e) CR, and without single top process
```
python DDB_mistagSF.py -Y 2017 -isTope True -WOPT 200-350
```
or for 2018 data, Top (muon) CR, and with single top, you can run using
```
python DDB_mistagSF.py -Y 2018 -isTope False -WPT 350-500
```


3. For MET bin analysis, Top (e) CR, and without single top process
```
python DDB_mistagSF.py -Y 2017 -isTope True -WOMET 200-270
```
or for 2018 data, Top (e) CR, and with single top, you can run using
```
python DDB_mistagSF.py -Y 2018 -isTope True -WMET 345-1000
```

## Run for Top (e+mu)
This `mergeEandMu.py` need TopE.root and TopMu.root which are produced by using previous python script. They are located in output directory as the results of previous python script.

If you want to add dir path as input and output directory, you can change or add the `dir` at L52 and L54

You can execute this
```
python mergeEandMu.py -Y year -isWithST True/False -a AnalysisRange
```

For year, you can use 2017 or 2018

For AnalysisRange, you can change it with:
* Inclusive
* pT200-350
* pT250-500
* pT500-2000
* MET200-270
* MET270-345
* MET345-1000

For example:
```
python mergeEandMu.py -Y 2017 -isWithST False -a MET345-1000
```


