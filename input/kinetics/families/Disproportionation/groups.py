#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/groups"
shortDesc = ""
longDesc = """

"""
recommended = True

template(reactants=["Y_rad_birad", "XH_Rrad"], products=["Y_H", "X_R"], ownReverse=False)

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*4'],
    ['BREAK_BOND', '*2', 'S', '*4'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Y_rad_birad",
    group = "OR{Y_1centerbirad, Y_rad}",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.05452e+06,2.11825e+06,2.14358e+06,2.15141e+06,2.14484e+06,2.12716e+06,2.07506e+06,2.02742e+06],"m^3/(mol*s)","*|/",[144.349,48.3746,26.4891,18.4195,12.5021,10.4188,8.85251,8.51003])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 69 rates.
[<Entry index=12 label="O_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=15 label="O_rad/NonDeO">, <Entry index=69 label="O_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=76 label="Cmethyl_Orad">]
[<Entry index=30 label="C_methyl">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=14 label="O_rad/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=69 label="O_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=2 label="XH_Rrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=69 label="O_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=4 label="O_atom_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=1 label="Y_rad_birad">, <Entry index=2 label="XH_Rrad">]
[<Entry index=8 label="O2_birad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=25 label="CO_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=73 label="Cmethyl_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 2,
    label = "XH_Rrad",
    group = 
"""
1  *2 R!H 0 {2,S} {3,S}
2  *3 R!H 1 {1,S}
3  *4 H 0 {1,S}
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
    index = 3,
    label = "Y_1centerbirad",
    group = 
"""
1  *1 {Cs,Cd,O} 2T
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.35976,2.38089,2.40849,2.43704,2.49134,2.54014,2.64132,2.72151],"m^3/(mol*s)","*|/",[305.164,322.161,339.674,356.631,388.143,416.631,477.848,529.197])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=4 label="O_atom_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=73 label="Cmethyl_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 4,
    label = "O_atom_triplet",
    group = 
