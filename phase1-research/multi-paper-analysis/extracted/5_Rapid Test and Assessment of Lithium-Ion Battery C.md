# Rapid Test and Assessment of Lithium-Ion Battery Cycle Life Based on Transfer Learning



--- Page 1 ---

IEEE TRANSACTIONS ON TRANSPORTATION ELECTRIFICATION, VOL. 10, NO. 4, DECEMBER 2024
9133
Rapid Test and Assessment of Lithium-Ion Battery
Cycle Life Based on Transfer Learning
Yuhao Zhu , Xin Gu , Kailong Liu , Senior Member, IEEE, Wenyuan Zhao,
and Yunlong Shang , Member, IEEE
Abstract— The cycle life test provides crucial support for
using and maintenance of lithium-ion batteries (LIBs). The
mainstream way to obtain the battery life is uninterrupted
charge–discharge testing, which usually takes one year or even
longer and hinders the industry development. How to rapidly
assess the life of new battery is a challenging task. To solve this
problem, a rapid life test method is proposed in this article,
which replaces the continuous test with prediction to suit for
different types of battery. This approach unites feature-based
transfer learning (TL) and prediction for the first time in life
assessment. The similarities and joint characteristics between
different types of batteries can be learned in feature-based TL,
which includes charge/discharge protocol and degradation trend.
The fine-tuning operation is avoided compared with traditional
TL to make life assessment more effective with less effort, which
can ensure the interpretability and generalization. The battery
internal characteristics are contained in these features, which
are extracted from charge–discharge data. Hence, the prediction
accuracy is not affected by the capacity regeneration and cliff
drop. To prove the validity, hundreds of thousands of samples
are collected and utilized from 139 LIB cells produced by four
different manufacturers. Experimental results show that the life
test speed is increased by eight times at least compared with
the mainstream method. The error is less than 8.7% using the
first 100 cycles to predict life with 3000 cycles. By calculation,
653-kW·h electricity is saved, and 651-kg carbon dioxide emission
is reduced in each test. The proposed method is promising for
rapid battery cycle life acquisition under various applications,
such as electric vehicles (EVs) and energy storage services (ESS).
Index Terms— Battery life test, end of life prediction, feature
extraction, lithium-ion batteries (LIBs), transfer learning (TL).
I. INTRODUCTION
L
ITHIUM-ION
batteries
(LIBs)
have
been
widely
deployed in electric vehicles (EVs) and energy storage
services (ESS) [1], [2]. Owing to the irreversible chemical
reactions, the battery capacity will gradually deteriorate in
actual continuous charging and discharging. The cycle life is
defined as the number of charge–discharge cycles when the
available capacity of a battery degrades to 80% of the initial
Manuscript received 14 September 2023; revised 6 December 2023;
accepted 7 January 2024. Date of publication 15 January 2024; date of
current version 27 December 2024. This work was supported in part by the
National Natural Science Foundation of China under Grant 62122041, Grant
62173211, Grant 62333013, and Grant 62373224, and in part by the Natural
Science Foundation of Shandong Province, China, under Grant ZR2021JQ25.
(Corresponding author: Yunlong Shang.)
The
authors
are
with
the
School
of
Control
Science
and
Engineering,
Shandong
University,
Jinan
250061,
China
(e-mail:
yuhao_zhu@mail.sdu.edu.cn; xgu1996@mail.sdu.edu.cn; kliu02@qub.ac.uk;
zhaowenyuan@mail.sdu.edu.cn; yshang@sdu.edu.cn).
Digital Object Identifier 10.1109/TTE.2024.3354107
value [3], [4]. According to the international electrotechnical
commission (IEC) test standards, such as IEC 61951-1:2017,
the battery cycle life is obtained by continuous charge and
discharge, as shown in Fig. 1(a). In fact, the charge–discharge
cycles can reach thousands or even more than 10 000 times,
leading to a long test time and high cost [5]. For example,
a lithium iron phosphate (LFP) battery with capacity of 2 Ah
can cycle up to 6000 times. With 1C-rate as standard, 2 h
are taken in one complete charge–discharge cycle. Hence,
it takes about one and a half years for fully testing and
costs about 3600 RMB in electricity charge. It seriously
restricts the rapid and high-quality development of the battery
industry [6], [7].
The key to solve the above problem is to replace con-
tinuous testing with accurate prediction, which is also the
main research purpose in this article. If the life can be
predicted by using the early dozens or 100 cycles, about
95% of test cost can be saved. However, the life rapid test
and assessment is essentially different from the traditional life
prediction. For the traditional life prediction in the previous
studies, a large amount of data similar to that of the battery
under test are available, which can be used to train the
prediction model. To guarantee the accuracy and rationality,
the used training data generally must exceed 50% of the total
data [8], [9], [10]. Meanwhile, the prediction is based on
recursive mode, which updates data in real time to ensure
effectiveness.
Contrarily, the rapid life test and assessment is applicable
to unknown new batteries. The amount of available data is
limited or even no similar data can be used. The length of
data is fixed, which cannot be updated in real time. Hence,
it is not difficult to find that there are two main challenges
and difficulties compared with the traditional life prediction
as follows.
1) A lot of aging data for the new battery is lacked to train
the life assessment model.
2) The battery life of thousands of cycles can only be
predicted with dozens or 100 cycles.
Obviously, the life rapid test and assessment are definitely
not an easy task. How to predict a very long life (e.g.,
thousands of cycles) with very little data (e.g., dozens or
100 cycles) is the key scientific question, which is exactly to be
solved in this article. The solution of this problem will make
it possible to rapid obtain battery life, saving a lot of testing
time and economic cost. Meanwhile, it can further reduce the
2332-7782 © 2024 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See https://www.ieee.org/publications/rights/index.html for more information.
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 2 ---

