import ROOT
import numpy as np
import whale_helper as helper
import aifc, os, subprocess, csv
import array


if __name__ == '__main__':
    fin = ROOT.TFile("data.root")
    ntuple = fin.Get("ntuple")
    
    ROOT.TMVA.Tools.Instance()
    fout = ROOT.TFile("test.root","RECREATE")
    
    factory = ROOT.TMVA.Factory("TMVAClassification", fout,
                                ":".join([
                                          "V",
                                          "!Silent",
                                          "Color",
                                          "DrawProgressBar",
                                          "Transformations=I;N;D;P;",
                                          "AnalysisType=Classification"]
                                         ))
    
    factory.AddVariable("ff","F")
    factory.AddVariable("fft0","F")
    factory.AddVariable("fft1","F")
    factory.AddVariable("fft2","F")
    factory.AddVariable("fft3","F")
    factory.AddVariable("fft4","F")
    factory.AddVariable("fft5","F")
    factory.AddVariable("fft6","F")
    factory.AddVariable("fft7","F")
    factory.AddVariable("fft8","F")
    factory.AddVariable("fft9","F")
    factory.AddVariable("sg0","F")
    factory.AddVariable("sg1","F")
    factory.AddVariable("sg2","F")
    factory.AddVariable("sg3","F")
    factory.AddVariable("sg4","F")
    factory.AddVariable("sg5","F")
    factory.AddVariable("sg6","F")
    factory.AddVariable("sg7","F")
    factory.AddVariable("sg8","F")
    factory.AddVariable("sg9","F")
    factory.AddVariable("sg10","F")
    factory.AddVariable("sg11","F")
    factory.AddVariable("sg12","F")
    factory.AddVariable("sg13","F")
    factory.AddVariable("sg14","F")
    factory.AddVariable("sg15","F")
    factory.AddVariable("sg16","F")
    factory.AddVariable("sg17","F")
    factory.AddVariable("sg18","F")
    factory.AddVariable("sg19","F")
    factory.AddVariable("sg20","F")
    factory.AddVariable("sg21","F")
    factory.AddVariable("sg22","F")
    factory.AddVariable("sg23","F")
    factory.AddVariable("sg24","F")
    factory.AddVariable("sg25","F")
    factory.AddVariable("sg26","F")
    factory.AddVariable("sg27","F")
    factory.AddVariable("sg28","F")
    factory.AddVariable("sg29","F")
    factory.AddVariable("sg30","F")
    factory.AddVariable("sg31","F")
    factory.AddVariable("sg32","F")
    factory.AddVariable("sg33","F")
    factory.AddVariable("sg34","F")
    factory.AddVariable("sg35","F")
    factory.AddVariable("sg36","F")
    factory.AddVariable("sg37","F")
    factory.AddVariable("sg38","F")
    factory.AddVariable("sg39","F")
    factory.AddSignalTree(ntuple)
    factory.AddBackgroundTree(ntuple)
    
    # cuts defining the signal and background sample
    sigCut = ROOT.TCut("whale > 0.5")
    bgCut = ROOT.TCut("whale <= 0.5")
    
    factory.PrepareTrainingAndTestTree(sigCut,   # signal events
                                       bgCut,    # background events
                                       ":".join([
                                                 "nTrain_Signal=20000",
                                                 "nTrain_Background=20000",
                                                 "nTest_Signal=0",
                                                 "nTest_Background=0",
                                                 "SplitMode=Random",
                                                 "NormMode=NumEvents",
                                                 "!V"
                                                 ]))
    '''
    met1 = factory.BookMethod(ROOT.TMVA.Types.kBDT, "BDT_5000",
                                    ":".join([
                                              "H",
                                              "!V",
                                              "NTrees=5000",
                                              "nEventsMin=500",
                                              "MaxDepth=1000000",
                                              "BoostType=AdaBoost",
                                              "AdaBoostBeta=0.5",
                                              "SeparationType=GiniIndex",
                                              "nCuts=20",
                                              "PruneMethod=NoPruning"
                                              ]))
    '''
    met2 = factory.BookMethod(ROOT.TMVA.Types.kBDT, "BDT_1000",
                                       ":".join([
                                                 "H",
                                                 "!V",
                                                 "NTrees=1000",
                                                 #"nEventsMin=100",
                                                 "MaxDepth=1000",
                                                 "BoostType=AdaBoost",
                                                 "AdaBoostBeta=0.5",
                                                 "SeparationType=GiniIndex",
                                                 "nCuts=200",
                                                 "PruneMethod=CostComplexity",
                                                 "PruneStrength=-1"
                                                 ]))
    
    met5 = factory.BookMethod(ROOT.TMVA.Types.kSVM, "SVM", "" );
    '''
    met3 = factory.BookMethod(ROOT.TMVA.Types.kMLP, "MLP_51",
                             ":".join([
                                       "H",
                                       "NCycles=500",
                                       "HiddenLayers=51",
                                       "NeuronType=sigmoid",
                                       "TrainingMethod=BP",
                                       "LearningRate=0.02",
                                       "DecayRate=0.01",
                                       "TestRate=10",
                                       "Sampling=1",
                                       "SamplingEpoch=1",
                                       "SamplingImportance=1",
                                       "ResetStep=50",
                                       "BPMode=sequential",
                                       "ConvergenceImprove=0",                                       
                                       "ConvergenceTests=-1"
                                       ]))
    met3 = factory.BookMethod(ROOT.TMVA.Types.kMLP, "MLP_51_51",
                              ":".join([
                                        "H",
                                        "NCycles=500",
                                        "HiddenLayers=51,51",
                                        "NeuronType=sigmoid",
                                        "TrainingMethod=BP",
                                        "LearningRate=0.02",
                                        "DecayRate=0.01",
                                        "TestRate=10",
                                        "Sampling=1",
                                        "SamplingEpoch=1",
                                        "SamplingImportance=1",
                                        "ResetStep=50",
                                        "BPMode=sequential",
                                        "ConvergenceImprove=0",
                                        "ConvergenceTests=-1"
                                        ]))
    
    met4 = factory.BookMethod(ROOT.TMVA.Types.kMLP, "MLP_ANN_51_10",
                             ":".join([
                                       "H",
                                       "NCycles=500",
                                       "HiddenLayers=51,10",
                                       "NeuronType=sigmoid",
                                       "TrainingMethod=BP",
                                       "LearningRate=0.02",
                                       "DecayRate=0.01",
                                       "TestRate=10",
                                       "Sampling=1",
                                       "SamplingEpoch=1",
                                       "SamplingImportance=1",
                                       "ResetStep=50",
                                       "BPMode=sequential",
                                       "ConvergenceImprove=0",
                                       "ConvergenceTests=-1"
                                       ]))
    
    met5 = factory.BookMethod(ROOT.TMVA.Types.kLikelihood, "BoostedLikelihood",
                                 ":".join([
                                           "Boost_Num=10",
                                           "Boost_Type=AdaBoost",
                                           "!TransformOutput",
                                           "PDFInterpol=KDE",
                                           "KDEtype=Gauss",
                                           "KDEiter=Adaptive",
                                           "KDEFineFactor=0.3",
                                           "KDEborder=None",
                                           "NAvEvtPerBin=50"
                                           ]))
    
    met6 = factory.BookMethod(ROOT.TMVA.Types.kCuts, "annealing",
                             ":".join([
                                       "!H",
                                       "!V",
                                       "FitMethod=SA",
                                       "EffSel",
                                       "MaxCalls=150000",
                                       "KernelTemp=IncAdaptive",
                                       "InitialTemp=1e+6",
                                       "MinTemp=1e-6",
                                       "Eps=1e-10",
                                       "UseDefaultScale"
                                        ]))
    '''
    
    factory.TrainAllMethods()
    factory.TestAllMethods()
    factory.EvaluateAllMethods()
    
    raw_input("Done. Press any key to exit.")

