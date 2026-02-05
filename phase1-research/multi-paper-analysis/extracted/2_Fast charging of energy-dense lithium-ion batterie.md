# Fast charging of energy-dense lithium-ion batteries



--- Page 1 ---

Nature  |  www.nature.com  |  1
Article
Fast charging of energy-dense lithium-ion 
batteries
Chao-Yang Wang1,2 ✉, Teng Liu1, Xiao-Guang Yang1,3, Shanhai Ge1, Nathaniel V. Stanley2, 
Eric S. Rountree2, Yongjun Leng1 & Brian D. McCarthy2 ✉
Lithium-ion batteries with nickel-rich layered oxide cathodes and graphite anodes 
have reached specific energies of 250–300 Wh kg−1 (refs. 1,2), and it is now possible to 
build a 90 kWh electric vehicle (EV) pack with a 300-mile cruise range. Unfortunately, 
using such massive batteries to alleviate range anxiety is ineffective for mainstream EV 
adoption owing to the limited raw resource supply and prohibitively high cost. 
Ten-minute fast charging enables downsizing of EV batteries for both affordability 
and sustainability, without causing range anxiety. However, fast charging of 
energy-dense batteries (more than 250 Wh kg−1 or higher than 4 mAh cm−2) remains a 
great challenge3,4. Here we combine a material-agnostic approach based on 
asymmetric temperature modulation with a thermally stable dual-salt electrolyte to 
achieve charging of a 265 Wh kg−1 battery to 75% (or 70%) state of charge in 12 (or 11) 
minutes for more than 900 (or 2,000) cycles. This is equivalent to a half million mile 
range in which every charge is a fast charge. Further, we build a digital twin of such a 
battery pack to assess its cooling and safety and demonstrate that thermally 
modulated 4C charging only requires air convection. This offers a compact and 
intrinsically safe route to cell-to-pack development. The rapid thermal modulation 
method to yield highly active electrochemical interfaces only during fast charging has 
important potential to realize both stability and fast charging of next-generation 
materials, including anodes like silicon and lithium metal.
Electric vehicle (EV) batteries must possess high energy density and fast 
rechargeability. Next-generation batteries with high specific capacity 
anodes are expected to reach more than 350 Wh kg−1 (ref. 2), which could 
increase cruise range to greater than 400 miles (Supplementary Fig. 1a). 
Whereas higher energy densities have long been pursued, fast charging 
has only recently received increased attention3,4. True fast charging 
batteries would have immediate impact; a conventional long-range EV 
with a 120 kWh pack requiring an hour to recharge could be replaced 
with an EV with a 60 kWh pack capable of 10-min fast charging while 
maintaining very similar travel time during long-distance trips (Sup-
plementary Fig. 1b). As there are not enough raw minerals for every 
internal combustion engine car to be replaced by a 120 kWh-equipped 
EV, fast charging is imperative for EVs to go mainstream.
Battery fast charging must be evaluated by three metrics simultane-
ously: (1) charge time, (2) specific energy acquired and (3) cycle number 
under the fast charge condition. Lack of any of the three numbers is 
inadequate or misleading. Such a figure of merit plot compiling all 
literature data is displayed in Fig. 1. The automotive-acceptable zone 
comprises a rectangle in the upper-left corner as defined by 150 Wh kg−1 
minimum energy acquired within 15 min, as set by the US Department of 
Energy4. The ideal target is 240 Wh kg−1 acquired energy (for example, 
charging a 300 Wh kg−1 battery to 80% state of charge (SOC)) after a 5 
min charge with a more than 2,000 cycle lifetime in which every charge 
is a fast charge. Figure 1a shows literature data in which cycle lifetime 
was more than 800, hence meeting the minimum automotive cycle life 
requirement; Fig. 1b shows batteries with a cycle lifetime of less than 
800 and hence far from automotive acceptable.
An exhaustive literature search revealed only three groups of tech-
nologies meeting the minimum automotive cycle lifetime requirement. 
First are lithium titanium oxide batteries, which can survive more than 
30,000 15C charge cycles; unfortunately, their less than 100 Wh kg−1 is 
not practical5. Also in this unsuitable regime are supercapacitors and 
0–25% SOC flash charging of lithium-ion batteries (LiBs). The second 
group are all-solid-state lithium metal batteries (LMBs), which dem-
onstrate outstanding energy density and a 1,000-cycle lifetime, but 
with slow charging times. The third group—including this report—has 
graphite anodes, with this report being the first of this group, to our 
knowledge, to enter the automotive-acceptable zone.
As the most widely used LiB anode material, graphite’s low equi-
librium potential (100 mV versus Li|Li+) yields high energy densities 
at heightened lithium plating risk; this detrimental side effect dur-
ing fast charging induces rapid capacity loss and safety risk. To avoid 
and/or minimize lithium plating while fast charging thick graphite 
anodes of energy-dense LiBs, one must enhance the electrochemi-
cal and transport processes, including electrolyte ion transport6,7, 
Li insertion kinetics and solid-particle diffusion8. Figure 1a,b show 
https://doi.org/10.1038/s41586-022-05281-0
Received: 8 February 2022
Accepted: 26 August 2022
Published online: xx xx xxxx
 Check for updates
1Electrochemical Engine Center (ECEC) and Department of Mechanical Engineering, Pennsylvania State University, University Park, PA, USA. 2EC Power, State College, PA, USA.  
3Present address: National Engineering Laboratory for Electric Vehicles, School of Mechanical Engineering, Beijing Institute of Technology, Beijing, China. ✉e-mail: cxw31@psu.edu; 
bmccarthy@ecpowergroup.com


--- Page 2 ---