9134
IEEE TRANSACTIONS ON TRANSPORTATION ELECTRIFICATION, VOL. 10, NO. 4, DECEMBER 2024
Fig. 1.
Comparison of mainstream test methods and proposed prediction-based test method. (a) International mainstream test method. (b) Proposed
prediction-based test method.
carbon dioxide emissions and promote the sustainable develop-
ment of battery industries. Nevertheless, there is little research
on this field. Many prior publications have concentrated on the
traditional life prediction. Summarizing these studies, it is not
difficult to find that there are roughly two types: model-based
methods [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]
and data-driven methods [6], [21], [22], [23], [24], [25], [26],
[27], [28], [29], [30], [31], [32], [33], [34].
1) Model-Based Methods: Four groups can be divided
in the LIBs’ model, which are the semi-empirical [11],
empirical [12], equivalent circuit [13], and electrochemical
models [14]. The model-based method is often combined with
experimental data to describe the aging behavior and to predict
the battery life. In fact, establishing an accurate model is a
challenging work. It requires a lot of physical knowledge or
experimental data in actual conditions. These data are often
unavailable or uneasy to acquire. Ma et al. [15] chose the expo-
nential model to characterize the capacity degradation trend.
The Gauss–Hermite particle filter (PF) is applied to predict
battery life. In fact, a series of problems will be caused by PF,
such as particle degradation and depletion, leading to inaccu-
rate RUL prediction. Ansari et al. [16] pointed that the internal
electrochemical characteristics will change with different oper-
ating conditions. It is hard to build an appropriate chemical
model to express the dynamic characteristics. Streb et al. [17]
studied the viability of reparameterization for electrochemical
model-based life prediction. For batteries in different appli-
cations, the number of internal parameters that need to be
reoptimized is completely different. Among them, the ohmic
and kinetic parameters need to be optimized, which bring
some difficulties to practical applications. Zhang et al. [18]
established the capacity loss model to predict life, which was
based on the aging mechanisms of solid–electrolyte interface
layer growth and active material loss. The parameters were
identified by recursive least squares method, and the prediction
error was less than ten cycles. However, it needed a lot of
cyclic experiments to obtain the relevant parameters, which
usually brought high costing. In addition, the model-based
methods are only suitable to a specific application or a single
type of battery. The generalization ability and robustness of the
model is insufficient compare with data-driven methods [19],
[20]. Therefore, the model-based methods are characterized by
limited robustness and poor dynamic.
2) Data-Driven Methods: Data-driven methods are attrac-
tive and mechanism-complex alternatives, which directly use
the historical data. It usually combines the data analysis tech-
nology to predict the battery life [21], [22]. Severson et al. [6]
used data from the early cycles to predict battery life. For
the first 100 cycles, the best models outputted a relatively
large error of 9.1%. Moreover, the prediction model is only
suitable for the same type of batteries. Wu et al. [23] pro-
posed a method based on neural network (NN) and important
sampling. The remaining useful life (RUL) prediction was
obtained with the error below 6%. However, the fixed hidden
neurons may cause low prediction accuracy for different
batteries. Zhang et al. [24] utilized long short-term memory
(LSTM) to learn the relation between battery capacity and
cycles. Dropout technology was adopted to solve the over-
fitting dispute. The prediction value with the error below
15 cycles was obtained by using less than 25% required data.
Richardson et al. [25] proposed a Gaussian process regression
(GPR) model to predict the capacity degradation and battery
life under dynamic conditions. Liu et al. [26] integrated the
electrochemical and empirical aging characteristics into the
GPR model. This method was promising for life prediction
under various cycle cases. Li et al. [27] combined LSTM and
Elman network to predict battery RUL. The results showed that
the prediction performance of the fusion algorithm was higher
than that of LSTM or Elman alone. Wang et al. [28] optimized
the support vector regression (SVR) by using artificial bee
colony (ABC) algorithm. The prediction error was less than
5%. Yang et al. [29] selected features related to life based
on voltage, capacity, and temperature. The NN and gradient
boosting regression tree were combined to predict battery life.
The process of the feature extraction was quite complicated,
leading to difficult implementation. Xiong et al. [30] pro-
posed a method for life prediction based on weighted least
squares support vector machine (WLSSVM) with only one
health indicator (HI) as an input. One HI cannot contain all
information about battery degradation, which brings the large
error of 9%. Meanwhile, the value of weight may affect the
prediction accuracy.
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 3 ---

ZHU et al.: RAPID TEST AND ASSESSMENT OF LIB CYCLE LIFE BASED ON TL
9135
The abovementioned studies are all for the traditional life
prediction, which are helpless to rapid test and assess for new
battery cycle life. Fortunately, Tan and Zhao [31] proposed
a life assessment method based on transfer learning (TL).
Although this method can apply the trained model to a new
battery, the similar data from the new battery is needed to fine-
tune the model to meet the adaptability. Hence, it is not a truly
battery life assessment. Similarly, Pan et al. [32] also proposed
a TL-based hybrid life assessment method under different
stresses, which concentrates on the model-based TL to fine-
tuning the network. Sun et al. [33] proposed a life assessment
method of cutting tool based on deep TL. It includes weight
transfer, hidden feature transfer, and weight update. This
method achieves good prediction effect, but the weight update
process required a certain length of new data. Moreover,
it is easy to produce the problem of gradient disappearing
and explosion. Matasci et al. [34] introduced an adaptive
classification method for remotely sensed images based on TL,
which was used to match and transfer the features of remotely
sensed images in different geographical regions. It ensured the
adaptability of the classification model trained by region A in
region B.
Therefore, to solve the above problems, a rapid life test and
assessment method is proposed based on feature-TL and deep
sparse autoencoder (DSAE). The aim of this study is to replace
the mainstream IEC continuous test method with the accurate
prediction-based method, which is displayed in Fig. 1(b).
Specifically, the features are extracted or calculated by DSAE
or charge–discharge information. The different features are
selected and further reconstructed by the feature-based TL,
which is innovatively used to learn the similarities between
different types of battery. Their own characteristic can be
maintained while the differences can be minimized. Mean-
while, the traditional time-consuming fine-tuning operation is
avoided. The reconstructed features are utilized to train the
regression network. By employing the trained network, the
thousands of cycle life of new battery are rapidly assessed.
Some indexes, such as the saved time and increased test
speed, are discussed in detail. The assessment effects using
different early cycles are also verified. This method can greatly
shorten the test time of new battery life and save costs
to promote the development of the battery industry. Several
crucial contributions can be summarized as follows.
1) Prediction replaces continuous testing. The mainstream
test method in industry is replaced with prediction-based
method in life assessment for the first time, which is
suitable for different types of battery and make the error
with less than 8.7%.
2) Life assesses more effective with less effort. The feature-
based TL is utilized to make the test speed increased
by eight times at least compared with the traditional
TL using fine-tuning operation. The battery life with
thousands of cycles can be predicted by using the first
100 cycles.
The remainder of this article is organized as follows.
Section II expounds the basic principle and algorithms descrip-
tion of feature-TL and DSAE. Then, the complete framework,
the used four battery datasets, and the feature extraction results
are given in Section III. Meanwhile, this section also specifies
the in-depth analyses of the performance of the proposed
method for cycle life assessment. Several comparative studies
are given. Finally, Section IV concludes this article.
II. METHODOLOGY
A. Deep Sparse AE
Autoencoder (AE) is one of the unsupervised deep learning
networks. It is widely used in data feature extraction [35].
Three parts are contained in AE, including the input layer, the
hidden layer, and the output layer. Its main task is to learn
an approximation to the identity function [36]. Some hidden
information about original data can be discovered by placing
constraints. These constraints are limiting the activation of
units to control the number of hidden units. Under this
operation, the AE is transformed to sparse AE (SAE). The
main steps of SAE acquisition were as follows.
For a sample x in battery dataset X = [x1, x2, . . . , xm], the
activation of hidden layer nodes is calculated by the following
equation:
h = g

