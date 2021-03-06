#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["XZ", "Y_rad_birad"], products=["YXZ."], ownReverse=False)

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "XZ",
    group = "OR{CZ, OCO, OCddO, OSi, OSiddO}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([10.697,199.951,1165.72,3791.58,16682.7,40832.8,136474,252096],"m^3/(mol*s)","*|/",[365.604,123.517,67.2139,46.0466,30.0333,24.0597,19.0737,17.7446])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 137 rates.
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=85 label="CO_O">, <Entry index=112 label="O_rad/OneDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=141 label="C_rad/H/TwoDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=86 label="CO/H2_O">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=125 label="C_methyl">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=110 label="O_sec_rad">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=124 label="Cs_rad">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=109 label="O_pri_rad">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=89 label="CO/Nd2_O">, <Entry index=125 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=85 label="CO_O">, <Entry index=124 label="Cs_rad">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=85 label="CO_O">, <Entry index=120 label="CO_pri_rad">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=106 label="H_rad">]
[<Entry index=85 label="CO_O">, <Entry index=106 label="H_rad">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=5 label="Cd/H2">, <Entry index=124 label="Cs_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=5 label="Cd/H2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=109 label="O_pri_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=125 label="C_methyl">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=107 label="Ct_rad">]
[<Entry index=11 label="Cd/H2_Cd/De2">, <Entry index=125 label="C_methyl">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=124 label="Cs_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=106 label="H_rad">]
[<Entry index=5 label="Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=130 label="C_rad/H2/Cb">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=118 label="Cb_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=1 label="XZ">, <Entry index=2 label="Y_rad_birad">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=153 label="Cd_pri_rad-Cdd/Cd">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=132 label="C_rad/H2/O">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=129 label="C_rad/H2/Ct">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=116 label="Cd_rad/NonDe">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "Y_rad_birad",
    group = "OR{Y_rad, Y_birad}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "CZ",
    group = 
"""
1  *1 {Cd,Cdd,Ct,CO,Sid,Sidd,Sit} 0 {2,{D,T}}
2  *2 {Cd,Cdd,Ct,Od,Sid,Sidd,Sit} 0 {1,{D,T}}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.968163,0.974782,0.97879,0.981481,0.984874,0.98693,0.989711,0.99113],"m^3/(mol*s)","*|/",[244.973,91.1578,52.7119,37.6525,25.9055,21.4329,17.7227,16.8237])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 136 rates.
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=85 label="CO_O">, <Entry index=112 label="O_rad/OneDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=141 label="C_rad/H/TwoDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=86 label="CO/H2_O">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=125 label="C_methyl">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=110 label="O_sec_rad">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=124 label="Cs_rad">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=109 label="O_pri_rad">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=89 label="CO/Nd2_O">, <Entry index=125 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=85 label="CO_O">, <Entry index=124 label="Cs_rad">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=85 label="CO_O">, <Entry index=120 label="CO_pri_rad">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=106 label="H_rad">]
[<Entry index=85 label="CO_O">, <Entry index=106 label="H_rad">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=5 label="Cd/H2">, <Entry index=124 label="Cs_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=5 label="Cd/H2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=109 label="O_pri_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=125 label="C_methyl">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=107 label="Ct_rad">]
[<Entry index=11 label="Cd/H2_Cd/De2">, <Entry index=125 label="C_methyl">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=124 label="Cs_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=106 label="H_rad">]
[<Entry index=5 label="Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=130 label="C_rad/H2/Cb">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=118 label="Cb_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=116 label="Cd_rad/NonDe">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=153 label="Cd_pri_rad-Cdd/Cd">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=132 label="C_rad/H2/O">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=129 label="C_rad/H2/Ct">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "Cd_Cd",
    group = 
"""
1  *1 Cd 0 {2,D}
2  *2 Cd 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.555263,0.622651,0.667323,0.69913,0.741522,0.768611,0.807242,0.828059],"m^3/(mol*s)","*|/",[161.643,68.7951,42.5792,31.5434,22.3826,18.6742,15.4135,14.5666])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 88 rates.
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=141 label="C_rad/H/TwoDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=125 label="C_methyl">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=124 label="Cs_rad">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=5 label="Cd/H2">, <Entry index=124 label="Cs_rad">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=5 label="Cd/H2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=109 label="O_pri_rad">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=11 label="Cd/H2_Cd/De2">, <Entry index=125 label="C_methyl">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=124 label="Cs_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=5 label="Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=130 label="C_rad/H2/Cb">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=118 label="Cb_rad">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=116 label="Cd_rad/NonDe">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=153 label="Cd_pri_rad-Cdd/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=132 label="C_rad/H2/O">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=129 label="C_rad/H2/Ct">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "Cd/H2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.09175,1.04965,1.02592,1.01089,0.993251,0.98353,0.972217,0.967786],"m^3/(mol*s)","*|/",[173.461,75.1229,47.1918,35.3742,25.5057,21.4761,17.8713,16.8777])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 60 rates.
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=141 label="C_rad/H/TwoDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=125 label="C_methyl">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=5 label="Cd/H2">, <Entry index=124 label="Cs_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=5 label="Cd/H2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=109 label="O_pri_rad">]
[<Entry index=11 label="Cd/H2_Cd/De2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=5 label="Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=130 label="C_rad/H2/Cb">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=118 label="Cb_rad">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=116 label="Cd_rad/NonDe">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=153 label="Cd_pri_rad-Cdd/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=132 label="C_rad/H2/O">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=129 label="C_rad/H2/Ct">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "Cd/H2_Cd/H2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.227687,0.306173,0.366176,0.412921,0.480544,0.526985,0.597562,0.637664],"m^3/(mol*s)","*|/",[99.1525,49.959,34.5722,27.6707,21.6126,19.0255,16.6507,16.0318])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 32 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=130 label="C_rad/H2/Cb">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=118 label="Cb_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=116 label="Cd_rad/NonDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=109 label="O_pri_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=132 label="C_rad/H2/O">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=153 label="Cd_pri_rad-Cdd/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=129 label="C_rad/H2/Ct">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=141 label="C_rad/H/TwoDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "Cd/H2_Cd/H/Nd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.513112,0.551408,0.581109,0.60551,0.644489,0.675305,0.733075,0.775788],"m^3/(mol*s)","*|/",[798.738,178.673,76.6523,45.3826,25.6564,19.822,17.2767,19.1124])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 8 rates.
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "Cd/H2_Cd/H/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([64.4312,24.4025,13.5547,9.12639,5.53074,4.0731,2.67771,2.15147],"m^3/(mol*s)","*|/",[13359.2,4233.56,2142.18,1366.52,784.173,564.343,366.208,295.921])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 7 rates.
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=125 label="C_methyl">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "Cd/H2_Cd/Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([83.5305,35.5558,21.2385,15.0355,9.73108,7.47414,5.22568,4.34884],"m^3/(mol*s)","*|/",[355.138,206.008,160.084,140.534,125.495,120.884,120.173,122.887])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 10,
    label = "Cd/H2_Cd/Nd/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1546.01,361.969,150.682,83.7152,39.9053,25.4496,13.8145,10.0883],"m^3/(mol*s)","*|/",[15928.1,2944.16,1069.54,544.591,234.194,141.064,71.5653,50.8108])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=106 label="H_rad">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "Cd/H2_Cd/De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([22346.5,2923.91,858.108,377.528,134.363,71.879,30.8373,20.0056],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=11 label="Cd/H2_Cd/De2">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "Cd/H/Nd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0992037,0.158101,0.211047,0.257436,0.333631,0.393395,0.499798,0.572145],"m^3/(mol*s)","*|/",[63.8129,26.4723,16.5137,12.578,9.77576,9.14997,10.2216,12.6595])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 10 rates.
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "Cd/H/Nd_Cd/H2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.162272,0.240842,0.309839,0.370164,0.47062,0.551754,0.704291,0.816017],"m^3/(mol*s)","*|/",[91.2828,33.5926,20.0303,15.0928,12.0143,11.7856,14.9656,20.7167])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 7 rates.
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "Cd/H/Nd_Cd/H/Nd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "Cd/H/Nd_Cd/H/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "Cd/H/Nd_Cd/Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "Cd/H/Nd_Cd/Nd/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "Cd/H/Nd_Cd/De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "Cd/H/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.189011,0.301509,0.396885,0.475005,0.59087,0.669954,0.783105,0.839078],"m^3/(mol*s)","*|/",[2247.01,868.372,491.83,337.025,210.397,158.701,109.037,90.3777])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 6 rates.
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 20,
    label = "Cd/H/De_Cd/H2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.189011,0.301509,0.396885,0.475005,0.59087,0.669954,0.783105,0.839078],"m^3/(mol*s)","*|/",[2247.01,868.372,491.83,337.025,210.397,158.701,109.037,90.3777])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 6 rates.
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 21,
    label = "Cd/H/De_Cd/H/Nd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "Cd/H/De_Cd/H/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "Cd/H/De_Cd/Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "Cd/H/De_Cd/Nd/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "Cd/H/De_Cd/De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "Cd/Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.051555,0.0901562,0.125434,0.155797,0.203057,0.23683,0.287607,0.314237],"m^3/(mol*s)","*|/",[7490.28,1169.05,392.98,193.184,81.9042,50.1227,27.2182,20.6269])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 7 rates.