2  |  Nature  |  www.nature.com
Article
examples in which these types of enhancement came close to being 
automotive-acceptable, achieved using alternative Li salts9, decreased 
electrode tortuosity10 or asymmetric temperature modulation 
(ATM)11. With one exception12, previous fast-charging studies used 
2–2.6 mAh cm−2 loadings, too low for EV batteries.
Alternative anodes are being aggressively researched; however, 
none is automotive-ready. Silicon anodes are promising13, but their 
drastic volume expansion (more than 300%) during lithiation causes 
rapid capacity loss, especially during fast charging14. Intermediate 
approaches achieving usable cycle life and rate capability use lower 
silicon content15–17. In general, the calendar life of Si-anode batteries 
is still only 20–30 months, against the EV requirement of 100–140 
months18,19. Lithium metal is another alternative anode, with some 
fast-charging results available20–22. However, LMBs capable of fast 
charging usually use thick lithium foils and excess electrolyte, result-
ing in low specific energies. The LMBs in Fig. 1 show a large gap from 
the automotive target22–25.
Towards the goal of acquiring 240 Wh kg−1 by 15-min fast charging 
with more than 800 cycle life, herein we selected a LiNi0.8Mn0.1Co0.1O2 
(NMC811) cathode with an areal capacity of 3.4 mAh cm−2 and cell-level 
specific energy of 265 Wh kg−1 in the 50 Ah format. By combining the 
ATM method with a dual-salt electrolyte and larger porosity anode 
for improved ion transport, we demonstrate an automotive-viable 
solution. The LiB lasted more than 900 cycles when charged at 4C 
to 75% SOC (about 250,000 miles), and around 2,000 cycles if the 
upper charge SOC was lowered to 70% (about 500,000 miles). This is 
a record-breaking combination of charge time, specific energy acquired 
and cycle life among all reported battery chemistries.
Asymmetric temperature modulation
The ATM method rapidly preheats the cell and then carries out fast 
charging at elevated temperatures to take advantage of thermally 
enhanced electrochemical and transport processes to eliminate lithium 
plating (Extended Data Fig. 1). After charging, the cell rapidly cools 
below 40 °C because of a large temperature difference driving fast heat 
dissipation26; the cell then rests and discharges around the ambient 
temperature as usual. Although ATM effectively eliminates lithium 
plating, its success hinges upon the notion that capacity degradation 
caused by the solid-electrolyte interphase (SEI) growth at elevated 
a
This work*
NMC811|Gr, 3.4 mAh cm–2
12 min-185 Wh kg–1, 2,000 cycles 
13 min-199 Wh kg–1, 900 cycles
Ref. 11*
NMC622|Gr, 1.85 mAh cm–2
10 min-156 Wh kg–1, 1,700 cycles
NMC532|Gr, 2.55 mAh cm–2
10 min-170 Wh kg–1, 2,500 cycles
Ref. 10
NMC532|Gr, 2.65 mAh cm–2
10 min-188 Wh kg–1, 600 cycles
Ref. 9
NMC811|Gr, 2.35 mAh cm–2
12 min-182 Wh kg–1, 500 cycles
Ref. 12
NMC622|Gr, 3.5 mAh cm–2
27 min-183 Wh kg–1, 300 cycles
Ref. 22*
NMC9.5.5|Ag-C(5μm), 6.8 mAh cm–2
120 min-423 Wh kg–1, 1,000 cycles
Ref. 21
NMC111|Li(300μm), 1.8 mAh cm–2
30 min-135 Wh kg–1, 250 cycles
Ref. 25*
NMC811|Li(50μm), 3.2 mAh cm–2
60 min-300 Wh kg–1, 190 cycles
Ref. 20
NMC442|Li(120μm), 1.75 mAh cm–2
16 min-159 Wh kg–1, 170 cycles
Ref. 24
NMC811|Anode free, 4.2 mAh cm–2
600 min-350 Wh kg–1, 70 cycles
Ref. 15*
NMC622|GB, 2.4 mAh cm–2
10 min-193 Wh kg–1, 500 cycles
Ref. 16
LFP|N-PSi@C, 2.7 mAh cm–2
10 min-176 Wh kg–1, 200 cycles
Ref. 17
LCO|SEAG, 3.5 mAh cm–2
20 min-195 Wh kg–1, 30 cycles
Ref. 5
LFP|LTO, 1.1 mAh cm–2
4 min-68 Wh kg–1, 30,000 cycles
Automotive
acceptable
400
300
200
100
0
Energy acquired by charging (Wh kg–1)
Ref. 22*
LMB
LiB with Si
Ideal target
This work*
Ref.11*
Ref. 5
LTO
SoA LiB
Automotive
acceptable
SoA LiB
Ideal target
400
300
200
100
0
Energy acquired by charging (Wh kg–1)
Charging time (min)
1
5
10
20 30
60
100
300
600
Charging time (min)
1
5
10
20 30
60
100
300
600
LMB
Ref. 24
Ref. 25*
LiB with Si
Ref. 15*
Ref. 17
Ref. 12
Ref. 9
Ref. 10
Ref. 16
Ref. 20
Ref. 21
LTO
b
Cycle number more than 800
Cycle number less than 800
*denotes cycling at ~60 °C
Cycle life ∝       area
50
1000
2000
Fig. 1 | Figure of merit of fast charging batteries. A summary of literature 
studies on specific energy acquired by charging versus charge time, with the 
cycle life under a given charging condition displayed as the bubble size. Cell 
energy densities estimated using a 50 Ah cell design; see Supplementary Fig. 2. 
a, Cells with a cycle number of more than 800. b, Cells with a cycle number of 
less than 800. Data are from refs. 5,9–12,15–17,20–22,24,25.


--- Page 3 ---