W (1)x + b(1)	
(1)
where W (1) is the weight that connected input layer and hidden
layer and b(1) is the bias vector. Connection weight between
hidden layer and output layer is used to reconstruct original
data
x′ = g

W (2)h + b(2)	
(2)
where x’ is the reconstructed data and W (2) is the weight
connecting hidden layer and output layer.
For all data xi, the reconstructed error is calculated to design
the cost function by the following equation:
J(W, b) = 1
m
m
X
i=1
1
2
xi −x′
i
2

+ λ
2
nl−1
X
l=1
sl
X
i=1
sl+1
X
j=1
n
W (l)
ji
o2
(3)
where nl is the number of layers, sl is the number of units in
the lth layer, and W (l)
ji are the weight vectors to connect the
lth layer and (l + 1)th layer. In the hidden layer, the average
activation of the jth unit is expressed as follows:
ρ j = 1
m
m
X
i=1
h j(xi),
j = 1, . . . , sl.
(4)
ρ is defined to restrict the activation. The overall constraint
for all units in hidden layer is shown as follows:
sl
X
j=1
KL(ρ||ρ j) =
sl
X
j=1
ρ log ρ
ρ j
+ (1 −ρ) log (1 −ρ)
(1 −ρ j)
(5)
where Kullback–Leiber (KL) (ρ || ρ j) is called KL divergence.
The cost function is now given as follows:
Jsparse(W, b) = J(W, b) + β
sl
X
j=1
KL(ρ||ρ j)
(6)
where β controls the weight of the sparsity penalty term.
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 4 ---

9136
IEEE TRANSACTIONS ON TRANSPORTATION ELECTRIFICATION, VOL. 10, NO. 4, DECEMBER 2024
Fig. 2.
Structure of TCA in this article.
To minimize (6), the partial derivative of Jsparse to W and b is
applied. The initial weight and bias vector by back propagation
are updated. Then, a trained SAE network is acquired. The
first SAE network could be trained by inputting original
capacity data. The weight W (1)
1
and hidden layer output h1
could be obtained. The second SAE, i.e., SAE2, could be
trained by using h1 as the input. By this operation, a series
of SAE networks could be generated. The DSAE network is
constructed by stacking hidden layers of these multiple SAE
networks. In this article, the DSAE is applied to extract the 1-D
hidden feature in capacity sequence, i.e., the original capacity
sequence is used as an input to DSAE, and the 1-D hidden
feature is outputted. Here, the used capacity sequence has been
handled with data processing technique (such as eliminating
outliers by 3σ-criterion, smoothing by moving average filter,
etc.). The feature may not be temporal dependencies and
certain trend in the original data, but it can reflect the capacity
degradation to some extent. Meanwhile, some correlations
between them and end of life may be existed.
B. Transfer Component Analysis
Transfer component analysis (TCA) is one of the strategies
in the symmetric feature-based TL [37], [38], [39]. The main
objective is to minimize the difference between the source
domain data and the target domain data, which uses the
maximum mean discrepancy (MMD) as the loss function as
follows:
MMD(X, Y) =

1
m
m
X
i=1
φ(xi)−1
n
n
X
i=1
φ(yi)

2
H
.
(7)
Moreover, the internal attributes, such as local relationship
and label dependencies, are maintained to the greatest extent.
The method is summarized as that the data of two domains are
simultaneously mapped to the high dimensional reproducing
kernel Hilbert space (RKHS) [40], [41]. In the mapped space,
the distance between the two domains is made as small as
possible to achieve strong adaptability. The main steps are as
follows.
As shown in Fig. 2, let AS = {X S, YS} = {xSi, ySi}n
i=1 be
the set of labeled source data. XT = {xTj}m
j=1 be the set of
unlabeled target data. The goal is to obtain target labels yT
exclusively based on the labeled data from AS in the training
stage. The samples of the two domains need to be mapped to
a common space through mapping φ, i.e., X S →φ(X S) = X∗
S
and XT →φ(XT ) = X∗
T . The MMD is used to evaluate the
distance difference between different domains. A prediction
learner is trained by using the mapped source domain data
{x∗
Si, ySi}n
i=1. It is applied to predict the target domain label yT .
Specially, in this article, X S represents the features extracted
from the source domain dataset, and YS represents the corre-
sponding cycle life labels, which are obtained from a large
amount of available cycle testing data of the existing batteries.
XT denotes the features extracted from the target domain
dataset. The target domain specifically refers to new batteries
that require life rapid assessment. There is no complete cycle
test data for the whole life; only a small amount of data are
available (such as 100 cycles). YT indicates that the cycle
life of battery to be assessed (unknown). The acquisition of
these features is obtained based on processed curves (such as
current, voltage, capacity, etc.). The data processing procedure
has been described in Section II-A, and the detail information
of features can be found in Section III-C. X∗
S and X∗
T are
obtained by reconstructing X S and XT with TCA, and the
assessment model is trained by using YS as the output to rapid
obtain YT .
Here, to achieve the rapid life assessment for new battery,
TCA must be utilized. The reason is that a lot of aging data
for new battery is lacked to train the model, which is only
constructed with a large amount of available data in different
types of batteries. The fundamentals and advantages of TCA
have already been stated in the previous content. When TCA
is utilized, the new battery life assessment model can be
constructed by a small amount of data (such as 100 cycles).
It can dramatically reduce the needed basic data for modeling
to greatly shorten the test time.
III. EXPERIMENTAL RESULTS AND DISCUSSION
A. Overall Framework
The proposed life assessment framework based on predic-
tion is shown in Fig. 3. The overall framework consists of
several main parts. High-precision battery test [Fig. 3(a)].
The battery cycle aging data are collected in the labo-
ratory, which utilizes the international mainstream battery
charging–discharging equipment, such as Arbin or AVL. The
batteries are charged and discharged in the temperature-
controlled cabinet. The work step controlling and data
collecting are carried out with the built-in upper computer soft-
ware. Furthermore, the cyclic data are stored in the host PC.
Battery data visualization and feature extraction [Fig. 3(b)].
The data processing is first implemented, which consists of
eliminating outliers by Pauta criterion and smoothing by
moving average filter. This step is done in the MATLAB 2021b
using its own computing and processing library, which make
the original data as an input. Then, the battery data are visual-
ized to form the different curves, such as capacity degradation.
The 1-D capacity hidden features are extracted by inputting
capacity data into DSAE. The feature set is formed with the
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 5 ---

