# Degradation of Commercial Lithium-Ion Cells as a Function of Chemistry and Cycling Conditions



--- Page 1 ---

Journal of The
Electrochemical Society
     
OPEN ACCESS
Degradation of Commercial Lithium-Ion Cells as a
Function of Chemistry and Cycling Conditions
To cite this article: Yuliya Preger et al 2020 J. Electrochem. Soc. 167 120532
 
View the article online for updates and enhancements.
You may also like
Bayesian cross-entropy methodology for
optimal design of validation experiments
X Jiang and S Mahadevan
-
Isothermal mass flow measurements in
microfabricated rectangular channels over
a very wide Knudsen range
John M Anderson, Matthew W Moorman,
Jason R Brown et al.
-
ECH pre-ionization and assisted startup in
the fully superconducting KSTAR tokamak
using second harmonic
Y.S. Bae, J.H. Jeong, S.I. Park et al.
-
This content was downloaded from IP address 103.156.242.198 on 05/02/2026 at 13:17


--- Page 2 ---

Degradation of Commercial Lithium-Ion Cells as a Function of
Chemistry and Cycling Conditions
Yuliya Preger,1,*,z
Heather M. Barkholtz,1 Armando Fresquez,2 Daniel L. Campbell,3
Benjamin W. Juba,4 Jessica Romàn-Kustas,4
Summer R. Ferreira,5 and
Babu Chalamala1,*
1Energy Storage Technology and Systems, Sandia National Laboratories, Albuquerque, New Mexico, United States of
America
2Advanced Power Sources R&D, Sandia National Laboratories, Albuquerque, New Mexico, United States of America
3Statistical Sciences, Sandia National Laboratories, Albuquerque, New Mexico, United States of America
4Materials Reliability, Sandia National Laboratories, Albuquerque, New Mexico, United States of America
5Renewable and Distributed Systems Integration, Sandia National Laboratories, Albuquerque, New Mexico, United States of
America
Energy storage systems with Li-ion batteries are increasingly deployed to maintain a robust and resilient grid and facilitate the
integration of renewable energy resources. However, appropriate selection of cells for different applications is difﬁcult due to
limited public data comparing the most commonly used off-the-shelf Li-ion chemistries under the same operating conditions. This
article details a multi-year cycling study of commercial LiFePO4 (LFP), LiNixCoyAl1−x−yO2 (NCA), and LiNixMnyCo1−x−yO2
(NMC) cells, varying the discharge rate, depth of discharge (DOD), and environment temperature. The capacity and discharge
energy retention, as well as the round-trip efﬁciency, were compared. Even when operated within manufacturer speciﬁcations, the
range of cycling conditions had a profound effect on cell degradation, with time to reach 80% capacity varying by thousands of
hours and cycle counts among cells of each chemistry. The degradation of cells in this study was compared to that of similar cells in
previous studies to identify universal trends and to provide a standard deviation for performance. All cycling ﬁles have been made
publicly available at batteryarchive.org, a recently developed repository for visualization and comparison of battery data, to
facilitate future experimental and modeling efforts.
© 2020 The Author(s). Published on behalf of The Electrochemical Society by IOP Publishing Limited. This is an open access
article distributed under the terms of the Creative Commons Attribution Non-Commercial No Derivatives 4.0 License (CC BY-
NC-ND, http://creativecommons.org/licenses/by-nc-nd/4.0/), which permits non-commercial reuse, distribution, and reproduction
in any medium, provided the original work is not changed in any way and is properly cited. For permission for commercial reuse,
please email: permissions@ioppublishing.org. [DOI: 10.1149/1945-7111/abae37]
Manuscript submitted May 27, 2020; revised manuscript received July 30, 2020. Published September 2, 2020. This was paper 605
presented at the Dallas, Texas, Meeting of the Society, May 26–May 30, 2019.
Supplementary material for this article is available online
Energy storage systems (ESS) consisting of Li-ion batteries are
expected to play a critical role in the integration of intermittent renewable
energy resources into the electric grid, as well as to provide back-up
power and enhanced resiliency.1–3 For applications in the electric grid,
ESS are expected to last for a decade or even longer. A typical MWh
system may contain as many as 100,000 cells assembled into packs. To
ensure system safety and reliability, cells must be selected based on
application speciﬁc requirements and performance characteristics. Yet
there are few comparisons of popular commercial cells under similar
operating conditions. In this work, we detail the cycling performance of
commercial LFP (LiFePO4), NCA (LiNixCoyAl1−x−yO2), and NMC
(LiNixMnyCo1−x−yO2) cells with an 18650 form factor, in the broadest
such comparison to be reported in a peer-reviewed publication.
Battery speciﬁcation sheets from manufacturers primarily focus
on safety metrics, such as current, voltage, and temperature bounds,
with limited information on performance metrics. Many publications
in the open literature have examined the long-term performance and
aging of commercial Li-ion cells in order to ﬁll this gap. There are
notable recent studies for each of the chemistries—LFP,4–11
NCA,6,10,12–14 and NMC,6,15–17—under calendar, constant current
square wave cycle, and grid duty cycle aging. However, each of
these studies typically focuses on a single chemistry under a limited
subset of conditions to understand the inﬂuence of a particular
variable, such as temperature, or the emergence of a particular
degradation phenomena, such as Li plating.
The short-term cycling performance18 and calorimetry19 for the
cells selected for the present study has been reported previously, and
this work is part of a broader effort at Sandia National Laboratories
to characterize the safety and reliability of commercial Li-ion cells.
This study examines the inﬂuence of temperature, depth of discharge
(DOD), and discharge current on the long-term degradation of the
commercial cells. Cycling was carried out under constant current
square wave duty cycles rather than grid duty cycles to better
understand the contribution of speciﬁc and simple cycling conditions
to the degradation process. Various metrics for comparing cell
degradation were investigated, including equivalent full cycle count,
discharge energy, and round-trip efﬁciency. The degradation of the
cells in this study was compared to that of similar cells in previous
studies to provide a standard deviation for performance and facilitate
a more data-informed adoption of these batteries.
Experimental Conditions
Tested batteries.—The commercial 18650 cells examined in this
work were manufactured by the following companies: LFP from
A123
Systems
(Part
#APR18650M1A,
1.1
Ah),
NCA
from
Panasonic (Part #NCR18650B, 3.2 Ah), and NMC from LG Chem
(Part #18650HG2, 3 Ah). The three batteries were selected because
they included common electrode formulations and were manufac-
tured by reputable companies. Table I provides additional speciﬁca-
tions for each cell, including the manufacturer-recommended oper-
ating bounds. According to inductively coupled plasma optical
emission spectrometry (ICP-OES), the elemental composition of
the NMC cathode is Ni0.84Mn0.06Co0.1 (a Ni-enriched variant of
NMC811). The NCA cathode is likely Ni0.81Co0.14Al0.05. A descrip-
tion of the ICP-OES procedure is provided below and the raw data is
given in Table SI (available online at stacks.iop.org/JES/167/
120532/mmedia).
ICP-OES.—The elemental composition of the NCA and NMC
cathodes was determined with an Avio 500 ICP-OES (Perkin Elmer)
equipped with a type K1 concentric nebulizer and bafﬂed cyclonic
zE-mail: ypreger@sandia.gov
*Electrochemical Society Member.
Journal of The Electrochemical Society, 2020 167 120532


--- Page 3 ---

spray chamber. The instrument parameters were as follows: RF-
power 1500 W, 15 L-Ar min−1 plasma ﬂow, 0.7 L-Ar min−1
nebulizer ﬂow, and 0.2 L-Ar min−1 auxiliary gas ﬂow. Prior to
analysis, samples of the active material on the Al current collector
were digested using a Mars 6 (CEM Corporation) extraction system.
Microwave digestion was carried out in two steps, with the ﬁrst
consisting of the addition of sulfuric acid (5 ml) to 0.03–0.05 g of
cathode sample in a Teﬂon microwave vessel. Samples were heated
for 0.5 h until they reached a temperature of 260 °C (maximum
microwave power, 1800 W) and held at that temperature for 0.25 h.
Following cooling and depressurization, hydrochloric acid (3 ml)
and nitric acid (3 ml) were added to the Teﬂon vessel and a second
microwave digestion cycle was completed as follows: 0.5 h ramp
to 200 °C (maximum microwave power, 1800 W) followed by a
hold at that temperature for 10 min. Sample digests were then diluted
to 50 ml. These digests were then diluted once more with addition
of an yttrium internal standard. Samples were analyzed along
with standard elemental reference materials (Inorganic Ventures).
The following background-corrected emission lines were chosen
for evaluation due to optimal performance: Li (670.784 nm),
Ni (231.604 nm), Co (228.616 nm), Mn (257.610 nm), and Al
(396.153 nm).
Cycling equipment.—Cycle aging was carried out using an Arbin
SCTS and an Arbin high-precision (Model: LBT21084) multi-
channel battery testing system. Individual cells were placed into
commercially available 18650 battery holders (Memory Protection
Devices). The holders were connected to the Arbin with 18 gauge
wire and the cable lengths kept below eight feet to minimize voltage
drop. During cycling, the cells were placed in SPX Tenney Model
T10C-1.5 environmental chambers, which can be controlled between
−73 °C and 200 °C. A K- or T-type thermocouple was attached to
the skin of each cell under test with Kapton tape to monitor the cell
skin temperature.
Cycle aging protocol.—At the start of the study, the as-received
cells were placed in thermal chambers for a day to equilibrate to the
desired cycling temperatures. Then, the cells were discharged. Each
round of cycling consisted of a capacity check, some number of
cycles at the designated conditions for that cell, and another capacity
check at the end (Scheme 1). The capacity check consisted of three
charge/discharge cycles from 0%–100% SOC at 0.5C (a rate of 1C
corresponds to the current that will discharge the full capacity of a
battery in one hour). 100% SOC is deﬁned as the capacity obtained
at a 0.5C constant current charge with a current taper to 0.05 A to the
maximum manufacturer-speciﬁed charging voltage. The same capa-
city check protocol was employed for all cells in the study.
A round of cycling for each cell varied from 125 to 1000 cycles,
depending on the rate of degradation at the speciﬁc test conditions.
The cycle count for a round was halved if a cell experienced over 5%
capacity loss in the previous round. These adjustments were
intended to offer enough granulation in the capacity decline curve
to enable observation of any changes in mechanism, while still
maintaining a reasonable check-up frequency during a nearly three-
year study. Electrochemical impedance spectroscopy (EIS) was
completed at intervals of approximately 3% capacity loss, and these
results will be expanded upon in a future publication. For the
purpose of this publication, the study was considered complete once
a cell reached 80% of its initial capacity.
Several abort guidelines were built into the cycling program to
avoid potentially abusive conditions for the cells. Cycling was
automatically stopped if the cell charge or discharge voltage was
more than 0.05 V outside of voltage range limits, and if the cell ever
exceeded the manufacturer-speciﬁed temperature.
Study conditions.—Table II illustrates the combinations of
temperatures, DOD, and discharge currents examined in this study.
These values were selected according to a design of experiment
approach in order to cover a broad range of manufacturer-recom-
mended parameter space and to identify the general dependence on
each variable. To ensure repeatability, each test was performed with
at least two cells.
The nominal capacities of the cells were used as references for
calculating C-rates. All cells were charged at a rate of 0.5C, per
manufacturer guidance. Unlike the other cells, NCA cells were not
discharged at 3C since the required current, 9 A, is outside of
manufacturer speciﬁcations. Cells were cycled at 40%–60% SOC
using a constant current (CC) protocol based on capacity limits.
Cells were cycled at 20%–80% SOC with a CC protocol using
voltage limits established from the discharge capacity curves of fresh
cells. Cells cycling at 0%–100% SOC were charged using a constant
current constant voltage (CCCV) protocol, with a current taper to
0.05 A. For the 100% DOD regime, LFP cells were cycled from 2 to
3.6 V, NCA cells from 2.5 to 4.2 V, and NMC cells from 2 to 4.2 V.
The cycling programs were not adjusted over the course of the study
as the cells aged and the SOC labels are based on discharge curves
from the fresh cells.
Results and Discussion
General analysis.—The lifetime performance of a battery
depends on complex physico-chemical processes inﬂuenced by
many operating variables. This study considered the inﬂuence of
three of the variables most readily controlled during operation—
temperature, DOD, and discharge rate. In Figs. 1 and 2, the cells are
compared based on their capacity retention, discharge energy
throughput, and round-trip efﬁciency (RTE), evaluations that are
useful for both laboratory research and ﬁeld implementation.
Figure 1 illustrates the discharge capacity retention vs equivalent
full cycle (EFC) count for all cells in the experimental matrix to
present an overall picture of cycle-induced aging. In this work, one
EFC is based on the nominal capacity of the cell. Therefore, for each
cell, the total capacity throughput was divided by the nominal
capacity to get the total equivalent full cycle count. The LFP cells
exhibit substantially longer cycle life spans under the examined
conditions: 2500 to 9000 EFC vs 250 to 1500 EFC for NCA cells
and 200 to 2500 EFC for NMC cells. Most of the LFP cells had not
reached 80% capacity by the conclusion of this study for the NCA
Table I. Commercial 18650-format lithium-ion battery manufac-
turer-speciﬁed operating bounds.
Battery
LFP
NCA
NMC
Nominal Capacity (Ah)
1.1
3.2
3
Nominal Voltage (V)
3.3
3.6
3.6
Voltage Range (V)
2 to 3.6
2.5 to 4.2
2 to 4.2
Max Discharge Current (A)
30
6
20
Acceptable Temperature (°C)
−30 to 60
0 to 45
−5 to 50
Nominal Mass (g)
39
48.5
47
Scheme 1. Structure of cycle aging study.
Journal of The Electrochemical Society, 2020 167 120532


--- Page 4 ---

and NMC cells, and their longer-term degradation will be reported in
a later work. The spread in the data for each of the chemistries
indicates that even within the manufacturer-speciﬁed operating
bounds there is signiﬁcant dependence on the speciﬁc cycling
conditions. Irrespective of the testing conditions, all cells exhibited
primarily linear degradation behavior, with slightly more rapid fade
at the beginning and end of cycling. This behavior is in agreement
with previous models of lithium-ion battery degradation which
propose three phases of capacity fade20,21:
Phase 1: Sudden drop in capacity as Li is consumed during SEI
formation
Phase 2: Linear degradation, generally associated with loss of Li
inventory in side reactions
Phase 3: Rapid capacity fade as the cell fails, often attributed to
an impedance increase
Figure 2a indicates the EFC for each cell to reach 80% capacity
under the given cycling conditions. Though cells may be used
beyond 80% capacity in grid applications, this value is a useful
benchmark as it is often the reference used by manufacturers in
speciﬁcation sheets to indicate end of life. For LFP cells that have
not yet reached 80% capacity, the lifetime was extrapolated based on
the present (linear) degradation rate. Among the three chemistries,
there is no universal dependence on temperature, DOD, or discharge
rate. A more systematic analysis of variable dependence is presented
below.
Though EFC is typically the metric by which batteries are
compared, cumulative discharge energy may offer more value for
ﬁeld implementation. The EFC may mask degradation differences
arising in batteries with different capacity and voltage ranges.
Figure 2b indicates the cumulative discharge energy for a cell under
each set of cycling conditions at 80% capacity retention. This value
was calculated by summing the energy from each individual
discharge of the cell. The performance differences between the
three chemistries were minimized once the analysis factored in the
lower capacity and voltage of the LFP cells (see Table I).
Round-trip efﬁciency, another important metric for technoeco-
nomic evaluation of LiBs, is shown in Fig. 2c.22 The RTE for a cycle
was calculated by dividing the discharge energy by the charge
energy. A single RTE is often assumed for economic evaluations;
however, RTE depends substantially on the cycling conditions,
including the charge/discharge rate, temperature, SOC, and rest time.
The LFP cells show higher RTEs than NCA and NMC cells at all
conditions, though the differences are minimized at lower discharge
rates. The NCA cells exhibited particular sensitivity to higher
discharge rates, with RTEs dropping 5%–10% for an increase in
discharge rate from 1C to 2C at all temperatures. The decrease in
RTE across all cycling conditions as the cells reach 80% capacity is
attributed to the increase in cell resistance as the SEI layer grows.
Capacity fade dependence on cycling variables.— Temperature
dependence.—Figures 3a–3c show a subset of cycling conditions for
each chemistry where only the oven temperature was varied
(additional plots in Fig. S1). The capacity fade rate increased with
increasing temperature for LFP cells but decreased for NMC cells.
The NCA cells did not exhibit a strong temperature dependence in
the examined range. Different temperature dependences suggest
different dominant degradation mechanisms. Though not observed in
this study, the transition between degradation mechanisms within a
single cell was previously documented by Waldmann et al.23 An
Arrhenius plot from their work on 18650 NMC/LMO-graphite cells
is reproduced in Fig. 4. Below 25 °C, the dominant aging mechanism
was Li plating, conﬁrmed by observation of metallic Li. Deposition
of Li onto the graphite anode can occur in parallel to intercalation
when the anode potential drops below 0 V vs Li/Li+ (promoted by
factors such as increasing SOC, increasing charge rate, and lower
temperature).24 Above 25 °C, the dominant mechanism was SEI
(solid-electrolyte interphase) growth, conﬁrmed by post-mortem
characterization of SEI thickness on the anodes and correlated to
resistance increases in the whole cells. The SEI is formed from the
decomposition products of electrolyte solvent and Li salt, a reaction
accelerated by increasing temperature.25 Previous studies of tem-
perature dependence may not have observed the transition between
the two degradation mechanisms in the same cell because they did
not consider a sufﬁciently broad temperature range.
The capacity fade data for NMC and LFP cells from the present
study was ﬁt in the linear region (after the initial period of rapid
capacity fade) to obtain aging rates as a function of temperature.
Comparison to the previously reported NMC-LMO data indicates
that the tipping point between different mechanisms (the point of
minimal degradation in Fig. 4) varies substantially with the
chemistry (Table III). For example, previous reports on cycle aging
of LFP cells indicate a tipping point at temperatures of 5 °C–10 °C,
with degradation rates increasing both above and below this
temperature.26 Studies of LFP cells that considered temperatures
only above 20 °C observed the capacity fade increase with
increasing temperature (consistent with the present work).27–29
Studies of NMC cells consistently indicate a tipping point around
35 °C. One report found that minimal capacity fade for NMC cells in
cycle aging followed 35 °C > 50 °C > 25 °C16 and several others
found a lower capacity fade rate at 45 °C than 20 °C.17,30 In contrast
to LFP and NMC cells, the NCA cells did not exhibit a strong
temperature dependence in the range of 15 °C to 35 °C (Fig. 3c).
Table II. Test matrix for all chemistriesa).
DOD, Temperature, Discharge Rateb)
40%–60%, 25 °C, 0.5C
0%–100%, 15 °C, 1C
0%–100%, 15 °C, 2C
40%–60%, 25 °C, 3C
20%–80%, 25 °C, 0.5C
0%–100%, 25 °C, 1C
0%–100%, 25 °C, 2C
20%–80%, 25 °C, 3C
0%–100%, 25 °C, 0.5C
0%–100%, 35 °C, 1C
0%–100%, 35 °C, 2C
0%–100%, 25 °C, 3C
a) The cycling conditions noted in the test matrix were applied to LFP and NMC cells. NCA cells were not subjected to any cycling conditions that included a
3C discharge rate, which is outside of the manufacturer-speciﬁed current limits for that cell. b) All cells were charged at a rate of 0.5C.
Figure 1. Discharge capacity retention for all LFP (blue), NMC (black), and
NCA (red) cells relative to the initial capacity of each individual cell. Circles
are data points from the capacity check at the conclusion of each round of
cycling and lines are a guide to the eye.
Journal of The Electrochemical Society, 2020 167 120532