Nature  |  www.nature.com  |  3
temperatures is a function of exposure time. Fortunately, such degrada-
tion is quite limited owing to the very short period of fast charging, as 
demonstrated in ref. 11. In this work, we further innovate the concept 
using much higher energy-density cells of NMC811 cathode material 
with loadings of 3.4 and 4.2 mAh cm−2 for two cell types. The anode 
material is artificial graphite and is matched to an NMC811 cathode 
with a negative to positive (N–P) capacity ratio of 1.1 in all cases. Two cell 
types were made (Supplementary Table 1a). First, baseline electrolyte 
cells had 1 M LiPF6 in ethylene carbonate (EC)/ethyl methyl carbonate 
(EMC) (3:7 by weight) + 2 wt% vinylene carbonate. Second, dual-salt 
electrolyte cells had the same solvent and additive as the baseline, but 
with 0.6 M LiPF6 and 0.6 M LiFSI.
Thermal stability was characterized by cycling each cell at 1C/1C at 
60 °C and plotting capacity retention versus time at 60 °C (Fig. 2a). Two 
cells had thicker 4.2 mAh cm−2 electrodes and either baseline or dual-salt 
electrolyte. A third cell had thinner 3.4 mAh cm−2 electrodes and base-
line electrolyte. The percent capacity retention versus cycle number for 
all three cells collapse onto a single curve, indicating that the SEI-caused 
cell degradation is indeed only a function of time as the specific sur-
face area of graphite in both the thin and thick anodes is the same.  
The dual salt used apparently does not change the SEI layer forma-
tion rate on the graphite anode; however, it did enhance electrolyte 
transport (Extended Data Fig. 2). The fitted curve in Fig. 2a provides a 
relation to calculate the capacity loss over time due to SEI degradation, 
clearly showing that batteries made of the present anode and cathode 
materials can survive at 60 °C for more than 1,000 h. If lithium plating 
could be fully eliminated during fast charging, this survival time would 
translate to thousands of extremely fast charging cycles (10–15 min 
per cycle) using the ATM method as the cells are at 60 °C only during 
preheating and fast charging.
The ATM cycling results of LiBs with areal loading of 4.2 mAh cm−2 and 
3.4 mAh cm−2 are plotted in Fig. 2b,c; solid lines with symbols denote 
actual cell degradation, whereas dashed lines represent the SEI-only 
degradation as derived from Fig. 2a. Actual cell degradation initially 
follows the SEI-only calculated dashed line, indicative of no lithium 
plating. At a threshold number of cycles, the actual degradation (solid 
lines) deviates from its corresponding dashed line, signalling lithium 
plating onset. The nonlinear behaviour of cell ageing, also known as 
capacity rollover, is normally believed to be caused by either lithium 
plating27–29 or cathode material impedance growth30. Here we find that 
capacity rollover occurs earlier when the areal capacities or charge cur-
rents become larger. Consequently, rollover is most probably caused 
by lithium plating as cathode instability should not be affected by the 
electrode areal capacity. Capacity rollover occurred earlier with faster 
charge rates (Fig. 2b,c), indicative of more severe lithium plating at 
higher C rates.
Comparing Fig. 2b with 2c shows that the less energy-dense LiB 
with an areal capacity of 3.4 mAh cm−2 achieves higher cycle numbers 
and higher charge C rates before marked capacity rollover. Qualita-
tively consistent trends are also observed from the voltage relaxa-
tion diagnostics (Extended Data Fig. 3a,b). However, actual cycling 
results are more restrictive than the voltage relaxation diagnostics on 
fresh cells, probably because of the aggravated effect of ageing in the 
former cases31. Indeed, Extended Data Fig. 3a,b shows no evidence of 
notable lithium plating when the charge rate is less than 2C for a fresh 
4.2 mAh cm−2 cell or less than 4C for a fresh 3.4 mAh cm−2 cell. However, 
the actual cycling results show that the 4.2 and 3.4 mAh cm−2 cells can-
not withstand higher than 1C and 1.5C charge rates, respectively. It is 
possible that, in continuously aged cells, lithium plating occurs later 
owing to degraded kinetics and mass transport properties. The depos-
ited lithium metal will quickly react with the solvent, which further 
degrades the rate capability and accelerates new lithium metal deposi-
tion. This positive feedback mechanism accelerates capacity loss, which 
is also supported by a sudden drop in coulombic efficiency (Extended 
Data Fig. 3c,d) and a sharp increase of cell impedance (Extended Data 
Fig. 3e,f).
These parametric results show that 15-min/4C fast charging of 
energy-dense batteries without Li plating cannot be achieved with 
ATM alone; the electrolyte mass transport needs further enhancement. 
Indeed, among all the parameters involved in the charging process, 
ionic conductivity and ionic diffusivity have the lowest activation 
energy (10–20 kJ mol−1) and attain the least improvement by tempera-
ture elevation11,32.
Improved ionic transport
Electrolyte ionic transport through porous electrodes can be increased 
with better intrinsic properties (that is, higher ionic conductivity, 
higher ionic diffusivity and higher Li+ transference number) or by reduc-
ing the ratio of electrode tortuosity to porosity (MacMullin number)8,33. 
Here, we take both measures by using a LiPF6–LiFSI dual-salt electrolyte 
and higher anode porosity.
Compared with LiPF6, LiFSI has similar ionic conductivity (around 
10 mS cm−1 at 25 °C) and a higher transference number (0.56 versus 0.38 
at 25 °C)9,34,35 (Supplementary Fig. 3), and importantly is more thermally 
a
b
c
Capacity retention (%)
100
95
90
85
80
Time at ≈ 60 °C (h)
0
100
200
300
400
500
600
700
800
900
1,000
Capacity retention (%)
Capacity retention (%)
100
95
90
85
80
75
70
65
100
95
90
85
80
75
70
65
0
50
100
150
200
250
300
350
400
450
500
0
100
200
300
400
500
600
700
800
900
1,000
Cycle number
Cycle number
Fitting, CR = 100–1.254t0.4, R2 = 0.992
4.2 mAh cm–2, 1C/1C cycling at 60 °C (baseline)
4.2 mAh cm–2, 1C/1C cycling at 60 °C (dual-salt)
3.4 mAh cm–2, 1C/1C cycling at 60 °C (baseline)
1C/1C cycling at 60 °C (120 min per cycle)
1C–100% SOC, ATM (60 min per cycle)
1.5C–75% SOC, ATM (30 min per cycle)
2C–75% SOC, ATM (22.5 min per cycle)
4.2 mAh cm–2 LiB
3.4 mAh cm–2 LiB
SEI degradation
Actual degradation
SEI degradation
Actual degradation
1C/1C cycling at 60 °C (120 min per cycle)
2C–80% SOC, ATM (24 min per cycle)
3C–80% SOC, ATM (16 min per cycle)
4C–70% SOC, ATM (10.7 min per cycle)
Fig. 2 | ATM cycles of energy-dense LiBs. a, Constant 1C/1C cycling at 60 °C to 
characterize SEI degradation. b, ATM fast charging of 4.2 mAh cm−2 batteries at 
1C, 1.5C and 2C to 100%, 75% and 75% SOC, respectively. c, ATM fast charging of 
3.4 mAh cm−2 batteries with the baseline electrolyte at 2C, 3C and 4C to 80%, 
80% and 70% SOC, respectively. The solid lines in b and c denote the actual cell 
capacity loss, whereas the dashed lines represent the portion of SEI-caused 
degradation as calculated from the fitting equation derived from a. Deviation 
of a solid line from a corresponding dashed line thus represents the portion of 
capacity loss due to lithium plating. CR, capacity retention.


--- Page 4 ---