ZHU et al.: RAPID TEST AND ASSESSMENT OF LIB CYCLE LIFE BASED ON TL
9137
Fig. 3.
Proposed life assessment framework based on prediction. (a) High precision battery testing and data acquisition. (b) Battery date visualization and
feature extraction. (c) Transfer component analysis and model training. (d) Life rapid test based on prediction.
capacity feature and others that extracted from the information,
such as the difference between the capacity–voltage curves
[Q(V )] of the 100th and 10th cycles [1Q100−10(V )]. The
acquisition of these other features is not relied on NN or
related algorithms but directly calculates mathematical statis-
tical features, such as variance, max/min, and so on. TL and
model training [Fig. 3(c)]. The different feature combinations
are chosen. The TCA is applied to reconstruct the features of
source (MIT) and target (other dataset) domains. Specifically,
the features extracted from different dataset are considered as
an input to the TCA, while the reconstructed features are the
output. Furthermore, the reconstructed source-domain features
are taken as inputs and the corresponding life as outputs to
train the regression network. Battery life rapid test based on
prediction [Fig. 3(d)]. The trained prediction network and
reconstructed target-domain battery features as an input are
used to rapidly assess life. The saved time, increased test
speed, and other indexes are discussed. The assessment effects
using different early cycles are also verified. Moreover, all
three parts of Fig. 3(b)–(d) are achieved in computing and
network library based on MATLAB 2021b.
B. Battery Dataset
In this section, the validity and feasibility of the proposed
method is verified using three public battery datasets and
one dataset generated by experiment. These batteries include
124 commercial LFP 18650 cells from MIT [6], four lithium
cobalt oxide (LCO) cells from CALCE [42], seven LCO
prismatic cells from Sandia National Laboratories (SNL) [43],
and four LFP 26650 power cells from valence technology
(VT), respectively. The nominal capacity is 1.1, 1.1, 1.35, and
2.5 Ah, respectively. Among them, the VT dataset is generated
through 5-year cycle testing in our own lab, as shown in
Fig. 3(a). The battery parameters are listed in Table I. More
detailed charge–discharge protocols information can be found
in corresponding references. The capacity degradation curves
TABLE I
BATTERY PARAMETERS IN DIFFERENT DATASETS
of different batteries are shown as Fig. 4. As shown in Fig. 4,
the LIBs’ life varies from 100 to 3000 cycles. The totally
different capacity degradation trends are caused by different
types of LIBs and different charge–discharge protocols.
C. Features Extraction and Presentation
The feature-based approach is popular and convincing for
predicting LIBs’ cycle life [2]. In this method, the features,
which are linear or nonlinear transformations of the original
data, are extracted and utilized in a regularized linear network.
Moreover, the crucial information about life is contained in
Q(V ) curves [44]. According to [6], high predictive per-
formance can be obtained by using extracted features from
1Q100−10(V ). Here, 1Q100−10(V ) = Q100(V ) −Q10(V ). The
subscript is the cycle number.
In this article, the features are extracted or generated by
the charge–discharge data and other information stream. These
different feature combinations are used in the elastic regression
network to predict the battery life. The sixfold cross-validation
and three Monte Carlo (MC) sampling are applied to choose
the parameters value. Five different models are utilized. The
used features of different models are as follows.
1) Only the variance of 1Q100−10(V ).
2) The additional features obtained during discharging
process.
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 6 ---

9138
IEEE TRANSACTIONS ON TRANSPORTATION ELECTRIFICATION, VOL. 10, NO. 4, DECEMBER 2024
Fig. 4.
Discharge capacity of different cells. (a) MIT, (b) CALCE, (c) SNL, and (d) VT in our own lab.
Fig. 5.
Correlation of different features with battery cycle life. (a) Correlation scatter plot. (b) Spearman correlation coefficient.
3) More features from additional data information, such as
temperature, internal resistance, and charging time.
4) The features with spearman correlation greater than 0.8.
5) The variance of 1Q100−10(V ) and hidden feature
extracted by DSAE. In addition to the hidden feature,
others are collectively referred to domain feature.
Based on 1Q100−10(V ) curves, discharging process, and
other data streams, the 22 domain features are obtained. All
features are shown in Appendix. To obtain and compare the
relationship between each feature and the battery cycle life,
the Spearman correlation coefficients (usually denoted by ρ) is
utilized to measure the correlation between two quantities. The
value of the ρ ranges from −1 to 1, which means that the value
is closer to −1 or 1, and the negative or positive correlation is
stronger. It is generally believed that the coefficient from 0 to
1 is divided into five categories with 0.2 interval, which are
extremely weak, weak, medium, strong, and extremely strong
correlation. The calculation process is given in the following
equation:
ρ =
Pn
i=1 (xi −¯x)(yi −¯y)
qPn
i=1 (xi −¯x)2 Pn
i=1 (yi −¯y)2
(8)
where ¯x represents the mean value of sample xi.
The correlation scatter plot is shown in Fig. 5(a), and ρ
is represented in Fig. 5(b). Here, the correlation coefficients
between different features and life are calculated by using
the MIT dataset. The size of correlation coefficient of used
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 7 ---