[<Entry index=26 label="Cd/Nd2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=124 label="Cs_rad">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 27,
    label = "Cd/Nd2_Cd/H2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00941914,0.0261713,0.0480516,0.0717847,0.117785,0.157658,0.229834,0.274927],"m^3/(mol*s)","*|/",[2669.44,773.457,379.624,240.732,140.231,103.455,71.1499,60.023])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 28,
    label = "Cd/Nd2_Cd/H/Nd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "Cd/Nd2_Cd/H/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "Cd/Nd2_Cd/Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "Cd/Nd2_Cd/Nd/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "Cd/Nd2_Cd/De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "Cd/Nd/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0633923,0.130009,0.198998,0.26338,0.371575,0.454401,0.587602,0.662314],"m^3/(mol*s)","*|/",[734.116,250.792,131.636,85.6411,50.017,36.2023,23.4859,18.8834])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 34,
    label = "Cd/Nd/De_Cd/H2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0633923,0.130009,0.198998,0.26338,0.371575,0.454401,0.587602,0.662314],"m^3/(mol*s)","*|/",[734.116,250.792,131.636,85.6411,50.017,36.2023,23.4859,18.8834])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 35,
    label = "Cd/Nd/De_Cd/H/Nd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "Cd/Nd/De_Cd/H/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "Cd/Nd/De_Cd/Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "Cd/Nd/De_Cd/Nd/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "Cd/Nd/De_Cd/De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "Cd/De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "Cd/De2_Cd/H2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "Cd/De2_Cd/H/Nd",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "Cd/De2_Cd/H/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     H 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "Cd/De2_Cd/Nd2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "Cd/De2_Cd/Nd/De",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "Cd/De2_Cd/De2",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
6     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "Cd_Cdd",
    group = 