4  |  Nature  |  www.nature.com
Article
stable. To leverage these properties, we switched to a dual-salt elec-
trolyte in which 1 M LiPF6 is replaced with 0.6 M LiFSI and 0.6 M LiPF6. 
A remarkable improvement of high-rate performance results, with the 
relative capacity under 6C discharging increasing from 70% to 90% 
relative to the baseline electrolyte (Extended Data Fig. 2). Additionally, 
LiFSI’s better thermal stability enables higher charging temperatures 
and so faster charging. A higher-porosity anode was also selected to 
reduce the tortuosity and MacMullin number based on the empirical 
relationship for graphite between porosity and MacMullin number36. 
Increasing the porosity from 0.26 to 0.35 increased the effective trans-
port properties by 40% while decreasing the energy density by only 
2% because of the need for more electrolyte (Supplementary Fig. 3b).
Fast charging energy-dense LiBs
Numerical modelling (Extended Data Fig. 4) and experimental voltage 
relaxation results (Extended Data Fig. 5) suggested that the new cell 
with the dual-salt electrolyte and higher porosity anode would have a 
maximum plating-free charge rate of 4C; this rate was used for experi-
mental cycling tests. Two cells of 3.4 mAh cm−2 areal capacity were ATM 
cycled to either 70% or 75% SOC. Figure 3a illustrates voltage and tem-
perature evolutions throughout the protocols. Before fast charging, 
the preheating step heated the cells from room temperature to 65 °C 
in around 1 min. Note that the preheating temperature was raised from 
60 to 65 °C to further lower lithium plating risk. The cell temperature 
was maintained at roughly 65 °C during fast charging, which took about 
11 min to reach 70% SOC and about 12 min to reach 75% SOC. Afterwards, 
the cells quickly cooled during C/3 discharge near room temperature.
Figure 3b displays the capacity retention data of both cycling tests, 
with dashed lines representing SEI-only degradation. When charging 
to 70% SOC, the actual cell degradation closely follows its calculated 
SEI-only degradation until approximately 1,200 cycles, indicating 
negligible lithium plating up to that point. The cell exceeded 2,000 
cycles before reaching 20% capacity loss. This 265 Wh kg−1 battery 
could take 4C charging for more than 2,000 cycles; with the specific 
energy acquired by the fast charge reaching 184 Wh kg−1, above the 
180 Wh kg−1 DOE target (Fig. 3c). For the cell charged to 75% SOC, the 
capacity retention deviated from the solid line after about 300 cycles 
(Fig. 3b). The cell then aged linearly, with no capacity rollover before 
end of life. This translates to a cell with a 900 fast charge cycle life, with 
each charge acquiring about 200 Wh kg−1 (Fig. 3c).
Extended Data Figure 6 examines the cycling results of different 
experimental combinations of electrode and electrolyte design. The 
baseline LiB cycle life under 4C charging is about 200 cycles. If a single 
improvement is made—electrode or electrolyte—the cycle life only 
increases to 600–700 cycles. Only by combining a dual-salt electrolyte 
with high-porosity anodes was more than 2,000 cycles achieved, cor-
responding to a remarkable approximate 500,000 miles driven. These 
experimental findings and additional modelling studies (Extended 
Data Fig. 7) highlight that several strategies must be synergistically 
combined to break through current limitations for fast charging 
energy-dense batteries.
Charging at elevated temperatures may prove beneficial to decrease 
degradation of active materials other than graphite. For instance, at 
high charge rates, the concentration gradient within active material par-
ticles results in stress and irreversible particle cracking; this is believed 
to be a major NMC811 ageing mechanism37. Suppose instead that the 
battery is fast charged at elevated temperatures to yield improved 
solid-state diffusivity, reduced gradients, relief of particle strain and 
hence suppressed mechanical loss. The same methodology also applies 
to silicon, in which fast solid diffusion is necessary to reduce volume 
expansion-induced stress38.
Pack cooling and safety
We next assessed the impact of an ATM strategy on cell cooling and 
safety at the pack level by building a digital 1/8-scale EV 12S1P pack 
model with aspirated air cooling based on the same 3.4 mAh cm−2, high 
porosity electrodes used above in a 150 Ah prismatic cell format (Fig. 4a 
and Supplementary Table 2). This 12S1P model represents one module 
out of eight in a full pack, with all cooled equivalently. The cells are 
only air cooled on the top and bottom surfaces, with the faces tightly 
packed together. GT-AutoLion3D was used to perform electrochemi-
cal–thermal fully coupled simulations of the pack with the same elec-
trochemical and electrode geometrical parameters from the validated 
one-dimensional (1D) model of Supplementary Table 3 and Extended 
Data Figs. 2 and 4. Pack simulations were carried out for the same cycle 
as in single cell testing (Fig. 3a): preheat to 65 °C, 4C charging to 75% 
SOC, 1 min rest and C/3 discharge.
The internal cell temperature distribution (Fig. 4b,c) was found to 
be quite uniform throughout the 4C charge and C/3 discharge owing 
to the much larger in-plane thermal conductivity (45.5 W m−1 K−1) 
of electrode-separator stacks relative to the through-plane 
(0.55 W m−1 K−1)39–41. Cooling just the top and bottom surfaces with a 
heat transfer coefficient h = 140 W m−2 K−1, accessible with forced air 
convection, was found to be sufficient to maintain battery tempera-
ture near 65 °C during 4C charging (Fig. 4c). In comparison, cooling of 
single cells (Fig. 3a) occurred under air natural convection with h less 
than  20 W m−2 K−1 because of the much larger surface area for heat 
dissipation. The simulations found that it took 11.6 min into the C/3 
discharge for the cells to cool below 40 °C (Fig. 4c), close to the roughly 
8 min observed in single-cell testing (Fig. 3a), and that this time could 
be reduced to around 5 min if air vents for aspirated convection were 
a
Voltage (V)
Temperature (°C)
4.2
3.9
3.6
3.3
3.0
2.7
80
60
40
20
–2
0
2
4
6
8
10
12 0.5
1.0
1.5
2.0
2.5
3.0
Time (min)
Time (h)
Preheating ≈ 1 min
10 min 40 s to 70% SOC
11 min 40 s to 75% SOC
75% SOC, discharging
70% SOC, discharging
4C charging at 65 °C
75% SOC, charging
70% SOC, charging
Passive cooling to ambient
Capacity retention (%)
Specifc energy after
fast charging (Wh kg–1)
100
95
90
85
80
200
180
160
140
120
Cycle number
Cycle number
0
200
400
600
800
1,000
1,200
1,400
1,600
1,800
2,000
0
200
400
600
800
1,000
1,200
1,400
1,600
1,800
2,000
3.4 mAh cm–2 LiB, enhanced ion transport
4C–75% SOC
4C–70% SOC
SEI degradation
Actual degradation
4C–75% SOC
4C–70% SOC
DOE target
b
c
Fig. 3 | Fast charging of energy-dense LiBs with enhanced ion transport. 
 a, Voltage and temperature profiles for an ATM cycle. b, Capacity retention 