ZHU et al.: RAPID TEST AND ASSESSMENT OF LIB CYCLE LIFE BASED ON TL
9139
TABLE II
USED FEATURES FOR DIFFERENT MODELS
TABLE III
ERROR OF LIFE PREDICTION RESULTS FOR MIT BATTERY
features may vary slightly in different datasets, but the life
prediction result will not change too much [30]. The specific
used features of different model are shown in Table II.
These features belong to different data domains, includ-
ing battery charging–discharging feature domain, capacity
hidden feature domain, and additional data streams feature
domain. Meanwhile, the feature-TL (TCA) is employed to
reconstruct features, which considers the original features in
source domain and target domain as an input and regards the
reconstructed features as an output. In this article, the specific
data for applying TL are MIT, CALCE, SNL, and VT cell data.
The MIT dataset is the source domain, while the other datasets
are the target domain. More detailed information about used
features can be found in Table IX of Appendix.
All 124 cells data in MIT dataset are used to train the
regression model. The 1–2 cells data from other battery dataset
(CALCE, SNL, and VT) are used to verify the training effect,
and then, the remaining battery data are utilized to complete
the test.
D. Results Presentation and Discussion
1) Life Prediction Based on the First 100 Cycles: The
life prediction results for different batteries are given in
Tables III–VI. To avoid redundancy, the results with model
5 only are given in Tables V and VI, respectively. It is worth
noting that four used dataset is divided into two categories to
verify the effectiveness of TCA, i.e., Classes A and B. Among
them, Class A refers to MIT battery data, and Class B refers to
CALCE, SNL, and VT battery data. The TCA is not performed
in [6] and [30], which means that the life of Class B battery is
directly predicted by the model trained with Class A battery
data.
Moreover, the prediction model in [6] is trained by using
50% of data, while the model in [30] is trained by using 100%
of data. The MIT data are regarded as the source domain,
which shares the largest available battery dataset currently.
The target domain refers to the other data, such as CALCE,
TABLE IV
LIFE PREDICTION COMPARISON FOR CALCE BATTERY
TABLE V
LIFE PREDICTION COMPARISON FOR SNL BATTERY WITH MODEL5
TABLE VI
LIFE PREDICTION COMPARISON FOR VT BATTERY WITH MODEL5
SNL, and VT, which are considered to the data of the battery
under test. That is, the MIT data are utilized to rapidly assess
other battery cycle life, which is totally different with MIT
battery. Meanwhile, all source-domain data must be used
during TCA, which can ensure that the information are not
lost. The transfer method is also consistent with the reality.
In the actual condition, it is based on a large amount of
battery data available to rapidly test and assess the cycle life
of the new battery, which is totally different from the available
LIBs. It means that the domain with large amount of data is
transferred to the domain with a smaller amount of data.
To further compare the prediction effect of different model,
the absolute error (AE) and relative error (RE) are used to
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 8 ---

9140
IEEE TRANSACTIONS ON TRANSPORTATION ELECTRIFICATION, VOL. 10, NO. 4, DECEMBER 2024
TABLE VII
PREDICTION ERROR COMPARISON FOR DIFFERENT BATTERIES WITH MODEL5
evaluate the results. The formula is defined as follows:
AE =
ypre −yact

(9)
RE = |ypre −yact|
yact
× 100%
(10)
where ypre and yact represent the life predicted value and actual
value, respectively.
The error of life prediction results for MIT battery is shown
in Table III. Here, we perform the internal partitioning in
MIT dataset, i.e., 93 cells are randomly selected for training
and the remaining 31 cells are used for testing, to verify the
effectiveness of the proposed method.
As shown in Table III, for 124 cylindrical cells in MIT
dataset, the prediction effect is worse than that of direct
prediction when the TCA are executed. Meanwhile, the degree
of deterioration is raised with the number of used features
increasing. The reason may be that the 124 cells are essentially
belong to the same type, i.e., the data characteristics of the
source domain and target domain are inherently very similar.
TCA is employed to solve the data matching problem of
source domain and target domain with different characteristics.
Hence, the utilization of TCA in this dataset is redundant.
Some information will be lost leading to inaccurate prediction.
In contrast, a large amount of data that are similar to that of
battery under test are used to train the prediction model, which
brings the more accurate results in direct prediction.
The prediction error comparison for different batteries is
given in Table VII. As mentioned above, Table IV shows
the life prediction results of CALCE battery. The relatively
reasonable results are obtained regardless of executing TCA
when Model 1 is utilized. The difference is that when the
data are reconstructed with TCA, the predictions are much
closer to the actual value. With the number of used features
increases, the prediction effect shows irregular change. The
prediction results become worse after TCA. The reason may
be the occurrence of negative transfer. The results of using
model 5 are also presented in Table IV. Compared with other
models, there is no substantial improvement in the accuracy
of direct prediction. The predicted value has little difference
with the actual value by performing TCA. The life prediction
of the three cells is 633, 682, and 712. As shown in Table VII,
the AE is 7, 20, and 24 cycles, respectively, which the RE is
less than 3.3%.
Table V shows the life prediction results of SNL battery.
As shown in Tables X and XI, the effect with TCA does
not seriously deteriorate with the used features increasing.
The reason may be that the life of such batteries is insen-
sitive to features except variance. As shown in Table VII,
the prediction AE in model 5 is 87, 9, 8, 30, 18, 25, and
27 cycles, respectively. The RE is less than 8.7%. Table VI
also presents the prediction results of VT battery. Owing to
the long cycle life of such batteries, the AE is relatively large,
which is 101, 105, 200, and 99 cycles, respectively. The RE
is less than 6.9%. The prediction errors of all batteries are
smaller than the maximum error (9.1%) in [6]. Meanwhile, the
method of rapidly assessing life in this article is suitable for
different types of battery compared with [6], and the hidden
feature extracted by DSAE is utilized, which represents the
battery degradation to some extent. In summary, the best life
predictions are obtained using variance and capacity hidden
feature regardless of the type of LIBs.
In all, the effectiveness of the rapid life testing with TCA
is achieved by using different feature combinations. When
features that are moderately or weakly correlated with life are
reconstructed and used, the prediction effect tends to be poor.
It is due to the occurrence of negative transfer. Therefore, it is
necessary to select and use features that are strongly correlated
with life. Then, TCA is used for rapid testing and assessment
of life. It can ensure the accuracy and robustness of prediction
to a certain extent.
2) Test Time and Electricity Cost Savings: Taking the Arbin
battery tester (BT-5HC/50V60A) as an example, the average
power of each test channel is about 250 W. The battery life
can be rapidly assessed with the first 100 cycles test. The
saved electricity for testing can be calculated by the following
equation. The saved time and electricity are shown in Fig. 6
W = Pave × t
(11)
where W is the saved electricity, Pave is the average power of
each test channel, and t represents the saved time.
As shown in Fig. 6, the life test time of the proposed method
is shortened by over 80% than mainstream IEC continuous
test method. The test speed is increased by more than eight
times and the saved electricity ranges from 378 to 1062 kW·h.
The test time and economic cost are remarkable saved. The
development of battery industry will be promoted.
Meanwhile, to better demonstrate the contribution of the
proposed method in reducing carbon dioxide (CO2) emissions,
we linked the test electricity to the standard coal consumption
(SCC). SCC is the amount of consumed coal to produce
1-kW·h electricity. According to the Annual Development
Report of China’s Power Industry 2023 issued by the govern-
ment of China, the SCC of China in 2022 is 300.7 g/kW·h,
generating about 0.997 kg of CO2. These values may vary
in different countries or regions. Hence, in conjunction with
the above analysis, the proposed method can reduce CO2
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 9 ---