"""
1  *1 Cd 0 {2,D}
2  *2 Cdd 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.30872,3.0126,2.41778,2.08074,1.71403,1.51781,1.27627,1.16003],"m^3/(mol*s)","*|/",[82.246,46.8845,36.6189,32.5555,29.849,29.3243,29.851,30.6638])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 10 rates.
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=125 label="C_methyl">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 48,
    label = "Cd_Ca",
    group = 
"""
1  *1 Cd 0 {2,D}
2  *2 Cdd 0 {1,D} {3,D}
3     C 0 {2,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.30872,3.0126,2.41778,2.08074,1.71403,1.51781,1.27627,1.16003],"m^3/(mol*s)","*|/",[82.246,46.8845,36.6189,32.5555,29.849,29.3243,29.851,30.6638])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 10 rates.
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=125 label="C_methyl">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 49,
    label = "Cd/H2_Ca",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     C 0 {2,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([15.7946,8.78145,6.14184,4.82235,3.5419,2.92766,2.24552,1.94916],"m^3/(mol*s)","*|/",[72.5868,55.2479,55.6,60.0366,71.3493,82.1513,103.087,117.278])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 6 rates.
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=125 label="C_methyl">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 50,
    label = "Cd/H/Nd_Ca",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     C 0 {2,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.443676,0.463287,0.473013,0.477964,0.481271,0.480771,0.474828,0.467796],"m^3/(mol*s)","*|/",[3.83496e+17,3.35813e+14,4.94104e+12,2.977e+11,8.93866e+09,1.09615e+09,6.74707e+07,1.68768e+07])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 51,
    label = "Cd/H/De_Ca",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     C 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    label = "Cd/Nd2_Ca",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     C 0 {2,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.443676,0.463287,0.473013,0.477964,0.481271,0.480771,0.474828,0.467796],"m^3/(mol*s)","*|/",[3.83496e+17,3.35813e+14,4.94104e+12,2.977e+11,8.93866e+09,1.09615e+09,6.74707e+07,1.68768e+07])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 53,
    label = "Cd/Nd/De_Ca",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     C 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    label = "Cd/De2_Ca",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     C 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    label = "Cd_Ck",
    group = 
"""
1  *1 Cd 0 {2,D}
2  *2 Cdd 0 {1,D} {3,D}
3     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    label = "Cd/H2_Ck",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     H 0 {1,S}
5     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    label = "Cd/H/Nd_Ck",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    label = "Cd/H/De_Ck",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    label = "Cd/Nd2_Ck",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
5     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    label = "Cd/Nd/De_Ck",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    label = "Cd/De2_Ck",
    group = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cdd 0 {1,D} {5,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    label = "Cdd_Cd",
    group = 
"""
1  *1 Cdd 0 {2,D}
2  *2 Cd 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([20.3059,13.1142,10.0811,8.45577,6.78184,5.9369,4.96433,4.53419],"m^3/(mol*s)","*|/",[461.934,136.133,71.4167,49.5228,35.0494,30.9907,30.2166,32.3346])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 6 rates.
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 63,
    label = "Ca_Cd",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D}
3     C 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([20.3059,13.1142,10.0811,8.45577,6.78184,5.9369,4.96433,4.53419],"m^3/(mol*s)","*|/",[461.934,136.133,71.4167,49.5228,35.0494,30.9907,30.2166,32.3346])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 6 rates.
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 64,
    label = "Ca_Cd/H2",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     H 0 {2,S}
5     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([53.9934,17.3901,8.88819,5.71436,3.32336,2.42146,1.61704,1.34066],"m^3/(mol*s)","*|/",[2.62653e+23,5.62899e+16,6.85339e+12,2.3474e+10,6.13992e+07,7.63691e+06,1.4781e+07,1.36666e+08])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 65,
    label = "Ca_Cd/H/Nd",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     H 0 {2,S}