under fast charging. c, Specific energy acquired after fast charging.


--- Page 5 ---

Nature  |  www.nature.com  |  5
larger, for example increasing h to 300 W m−2 K−1 (Extended Data Fig. 8). 
These numerical results demonstrate the feasibility for ATM-enabled 
battery packs to achieve safe 4C charging while also replacing tradi-
tional liquid-refrigeration cooling with passive air thermal manage-
ment. In practice, forced air convection could easily be implemented 
by installing a charger-powered fan, with cooling switching to aspirated 
air cooling during driving to reduce power consumption.
The safety of charging batteries at 65 °C is ensured by a combination 
of very short exposure to elevated temperatures and use of a more ther-
mally stable lithium salt. The total elevated temperature exposure time 
amounts to 167 h (10 min per cycle) for 1,000 fast-charge cycles, only 
0.167% of a 12-year electric vehicle lifetime. Indeed, capacity retention 
loss due to accelerated SEI degradation over 167 h is still much lower than 
the 20% total loss limit (Fig. 2a), implying no safety concerns. Recent 
work42, appearing after our initial submission, showed that NMC/graph-
ite cells could be safely cycled at 70 °C for 6  months with little ageing. 
A new perspective, also published after initial submission, concluded 
that intrinsically safe batteries of the future must be heat-tolerant and 
exhibit great resistance to thermal runaway43. Charging at elevated tem-
peratures eliminates Li plating while also enhancing safety. Finally, we 
note that thermally modulated 4C charging requires only air convection 
from the bottom and top cell surfaces, permitting an intrinsically safe 
and reliable pack design. By contrast, traditional battery packs must 
resort to liquid cooling through sophisticated three-dimensional cool-
ant channels, which are subject to intense squeezing from cell expansion 
upon ageing and are thus prone to coolant leakage.
Online content
Any methods, additional references, Nature Research reporting summa-
ries, source data, extended data, supplementary information, acknowl-
edgements, peer review information; details of author contributions 
and competing interests; and statements of data and code availability 
are available at https://doi.org/10.1038/s41586-022-05281-0.
1.	
Wu, Y. et al. An empirical model for the design of batteries. ACS Energy Lett. 5, 807–816 
(2020).
2.	
Deng, J., Bae, C., Denlinger, A. & Miller, T. Electric vehicles batteries: requirements and 
challenges. Joule 4, 511–515 (2020).
3.	
Cheeseman, H. Fast-charging Li-metal batteries. ARPA-E https://arpa-e.energy.gov/
open-2021/webinars (2021).
4.	
Howell, D. et al. Enabling fast charging: a technology gap assessment. US Department of 
Energy https://www.energy.gov/sites/default/files/2017/10/f38/XFC%20Technology%20
Gap%20Assessment%20Report_FINAL_10202017.pdf (2017).
5.	
Zaghib, K. et al. Safe and fast-charging Li-ion battery with long shelf life for power 
applications. J. Power Sources 196, 3949–3954 (2011).
6.	
Colclasure, A. M. et al. Electrode scale and electrolyte transport effects on extreme fast 
charging of lithium-ion cells. Electrochim. Acta 337, 135854 (2020).
7.	
Logan, E. R. et al. Ester-based electrolytes for fast charging of energy dense lithium-ion 
batteries. J. Phys. Chem. C 124, 12269–12280 (2020).
8.	
Liu, T., Yang, X., Ge, S., Leng, Y. & Wang, C. Y. Ultrafast charging of energy-dense 
lithium-ion batteries for urban air mobility. eTransportation 7, 100103 (2021).
9.	
Du, Z., Wood Iii, D. L. & Belharouak, I. Enabling fast charging of high energy density Li-ion 
cells with high lithium ion transport electrolytes. Electrochem. Comm. 103, 109–113 
(2019).
10.	
Chen, K. et al. Efficient fast-charging of lithium-ion batteries enabled by laser-patterned 
three-dimensional graphite anode architectures. J. Power Sources 471, 228475  
(2020).
+
A
-
a
Cathode Ni foil
Anode
k   = 45.5
W m–1 K–1
k   = 0.55 W m–1 K–1
Aspirated air convection 12S1P pack model
Ta = 25 °C
h = 140 W m–2 K–1
T – Tavg (°C)
0
–1
1
2
b
c
610 s
Tavg = 66 °C
Temperature (°C)
Time (min)
70
60
50
40
30
20
0
14
28
42
56
70
84
98
112
126
140
1
2
3
Rest
4C charge
C/3 discharge
Max. temperature (cell centre)
Min. temperature (cell bottom)
Time (min)
0
14
28
42
56
70
84
98
112
126
140
Voltage (V)
4.2
4.0
3.8
3.6
3.4
3.2
3.0
2.8
Rest
4C charge
C/3 discharge
d
720 s
Tavg = 63 °C
1,470 s
Tavg = 39.5 °C
Cell
centre
cutaway
+
+
+
–
–
–
+
-
Fig. 4 | Electrochemical–thermal coupled simulations of a 12S1P pack of  
150 Ah prismatic cells. a, Cell construction, pack model and thermal 
conditions under aspirated air convection. b, 3D temperature difference 
contours in 150 Ah prismatic cells at three representative time instants during 
4C charge–C/3 discharge cycling. c, Evolution of maximum and minimum 
temperatures in the prismatic cell. d, Cell voltage evolution during cycling.


--- Page 6 ---