ZHU et al.: RAPID TEST AND ASSESSMENT OF LIB CYCLE LIFE BASED ON TL
9141
Fig. 6.
Comparisons of saved time and electricity cost.
TABLE VIII
COMPARISON OF LIFE ASSESSMENT FOR VT BATTERY
USING DIFFERENT CYCLES
emissions by 377–1059 kg, which demonstrates the great
potential in energy saving and emission reductions.
3) Life Prediction in Different Cycles: To enhance the
users’ selectivity for the test time, the electricity cost, and
the prediction accuracy, Table VIII presented the comparison
of VT battery life assessments using different early cycles.
As shown in Table VIII, the first 50 cycles only are used
to save more than 95% of the life test time, but it leads
to a large prediction error. The max RE is more than 13%.
With the used cycles increasing, the assessment accuracy is
improved, which in turn further increases the testing time. The
electricity cost for each test increases accordingly. When the
first 350 cycles are used, the maximum RE is only 1.2%. The
test time is only shortened by about 70%. Hence, according
to different conditions, the users can independently choose the
test time, accuracy, and so on. The proposed method has strong
flexibility.
IV. CONCLUSION
In this study, the data-driven method is proposed for rapid
assessing the cycle life in different types of batteries, which
utilizes the accurate prediction to replace with mainstream
continuous test. It is suitable for different types of bat-
teries. Meanwhile, using of feature-TL makes life assess
more effective with less effort, which avoids the fine-tuning
operation to save time compared with traditional TL. This
TABLE IX
SUMMARY OF EXTRACTED OR CALCULATED DOMAIN FEATURES
article provides a comprehensive research status of the life
assessment and prediction. The principles and description of
DSAE and feature-TL, overall implementation framework, and
used battery dataset and in-depth discussion of the experiment
results are also given. The effectiveness, generalizability, and
the economy of the proposed method are emphasized by
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 10 ---