--- Page 5 ---

This behavior is consistent with a previous publication wherein the
capacity fade rate of commercial NCA cells increased below 25 °C
(due to Li plating) but did not vary signiﬁcantly between 25 °C and
60 °C.12 The study did not incorporate materials characterization to
explain this lack of temperature dependence, although the authors
proposed that the manufacturer had optimized the cell for high
Figure 2. (a) Equivalent full cycle (EFC)
count at 80% capacity for all cells and cycling
conditions. Each bar represents the average
EFC for all cells cycled at that condition. The
values for individual cells are noted with a
“+”. If a bar does not include values for
individual cells, then those cells have not yet
reached 80% capacity and the indicated EFC
is extrapolated based on the present degrada-
tion rate for those cells. (b) Cumulative
discharge energy at 80% capacity for all cells
and cycling conditions. Each bar represents
the average discharge energy for all cells
cycled at that condition. (c) Round-trip efﬁ-
ciency (RTE) for all cells and cycling condi-
tions. Each bar represents the average initial
RTE for all cells cycled at that condition. The
RTE at the end of the study is indicated with a
dot. If a bar does not include a dot, then those
cells have not yet reached 80% capacity.
Journal of The Electrochemical Society, 2020 167 120532


--- Page 6 ---

temperature operation. A more recent study of comparable NCA
cells identiﬁed slightly higher degradation at 25 °C than 60 °C.31
While the tipping point temperature will certainly be inﬂuenced
by other cycling conditions, the 30 °C gap in preferred conditions for
LFP and NMC cells has implications for best practices in battery
thermal management as well as the development of accurate
degradation models. Many models assume optimal performance at
25 °C with higher temperatures only accelerating SEI formation. It
should be noted that the above analysis only applies to cycle aging
studies. For calendar aging studies across LFP,6,9 NCA,6 and
NMC6,15 cells, capacity fade consistently decreased with decreasing
temperature. Li plating can occur only during charging; thus, SEI
growth is the dominant degradation mechanism during calendar
aging, with increasing temperatures accelerating the reaction of
electrolyte solvent and Li salt.
Depth of discharge dependence.—For all cells in this study, the
rate of capacity fade increased with an increasing depth of discharge
(Figs. 3d–3f). Greater volume change in the graphite during (de)
intercalation increases stress and microcracks.17,43 Newly-formed
cracks enable further reaction between the electrolyte and Li, leading
to more SEI formation, loss of Li inventory, and capacity fade. Some
studies have shown that only the width of the voltage window
matters.35 In others, the speciﬁc placement of the voltage window
was signiﬁcant, a phenomenon variously attributed to:
(1)
transition between graphite stages (at speciﬁc voltages) with
differing
lattice
parameters
enhancing
cracking
and
SEI
formation,15 or
(2)
slow Li diffusion at particular voltages leading to Li build-up
and graphite particle fracturing36
The results of the present study cannot be used to address this
discrepancy as the mid-point of the depth of discharge window was
not varied.
Compared to LFP7,33,34 cells, the NCA35–37 and NMC15,17,38,39
cells experienced a more dramatic transition in capacity fade from
partial to complete DOD and this result is consistent with previous
studies. This transition could be attributed to the metal oxide
cathodes’ higher operating voltages (100% SOC corresponds to
4.2 V for NCA and NMC vs 3.6 V for LFP), which could promote
electrolyte oxidation.44,45 A separate study of LFP cathode half cells
charged to different voltages (with an electrolyte of 1 M LiPF6 in
EC:DEC 1:1 weight ratio) showed optimal performance at 3.9 V vs
Li/Li+, with no difference in long-term cycling degradation between
Figure 3. Discharge capacity fade as a function of (a)–(c) temperature, (d)–(f) DOD, and (g)–(i) discharge rate for all chemistries. For each plot, all conditions
other than the variable of interest were unchanged. Symbols are data points from the capacity check at the conclusion of each round of cycling and lines are a
guide to the eye. (a)–(c) are at 1C discharge and 0%–100% SOC. (d)–(f) are at 0.5C discharge and 25 °C. (g)–(i) are at 0%–100% SOC and 25 °C. Note the
different endpoints on the x-axes.
Figure 4. Arrhenius plot for the capacity fade rate of cells. The solid lines
correspond to linear ﬁts of the data. Black corresponds to data from
Waldmann et al.23 on 18650 NMC-LMO cells cycled at 1C in a temperature
range of −20 °C to 70 °C. Data from the present study for cells cycled at
0%–100% SOC with a 1C discharge rate is shown in red for NMC cells and
blue for LFP cells.
Journal of The Electrochemical Society, 2020 167 120532