6  |  Nature  |  www.nature.com
Article
11.	
Yang, X.-G. et al. Asymmetric temperature modulation for extreme fast charging of 
lithium-ion batteries. Joule 3, 3002–3019 (2019).
12.	
Han, J.-G. et al. An electrolyte additive capable of scavenging HF and PF5 enables fast 
charging of lithium-ion batteries in LiPF6-based electrolytes. J. Power Sources 446, 
227366 (2020).
13.	
Gonzalez, A. F., Yang, N.-H. & Liu, R.-S. Silicon anode design for lithium-ion batteries: 
progress and perspectives. J. Phys. Chem. C 121, 27775–27787 (2017).
14.	
Lee, S. K., McDowell, M. T., Choi, J. W. & Cui, Y. Anomalous shape changes of silicon 
nanopillars by electrochemical lithiation. Nano Lett. 11, 3034–3039 (2011).
15.	
Son, I. H. et al. Graphene balls for lithium rechargeable batteries with fast charging and 
high volumetric energy densities. Nat. Commun. 8, 1561 (2017).
16.	
Wang, B. et al. Ultrafast-charging silicon-based coral-like network anodes for lithium-ion 
batteries with high energy and power densities. ACS Nano 13, 2307–2315 (2019).
17.	
Kim, N., Chae, S., Ma, J., Ko, M. & Cho, J. Fast-charging high-energy lithium-ion batteries 
via implantation of amorphous silicon nanolayer in edge-plane activated graphite 
anodes. Nat. Commun. 8, 812 (2017).
18.	
McBrayer, J. D. et al. Calendar aging of silicon-containing batteries. Nat. Energy 6,  
866–872 (2021).
19.	
Masias, A., Marcicki, J. & Paxton, W. A. Opportunities and challenges of batteries in 
automotive applications. ACS Energy Lett. 6, 621–630 (2021).
20.	 Zheng, J. et al. Electrolyte additive enabled fast charging and stable cycling lithium metal 
batteries. Nat. Energy 2, 17012 (2017).
21.	
Peng, Z. et al. High-power lithium metal batteries enabled by high-concentration 
acetonitrile-based electrolytes with vinylene carbonate additive. Adv. Funct. Mater. 30, 
2001285 (2020).
22.	 Lee, Y.-G. et al. High-energy long-cycling all-solid-state lithium metal batteries enabled 
by silver–carbon composite anodes. Nat. Energy 5, 299–308 (2020).
23.	 Niu, C. et al. High-energy lithium metal pouch cells with limited anode swelling and long 
stable cycles. Nat. Energy 4, 551–559 (2019).
24.	 Ren, X. et al. Enabling high-voltage lithium-metal batteries under practical conditions. 
Joule 3, 1662–1676 (2019).
25.	 Leng, Y. et al. Fast charging of energy-dense lithium metal batteries in localized 
ether-based highly concentrated electrolytes. J. Electrochem. Soc. 168, 060548  
(2021).
26.	 Liu, T., Ge, S., Yang, X.-G. & Wang, C.-Y. Effect of thermal environments on fast charging 
Li-ion batteries. J. Power Sources 511, 230466 (2021).
27.	
Keil, J. et al. Linear and nonlinear aging of lithium-ion cells investigated by 
electrochemical analysis and in-situ neutron diffraction linear and nonlinear aging of 
lithium-ion cells investigated by electrochemical analysis and in-situ neutron diffraction. 
J. Electrochem. Soc. 166, A3908 (2019).
28.	 Schuster, S. F. et al. Nonlinear aging characteristics of lithium-ion cells under different 
operational conditions. J. Energy Storage 1, 44–53 (2015).
29.	 Yang, X.-G., Leng, Y., Zhang, G., Ge, S. & Wang, C.-Y. Modeling of lithium plating induced 
aging of lithium-ion batteries: transition from linear to nonlinear aging. J. Power Sources 
360, 28–40 (2017).
30.	 Ma, X. et al. Hindering Rollover Failure of Li[Ni0.5Mn0.3Co0.2]O2/Graphite Pouch Cells 
during Long-Term Cycling. J. Electrochem. Soc. 166, A711 (2019).
31.	
Yang, X.-G., Ge, S., Liu, T., Leng, Y. & Wang, C.-Y. A look into the voltage plateau signal for 
detection and quantification of lithium plating in lithium-ion cells. J. Power Sources 395, 
251–261 (2018).
32.	 Ogihara, N. et al. Theoretical and experimental analysis of porous electrodes for 
lithium-ion batteries by electrochemical impedance spectroscopy using a symmetric 
cell. J. Electrochem. Soc. 159, A1034–A1039 (2012).
33.	 Newman, J. S. & Tobias, C. W. Theoretical analysis of current distribution in porous 
electrodes. J. Electrochem. Soc. 109, 1183 (1962).
34.	 Li, L. et al. Transport and electrochemical properties and spectral features of 
non-aqueous electrolytes containing LiFSI in linear carbonate solvents. J. Electrochem. 
Soc. 158, A74 (2011).
35.	 Han, H.-B. et al. Lithium bis(fluorosulfonyl)imide (LiFSI) as conducting salt for 
nonaqueous liquid electrolytes for lithium-ion batteries: physicochemical and 
electrochemical properties. J. Power Sources 196, 3623–3632 (2011).
36.	 Landesfeind, J., Hattendorff, J., Ehrl, A., Wall, W. A. & Gasteiger, H. A. Tortuosity 
determination of battery electrodes and separators by impedance spectroscopy.  
J. Electrochem. Soc. 163, A1373–A1387 (2016).
37.	
Bi, Y. et al. Reversible planar gliding and microcracking in a single-crystalline Ni-rich 
cathode. Science 370, 1313–1317 (2020).
38.	 Li, Y. et al. Growth of conformal graphene cages on micrometre-sized silicon particles as 
stable battery anodes. Nat. Energy 1, 15029 (2016).
39.	 Yang, X.-G., Zhang, G. & Wang, C. Y. Computational design and refinement of self-heating 
lithium ion batteries. J. Power Sources 328, 203–211 (2016).
40.	 Zhang, J., Wu, B., Li, Z. & Huang, J. Simultaneous estimation of thermal parameters for 
large-format laminated lithium-ion batteries. J. Power Sources 259, 106–116 (2014).
41.	
Ye, Y., Saw, L. H., Shi, Y., Somasundaram, K. & Tay, A. A. O. Effect of thermal contact 
resistances on fast charging of large format lithium ion batteries. Electrochim. Acta 134, 
327–337 (2014).
42.	 Aiken, C. P. et al. Li[Ni0.5Mn0.3Co0.2]O2 as a superior alternative to LiFePO4 for long- 
lived low voltage li-ion cells. J. Electrochem. Soc. 169, 050512 (2022).
43.	 Longchamps, R. S., Yang, X. G. & Wang, C. Y. Fundamental insights into battery thermal 
management and safety. ACS Energy Lett. 7, 1103–1111 (2022).
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in 
published maps and institutional affiliations.
Springer Nature or its licensor holds exclusive rights to this article under a publishing 
agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted 
manuscript version of this article is solely governed by the terms of such publishing 
agreement and applicable law.
© The Author(s), under exclusive licence to Springer Nature Limited 2022