5     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.57845,4.03603,4.31506,4.49571,4.70236,4.8051,4.88941,4.88797],"m^3/(mol*s)","*|/",[2.755e+12,3.25877e+11,1.09278e+11,5.73914e+10,2.81908e+10,1.92483e+10,1.19561e+10,9.38791e+09])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 66,
    label = "Ca_Cd/H/De",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     H 0 {2,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    label = "Ca_Cd/Nd2",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     {Cs,O} 0 {2,S}
5     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([43.3342,32.1343,26.7134,23.5338,19.9595,17.9846,15.4741,14.225],"m^3/(mol*s)","*|/",[6.47623e+12,9.24013e+11,3.4812e+11,1.97585e+11,1.06746e+11,7.70248e+10,5.13287e+10,4.16652e+10])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 68,
    label = "Ca_Cd/Nd/De",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     {Cs,O} 0 {2,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    label = "Ca_Cd/De2",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     C 0 {1,D}
4     {Cd,Ct,Cb,CO} 0 {2,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    label = "Ck_Cd",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D}
3     Od 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    label = "Ck_Cd/H2",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     Od 0 {1,D}
4     H 0 {2,S}
5     H 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    label = "Ck_Cd/H/Nd",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     Od 0 {1,D}
4     H 0 {2,S}
5     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    label = "Ck_Cd/H/De",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     Od 0 {1,D}
4     H 0 {2,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    label = "Ck_Cd/Nd2",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     Od 0 {1,D}
4     {Cs,O} 0 {2,S}
5     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    label = "Ck_Cd/Nd/De",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     Od 0 {1,D}
4     {Cs,O} 0 {2,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    label = "Ck_Cd/De2",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cd 0 {1,D} {4,S} {5,S}
3     Od 0 {1,D}
4     {Cd,Ct,Cb,CO} 0 {2,S}
5     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    label = "Cdd_Cdd",
    group = 
"""
1  *1 Cdd 0 {2,D}
2  *2 Cdd 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    label = "Ca_Ca",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cdd 0 {1,D} {4,D}
3     C 0 {1,D}
4     C 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    label = "Ck_Ck",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cdd 0 {1,D} {4,D}
3     Od 0 {1,D}
4     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    label = "Ca_Ck",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cdd 0 {1,D} {4,D}
3     C 0 {1,D}
4     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    label = "Ck_Ca",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Cdd 0 {1,D} {4,D}
3     Od 0 {1,D}
4     C 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    label = "Cdd_Od",
    group = 
"""
1  *1 Cdd 0 {2,D}
2  *2 Od 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    label = "CO2",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Od 0 {1,D}
3     Od 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    label = "Ck_O",
    group = 
"""
1  *1 Cdd 0 {2,D} {3,D}
2  *2 Od 0 {1,D}
3     C 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    label = "CO_O",
    group = 
"""
1  *1 CO 0 {2,D}
2  *2 Od 0 {1,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0147393,0.0262823,0.0369787,0.0462595,0.0607988,0.071234,0.0869428,0.0951552],"m^3/(mol*s)","*|/",[6.67359e+07,1.89789e+06,226511,55298.1,9609.32,3397.09,865.739,442.607])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 6 rates.
[<Entry index=85 label="CO_O">, <Entry index=112 label="O_rad/OneDe">]
[<Entry index=86 label="CO/H2_O">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=89 label="CO/Nd2_O">, <Entry index=125 label="C_methyl">]
[<Entry index=85 label="CO_O">, <Entry index=124 label="Cs_rad">]
[<Entry index=85 label="CO_O">, <Entry index=120 label="CO_pri_rad">]
[<Entry index=85 label="CO_O">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 86,
    label = "CO/H2_O",
    group = 
"""
1  *1 CO 0 {2,D} {3,S} {4,S}
2  *2 Od 0 {1,D}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.54197,1.76526,1.15221,0.861947,0.593478,0.470267,0.338415,0.282872],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=86 label="CO/H2_O">, <Entry index=127 label="C_rad/H2/Cs">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 87,
    label = "CO/H/Nd_O",
    group = 
"""
1  *1 CO 0 {2,D} {3,S} {4,S}
2  *2 Od 0 {1,D}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    label = "CO/H/De_O",
    group = 
"""
1  *1 CO 0 {2,D} {3,S} {4,S}
2  *2 Od 0 {1,D}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    label = "CO/Nd2_O",
    group = 
"""
1  *1 CO 0 {2,D} {3,S} {4,S}
2  *2 Od 0 {1,D}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000184971,0.000696065,0.00153285,0.00258478,0.00493343,0.00722949,0.0118877,0.0150984],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=89 label="CO/Nd2_O">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 90,
    label = "CO/Nd/De_O",
    group = 
"""
1  *1 CO 0 {2,D} {3,S} {4,S}
2  *2 Od 0 {1,D}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    label = "CO/De2_O",
    group = 
"""
1  *1 CO 0 {2,D} {3,S} {4,S}
2  *2 Od 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    label = "Ct_Ct",
    group = 
"""
1  *1 Ct 0 {2,T}
2  *2 Ct 0 {1,T}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.3021,5.23434,4.29133,3.76181,3.19502,2.90001,2.55464,2.40216],"m^3/(mol*s)","*|/",[204.124,69.7066,40.7768,30.6072,23.8643,22.1298,22.3035,23.768])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 26 rates.
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=109 label="O_pri_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=110 label="O_sec_rad">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=107 label="Ct_rad">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=106 label="H_rad">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 93,
    label = "Ct/H_Ct/H",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.56553,3.79836,2.52556,1.93078,1.38893,1.14593,0.896862,0.800551],"m^3/(mol*s)","*|/",[491.234,107.002,50.7479,34.9292,26.9315,26.517,31.5867,38.14])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 14 rates.
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=109 label="O_pri_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=110 label="O_sec_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=107 label="Ct_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 94,
    label = "Ct/H_Ct/Nd",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     {Cs,O} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([28.5859,36.5635,42.1563,46.1879,51.4474,54.5936,58.4185,59.8893],"m^3/(mol*s)","*|/",[1.52922e+12,4.3731e+11,3.171e+11,3.06579e+11,3.55953e+11,4.26123e+11,5.8446e+11,6.92276e+11])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 95,
    label = "Ct/H_Ct/De",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([513.981,188.772,102.97,68.5094,40.9187,29.8816,19.4373,15.5424],"m^3/(mol*s)","*|/",[117113,21380.9,7764.42,3967.98,1723.45,1047.81,540.507,387.617])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=125 label="C_methyl">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 96,
    label = "Ct/Nd_Ct/H",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cs,O} 0 {1,S}
4     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.393469,1.03527,1.84,2.69019,4.29776,5.66232,8.08541,9.57527],"m^3/(mol*s)","*|/",[1.69386e+11,4.52101e+09,8.05344e+08,3.23349e+08,1.40131e+08,1.00611e+08,7.80764e+07,7.33164e+07])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 97,
    label = "Ct/Nd_Ct/Nd",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    label = "Ct/Nd_Ct/De",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    label = "Ct/De_Ct/H",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {2,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.295728,0.724563,1.23385,1.75325,2.70286,3.48568,4.83739,5.64764],"m^3/(mol*s)","*|/",[374.794,205.144,146.899,119.187,93.3335,81.3386,68.3464,62.7927])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 100,
    label = "Ct/De_Ct/Nd",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    label = "Ct/De_Ct/De",
    group = 
"""
1  *1 Ct 0 {2,T} {3,S}
2  *2 Ct 0 {1,T} {4,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {2,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    label = "OCO",
    group = 
"""
1  *1 Od 0 {2,D}
2  *2 CO 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    label = "OSi",
    group = 
"""
1  *1 Od 0 {2,D}
2  *2 Si 0 {1,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    label = "OCddO",
    group = 
"""
1  *1 Od 0 {2,D}
2  *2 Cdd 0 {1,D} {3,D}
3     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    label = "OSiddO",
    group = 
"""
1  *1 Od 0 {2,D}
2  *2 Sidd 0 {1,D} {3,D}
3     Od 0 {2,D}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    label = "H_rad",
    group = 
"""
1  *3 H 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4750.51,1028.42,409.513,221.255,102.164,64.0882,34.219,24.8918],"m^3/(mol*s)","*|/",[1372.25,367.006,169.943,103.144,56.5652,40.1662,26.2978,21.7497])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 42 rates.
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=106 label="H_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=85 label="CO_O">, <Entry index=106 label="H_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=106 label="H_rad">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=106 label="H_rad">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=106 label="H_rad">]
[<Entry index=5 label="Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=106 label="H_rad">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=106 label="H_rad">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=106 label="H_rad">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=106 label="H_rad">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=106 label="H_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 107,
    label = "Ct_rad",
    group = 
"""
1  *3 Ct 1 {2,T}
2     Ct 0 {1,T}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([172842,11918.1,2376.65,807.044,207.286,90.9913,29.8559,16.8801],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=107 label="Ct_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 108,
    label = "O_rad",
    group = 
"""
1  *3 O 1 {2,S}
2     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.28026,1.47991,1.14621,0.969162,0.7894,0.700673,0.602638,0.562532],"m^3/(mol*s)","*|/",[8033.06,1057.49,327.816,156.711,68.8566,46.5251,34.8777,35.8872])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 8 rates.
[<Entry index=85 label="CO_O">, <Entry index=112 label="O_rad/OneDe">]
[<Entry index=5 label="Cd/H2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=109 label="O_pri_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=110 label="O_sec_rad">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=109 label="O_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 109,
    label = "O_pri_rad",
    group = 
"""
1  *3 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([37367.5,3185.59,741.135,283.927,87.5283,44.0354,18.3532,12.2349],"m^3/(mol*s)","*|/",[2.79489e+06,54782.3,5948.68,1645.02,577.239,546.411,1476.02,4449.56])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 3 rates.
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=109 label="O_pri_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=109 label="O_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 110,
    label = "O_sec_rad",
    group = 
"""
1  *3 O 1 {2,S}
2     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00298107,0.00775875,0.0136835,0.0198874,0.0314911,0.04122,0.0582001,0.0683987],"m^3/(mol*s)","*|/",[201544,14801.9,3216.86,1195.66,364.529,185.911,81.3664,56.2235])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=26 label="Cd/Nd2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=85 label="CO_O">, <Entry index=112 label="O_rad/OneDe">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=5 label="Cd/H2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=110 label="O_sec_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 111,
    label = "O_rad/NonDe",
    group = 
"""
1  *3 O 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000471988,0.00174346,0.00379302,0.00634016,0.0119549,0.0173741,0.0281938,0.0355125],"m^3/(mol*s)","*|/",[7.56638e+10,2.22081e+08,6.82022e+06,675749,38260.7,6939.94,737.621,247.451])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 3 rates.
[<Entry index=26 label="Cd/Nd2">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=111 label="O_rad/NonDe">]
[<Entry index=5 label="Cd/H2">, <Entry index=111 label="O_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 112,
    label = "O_rad/OneDe",
    group = 
"""
1  *3 O 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.203747,0.199715,0.196486,0.193808,0.189544,0.186227,0.180229,0.176024],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=85 label="CO_O">, <Entry index=112 label="O_rad/OneDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 113,
    label = "Cd_rad",
    group = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([95.3986,28.2959,13.7791,8.58353,4.80484,3.42512,2.22647,1.82444],"m^3/(mol*s)","*|/",[15086.8,2882.56,1188.22,697.78,388.704,287.881,208.729,187.825])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=116 label="Cd_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 114,
    label = "Cd_pri_rad",
    group = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([59.1401,17.0671,8.21265,5.09082,2.84742,2.03801,1.34493,1.11891],"m^3/(mol*s)","*|/",[290658,33719.6,10681.1,5365.48,2523.99,1716.66,1138.98,997.679])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=114 label="Cd_pri_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=114 label="Cd_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 115,
    label = "Cd_sec_rad",
    group = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([533.478,174.642,88.7709,56.2896,31.6007,22.2004,13.6686,10.6056],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=116 label="Cd_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 116,
    label = "Cd_rad/NonDe",
    group = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([533.478,174.642,88.7709,56.2896,31.6007,22.2004,13.6686,10.6056],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=116 label="Cd_rad/NonDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 117,
    label = "Cd_rad/OneDe",
    group = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cd 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    label = "Cb_rad",
    group = 
"""
1  *3 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([25348.9,3900.97,1260.68,591.064,227.507,127.442,58.016,38.7075],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=118 label="Cb_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 119,
    label = "CO_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.33486,2.29834,1.83041,1.56818,1.286,1.13679,0.955586,0.869804],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=85 label="CO_O">, <Entry index=120 label="CO_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 120,
    label = "CO_pri_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.33486,2.29834,1.83041,1.56818,1.286,1.13679,0.955586,0.869804],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=85 label="CO_O">, <Entry index=120 label="CO_pri_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 121,
    label = "CO_sec_rad",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R!H 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    label = "CO_rad/NonDe",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    label = "CO_rad/OneDe",
    group = 
"""
1  *3 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    label = "Cs_rad",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00642267,0.0168955,0.0301479,0.0443149,0.0716172,0.0954001,0.13945,0.168241],"m^3/(mol*s)","*|/",[76.0424,37.3151,26.0231,21.274,17.505,16.1855,15.5417,15.9008])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 77 rates.
[<Entry index=50 label="Cd/H/Nd_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=141 label="C_rad/H/TwoDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=86 label="CO/H2_O">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=125 label="C_methyl">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=26 label="Cd/Nd2">, <Entry index=124 label="Cs_rad">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=89 label="CO/Nd2_O">, <Entry index=125 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=85 label="CO_O">, <Entry index=124 label="Cs_rad">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=5 label="Cd/H2">, <Entry index=124 label="Cs_rad">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=11 label="Cd/H2_Cd/De2">, <Entry index=125 label="C_methyl">]
[<Entry index=12 label="Cd/H/Nd">, <Entry index=124 label="Cs_rad">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=52 label="Cd/Nd2_Ca">, <Entry index=124 label="Cs_rad">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=130 label="C_rad/H2/Cb">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=125 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=132 label="C_rad/H2/O">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=129 label="C_rad/H2/Ct">]
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=124 label="Cs_rad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 125,
    label = "C_methyl",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0444315,0.0943313,0.148178,0.200218,0.291637,0.365422,0.493504,0.573395],"m^3/(mol*s)","*|/",[71.4323,42.0806,32.702,28.6182,25.4173,24.4492,24.5626,25.6626])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 42 rates.
[<Entry index=49 label="Cd/H2_Ca">, <Entry index=125 label="C_methyl">]
[<Entry index=34 label="Cd/Nd/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=9 label="Cd/H2_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=96 label="Ct/Nd_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=99 label="Ct/De_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=10 label="Cd/H2_Cd/Nd/De">, <Entry index=125 label="C_methyl">]
[<Entry index=89 label="CO/Nd2_O">, <Entry index=125 label="C_methyl">]
[<Entry index=94 label="Ct/H_Ct/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=95 label="Ct/H_Ct/De">, <Entry index=125 label="C_methyl">]
[<Entry index=67 label="Ca_Cd/Nd2">, <Entry index=125 label="C_methyl">]
[<Entry index=27 label="Cd/Nd2_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=13 label="Cd/H/Nd_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=64 label="Ca_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=8 label="Cd/H2_Cd/H/De">, <Entry index=125 label="C_methyl">]
[<Entry index=11 label="Cd/H2_Cd/De2">, <Entry index=125 label="C_methyl">]
[<Entry index=20 label="Cd/H/De_Cd/H2">, <Entry index=125 label="C_methyl">]
[<Entry index=65 label="Ca_Cd/H/Nd">, <Entry index=125 label="C_methyl">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=125 label="C_methyl">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=125 label="C_methyl">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 126,
    label = "C_pri_rad",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.00181998,0.00557309,0.0109278,0.0171409,0.0301563,0.0424037,0.0670688,0.0846166],"m^3/(mol*s)","*|/",[187.053,47.0652,21.8008,13.6353,8.27623,6.63893,5.84435,6.16936])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 15 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=130 label="C_rad/H2/Cb">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=86 label="CO/H2_O">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=132 label="C_rad/H2/O">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=129 label="C_rad/H2/Ct">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 127,
    label = "C_rad/H2/Cs",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0494426,0.0619386,0.0716082,0.0793981,0.0913984,0.100439,0.116325,0.127281],"m^3/(mol*s)","*|/",[46.0869,26.0258,19.1084,15.6818,12.3086,10.7258,9.4692,9.76895])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 8 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=86 label="CO/H2_O">, <Entry index=127 label="C_rad/H2/Cs">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=127 label="C_rad/H2/Cs">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 128,
    label = "C_rad/H2/Cd",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.38648e-06,5.32951e-05,0.000276483,0.000824538,0.0032035,0.00717947,0.0207294,0.0347926],"m^3/(mol*s)","*|/",[1.79779e+06,22125.7,1720.03,341.749,58.0663,27.3064,21.2549,27.8371])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=128 label="C_rad/H2/Cd">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=128 label="C_rad/H2/Cd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 129,
    label = "C_rad/H2/Ct",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000316707,0.00240767,0.00807726,0.0180212,0.0487536,0.0879919,0.19062,0.277434],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=129 label="C_rad/H2/Ct">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 130,
    label = "C_rad/H2/Cb",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cb 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000198959,0.00145041,0.00474494,0.0104104,0.0275793,0.0491536,0.104712,0.151128],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=130 label="C_rad/H2/Cb">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 131,
    label = "C_rad/H2/CO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     CO 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    label = "C_rad/H2/O",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0286632,0.0263254,0.0248489,0.0238051,0.0223846,0.0214298,0.0199337,0.0190108],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=132 label="C_rad/H2/O">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 133,
    label = "C_sec_rad",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.34966e-05,0.000276648,0.000975227,0.00224861,0.00633729,0.0117198,0.026217,0.0387624],"m^3/(mol*s)","*|/",[981.915,225.381,95.1916,54.3949,27.7729,18.9774,11.9204,9.70916])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=141 label="C_rad/H/TwoDe">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=134 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 134,
    label = "C_rad/H/NonDeC",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0471925,0.0500841,0.0515331,0.0522732,0.0527645,0.0526829,0.0517764,0.0507149],"m^3/(mol*s)","*|/",[3.88882e+20,7.52766e+16,4.85997e+14,1.77868e+13,3.10575e+11,2.91984e+10,1.3955e+09,3.27287e+08])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=134 label="C_rad/H/NonDeC">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=134 label="C_rad/H/NonDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 135,
    label = "C_rad/H/NonDeO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    label = "C_rad/H/CsO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    label = "C_rad/H/O2",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     O 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    label = "C_rad/H/OneDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.40886e-05,0.000143645,0.00057471,0.00144199,0.0045178,0.00890448,0.0216934,0.0334825],"m^3/(mol*s)","*|/",[1.12311e+17,3.27321e+12,6.52245e+09,1.07772e+08,707739,39041.4,1182.43,300.071])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 139,
    label = "C_rad/H/OneDeC",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.40886e-05,0.000143645,0.00057471,0.00144199,0.0045178,0.00890448,0.0216934,0.0334825],"m^3/(mol*s)","*|/",[1.12311e+17,3.27321e+12,6.52245e+09,1.07772e+08,707739,39041.4,1182.43,300.071])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=139 label="C_rad/H/OneDeC">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 140,
    label = "C_rad/H/OneDeO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    label = "C_rad/H/TwoDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.06723e-10,8.85537e-08,2.22359e-06,1.89829e-05,0.000274832,0.00135705,0.0112488,0.0320253],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=141 label="C_rad/H/TwoDe">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 142,
    label = "C_ter_rad",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.000508558,0.00122771,0.00206877,0.00291591,0.0044413,0.00567697,0.00775843,0.00896395],"m^3/(mol*s)","*|/",[325.698,146.483,95.7508,74.3397,56.5275,49.2618,42.5413,40.2522])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 8 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=144 label="C_rad/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 143,
    label = "C_rad/NonDeC",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cs,O} 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0661173,0.0415453,0.0312122,0.0256715,0.0199374,0.0170089,0.0135525,0.011952],"m^3/(mol*s)","*|/",[1649.69,758.601,514.378,413.08,330.613,298.218,270.436,262.494])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=144 label="C_rad/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 144,
    label = "C_rad/Cs3",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0661173,0.0415453,0.0312122,0.0256715,0.0199374,0.0170089,0.0135525,0.011952],"m^3/(mol*s)","*|/",[1649.69,758.601,514.378,413.08,330.613,298.218,270.436,262.494])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=7 label="Cd/H2_Cd/H/Nd">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=144 label="C_rad/Cs3">]
[<Entry index=93 label="Ct/H_Ct/H">, <Entry index=144 label="C_rad/Cs3">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 145,
    label = "C_rad/NDMustO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     O 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    label = "C_rad/OneDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.42666e-05,0.000106207,0.000351849,0.000778457,0.00208403,0.00373773,0.00802955,0.0116376],"m^3/(mol*s)","*|/",[2.1415e+19,1.56155e+15,5.1173e+12,1.1251e+11,9.46518e+08,5.35416e+07,1.1484e+06,166502])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 147,
    label = "C_rad/Cs2",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.42666e-05,0.000106207,0.000351849,0.000778457,0.00208403,0.00373773,0.00802955,0.0116376],"m^3/(mol*s)","*|/",[2.1415e+19,1.56155e+15,5.1173e+12,1.1251e+11,9.46518e+08,5.35416e+07,1.1484e+06,166502])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=147 label="C_rad/Cs2">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 148,
    label = "C_rad/ODMustO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    label = "C_rad/TwoDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.60581e-11,7.47703e-09,1.57429e-07,1.19509e-06,1.49404e-05,6.75529e-05,0.000497924,0.00133676],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 150,
    label = "C_rad/Cs",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.60581e-11,7.47703e-09,1.57429e-07,1.19509e-06,1.49404e-05,6.75529e-05,0.000497924,0.00133676],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=150 label="C_rad/Cs">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 151,
    label = "C_rad/TDMustO",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    label = "C_rad/ThreeDe",
    group = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    label = "Cd_pri_rad-Cdd/Cd",
    group = 
"""
1  *3 Cd 1 {2,D} {3,S}
2     Cdd 0 {1,D} {4,D}
3     H 0 {1,S}
4     Cd 0 {2,D}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.28696e-05,0.00019178,0.000794394,0.00225648,0.00988159,0.0277185,0.149561,0.44353],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=6 label="Cd/H2_Cd/H2">, <Entry index=153 label="Cd_pri_rad-Cdd/Cd">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:16:06 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = -1,
    label = "Y_rad",
    group = 
"""
1  *3 R 1
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = -1,
    label = "Y_birad",
    group = 
"""
1  *3 R {2S,2T}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

tree(
"""
L1: XZ
    L2: CZ
        L3: Cd_Cd
            L4: Cd/H2
                L5: Cd/H2_Cd/H2
                L5: Cd/H2_Cd/H/Nd
                L5: Cd/H2_Cd/H/De
                L5: Cd/H2_Cd/Nd2
                L5: Cd/H2_Cd/Nd/De
                L5: Cd/H2_Cd/De2
            L4: Cd/H/Nd
                L5: Cd/H/Nd_Cd/H2
                L5: Cd/H/Nd_Cd/H/Nd
                L5: Cd/H/Nd_Cd/H/De
                L5: Cd/H/Nd_Cd/Nd2
                L5: Cd/H/Nd_Cd/Nd/De
                L5: Cd/H/Nd_Cd/De2
            L4: Cd/H/De
                L5: Cd/H/De_Cd/H2
                L5: Cd/H/De_Cd/H/Nd
                L5: Cd/H/De_Cd/H/De
                L5: Cd/H/De_Cd/Nd2
                L5: Cd/H/De_Cd/Nd/De
                L5: Cd/H/De_Cd/De2
            L4: Cd/Nd2
                L5: Cd/Nd2_Cd/H2
                L5: Cd/Nd2_Cd/H/Nd
                L5: Cd/Nd2_Cd/H/De
                L5: Cd/Nd2_Cd/Nd2
                L5: Cd/Nd2_Cd/Nd/De
                L5: Cd/Nd2_Cd/De2
            L4: Cd/Nd/De
                L5: Cd/Nd/De_Cd/H2
                L5: Cd/Nd/De_Cd/H/Nd
                L5: Cd/Nd/De_Cd/H/De
                L5: Cd/Nd/De_Cd/Nd2
                L5: Cd/Nd/De_Cd/Nd/De
                L5: Cd/Nd/De_Cd/De2
            L4: Cd/De2
                L5: Cd/De2_Cd/H2
                L5: Cd/De2_Cd/H/Nd
                L5: Cd/De2_Cd/H/De
                L5: Cd/De2_Cd/Nd2
                L5: Cd/De2_Cd/Nd/De
                L5: Cd/De2_Cd/De2
        L3: Cd_Cdd
            L4: Cd_Ca
                L5: Cd/H2_Ca
                L5: Cd/H/Nd_Ca
                L5: Cd/H/De_Ca
                L5: Cd/Nd2_Ca
                L5: Cd/Nd/De_Ca
                L5: Cd/De2_Ca
            L4: Cd_Ck
                L5: Cd/H2_Ck
                L5: Cd/H/Nd_Ck
                L5: Cd/H/De_Ck
                L5: Cd/Nd2_Ck
                L5: Cd/Nd/De_Ck
                L5: Cd/De2_Ck
        L3: Cdd_Cd
            L4: Ca_Cd
                L5: Ca_Cd/H2
                L5: Ca_Cd/H/Nd
                L5: Ca_Cd/H/De
                L5: Ca_Cd/Nd2
                L5: Ca_Cd/Nd/De
                L5: Ca_Cd/De2
            L4: Ck_Cd
                L5: Ck_Cd/H2
                L5: Ck_Cd/H/Nd
                L5: Ck_Cd/H/De
                L5: Ck_Cd/Nd2
                L5: Ck_Cd/Nd/De
                L5: Ck_Cd/De2
        L3: Cdd_Cdd
            L4: Ca_Ca
            L4: Ck_Ck
            L4: Ca_Ck
            L4: Ck_Ca
        L3: Cdd_Od
            L4: CO2
            L4: Ck_O
        L3: CO_O
            L4: CO/H2_O
            L4: CO/H/Nd_O
            L4: CO/H/De_O
            L4: CO/Nd2_O
            L4: CO/Nd/De_O
            L4: CO/De2_O
        L3: Ct_Ct
            L4: Ct/H_Ct/H
            L4: Ct/H_Ct/Nd
            L4: Ct/H_Ct/De
            L4: Ct/Nd_Ct/H
            L4: Ct/Nd_Ct/Nd
            L4: Ct/Nd_Ct/De
            L4: Ct/De_Ct/H
            L4: Ct/De_Ct/Nd
            L4: Ct/De_Ct/De
    L2: OCO
    L2: OSi
    L2: OCddO
    L2: OSiddO
L1: Y_rad_birad
    L2: H_rad
    L2: Ct_rad
    L2: O_rad
        L3: O_pri_rad
        L3: O_sec_rad
            L4: O_rad/NonDe
            L4: O_rad/OneDe
    L2: Cd_rad
        L3: Cd_pri_rad
        L3: Cd_sec_rad
            L4: Cd_rad/NonDe
            L4: Cd_rad/OneDe
    L2: Cb_rad
    L2: CO_rad
        L3: CO_pri_rad
        L3: CO_sec_rad
            L4: CO_rad/NonDe
            L4: CO_rad/OneDe
    L2: Cs_rad
        L3: C_methyl
        L3: C_pri_rad
            L4: C_rad/H2/Cs
            L4: C_rad/H2/Cd
            L4: C_rad/H2/Ct
            L4: C_rad/H2/Cb
            L4: C_rad/H2/CO
            L4: C_rad/H2/O
        L3: C_sec_rad
            L4: C_rad/H/NonDeC
            L4: C_rad/H/NonDeO
                L5: C_rad/H/CsO
                L5: C_rad/H/O2
            L4: C_rad/H/OneDe
                L5: C_rad/H/OneDeC
                L5: C_rad/H/OneDeO
            L4: C_rad/H/TwoDe
        L3: C_ter_rad
            L4: C_rad/NonDeC
                L5: C_rad/Cs3
                L5: C_rad/NDMustO
            L4: C_rad/OneDe
                L5: C_rad/Cs2
                L5: C_rad/ODMustO
            L4: C_rad/TwoDe
                L5: C_rad/Cs
                L5: C_rad/TDMustO
            L4: C_rad/ThreeDe
    L2: Cd_pri_rad-Cdd/Cd
"""
)

forbidden(
    label = "O2_birad",
    group = 
"""
1  *3 O 1 {2,S}
2     O 1 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

forbidden(
    label = "O2d",
    group = 
"""
1  *1 O 0 {2,D}
2  *2 O 0 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