--- Page 7 ---

maximum voltages of 3.6 and 4.2 V.46 These results suggest that the
electrochemical cycling behavior of LFP cathodes charged with
different upper voltage limits merits further exploration, as the
results could vary with the cell manufacturing and electrolyte
composition. Irrespective of chemistry, in calendar aging studies,
capacity fade consistently increased with SOC, as lower anode
potentials enhance electrolyte reduction and Li incorporation into the
growing SEI. As in cycle aging studies, NCA and NMC cells
exhibited particularly rapid capacity fade at 100% SOC.6
Discharge rate dependence.—Higher discharge rates are ex-
pected to accelerate capacity fade due to increased stress on the
electrodes from rapid volume change.32,40,41 In Figs. 3g–3h, the
discharge rate dependence for NMC and LFP cells appears low.
However, for NCA cells, capacity fade decreased with increasing
discharge rate (Fig. 3i). Wei et al. observed the same trend and
attributed it to increased impedance for cells cycled at lower
discharge rates (a physical explanation for this phenomenon was not
offered).42 It is possible that the higher discharge rate may increase
cell self-heating (Table SII), leading to improved performance; but,
the NCA cells did not exhibit a particularly strong temperature
dependence. It is also possible that the shorter period of cycling
needed to complete discharge (1 h for 1C vs 0.5 h for 2C) can
minimize the degree of calendar aging over the course of hundreds
of cycles. Figure S2 shows the capacity fade with respect to time
spent cycling rather than EFC and the gap between cells at different
discharge rates is slightly reduced. It is unclear why the NCA cells
are more strongly inﬂuenced by the discharge rate than the other
chemistries.
Analysis of variance.—The cycling data was further examined by
analysis of variance (ANOVA) to more precisely quantify which
conditions contribute to degradation. This also enabled consideration
of all cells at once, unlike the variable dependence in previous
sections, which only considered systematic variation of single
variables. The output variable of interest, % initial capacity, had
been measured at different cycle counts across the separate experi-
ments. Therefore, to enable comparison of % capacity at a speciﬁc
EFC with respect to the factors of interest, regression ﬁts of %
capacity vs EFC data were performed for all cells. Occasionally,
linear or quadratic ﬁts were used, but in most cases a cubic ﬁt was
best. Interpolation was completed only within the range of real data
values. General linear models were ﬁt and ANOVA was performed
at 200 EFC (before most of the NCA and NMC cells had reached
Table III. Summary of studies examining temperature, depth of discharge, and discharge rate dependence in commercial cells (cylindrical format,
unless otherwise noted).
Chemistry
Reference
Other Conditionsa)
Performanceb)
Temperature (°C)
27
0%–100%, 1C/1C
25 > 40 > 50 > 60
28
0%–100%, 1C/3C
25 > 55
LFP
32c)
0%–100%, 1C/1C
5 > −5 > 12 > −20 > 30
29c)
2.2–3.65V, 1C/1C
25 ∼35 > 45 > 55 > 65
this work
0%–100%, 0.5C/1C
15 > 25 > 35
12
0%–100%, 0.5C/0.5C
25 ∼30 ∼40 ∼50 ∼60 > 20 > 15 > 5 > 0
NCA
31
2.5–4.2 V, 0.64C/0.64C
60 > 25
this work
0%–100%, 0.5C/1C
15 ∼25 ∼35
23
0%–100%, 1C/1C
25 > 50 > 60 > 70 ∼0 > −10 > −20
16
3.0–4.2 V, 0.5C/1C
35 > 50 > 25
NMC
30
2.75–4.2 V, 1C/1C
45 > 20
17
various
45 > 20
this work
0%–100%, 0.5C/1C
35 > 25 > 15
Depth of Discharge (% or V)
33
60 °C, 0.5C/0.5C
45–55 ∼40–60 ∼25–75 ∼10–90 ∼5–95
34
30 °C, 1C/1C
47.5–52.5 > 20–80 ∼0–100 > 45–55 > 35–65 ∼25–75
LFP
7
40 °C, 1C/1C
45–55 ∼25–75 ∼0–100
this work
25 °C, 0.5C/1C
40–60 > 20–80 ∼0–100
35
25 °C, 1C/1C
0–60 ∼10–70 ∼40–100 > 0–100
NCA
36c,d)
40 °C, 0.5C/0.5C
3.4–4.0 > 3.0–4.0 > 3.0–4.1 > 3.6–4.2 > 3.4–4.2 > 3.0–4.2 > 3.0–4.3
37
30 °C, 0.3C/1C
40–60 > 25–75 ∼10–90 > 0–100
this work
25 °C, 0.5C/1C
40–60 > 20–80 > 0–100
17
20 °C, 1C/1C
37.5–62.5 > 0–100 > 25–75 > 10–90 > 20–80 ∼5–95
15
35 °C, 1C/1C
47.5–52.5 > 45–55 > 40–60 > 25–75 > 10–90 ∼0–100
NMC
38d)
25/35/45 °C, 0.33C/1C
40–60 ∼32.5–67.5 ∼25–75 > 17.5–82.5 > 10–90 > 0–100
39d)
25 °C, 6C/6C
0–20 > 20–40 ∼40–60 ∼60–80 > 80–100 > 0–100
this work
25 °C, 0.5C/1C
40–60 > 20–80 > 0–100
Discharge Rate (C-rate)
40
25 °C, 0%–100%, 0.5C
0.04C > 0.2C ∼0.5C > C > 2C
LFP
41d)
25 °C, 2.5–3.7 V, 0.5C
0.2C > 1C > 2C > 3C > 4C > 5C
this work
15/25/35 °C, 0%–100%, 0.5C
0.5C ∼1C ∼2C > 3C
NCA
42
25 °C, 2.5–4.2 V, 0.5C
2C > 1.5C
this work
15/25/35 °C, 0%–100%, 0.5C
2C > 1C > 0.5C
17
0%–100%, 1C
1C > 2C at 20 °C; 1C ∼2C at 45 °C
NMC
38d)
35 °C, 10%–90%, 0.33C
0.33C ∼1C ∼2C
32
22 °C, 2.75–4.2 V, 0.5C
1C > 3C
this work
15/25/35 °C, 0%–100%, 0.5C
no systematic dependence
a) Cycling conditions held constant listed in the order of: temperature, depth of discharge given as SOC or voltage range, and charge/discharge rate. b) Better
performance corresponds to a lower degradation rate. c) Non-commercial. d) Pouch or prismatic format.
Journal of The Electrochemical Society, 2020 167 120532