--- Page 7 ---

Methods
Cell materials and fabrication
LiNi0.8Mn0.1Co0.1O2 (NMC811) and graphite were used as the cathode 
and anode materials for cell fabrication in this work. With different 
combinations of loadings and porosities, testing results coming from 
three types of electrode are presented. As shown in Supplementary 
Table 1, the ‘Energy-dense+’ cell had a mass loading of 21.3 mg cm−2 on 
the cathode side; this was matched with a 13.4 mg cm−2 anode to give 
a corresponding design capacity of 4.2 mAh cm−2. For the cell with an 
areal capacity of 3.4 mAh cm−2, the mass loadings were 17.2 mg cm−2 
and 10.8 mg cm−2 for cathode and anode, respectively. Mass-produced 
industrial electrodes for high-energy LiBs usually have low porosity, 
which equalled 0.26 for the baseline cells in this study. A high porosity 
anode (ε = 0.35) is used to improve the mass transport in the electrolyte 
phase during fast charging, while the porosity in the cathode is kept at 
0.3 for all the cells. The electrolytes used in this study had two formulas. 
The baseline electrolyte consisted of 1 M LiPF6 dissolved in EC/EMC  
(3:7 by weight) + 2 wt% vinylene carbonate. The dual-salt electrolyte 
used the same solvent and additive as the baseline, but the salt was 
replaced by 0.6 M LiFSI and 0.6 M LiPF6. The test pouch cells were fab-
ricated in 3–5 Ah formats to demonstrate the cell-level performance. 
For actual cells used in EV applications, the capacity can reach more 
than 50 Ah (ref. 44). If we use a 50 Ah design to evaluate the specific 
energy of the cells, it could reach 283 Wh kg−1 when using high loading 
electrodes of 4.2 mAh cm−2. Under an areal capacity of 3.4 mAh cm−2, 
the specific capacity of the cell comes to 271 Wh kg−1; if a high porosity 
anode is adopted, then the specific capacity becomes 265 Wh kg−1.
The cells fabricated for ATM cycling had an embedded Ni foil for 
preheating; the 27-µm-thick foil was coated with polyethylene tereph-
thalate (total weight was 1.5% of the battery mass) and placed inside the 
cell45. The internal self-heating structure enables rapid heating of LiBs 
with heating rates up to 1 °C s−1 while maintaining a good temperature 
uniformity regardless of the cell format46.
Cycling tests
Cycling tests were done with an Arbin Instruments BT2000. For thermal 
stability characterization, the cells were placed in a 60 °C environment 
chamber, cycled under 1C CCCV charging (4.15 cut-off voltage, C/3 
cut-off current) and followed by a 1C discharge to 2.7 V. ATM cycling 
tests were conducted in the 20 °C ambient and comprised a preheating 
step, fast charging step (with internal heating turned off) and a dis-
charge step. We achieved preheating with an internal heating element 
made of a 30-µm-thick nickel foil embedded in the centre electrode 
layers45, which only weighs 1.5% that of the cell. As shown in Extended 
Data Fig. 1a, the heating sheet has two terminals; one end is connected to 
the negative terminal of the cell, and the other end is extended from the 
cell and forms a third terminal called the activation terminal. Extended 
Data Figure 1b shows the evolution of cell temperature during heating. 
When applying a 3.3 V voltage (around the open circuit voltage of the 
discharged battery) to the heating element, we can get a heating rate 
of 0.75 °C s−1, that is, heating a cell from room temperature to 60–65 °C 
within 1 min. The maximum temperature difference between the heater 
surface and cell outer surface is roughly 10 °C during preheating and 
diminishes to around 1 °C, 10 s after preheating ceases. Here the cell 
outer surface temperature was measured with a thermocouple, and 
the internal heater temperature was back-calculated from the foil 
resistance based on a precalibrated linear relationship47.
The cell starts charging after reaching a target charge temperature. 
The charging process uses a CCCV protocol; the cut-off current equalled 
half of the CC charging current, and the charge step terminates either 
when the target SOC or the cut-off current is reached. The target SOCs 
ranged from 70% to 80% in different tests, and the cut-off voltage was 
also adjusted to match the target SOCs, that is, under target SOCs of 80%, 
75% and 70%, the cut-off voltages were 4.15 V, 4.1 V and 4.0 V, respectively. 
Once the high-current charging ceases, the large internal heat genera-
tion vanishes, and the battery temperature drops close to ambient within 
several minutes and continues during the discharge step.
Electrochemical–thermal model
Commercial software, GT-AutoLion in 1D (for single cells) and 3D 
(for packs) versions, was used to solve the physics-based ECT model 
(governing equations shown in the Supplementary Information equa-
tions (S1)–(11)); an identical 1D model was used in our earlier study26. The 
modelling parameters used in this work are summarized in Supplemen-
tary Table 2, and comparison of the model’s results with experimental 
data is shown in Extended Data Figs. 2 and 4. The occurrence of lithium 
plating is determined by Supplementary Information equation (12).
Electrochemical impedance spectroscopy
The electrochemical impedance spectroscopy (EIS) tests were conducted 
with a Solatron ModuLlab Xm. The cells were held at 3.96 V (approximately 
80% SOC) for more than 2 h before the tests. A signal with 2 mV amplitude 
was applied to the cell with a frequency sweep from 10 kHz to 0.01 Hz. The 
impedance in the complex plane has a similar shape to the equivalent 
circuit depicted in Extended Data Fig. 9a. The impedance at different 
frequencies corresponds to different electrochemical processes in the 
battery. The high-frequency resistance is set to be the resistance at 1 kHz, 
which comes from the contact resistance, the ohmic resistance in the solid 
phase of electrodes and the ohmic resistance of electrolyte that fills the 
pores of the electrodes and separators. At low frequency, the impedance 
in the complex plane shows a straight line with roughly a 45° phase angle, 
which is known as the Warburg element (semi-infinite), ZW, describing the 
diffusion process in solid particles. In between, the semicircles correspond 
to the charge transfer process at different reaction interfaces, and the 
resistance of this segment is known as the charge transfer resistance, Rct.
An equivalent circuit with four components is used to fit and interpret 
the results of the EIS tests48. The details of the equivalent circuit and the 
derivation of fitting expression (Supplementary equations (13)–(18)) 
are given in the Supplementary Information.
Data availability
All data generated or analysed during this study are included in this 
published article, the Extended Data and the Supplementary Information.
 