9142
IEEE TRANSACTIONS ON TRANSPORTATION ELECTRIFICATION, VOL. 10, NO. 4, DECEMBER 2024
TABLE X
LIFE PREDICTION COMPARISON FOR SNL BATTERY WITH MODEL2
TABLE XI
LIFE PREDICTION COMPARISON FOR SNL BATTERY WITH MODEL4
comparison with other existing methods. The several main
problems are solved successfully, and some important con-
clusions are summarized as follows.
1) The problem of new battery life rapid assessment is
solved by the presented intelligent prediction-based
method, which replaces the mainstream continuous test
in industry. The error is less than 8.7% by using the first
100 cycles.
2) The fine-tune network operation is not needed by using
the feature-based TL compared with traditional TL-
based prediction, which can assess life more effective
with less effort. It ensures the strong adaptability and
robustness. The test speed is increased by eight times at
least, and 653-kW·h electricity is saved for each testing.
3) The life assessment effect using different cycles is
verified; 96% test time is reduced by using the first
50 cycles, while the prediction error is less than 1.2%
with the 350 cycles. This method has strong flexibility
and selectivity.
In future work, the proposed method verification should be
done with larger capacity and more types of cell samples, and
the potentiality should be discussed in practical applications,
such as EVs and ESS.
APPENDIX
In this article, the domain features include discharge-related
features and additional data stream features. All features
information is shown in Table IX, and internal resistance and
temperature information are not provided in SNL dataset. So,
the prediction result of model 3 is not given. The life prediction
comparisons for SNL battery with Models 2 and 4 are shown
in Tables X and XI, respectively.
REFERENCES
[1] S. Wang, S. Jin, D. Bai, Y. Fan, H. Shi, and C. Fernandez, “A critical
review of improved deep learning methods for the remaining useful life
prediction of lithium-ion batteries,” Energy Rep., vol. 7, pp. 5562–5574,
Nov. 2021.
[2] G. Vennam and A. Sahoo, “A dynamic SOH-coupled lithium-ion cell
model for state and parameter estimation,” IEEE Trans. Energy Convers.,
vol. 38, no. 2, pp. 1–10, Jun. 2022.
[3] J. Zhu et al., “Data-driven capacity estimation of commercial lithium-
ion batteries from voltage relaxation,” Nature Commun., vol. 13, no. 1,
p. 2261, Apr. 2022.
[4] Z. Zhou, Y. Liu, M. You, R. Xiong, and X. Zhou, “Two-stage aging
trajectory prediction of LFP lithium-ion battery based on transfer learn-
ing with the cycle life prediction,” Green Energy Intell. Transp., vol. 1,
no. 1, Jun. 2022, Art. no. 100008.
[5] K. Liu, Y. Shang, Q. Ouyang, and W. D. Widanage, “A data-driven
approach with uncertainty quantification for predicting future capacities
and remaining useful life of lithium-ion battery,” IEEE Trans. Ind.
Electron., vol. 68, no. 4, pp. 3170–3180, Apr. 2021.
[6] K. A. Severson et al., “Data-driven prediction of battery cycle life
before capacity degradation,” Nature Energy, vol. 4, no. 5, pp. 383–391,
Mar. 2019.
[7] X. Hu, L. Xu, X. Lin, and M. Pecht, “Battery lifetime prognostics,”
Joule, vol. 4, no. 2, pp. 310–346, Feb. 2020.
[8] Y. Yang, “A machine-learning prediction method of lithium-ion battery
life based on charge process for different applications,” Appl. Energy,
vol. 292, Jun. 2021, Art. no. 116897.
[9] M. Wei, M. Ye, Q. Wang, Xinxin-Xu, and J. P. Twajamahoro, “Remain-
ing useful life prediction of lithium-ion batteries based on stacked
autoencoder and Gaussian mixture regression,” J. Energy Storage,
vol. 47, Mar. 2022, Art. no. 103558.
[10] K. Liu, Z. Wei, C. Zhang, Y. Shang, R. Teodorescu, and Q.-L. Han,
“Towards long lifetime battery: AI-based manufacturing and manage-
ment,” IEEE/CAA J. Automat. Sinica, vol. 9, no. 7, pp. 1139–1165,
Jul. 2022.
[11] N. Yang et al., “An improved semi-empirical model for thermal anal-
ysis of lithium-ion batteries,” Electrochimica Acta, vol. 311, pp. 8–20,
Jul. 2019.
[12] E. Wikner and T. Thiringer, “Extending battery lifetime by avoiding
high SOC,” Appl. Sci., vol. 8, no. 10, p. 1825, Oct. 2018.
[13] Z. Huang, M. Best, J. Knowles, and A. Fly, “Adaptive piecewise equiva-
lent circuit model with SOC/SOH estimation based on extended Kalman
filter,” IEEE Trans. Energy Convers., vol. 38, no. 2, pp. 959–970,
Jun. 2022.
[14] G. Vennam, A. Sahoo, and S. Ahmed, “A survey on lithium-ion battery
internal and external degradation modeling and state of health estima-
tion,” J. Energy Storage, vol. 52, no. 1, Aug. 2022, Art. no. 104720.
[15] Y. Ma, Y. Chen, X. Zhou, and H. Chen, “Remaining useful life prediction
of lithium-ion battery based on Gauss–Hermite particle filter,” IEEE
Trans. Control Syst. Technol., vol. 27, no. 4, pp. 1788–1795, Jul. 2019.
[16] S.
Ansari,
A.
Ayob,
M.
S.
Hossain
Lipu,
A.
Hussain,
and
M. H. M. Saad, “Remaining useful life prediction for lithium-ion bat-
tery storage system: A comprehensive review of methods, key factors,
issues and future outlook,” Energy Rep., vol. 8, pp. 12153–12185,
Nov. 2022.
[17] M. Streb, M. Andersson, V. L. Klass, M. Klett, M. Johansson,
and G. Lindbergh, “Investigating re-parametrization of electrochemical
model-based battery management using real-world driving data,” eTrans-
portation, vol. 16, Apr. 2023, Art. no. 100231.
[18] Y. Zhang, R. Xiong, H. He, X. Qu, and M. Pecht, “State of charge-
dependent aging mechanisms in graphite/Li(NiCoAl)O2 cells: Capacity
loss modeling and remaining useful life prediction,” Appl. Energy,
vol. 255, Dec. 2019, Art. no. 113818.
[19] D. Gong, Y. Gao, Y. Kou, and Y. Wang, “Early prediction of cycle life
for lithium-ion batteries based on evolutionary computation and machine
learning,” J. Energy Storage, vol. 51, Jul. 2022, Art. no. 104376.
[20] M. Hossain, M. E. Haque, and M. T. Arif, “Online model parameter and
state of charge estimation of Li-ion battery using unscented Kalman filter
considering effects of temperatures and C-rates,” IEEE Trans. Energy
Convers., vol. 37, no. 4, pp. 2498–2511, Dec. 2022.
[21] I. Sanz-Gorrachategui et al., “Remaining useful life estimation for LFP
cells in second-life applications,” IEEE Trans. Instrum. Meas., vol. 70,
pp. 1–10, 2021.
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 


--- Page 11 ---

