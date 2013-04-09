import ROOT
import numpy as np
import whale_helper as helper
import aifc, os, subprocess, csv
import array
from math import fabs

if __name__ == '__main__':
    var0 = array.array('f',[0])
    var1 = array.array('f',[0])
    var2 = array.array('f',[0])
    var3 = array.array('f',[0])
    var4 = array.array('f',[0])
    var5 = array.array('f',[0])
    var6 = array.array('f',[0])
    var7 = array.array('f',[0])
    var8 = array.array('f',[0])
    var9 = array.array('f',[0])
    var10 = array.array('f',[0])
    var11 = array.array('f',[0])
    var12 = array.array('f',[0])
    var13 = array.array('f',[0])
    var14 = array.array('f',[0])
    var15 = array.array('f',[0])
    var16 = array.array('f',[0])
    var17 = array.array('f',[0])
    var18 = array.array('f',[0])
    var19 = array.array('f',[0])
    var20 = array.array('f',[0])
    var21 = array.array('f',[0])
    var22 = array.array('f',[0])
    var23 = array.array('f',[0])
    var24 = array.array('f',[0])
    var25 = array.array('f',[0])
    var26 = array.array('f',[0])
    var27 = array.array('f',[0])
    var28 = array.array('f',[0])
    var29 = array.array('f',[0])
    var30 = array.array('f',[0])
    var31 = array.array('f',[0])
    var32 = array.array('f',[0])
    var33 = array.array('f',[0])
    var34 = array.array('f',[0])
    var35 = array.array('f',[0])
    var36 = array.array('f',[0])
    var37 = array.array('f',[0])
    var38 = array.array('f',[0])
    var39 = array.array('f',[0])
    var40 = array.array('f',[0])
    var41 = array.array('f',[0])
    var42 = array.array('f',[0])
    var43 = array.array('f',[0])
    var44 = array.array('f',[0])
    var45 = array.array('f',[0])
    var46 = array.array('f',[0])
    var47 = array.array('f',[0])
    var48 = array.array('f',[0])
    var49 = array.array('f',[0])
    var50 = array.array('f',[0])
    
    reader = ROOT.TMVA.Reader()
    reader.AddVariable("ff",var0)
    reader.AddVariable("fft0",var1)
    reader.AddVariable("fft1",var2)
    reader.AddVariable("fft2",var3)
    reader.AddVariable("fft3",var4)
    reader.AddVariable("fft4",var5)
    reader.AddVariable("fft5",var6)
    reader.AddVariable("fft6",var7)
    reader.AddVariable("fft7",var8)
    reader.AddVariable("fft8",var9)
    reader.AddVariable("fft9",var10)
    reader.AddVariable("sg0",var11)
    reader.AddVariable("sg1",var12)
    reader.AddVariable("sg2",var13)
    reader.AddVariable("sg3",var14)
    reader.AddVariable("sg4",var15)
    reader.AddVariable("sg5",var16)
    reader.AddVariable("sg6",var17)
    reader.AddVariable("sg7",var18)
    reader.AddVariable("sg8",var19)
    reader.AddVariable("sg9",var20)
    reader.AddVariable("sg10",var21)
    reader.AddVariable("sg11",var22)
    reader.AddVariable("sg12",var23)
    reader.AddVariable("sg13",var24)
    reader.AddVariable("sg14",var25)
    reader.AddVariable("sg15",var26)
    reader.AddVariable("sg16",var27)
    reader.AddVariable("sg17",var28)
    reader.AddVariable("sg18",var29)
    reader.AddVariable("sg19",var30)
    reader.AddVariable("sg20",var31)
    reader.AddVariable("sg21",var32)
    reader.AddVariable("sg22",var33)
    reader.AddVariable("sg23",var34)
    reader.AddVariable("sg24",var35)
    reader.AddVariable("sg25",var36)
    reader.AddVariable("sg26",var37)
    reader.AddVariable("sg27",var38)
    reader.AddVariable("sg28",var39)
    reader.AddVariable("sg29",var40)
    reader.AddVariable("sg30",var41)
    reader.AddVariable("sg31",var42)
    reader.AddVariable("sg32",var43)
    reader.AddVariable("sg33",var44)
    reader.AddVariable("sg34",var45)
    reader.AddVariable("sg35",var46)
    reader.AddVariable("sg36",var47)
    reader.AddVariable("sg37",var48)
    reader.AddVariable("sg38",var49)
    reader.AddVariable("sg39",var50)
    reader.BookMVA("BDT","weights/TMVAClassification_BDT_1000.weights.xml")
    reader.BookMVA("MLP","weights/TMVAClassification_MLP_51.weights.xml")
    reader.BookMVA("SVM","weights/TMVAClassification_SVM.weights.xml")
    reader.BookMVA("MLP5151","weights/TMVAClassification_MLP_51_51.weights.xml")
    reader.BookMVA("MLP5110","weights/TMVAClassification_MLP_ANN_51_10.weights.xml")
    reader.BookMVA("BDT2","weights/TMVAClassification_BDT_5000.weights.xml")
    
    fin = ROOT.TFile("test_data.root")
    #fin = ROOT.TFile("data.root")
    tree = fin.Get("ntuple")
    f1 = open('sub_1.txt', 'w')
    f2 = open('sub_2.txt', 'w')
    f3 = open('sub_3.txt', 'w')
    f4 = open('sub_4.txt', 'w')
    for feature in tree:
        var0[0] = feature.ff
        var1[0] = feature.fft0
        var2[0] = feature.fft1
        var3[0] = feature.fft2
        var4[0] = feature.fft3
        var5[0] = feature.fft4
        var6[0] = feature.fft5
        var7[0] = feature.fft6
        var8[0] = feature.fft7
        var9[0] = feature.fft8
        var10[0] = feature.fft9
        var11[0] = feature.sg0
        var12[0] = feature.sg1
        var13[0] = feature.sg2
        var14[0] = feature.sg3
        var15[0] = feature.sg4
        var16[0] = feature.sg5
        var17[0] = feature.sg6
        var18[0] = feature.sg7
        var19[0] = feature.sg8
        var20[0] = feature.sg9
        var21[0] = feature.sg10
        var22[0] = feature.sg11
        var23[0] = feature.sg12
        var24[0] = feature.sg13
        var25[0] = feature.sg14
        var26[0] = feature.sg15
        var27[0] = feature.sg16
        var28[0] = feature.sg17
        var29[0] = feature.sg18
        var30[0] = feature.sg19
        var31[0] = feature.sg20
        var32[0] = feature.sg21
        var33[0] = feature.sg22
        var34[0] = feature.sg23
        var35[0] = feature.sg24
        var36[0] = feature.sg25
        var37[0] = feature.sg26
        var38[0] = feature.sg27
        var39[0] = feature.sg28
        var40[0] = feature.sg29
        var41[0] = feature.sg30
        var42[0] = feature.sg31
        var43[0] = feature.sg32
        var44[0] = feature.sg33
        var45[0] = feature.sg34
        var46[0] = feature.sg35
        var47[0] = feature.sg36
        var48[0] = feature.sg37
        var49[0] = feature.sg38
        var50[0] = feature.sg39
        file_in = feature.whale

        bdtOutput = reader.EvaluateMVA("BDT2")
        bdtOutput2 = reader.EvaluateMVA("MLP")
        bdtOutput3 = reader.EvaluateMVA("SVM")
        bdtOutput4 = reader.EvaluateMVA("MLP5151")
        bdtOutput5 = reader.EvaluateMVA("MLP5110")
        f1.write(str(fabs(bdtOutput2)))
        f1.write('\n')
        f2.write(str(fabs(bdtOutput3)))
        f2.write('\n')
        f3.write(str(fabs(bdtOutput4)))
        f3.write('\n')
        f4.write(str(fabs(bdtOutput5)))
        f4.write('\n')
        #print  bdtOutput, bdtOutput2, bdtOutput3, bdtOutput4, bdtOutput5, file_in