44.	 Lima, P. Samsung SDI 94 Ah battery cell full specifications. PushEVs https://pushevs.
com/2018/04/05/samsung-sdi-94-ah-battery-cell-full-specifications/ (2021).
45.	 Wang, C. Y. et al. Lithium-ion battery structure that self-heats at low temperatures. Nature 
529, 515–518 (2016).
46.	 Yang, X. G., Liu, T. & Wang, C. Y. Innovative heating of large-size automotive Li-ion cells.  
J. Power Sources 342, 598–604 (2017).
47.	
Zhang, G. et al. Rapid self-heating and internal temperature sensing of lithium-ion 
batteries at low temperatures. Electrochim. Acta 218, 149–155 (2016).
48.	 Leng, Y. et al. Electrochemical cycle-life characterization of high energy lithium-ion cells 
with thick Li(Ni0.6Mn0.2Co 0.2)O2 and graphite electrodes. J. Electrochem. Soc. 164, 
A1037–A1049 (2017).
Acknowledgements Partial support from the US Department of Energy’s Office of Energy 
Efficiency and Renewable Energy (EERE) under award no. DE-EE0008355, the William E. 
Diefenderfer Endowment and Air Force STTR under contract FA864921P1620 is gratefully 
acknowledged. We are also grateful to Gamma Technologies for offering GT-AutoLion software.
Author contributions C.Y.W., T.L., B.D.M. and E.S.R. wrote the manuscript. S.G. designed and 
built the cells. T.L. and X.G.Y. designed the experiments. T.L. built the test stand and carried out 
the experiments. Y.L. optimized electrolytes in coin cells. C.Y.W., N.V.S. and B.D.M. designed 
and performed 3D numerical simulations. All authors contributed to development of the 
manuscript and to discussions as the project developed.
Competing interests B.D.M., E.S.R., N.V.S. and C.Y.W. have a financial interest in EC Power.
Additional information
Supplementary information The online version contains supplementary material available at 
https://doi.org/10.1038/s41586-022-05281-0.
Correspondence and requests for materials should be addressed to Chao-Yang Wang or 
Brian D. McCarthy.
Peer review information Nature thanks the anonymous reviewers for their contribution to the 
peer review of this work.
Reprints and permissions information is available at http://www.nature.com/reprints.


--- Page 8 ---

Article
Extended Data Fig. 1 | LiB design for ATM cycling. a, LiB with an embedded 
nickel foil for internal heating. Before each charging, current goes through the 
internal heating structure and heats up the cell to 65 °C in less than one minute. 
After reaching the target temperature, the charging channel starts to take in 
energy and maintains thermal balance throughout the charging process.  
b, Cell and heating-foil temperatures versus heating time. A heating rate of 
0.75 °C s−1 was achieved when applying 3.3 V on the heating channel.


--- Page 9 ---

Extended Data Fig. 2 | Rate performance tests and model validation. a, Cell with baseline electrolyte. b, Cell with dual-salt electrolyte; the simulated 
transference number was 0.48.


--- Page 10 ---

Article
Extended Data Fig. 3 | Ageing mechanisms under ATM cycling. a, b, Lithium plating detection with voltage relaxation method for 4.2 mAh cm−2 LiBs and 
3.4 mAh cm−2 LiBs. c, d, Coulombic efficiency during cycling. e, f, Change of resistance attained by EIS tests. Baseline electrolyte was used in these tests.


--- Page 11 ---

Extended Data Fig. 4 | Numerical prediction of lithium plating at various 
charge rates with T=60°C. a, Experimental and simulated voltage profiles for 
baseline cells. b, Simulated lithium deposition potential for baseline cells.  
c, Experimental and simulated voltage profiles for cells with dual-salt 
electrolyte. d, Simulated lithium deposition potential for cells with dual-salt 
electrolyte.


--- Page 12 ---

Article
Extended Data Fig. 5 | Ageing mechanisms under fast charging of batteries with enhanced ion transport. a, Lithium plating detection with voltage relaxation 
method for 3.4 mAh cm−2 LiBs with enhanced ion transport. b, Coulombic efficiency during cycling. c, Change of resistance attained by EIS tests.


--- Page 13 ---

Extended Data Fig. 6 | Fast charging cycling with different combinations of electrodes and electrolytes. Use of either the mixed dual-salt electrolyte or 
higher porosity anodes failed to give long cycle lifetime; both were required for long cycle lifetime.


--- Page 14 ---

Article
Extended Data Fig. 7 | Parameter map of lithium plating-free (LPF) charging 
(3.4 mAh cm−2). a, Simulated LPF region given by relative ion transport 
resistance and charge transfer resistance when 3C charging the battery 
(*denotes unitless variables, referenced with the properties of a fresh baseline 
cell charging at 60 °C). b, Simulated LPF region given by relative ion transport 
resistance and charge transfer resistance when 4C charging the battery, in 
which the open symbol labelled as 65 °C denotes the high porosity anode.  
c, Change of charge transfer resistance during aging attained from EIS tests 
and analysis. d, Change of ion transport resistance during ageing attained from 
EIS tests and analysis.


--- Page 15 ---

Extended Data Fig. 8 | Effects of heat transfer coefficient. Effects during C/3 
discharge on 4C charge - C/3 discharge cycling under otherwise the cooling 
condition of 140 W per m2K, indicative of dramatic shortening in time for the 
battery to cool down to below 40 °C. Note that a heat transfer coefficient 
of 300 W per m2K is still attainable by strong aspirated air convection. a, Cell 
temperature curves. b, Cell voltage curves. c, Spatial temperature nonuniformity, 
Tmax – Tmin, as a function of time.


--- Page 16 ---

Article
Extended Data Fig. 9 | EIS tests and equivalent circuit for fitting. a, Typical 
shape and interpretation for cell impedance in the complex plane. b, Equivalent 
circuit and the mathematical expression to fit the experimental results. c, EIS 
results and fitting curve for baseline cell under ATM cycling with 3C charging to 
80% SOC. d, EIS results and fitting curve for cell with enhanced ion-transport 
under ATM cycling with 4C charging to 70% SOC. e, EIS results and fitting curve 
for cell with enhanced ion-transport under ATM cycling with 4C charging to 
75% SOC.