ZHU et al.: RAPID TEST AND ASSESSMENT OF LIB CYCLE LIFE BASED ON TL
9143
[22] D. Shen, L. Wu, G. Kang, Y. Guan, and Z. Peng, “A novel online method
for predicting the remaining useful life of lithium-ion batteries consid-
ering random variable discharge current,” Energy, vol. 218, Mar. 2021,
Art. no. 119490.
[23] J. Wu, C. Zhang, and Z. Chen, “An online method for lithium-ion battery
remaining useful life estimation using importance sampling and neural
networks,” Appl. Energy, vol. 173, pp. 134–140, Jul. 2016.
[24] Y. Zhang, R. Xiong, H. He, and M. G. Pecht, “Long short-term memory
recurrent neural network for remaining useful life prediction of lithium-
ion batteries,” IEEE Trans. Veh. Technol., vol. 67, no. 7, pp. 5695–5705,
Jul. 2018.
[25] R. R. Richardson, M. A. Osborne, and D. A. Howey, “Battery health
prediction under generalized conditions using a Gaussian process tran-
sition model,” J. Energy Storage, vol. 23, pp. 320–328, Jun. 2019.
[26] K. Liu, X. Hu, Z. Wei, Y. Li, and Y. Jiang, “Modified Gaussian process
regression models for cyclic capacity prediction of lithium-ion batter-
ies,” IEEE Trans. Transport. Electrific., vol. 5, no. 4, pp. 1225–1236,
Dec. 2019.
[27] X. Li, L. Zhang, Z. Wang, and P. Dong, “Remaining useful life
prediction for lithium-ion batteries based on a hybrid model combining
the long short-term memory and Elman neural networks,” J. Energy
Storage, vol. 21, pp. 510–518, Feb. 2019.
[28] Y. Wang, Y. Ni, S. Lu, J. Wang, and X. Zhang, “Remaining useful
life prediction of lithium-ion batteries using support vector regression
optimized by artificial bee colony,” IEEE Trans. Veh. Technol., vol. 68,
no. 10, pp. 9543–9553, Oct. 2019.
[29] F. Yang, D. Wang, F. Xu, Z. Huang, and K.-L. Tsui, “Lifespan prediction
of lithium-ion batteries based on various extracted features and gradient
boosting regression tree model,” J. Power Sources, vol. 476, Nov. 2020,
Art. no. 228654.
[30] W. Xiong, G. Xu, Y. Li, F. Zhang, P. Ye, and B. Li, “Early prediction
of lithium-ion battery cycle life based on voltage-capacity discharge
curves,” J. Energy Storage, vol. 62, Jun. 2023, Art. no. 106790.
[31] Y. Tan and G. Zhao, “Transfer learning with long short-term memory
network for state-of-health prediction of lithium-ion batteries,” IEEE
Trans. Ind. Electron., vol. 67, no. 10, pp. 8723–8731, Oct. 2020.
[32] D. Pan, H. Li, and S. Wang, “Transfer learning-based hybrid remaining
useful life prediction for lithium-ion batteries under different stresses,”
IEEE Trans. Instrum. Meas., vol. 71, pp. 1–10, 2022.
[33] C. Sun, M. Ma, Z. Zhao, S. Tian, R. Yan, and X. Chen, “Deep transfer
learning based on sparse autoencoder for remaining useful life prediction
of tool in manufacturing,” IEEE Trans. Ind. Informat., vol. 15, no. 4,
pp. 2416–2425, Apr. 2019.
[34] G. Matasci, M. Volpi, M. Kanevski, L. Bruzzone, and D. Tuia, “Semisu-
pervised transfer component analysis for domain adaptation in remote
sensing image classification,” IEEE Trans. Geosci. Remote Sens., vol. 53,
no. 7, pp. 3550–3564, Jul. 2015.
[35] A. Ng, “Sparse autoencoder,” CS294A Lect. Notes, vol. 72, pp. 1–19,
Oct. 2011.
[36] Y. Zhu, X. Wu, J. Qiang, X. Hu, Y. Zhang, and P. Li, “Representation
learning with deep sparse auto-encoder for multi-task learning,” Pattern
Recognit., vol. 129, Sep. 2022, Art. no. 108742.
[37] F. Zhuang et al., “A comprehensive survey on transfer learning,” Proc.
IEEE, vol. 109, no. 1, pp. 43–76, Jan. 2021.
[38] S. J. Pan and Q. Yang, “A survey on transfer learning,” IEEE Trans.
Knowl. Data Eng., vol. 22, no. 10, pp. 1345–1359, Oct. 2010.
[39] M. Lotfollahi et al., “Mapping single-cell data to reference atlases
by transfer learning,” Nature Biotechnol., vol. 40, no. 1, pp. 121–130,
Jan. 2022.
[40] T. Jing, X. Tian, H. Hu, and L. Ma, “Deep learning-based cloud–
edge collaboration framework for remaining useful life prediction of
machinery,” IEEE Trans. Ind. Informat., vol. 18, no. 10, pp. 7208–7218,
Oct. 2022.
[41] S. J. Pan, I. W. Tsang, J. T. Kwok, and Q. Yang, “Domain adaptation
via transfer component analysis,” IEEE Trans. Neural Netw., vol. 22,
no. 2, pp. 199–210, Feb. 2011.
[42] W. He, N. Williard, M. Osterman, and M. Pecht, “Prognostics of lithium-
ion batteries based on Dempster–Shafer theory and the Bayesian Monte
Carlo method,” J. Power Sources, vol. 196, no. 23, pp. 10314–10321,
Dec. 2011.
[43] Y. Xing, E. W. M. Ma, K.-L. Tsui, and M. Pecht, “An ensemble model
for predicting the remaining useful performance of lithium-ion batteries,”
Microelectron. Rel., vol. 53, no. 6, pp. 811–820, Jun. 2013.
[44] P. M. Attia, K. A. Severson, and J. D. Witmer, “Statistical learning for
accurate and interpretable battery lifetime prediction,” J. Electrochem.
Soc., vol. 168, no. 9, Sep. 2021, Art. no. 090547.
Yuhao Zhu received the B.S. and M.S. degrees in
electrical engineering from the Shandong Univer-
sity of Science and Technology, Qingdao, China,
in 2021 and in 2018, respectively. He is currently
pursuing the Ph.D. degree in energy power with
the School of Control Science and Engineering,
Shandong University, Jinan, China.
His research interests include state estimation
and remaining useful life prediction for lithium-ion
batteries.
Xin Gu received the M.S. degree from the Key
Laboratory of Advanced Manufacturing Technol-
ogy, Ministry of Education, Guizhou University,
Guiyang, China, in 2021. He is currently pursu-
ing the Ph.D. degree in control theory and control
engineering with the School of Control Science and
Engineering, Shandong University, Jinan, China.
His research interests include state estimation and
fault diagnosis for lithium-ion batteries.
Kailong Liu (Senior Member, IEEE) received the
Ph.D. degree in electrical engineering from Queen’s
University Belfast, Belfast, U.K., in 2018.
He was an Assistant Professor at the University
of Warwick, Coventry, U.K., and a Visiting Student
Researcher at Tsinghua University, Beijing, China.
He is a Professor at the School of Control Science
and Engineering, Shandong University, Jinan, China.
His research interests include modeling, optimiza-
tion and control with applications to electrical/hybrid
vehicles, energy storage, and battery manufacture
and management.
Dr. Liu is on editorial boards of some journals of his area, including IEEE
TRANSACTIONS ON TRANSPORTATION ELECTRIFICATION, Renewable and
Sustainable Energy Reviews, IEEE/CAA JOURNAL OF AUTOMATICA SINICA,
Applied Energy, and Control Engineering Practice.
Wenyuan Zhao received the B.S. degree in automa-
tion from Qingdao University, Qingdao, China,
in 2021. He is currently pursuing the M.S. degree in
control engineering with the School of Control Sci-
ence and Engineering, Shandong University, Jinan,
China.
His research interests include the optimization of
lithium-ion battery fast charging and the design of
battery management systems.
Yunlong Shang (Member, IEEE) received the B.S.
degree in automation from the Hefei University of
Technology, Hefei, China, in 2008, and the Ph.D.
degree in control theory and control engineering
from Shandong University, Jinan, China, in 2017.
In 2019, he joined Shandong University, where he
is currently a Professor with the School of Control
Science and Engineering. From September 2015 to
October 2017, he conducted scientific research as
a Joint Ph.D. Student with the Department of
Electrical and Computer Engineering, San Diego
State University, San Diego, CA, USA, where he was a Postdoctoral Research
Fellow, from December 2017 to January 2019. His current research interests
include battery balancing, battery modeling and states estimation, self-heating
for low-temperature batteries, and design of battery management systems.
Dr. Shang won the Outstanding Paper Award of the IEEE TRANSACTIONS
ON INDUSTRIAL ELECTRONICS in 2022.
Authorized licensed use limited to: INDIAN INSTITUTE OF TECHNOLOGY DELHI. Downloaded on February 05,2026 at 13:22:55 UTC from IEEE Xplore.  Restrictions apply. 