--- Page 8 ---

80% capacity). Three of the four individual factors (cell chemistry,
discharge rate, and SOC range) were found to be signiﬁcant in
explaining variability in % capacity. The p values from ANOVA
(Table SIII) are below the chosen signiﬁcance level of 0.05.
Additionally, there was a signiﬁcant interaction between cell
chemistry and SOC range, and cell chemistry and temperature.
Residual plots (Fig. S3) from this model ﬁt show that the assump-
tions of randomness, constant variance, and normally distributed
residuals are all reasonable. In addition, no concerning patterns are
seen.
Figure 5 shows the main effects and interactions plot for all four
factors at 200 EFC, demonstrating the importance of not drawing
general conclusions about variable dependence for different chemis-
tries. Across all of the tested cells, the % capacity does not change
systematically across discharge rate and temperature (Figs. 5b, 5d).
Cell chemistry and SOC range have larger effects across their
respective levels (Figs. 5a, 5c). For example, at the same EFC, LFP
cells have retained on average 7% more capacity than NCA cells and
9% more capacity than NMC cells. Several factors are involved in
signiﬁcant interactions with each other. Figure 5f shows that the
SOC range affects % capacity for the NCA and NMC cells similarly
(5%–10% lower at 0%–100%), but SOC range has little effect on the
capacity for LFP cells. Additionally, temperature affects % capacity
for NMC and LFP cells in opposing trends (Fig. 5g). The NMC cells
likely exhibit a less systematic trend between 15 and 35 °C because
this analysis factors in all of the cells at 25 °C cycled at intermediate
SOCs, while Figs. 3b and 4 focused exclusively on the inﬂuence of
temperature.
Consistency of literature cycling data.—Battery degradation
models and conclusions about the performance of particular che-
mistries are often based on a single data set. To probe the validity of
this approach, the degradation of the cells in this study was
compared to that of similar commercial 18650 cells examined in
previous studies. Figure 6 shows a subset of these comparisons and
the rest are given in Fig. S4. Degradation data for cells from the
same manufacturer appears consistent across publications, even
those separated by several years (Figs. 6b, 6c). However, for cells
from different manufacturers sometimes the degradation rate is the
same (Fig. 6e) and sometimes it is not (over three times difference in
cycle count to 80% capacity in Fig. 6f). These differences suggest
that lifetime prognostics based on a particular cell from a particular
manufacturer cannot be broadly extrapolated, even to other cells
with the same standard form factor, chemistry, and capacity. Subtle
variations in materials, such as electrolyte composition, can
substantially impact battery lifetime (though that level of detail
would not be available on a basic battery speciﬁcation sheet).
Empirical battery degradation models would beneﬁt from the
incorporation of larger data sets and reporting values with a standard
deviation to give users a better sense of the true lifetime of these
cells. However, the analysis above, particularly the comparison in
Table III, shows that even though precise lifetimes may differ,
variable dependence trends are broadly consistent within a particular
chemistry.
Conclusions
Commercial Li-ion batteries based on NMC, NCA, and LFP
chemistries were cycled with varying temperature, depth of dis-
charge, and discharge rate. The capacity and discharge energy
retention, as well as the round-trip efﬁciency, were compared. The
dependence on each cycling variable was analyzed qualitatively as
well as by analysis of variance. Key insights from this work include:
(1)
Even within manufacturer speciﬁed operating ranges, the
equivalent full cycle count at 80% capacity varied up to
thousands of cycles depending on the conditions.
(2)
LFP cells had the highest cycle lifetime across all conditions,
but this performance gap was reduced when cells were
compared according to the discharge energy throughput. The
latter metric factored in the lower capacity and lower voltage of
the LFP cells, illustrating the importance of identifying the
appropriate metrics for each application.
(3)
The RTE can vary up to 10% among fresh cells depending on the
cycling conditions and can decrease over 5% as a cell ages. LFP
cells generally had higher RTEs at all conditions and for all cells,
RTE consistently decreased with increasing discharge rate.
(4)
Based on the current work and a review of previous commercial
cell studies, trends in temperature, depth of discharge, and
discharge rate dependence are chemistry speciﬁc. Variable
dependence in one chemistry should not be broadly extrapolated
to all lithium-ion batteries.
(5)
In the 15 °C to 35 °C temperature range, the capacity fade rate
increased with increasing temperature for LFP cells but de-
creased for NMC cells, indicating different dominant degrada-
tion mechanisms. These results illustrate the value of varying
multiple temperatures within a normal operating range rather
than looking solely at extreme temperatures. The gap in
preferred conditions for LFP and NMC cells has implications
for battery thermal management. A survey of the literature and
Figure 5. Main effects (a)–(d) and interactions (e)–(g) plots for model ﬁt at 200 EFC. Mean % capacity refers to the average value for all cells at the speciﬁed
conditions at 200 EFC. This value is derived from regression ﬁts of the % initial capacity vs EFC data shown earlier since the % initial capacity of all cells had
been measured at slightly different cycle counts across the separate experiments.
Journal of The Electrochemical Society, 2020 167 120532