"""
1  *1 O 2T
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([16.3444,16.398,16.4819,16.5726,16.7487,16.9082,17.2384,17.4979],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=4 label="O_atom_triplet">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 5,
    label = "CH2_triplet",
    group = 
"""
1  *1 C 2T {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.32044,1.33452,1.35259,1.37121,1.4066,1.43842,1.50459,1.55725],"m^3/(mol*s)","*|/",[11525.4,12724.3,13958.6,15175.9,17514.8,19722.8,24775.1,29333.2])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 3 rates.
[<Entry index=5 label="CH2_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=73 label="Cmethyl_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 6,
    label = "Y_rad",
    group = 
"""
1  *1 R 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.957364,0.956978,0.956356,0.955681,0.954377,0.953205,0.950814,0.948967],"m^3/(mol*s)","*|/",[162.467,50.7397,26.4999,17.8116,11.5678,9.39644,7.75553,7.3765])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 64 rates.
[<Entry index=12 label="O_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=15 label="O_rad/NonDeO">, <Entry index=69 label="O_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=76 label="Cmethyl_Orad">]
[<Entry index=30 label="C_methyl">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=14 label="O_rad/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=69 label="O_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=2 label="XH_Rrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=69 label="O_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=25 label="CO_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=73 label="Cmethyl_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 7,
    label = "H_rad",
    group = 
"""
1  *1 H 1
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.04923,2.00495,1.99303,1.99456,2.01341,2.03932,2.10627,2.16641],"m^3/(mol*s)","*|/",[55.6741,39.628,32.3143,28.2053,23.8016,21.5065,18.8217,17.6473])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 8 rates.
[<Entry index=7 label="H_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=76 label="Cmethyl_Orad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 8,
    label = "O2_birad",
    group = 
"""
1  *1 O 1 {2,S}
2     O 1 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0103618,0.0182511,0.0258222,0.0327027,0.04432,0.0535799,0.0700959,0.081172],"m^3/(mol*s)","*|/",[4.51606e+06,91768.5,9632.47,2294.19,440.285,186.73,78.2958,60.1972])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 9 rates.
[<Entry index=8 label="O2_birad">, <Entry index=69 label="O_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=2 label="XH_Rrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 9,
    label = "C2b",
    group = 
"""
1  *1 C 1 {2,T}
2     C 1 {1,T}
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
    index = 10,
    label = "Ct_rad",
    group = 
"""
1  *1 C 1 {2,T}
2     C 0 {1,T}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.62938,3.6549,3.69505,3.73871,3.8243,3.90273,4.0678,4.20012],"m^3/(mol*s)","*|/",[9.64356,8.73632,8.09965,7.61755,6.92025,6.42888,5.63744,5.14896])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=10 label="Ct_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 11,
    label = "O_rad",
    group = 
"""
1  *1 O 1 {2,S}
2     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.36607,7.14839,7.0614,7.0308,7.04049,7.08697,7.23781,7.38552],"m^3/(mol*s)","*|/",[7.75769,6.06084,5.37074,5.03389,4.7531,4.66816,4.6848,4.77856])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 7 rates.
[<Entry index=12 label="O_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=15 label="O_rad/NonDeO">, <Entry index=69 label="O_Csrad">]
[<Entry index=14 label="O_rad/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 12,
    label = "O_pri_rad",
    group = 
"""
1  *1 O 1 {2,S}
2     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([10.0119,9.60264,9.42788,9.35452,9.33707,9.3891,9.59477,9.80876],"m^3/(mol*s)","*|/",[14.5257,10.189,8.55283,7.78297,7.15435,6.96329,6.98389,7.17213])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=12 label="O_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 13,
    label = "O_sec_rad",
    group = 
"""
1  *1 O 1 {2,S}
2     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([3.08746,3.0976,3.11345,3.13057,3.16383,3.19396,3.25634,3.30537],"m^3/(mol*s)","*|/",[7314.59,5397.7,4633.53,4268.51,3990.08,3947.26,4145.59,4465.84])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 2 rates.
[<Entry index=14 label="O_rad/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=15 label="O_rad/NonDeO">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 14,
    label = "O_rad/NonDeC",
    group = 
"""
1  *1 O 1 {2,S}
2     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.3573,4.3716,4.39397,4.41814,4.46508,4.50761,4.59563,4.66483],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=14 label="O_rad/NonDeC">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 15,
    label = "O_rad/NonDeO",
    group = 
"""
1  *1 O 1 {2,S}
2     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([2.18769,2.19487,2.2061,2.21824,2.2418,2.26316,2.30735,2.34209],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=15 label="O_rad/NonDeO">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 16,
    label = "O_rad/OneDe",
    group = 
"""
1  *1 O 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "Cd_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.60136,1.48227,1.41573,1.37343,1.32301,1.29421,1.25795,1.24111],"m^3/(mol*s)","*|/",[36.8093,25.5471,21.1019,18.9092,16.9899,16.3278,16.2876,16.9189])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=18 label="Cd_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 18,
    label = "Cd_pri_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.60136,1.48227,1.41573,1.37343,1.32301,1.29421,1.25795,1.24111],"m^3/(mol*s)","*|/",[36.8093,25.5471,21.1019,18.9092,16.9899,16.3278,16.2876,16.9189])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=18 label="Cd_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 19,
    label = "Cd_sec_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
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
    index = 20,
    label = "Cd_rad/NonDeC",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     Cs 0 {1,S}
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
    index = 21,
    label = "Cd_rad/NonDeO",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
3     O 0 {1,S}
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
    label = "Cd_rad/OneDe",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     C 0 {1,D}
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
    index = 23,
    label = "Cb_rad",
    group = 
"""
1  *1 Cb 1 {2,B} {3,B}
2     {Cb,Cbf} 0 {1,B}
3     {Cb,Cbf} 0 {1,B}
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
    label = "CO_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([32.725,32.8324,33.0004,33.1819,33.5344,33.8538,34.5149,35.0346],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=25 label="CO_pri_rad">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 25,
    label = "CO_pri_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
2     O 0 {1,D}
3     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([32.725,32.8324,33.0004,33.1819,33.5344,33.8538,34.5149,35.0346],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=25 label="CO_pri_rad">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 26,
    label = "CO_sec_rad",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
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
    index = 27,
    label = "CO_rad/NonDe",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
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
    index = 28,
    label = "CO_rad/OneDe",
    group = 
"""
1  *1 C 1 {2,D} {3,S}
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
    index = 29,
    label = "Cs_rad",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     R 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.13642,1.00136,0.921672,0.868058,0.798763,0.754568,0.68904,0.650737],"m^3/(mol*s)","*|/",[6.08907,5.35884,5.13327,5.06694,5.07962,5.1414,5.29859,5.4202])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 30 rates.
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=73 label="Cmethyl_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 30,
    label = "C_methyl",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.50495,1.33059,1.22609,1.15495,1.06183,1.00165,0.911176,0.857581],"m^3/(mol*s)","*|/",[22.8473,20.2602,19.7444,19.8451,20.5596,21.3957,23.2589,24.7462])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 6 rates.
[<Entry index=30 label="C_methyl">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 31,
    label = "C_pri_rad",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.788639,0.740618,0.716422,0.70282,0.689824,0.685204,0.68562,0.691011],"m^3/(mol*s)","*|/",[5.16379,4.64379,4.52596,4.52625,4.61793,4.72539,4.94174,5.09183])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 14 rates.
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=69 label="O_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 32,
    label = "C_rad/H2/Cs",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.964342,0.89993,0.866441,0.846808,0.826358,0.817227,0.811346,0.813267],"m^3/(mol*s)","*|/",[28.5822,17.312,13.0154,10.8639,8.79847,7.83885,6.85243,6.49044])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 33,
    label = "C_rad/H2/Cd",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cd 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.05226,0.938861,0.8799,0.844656,0.805962,0.786393,0.766838,0.761783],"m^3/(mol*s)","*|/",[2.74304,4.27222,5.76153,7.0652,9.11688,10.5966,12.846,14.0452])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=69 label="O_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 34,
    label = "C_rad/H2/Ct",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Ct 0 {1,S}
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
    index = 35,
    label = "C_rad/H2/Cb",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     Cb 0 {1,S}
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
    label = "C_rad/H2/CO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 37,
    label = "C_rad/H2/O",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     O 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.435237,0.438297,0.443112,0.448348,0.458612,0.468017,0.487812,0.50368],"m^3/(mol*s)","*|/",[7.14587,7.82986,8.39763,8.88801,9.71657,10.4118,11.8138,12.9351])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 4 rates.
[<Entry index=37 label="C_rad/H2/O">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 38,
    label = "C_sec_rad",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.86559,1.60244,1.4467,1.34153,1.20496,1.11742,0.987012,0.910621],"m^3/(mol*s)","*|/",[30.0291,21.8871,18.6639,17.0058,15.3423,14.4972,13.4432,12.888])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=59 label="Cdpri_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 39,
    label = "C_rad/H/NonDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.86559,1.60244,1.4467,1.34153,1.20496,1.11742,0.987012,0.910621],"m^3/(mol*s)","*|/",[30.0291,21.8871,18.6639,17.0058,15.3423,14.4972,13.4432,12.888])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=59 label="Cdpri_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 40,
    label = "C_rad/H/NonDeO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 41,
    label = "C_rad/H/CsO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 42,
    label = "C_rad/H/O2",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 43,
    label = "C_rad/H/OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 44,
    label = "C_rad/H/OneDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
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
    label = "C_rad/H/OneDeO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 46,
    label = "C_rad/H/TwoDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
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
    index = 47,
    label = "C_ter_rad",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     R!H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.39555,1.04959,0.854805,0.728663,0.573068,0.4794,0.35115,0.283672],"m^3/(mol*s)","*|/",[6.12503,4.5173,4.07351,3.96435,4.02768,4.17114,4.48798,4.70333])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=69 label="O_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 48,
    label = "C_rad/NonDeC",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cs,O} 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.39555,1.04959,0.854805,0.728663,0.573068,0.4794,0.35115,0.283672],"m^3/(mol*s)","*|/",[6.12503,4.5173,4.07351,3.96435,4.02768,4.17114,4.48798,4.70333])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=69 label="O_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 49,
    label = "C_rad/Cs3",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.39555,1.04959,0.854805,0.728663,0.573068,0.4794,0.35115,0.283672],"m^3/(mol*s)","*|/",[6.12503,4.5173,4.07351,3.96435,4.02768,4.17114,4.48798,4.70333])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 5 rates.
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=69 label="O_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 50,
    label = "C_rad/NDMustO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 51,
    label = "C_rad/OneDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 52,
    label = "C_rad/Cs2",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
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
    index = 53,
    label = "C_rad/ODMustO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 54,
    label = "C_rad/TwoDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 55,
    label = "C_rad/Cs",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     Cs 0 {1,S}
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
    label = "C_rad/TDMustO",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 57,
    label = "C_rad/ThreeDe",
    group = 
"""
1  *1 C 1 {2,S} {3,S} {4,S}
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
    index = 58,
    label = "Cdpri_Rrad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0790128,0.113027,0.140105,0.161668,0.193338,0.215237,0.248321,0.266706],"m^3/(mol*s)","*|/",[1.83978e+06,39571.8,4157.75,967.229,172.938,68.5111,26.1038,19.7208])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 9 rates.
[<Entry index=30 label="C_methyl">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=59 label="Cdpri_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 59,
    label = "Cdpri_Csrad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.0790128,0.113027,0.140105,0.161668,0.193338,0.215237,0.248321,0.266706],"m^3/(mol*s)","*|/",[1.83978e+06,39571.8,4157.75,967.229,172.938,68.5111,26.1038,19.7208])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 9 rates.
[<Entry index=30 label="C_methyl">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=59 label="Cdpri_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=59 label="Cdpri_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 60,
    label = "Cdpri_Cdrad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
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
    label = "Cdpri_COrad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
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
    label = "Cdpri_Orad",
    group = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
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
    index = 63,
    label = "COpri_Rrad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
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
    index = 64,
    label = "COpri_Csrad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
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
    index = 65,
    label = "COpri_Cdrad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
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
    index = 66,
    label = "COpri_COrad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
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
    label = "COpri_Orad",
    group = 
"""
1  *2 CO 0 {2,S} {3,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
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
    index = 68,
    label = "O_Rrad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 {Cs,Cd,CO} 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.41705,4.19854,4.09289,4.0372,3.99199,3.98481,4.01755,4.06777],"m^3/(mol*s)","*|/",[72.3005,42.7287,31.6858,26.2015,20.9419,18.4761,15.866,14.8372])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 21 rates.
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=69 label="O_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=4 label="O_atom_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=69 label="O_Csrad">]
[<Entry index=15 label="O_rad/NonDeO">, <Entry index=69 label="O_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=69 label="O_Csrad">]
[<Entry index=25 label="CO_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=14 label="O_rad/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 69,
    label = "O_Csrad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([4.41705,4.19854,4.09289,4.0372,3.99199,3.98481,4.01755,4.06777],"m^3/(mol*s)","*|/",[72.3005,42.7287,31.6858,26.2015,20.9419,18.4761,15.866,14.8372])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 21 rates.
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=69 label="O_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=69 label="O_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=4 label="O_atom_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=69 label="O_Csrad">]
[<Entry index=15 label="O_rad/NonDeO">, <Entry index=69 label="O_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=69 label="O_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=69 label="O_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=69 label="O_Csrad">]
[<Entry index=25 label="CO_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=69 label="O_Csrad">]
[<Entry index=14 label="O_rad/NonDeC">, <Entry index=69 label="O_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=69 label="O_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=69 label="O_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 70,
    label = "O_Cdrad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
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
    label = "O_COrad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
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
    label = "Cmethyl_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.574,1.42998,1.33763,1.27162,1.18076,1.11906,1.02154,0.961053],"m^3/(mol*s)","*|/",[6.45954,7.26662,7.96986,8.54671,9.41708,10.043,11.0701,11.7327])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 14 rates.
[<Entry index=18 label="Cd_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=76 label="Cmethyl_Orad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=73 label="Cmethyl_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 73,
    label = "Cmethyl_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([1.44607,1.30835,1.21991,1.15663,1.06947,1.01026,0.916696,0.858739],"m^3/(mol*s)","*|/",[6.91452,7.84628,8.65656,9.32114,10.3233,11.043,12.2196,12.9745])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 13 rates.
[<Entry index=18 label="Cd_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=73 label="Cmethyl_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=73 label="Cmethyl_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 74,
    label = "Cmethyl_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
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
    label = "Cmethyl_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
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
    label = "Cmethyl_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([7.0374,6.87647,6.81021,6.78528,6.78787,6.81797,6.92009,7.02108],"m^3/(mol*s)")),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 1 rates.
[<Entry index=7 label="H_rad">, <Entry index=76 label="Cmethyl_Orad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 77,
    label = "Cpri_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.814721,0.784334,0.767353,0.7567,0.7444,0.737794,0.730511,0.728021],"m^3/(mol*s)","*|/",[2.71544,2.72074,2.92129,3.14012,3.51666,3.80373,4.27193,4.55206])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 12 rates.
[<Entry index=12 label="O_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=79 label="C/H2/Nd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 78,
    label = "C/H2/Nd_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.814721,0.784334,0.767353,0.7567,0.7444,0.737794,0.730511,0.728021],"m^3/(mol*s)","*|/",[2.71544,2.72074,2.92129,3.14012,3.51666,3.80373,4.27193,4.55206])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 12 rates.
[<Entry index=12 label="O_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=79 label="C/H2/Nd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 79,
    label = "C/H2/Nd_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.814721,0.784334,0.767353,0.7567,0.7444,0.737794,0.730511,0.728021],"m^3/(mol*s)","*|/",[2.71544,2.72074,2.92129,3.14012,3.51666,3.80373,4.27193,4.55206])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 12 rates.
[<Entry index=12 label="O_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=10 label="Ct_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=5 label="CH2_triplet">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=79 label="C/H2/Nd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=79 label="C/H2/Nd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 80,
    label = "C/H2/Nd_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H2/Nd_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H2/Nd_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H2/De_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C/H2/De_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C/H2/De_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 86,
    label = "C/H2/De_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 87,
    label = "C/H2/De_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     H 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "Csec_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.461136,0.44391,0.434253,0.428174,0.421117,0.417293,0.412997,0.411452],"m^3/(mol*s)","*|/",[2.88643,2.91915,3.16344,3.42488,3.87359,4.21666,4.77949,5.11865])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 11 rates.
[<Entry index=10 label="Ct_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 89,
    label = "C/H/NdNd_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.461136,0.44391,0.434253,0.428174,0.421117,0.417293,0.412997,0.411452],"m^3/(mol*s)","*|/",[2.88643,2.91915,3.16344,3.42488,3.87359,4.21666,4.77949,5.11865])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 11 rates.
[<Entry index=10 label="Ct_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 90,
    label = "C/H/NdNd_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    kinetics = KineticsData(Tdata=([300,400,500,600,800,1000,1500,2000],"K"), kdata=([0.461136,0.44391,0.434253,0.428174,0.421117,0.417293,0.412997,0.411452],"m^3/(mol*s)","*|/",[2.88643,2.91915,3.16344,3.42488,3.87359,4.21666,4.77949,5.11865])),
    reference = None,
    referenceType = "",
    shortDesc = u"""Group additive kinetics.""",
    longDesc = 
u"""
Fitted to 11 rates.
[<Entry index=10 label="Ct_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=18 label="Cd_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=33 label="C_rad/H2/Cd">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=12 label="O_pri_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=32 label="C_rad/H2/Cs">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=30 label="C_methyl">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=8 label="O2_birad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=7 label="H_rad">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=39 label="C_rad/H/NonDeC">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=37 label="C_rad/H2/O">, <Entry index=90 label="C/H/NdNd_Csrad">]
[<Entry index=49 label="C_rad/Cs3">, <Entry index=90 label="C/H/NdNd_Csrad">]
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
        ("Fri Jun  3 13:15:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen generated new group additivity values for this entry."""),
    ],
)

entry(
    index = 91,
    label = "C/H/NdNd_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    label = "C/H/NdNd_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    index = 93,
    label = "C/H/NdNd_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
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
    index = 94,
    label = "C/H/NdDe_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 95,
    label = "C/H/NdDe_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 96,
    label = "C/H/NdDe_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 97,
    label = "C/H/NdDe_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C/H/NdDe_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C/H/DeDe_Rrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 {Cs,Cd,CO,O} 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    index = 100,
    label = "C/H/DeDe_Csrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C/H/DeDe_Cdrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cd 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C/H/DeDe_COrad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 CO 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
    label = "C/H/DeDe_Orad",
    group = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     {Cd,Ct,Cb,CO} 0 {1,S}
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
L1: Y_rad_birad
    L2: Y_1centerbirad
        L3: O_atom_triplet
        L3: CH2_triplet
    L2: Y_rad
        L3: H_rad
        L3: O2_birad
        L3: C2b
        L3: Ct_rad
        L3: O_rad
            L4: O_pri_rad
            L4: O_sec_rad
                L5: O_rad/NonDeC
                L5: O_rad/NonDeO
                L5: O_rad/OneDe
        L3: Cd_rad
            L4: Cd_pri_rad
            L4: Cd_sec_rad
                L5: Cd_rad/NonDeC
                L5: Cd_rad/NonDeO
                L5: Cd_rad/OneDe
        L3: Cb_rad
        L3: CO_rad
            L4: CO_pri_rad
            L4: CO_sec_rad
                L5: CO_rad/NonDe
                L5: CO_rad/OneDe
        L3: Cs_rad
            L4: C_methyl
            L4: C_pri_rad
                L5: C_rad/H2/Cs
                L5: C_rad/H2/Cd
                L5: C_rad/H2/Ct
                L5: C_rad/H2/Cb
                L5: C_rad/H2/CO
                L5: C_rad/H2/O
            L4: C_sec_rad
                L5: C_rad/H/NonDeC
                L5: C_rad/H/NonDeO
                    L6: C_rad/H/CsO
                    L6: C_rad/H/O2
                L5: C_rad/H/OneDe
                    L6: C_rad/H/OneDeC
                    L6: C_rad/H/OneDeO
                L5: C_rad/H/TwoDe
            L4: C_ter_rad
                L5: C_rad/NonDeC
                    L6: C_rad/Cs3
                    L6: C_rad/NDMustO
                L5: C_rad/OneDe
                    L6: C_rad/Cs2
                    L6: C_rad/ODMustO
                L5: C_rad/TwoDe
                    L6: C_rad/Cs
                    L6: C_rad/TDMustO
                L5: C_rad/ThreeDe
L1: XH_Rrad
    L2: Cdpri_Rrad
        L3: Cdpri_Csrad
        L3: Cdpri_Cdrad
        L3: Cdpri_COrad
        L3: Cdpri_Orad
    L2: COpri_Rrad
        L3: COpri_Csrad
        L3: COpri_Cdrad
        L3: COpri_COrad
        L3: COpri_Orad
    L2: O_Rrad
        L3: O_Csrad
        L3: O_Cdrad
        L3: O_COrad
    L2: Cmethyl_Rrad
        L3: Cmethyl_Csrad
        L3: Cmethyl_Cdrad
        L3: Cmethyl_COrad
        L3: Cmethyl_Orad
    L2: Cpri_Rrad
        L3: C/H2/Nd_Rrad
            L4: C/H2/Nd_Csrad
            L4: C/H2/Nd_Cdrad
            L4: C/H2/Nd_COrad
            L4: C/H2/Nd_Orad
        L3: C/H2/De_Rrad
            L4: C/H2/De_Csrad
            L4: C/H2/De_Cdrad
            L4: C/H2/De_COrad
            L4: C/H2/De_Orad
    L2: Csec_Rrad
        L3: C/H/NdNd_Rrad
            L4: C/H/NdNd_Csrad
            L4: C/H/NdNd_Cdrad
            L4: C/H/NdNd_COrad
            L4: C/H/NdNd_Orad
        L3: C/H/NdDe_Rrad
            L4: C/H/NdDe_Csrad
            L4: C/H/NdDe_Cdrad
            L4: C/H/NdDe_COrad
            L4: C/H/NdDe_Orad
        L3: C/H/DeDe_Rrad
            L4: C/H/DeDe_Csrad
            L4: C/H/DeDe_Cdrad
            L4: C/H/DeDe_COrad
            L4: C/H/DeDe_Orad
"""
)

forbidden(
    label = "O2d",
    group = 
"""
1  *2 O 0 {2,D}
2  *3 O 0 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

forbidden(
    label = "O_Orad",
    group = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 O 1 {1,S}
3  *4 H 0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