--- Page 9 ---

the results here suggest that LFP cells are more suited for lower
temperature applications.
(6)
The NMC and NCA cells exhibited a stronger dependence on
depth of discharge, with greater sensitivity to full SOC range
cycling than LFP cells.
(7)
Battery degradation models would beneﬁt from the incorpora-
tion of larger data sets and reporting values with a standard
deviation. Most models are evaluated against a single experi-
mental data set, but a comparison of the degradation data in this
study to previous commercial cell cycling studies shows the
variation possible even under the same conditions.
Future work will include combining electrochemical and mate-
rials characterization to identify the origin of the varying lifetimes
observed in this study. A subset of the cells will be cycled beyond
80% capacity to identify the causes and early warning signs of
transition from linear degradation to rapid capacity fade.
One of the primary difﬁculties in completing this analysis lay in
comparing the data to previous published results, which were
typically reported as plots rather than raw data. Thus, batteryarc-
hive.org was created as a searchable repository for easy visualiza-
tion, analysis, and comparison of battery data across institutions. All
cycling ﬁles from the present study have been uploaded to this site
and we are currently working with other groups with large data sets
to share them here. This aggregation of data sets is intended to
facilitate future experimental and modeling efforts.
Acknowledgments
This work was supported by the US Department of Energy Ofﬁce
of Electricity, Energy Storage Program. The authors wish to thank Dr.
Imre Gyuk for his support of research advancing safety and reliability
in stationary energy storage. We would like to thank Dr. Valerio de
Angelis for his substantial efforts in developing batteryarchive.org and
the CUNY Energy Institute, part of the City College of New York, for
providing site access. We are also grateful to Drs. Daniel Wesolowski,
Reed Wittman, and Loraine Torres-Castro for thoughtful feedback on
the manuscript. Sandia National Laboratories is a multi-mission
laboratory managed and operated by National Technology and
Engineering Solutions of Sandia, LLC., a wholly owned subsidiary
of Honeywell International, Inc., for the U.S. Department of Energy’s
National Nuclear Security Administration under contract DE-NA-
0003525. This paper describes objective technical results and analysis.
Any subjective views or opinions that might be expressed in the paper
do not necessarily represent the views of the U.S. Department of
Energy or the United States Government.
Figure 6. Comparison of battery cycling capacity fade across studies. The chemistry and cycling conditions, given as DOD, temperature, and charge/discharge
rate, are noted for each plot. For each data set, the year of publication, cell manufacturer, cell capacity, and number of cells cycled under the speciﬁed conditions
are noted (when provided in the original publication). “NA” indicates that the speciﬁed information was not available. The lines are a guide to the eye and error
bars are based on standard deviation when data for multiple cells was available. All references to previous studies were presented in Table III except for Hayashi
et al. 201447 in (c) and Paul et al. 201848 in (f).
Journal of The Electrochemical Society, 2020 167 120532


--- Page 10 ---

Author contributions
H.M.B. and S.R.F. designed the original study. A.F. and Y.P.
executed the cycling experiments, and J. R.-K. and B.W. Juba
completed ICP. Y.P. carried out the general data analysis and wrote
the paper, with D.L.C. contributing to the statistical analysis. All
authors participated in discussion of the results, as well as the
preparation of the paper.
ORCID
Yuliya Preger
https://orcid.org/0000-0001-8558-2529
Jessica Romàn-Kustas
https://orcid.org/0000-0003-1879-0234
Babu Chalamala
https://orcid.org/0000-0003-0469-636X
References
1. B. Diouf and R. Pode, Renew. Energy, 76, 375 (2015).
2. T. M. Gür, Energy Environ. Sci., 11, 2696 (2018).
3. DOE Global Energy Storage Database, https://sandia.gov/ess-ssl/global-energy-
storage-database/ (accessed on 16th August 2020).
4. M. Dubarry and B. Y. Liaw, J. Power Sources, 194, 541 (2009).
5. M. Kassem, J. Bernard, R. Revel, S. Pélissier, F. Duclaud, and C. Delacourt,
J. Power Sources, 208, 296 (2012).
6. P. Keil, S. F. Schuster, J. Wilhelm, J. Travi, A. Hauser, R. C. Karl, and A. Jossen,
J. Electrochem. Soc., 163, A1872 (2016).
7. M. Lewerenz, J. Münnix, J. Schmalstieg, S. Käbitz, M. Knips, and D. U. Sauer,
J. Power Sources, 345, 254 (2017).
8. S. Sun, T. Guan, P. Zuo, Y. Gao, X. Cheng, C. Du, and G. Yin, ChemElectroChem,
5, 2301 (2018).
9. M. Naumann, M. Schimpe, P. Keil, H. C. Hesse, and A. Jossen, J. Energy Storage,
17, 153 (2018).
10. A. J. Crawford, Q. Huang, M. C. W. Kintner-Meyer, J.-G. Zhang, D. M. Reed,
V. L. Sprenkle, V. V. Viswanathan, and D. Choi, J. Power Sources, 380, 185 (2018).
11. K. A. Severson et al., Nat. Energy, 4, 383 (2019).
12. T. Waldmann, M. Kasper, and M. Wohlfahrt-Mehrens, Electrochim. Acta, 178, 525
(2015).
13. P. Keil and A. Jossen, J. Electrochem. Soc., 164, A6066 (2017).
14. M. Dubarry, A. Devie, and K. McKenzie, J. Power Sources, 358, 39 (2017).
15. M. Ecker, N. Nieto, S. Käbitz, J. Schmalstieg, H. Blanke, A. Warnecke, and
D. U. Sauer, J. Power Sources, 248, 839 (2014).
16. S. F. Schuster, T. Bach, E. Fleder, J. Müller, M. Brand, G. Sextl, and A. Jossen,
J. Energy Storage, 1, 44 (2015).
17. A. Maheshwari, M. Heck, and M. Santarelli, Electrochim. Acta, 273, 335 (2018).
18. H. M. Barkholtz, A. Fresquez, B. R. Chalamala, and S. R. Ferreira, J. Electrochem.
Soc., 164, A2697 (2017).
19. H. M. Barkholtz, Y. Preger, S. Ivanov, J. Langendorf, L. Torres-Castro, J. Lamb,
B. Chalamala, and S. R. Ferreira, J. Power Sources, 435, 226777 (2019).
20. R. Spotnitz, J. Power Sources, 113, 72 (2003).
21. X.-G. Yang, Y. Leng, G. Zhang, S. Ge, and C.-Y. Wang, J. Power Sources, 360, 28
(2017).
22. K. Mongird, V. Viswanathan, P. Balducci, J. Alam, V. Fotedar, V. Koritarov, and
B. Hadjerioua, Energy Storage Technology and Cost Characterization Report,
Paciﬁc Northwest National Laboratory (2019), https://doi.org/10.2172/1573487.
23. T. Waldmann, M. Wilka, M. Kasper, M. Fleischhammer, and M. Wohlfahrt-
Mehrens, J. Power Sources, 262, 129 (2014).
24. T. Waldmann, B.-I. Hogg, and M. Wohlfahrt-Mehrens, J. Power Sources, 384, 107
(2018).
25. S. J. An, J. Li, C. Daniel, D. Mohanty, S. Nagpure, and D. L. Wood III, Carbon,
105, 52 (2016).
26. V. Ruiz, A. Kriston, I. Adanouj, M. Destro, D. Fontana, and A. Pfrang,
Electrochim. Acta, 240, 495 (2017).
27. L. Tan, L. Zhang, Q. Sun, M. Shen, Q. Qu, and H. Zheng, Electrochim. Acta, 111,
802 (2013).
28. H. Song, Z. Cao, X. Chen, H. Lu, M. Jia, Z. Zhang, Y. Lai, J. Li, and Y. Liu,
J. Solid State Electrochem., 17, 599 (2013).
29. S. Yi, B. Wang, Z. Chen, R. Wang, and D. Wang, Ionics, 25, 2139 (2019).
30. A. Friesen, X. Mönnighoff, M. Börner, J. Haetge, F. M. Schappacher, and
M. Winter, J. Power Sources, 342, 88 (2017).
31. H. Wang, S. Frisco, E. Gottlieb, R. Yuan, and J. F. Whitacre, J. Power Sources,
426, 67 (2019).
32. T. S. Bryden, A. Holland, G. Hilton, B. Dimitrov, C. Ponce de León Albarrán, and
A. Cruden, Energy Procedia, 151, 194 (2018).
33. J. Wang, P. Liu, J. Hicks-Garner, E. Sherman, S. Soukiazian, M. Verbrugge,
H. Tataria, J. Musser, and P. Finamore, J. Power Sources, 196, 3942 (2011).
34. E. Sarasketa-Zabala, I. Gandiaga, E. Martinez-Laserna, L. M. Rodriguez-Martinez,
and I. Villarreal, J. Power Sources, 275, 573 (2015).
35. S. Watanabe, M. Kinoshita, T. Hosokawa, K. Morigaki, and K. Nakura, J. Power
Sources, 260, 50 (2014).
36. J. Li, J. Harlow, N. Stakheiko, N. Zhang, J. Paulsen, and J. Dahn, J. Electrochem.
Soc., 165, A2682 (2018).
37. Y. Zhang, R. Xiong, H. He, X. Qu, and M. Pecht, Appl. Energy, 255, 113818
(2019).
38. J. de Hoog, J.-M. Timmermans, D. Ioan-Stroe, M. Swierczynski, J. Jaguemont,
S. Goutam, N. Omar, J. Van Mierlo, and P. Van Den Bossche, Appl. Energy, 200,
47 (2017).
39. Y. Gao, J. Jiang, C. Zhang, W. Zhang, and Y. Jiang, J. Power Sources, 400, 641
(2018).
40. M. Dubarry, C. Truchot, and B. Y. Liaw, J. Power Sources, 258, 408 (2014).
41. S. Sun, T. Guan, X. Cheng, P. Zuo, Y. Gao, C. Du, and G. Yin, RSC Adv., 8, 25695
(2018).
42. D. Cui, J. Wang, A. Sun, H. Song, and W. Wei, Scanning, 2593780 (2018), https://
www.hindawi.com/journals/scanning/2018/2593780/.
43. H. Zheng, L. Tan, L. Zhang, Q. Qu, Z. Wan, Y. Wang, M. Shen, and H. Zheng,
Electrochim. Acta, 173, 323 (2015).
44. A. S. Mussa, M. Klett, M. Behm, G. Lindbergh, and R. W. Lindström, J. Energy
Storage, 13, 325 (2017).
45. B. Lunz, Z. Yan, J. B. Gerschler, and D. U. Sauer, Energy Policy, 46, 511
(2012).
46. H. Zheng, L. Chai, X. Song, and V. Battaglia, Electrochim. Acta, 62, 256 (2012).
47. T. Hayashi, J. Okada, E. Toda, R. Kuzuo, N. Oshimura, N. Kuwata, and
J. Kawamura, J. Electrochem. Soc., 161, A1007 (2014).
48. N. Paul, J. Keil, F. M. Kindermann, S. Schebesta, O. Dolotko, M. J. Mühlbauer,
L. Kraft, S. V. Erhard, A. Jossen, and R. Gilles, J. Energy Storage, 17, 383 (2018).
Journal of The Electrochemical Society, 2020 167 120532
