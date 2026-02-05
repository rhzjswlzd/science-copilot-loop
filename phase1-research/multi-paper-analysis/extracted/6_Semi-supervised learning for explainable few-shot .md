# Semi-supervised learning for explainable few-shot battery lifetime prediction



--- Page 1 ---

Article
Semi-supervised learning for explainable few-
shot battery lifetime prediction
An innovative semi-supervised machine learning method is proposed in this work
to tackle the challenge of data shortage for battery lifetime prediction. By
leveraging low-cost unlabeled data, the proposed method reveals the underlying
data patterns of battery capacity degradation, thereby achieving both superior
prediction accuracy and interpretability. Furthermore, the proposed method
achieves grand economic value by substantially reducing the costs of battery
testing, leading to signiﬁcant importance in the R&D of rechargeable batteries.
Accurate model
Supervised learning
•
Expensive
•
Time consuming
Less-accurate
partial-view model
Large amount of
unlabeled data
Better trained 
complete-view
model
792
472
•
Cost effective
•
More common
…
…
…
…
Semi-supervised learning
Side 
information
744
645
…
567
792
…
634
472
…
693
560
…
Large amount of labeled data
l
a
n
o
it
n
e
v
n
o
C
d
o
h
t
e
m
d
e
s
o
p
o
r
P
d
o
h
t
e
m
Limited # of labeled data
Nanlin Guo, Sihui Chen, Jun
Tao, Yang Liu, Jiayu Wan, Xin Li
taojun@fudan.edu.cn (J.T.)
yang.liu2@dukekunshan.edu.cn (Y.L.)
wanjy@sjtu.edu.cn (J.W.)
xinli.ece@duke.edu (X.L.)
Highlights
Battery lifetime is predicted using
limited data through semi-
supervised learning
The proposed method performs
superior in both accuracy and
interpretability
Economic costs are signiﬁcantly
reduced by lessening the need for
labeled data
Guo et al., Joule 8, 1820–1836
June 19, 2024 ª 2024 Elsevier Inc.
https://doi.org/10.1016/j.joule.2024.02.020
ll


--- Page 2 ---

Article
Semi-supervised learning for explainable
few-shot battery lifetime prediction
Nanlin Guo,1,5 Sihui Chen,2,5 Jun Tao,1,* Yang Liu,3,* Jiayu Wan,4,6,* and Xin Li3,*
SUMMARY
Accurate prediction of battery lifetime is critical for ensuring timely
maintenance and safety of batteries. Although data-driven methods
have made signiﬁcant progress, their model accuracy is often
hampered by a scarcity of labeled data. To address this challenge,
we developed a semi-supervised learning technique named partial
Bayesian co-training (PBCT), enhancing the modeling of battery life-
time prediction. Leveraging the low-cost unlabeled data, our model
extracts hidden information to improve the understanding of the
underlying data patterns and achieve higher lifetime prediction ac-
curacy. PBCT outperforms existing approaches by up to 21.9% on
lifetime prediction accuracy, with negligible overhead for data
acquisition. Moreover, our research suggests that incorporating un-
labeled data into the training process can help to uncover critical
factors that impact battery lifetime, which may be overlooked
with a limited number of labeled data alone. The proposed semi-su-
pervised approach sheds light on the future direction for efﬁcient
and explainable data-driven battery status estimation.
INTRODUCTION
Lithium-ion batteries (LIBs) have been deployed in a wide variety of domains such as
portable electronics and electric vehicles (EVs) for reliable energy supply promoted
by multiple advantages such as high energy density and long lifetime.1–4 As LIBs are
playing critical roles in modern society, their health conditions need to be carefully
managed to guarantee the sustainable and safe operations of the corresponding ap-
plications.5 This motivates extensive study on the estimation of battery health states,
with the prediction of lifetime attracting massive attention, as it is among the most
important key performance indicators (KPIs) of LIBs.6,7 The accurate prediction of
lifetime can be applied to facilitate both manufacturing and usage of LIBs such
that it can be utilized by a manufacturer for sorting high-quality batteries and by
the battery management system (BMS) to forecast the time for maintenance or
change.8,9 In speciﬁc, a manufacturer may desire to know the length of the whole
lifespan of a battery, whereas the BMS prefers to estimate the remaining useful
life (RUL). Conventional battery lifetime prediction approaches tend to establish
an electric circuit equivalent model to represent the physical characteristics of the
battery and predict the battery degradation, and hence lifetime, using various
ﬁltering techniques.10–12 In this line of research, physical and semi-empirical models
have been proposed to clarify the dynamics of lithium batteries during degradation
(e.g., growth of the solid-electrolyte interphase,13,14 lithium plating,15,16 and active
material loss17,18). However, the model-based methods are usually hampered by the
limited representation capability of the electric circuit equivalent models and can
easily be impacted by the cumulative error of ﬁltering techniques when predicting
far future events, thereby leading to inferior prediction accuracy.19
CONTEXT & SCALE
Data-driven methods have been
extensively utilized for battery
lifetime prediction to achieve high
accuracy using only early-cycle
battery testing data. Despite the
offered advances, they are usually
limited by the shortage of data, as
labeled data are often expensive
to obtain owing to the high costs
of testing a battery to its end of
life. To tackle this challenge, this
work proposes an innovative
semi-supervised learning-based
solution, which incorporates
external information from massive
unlabeled data to facilitate the
training of a prediction model.
While semi-supervised learning
can substantially improve
prediction accuracy, we found
that it can also help with
understanding the
electrochemical principles of
battery degradation by precisely
recognizing the features with
physical importance. Most
importantly, the proposed
method can signiﬁcantly reduce
the economic costs by achieving
equivalent accuracy using less
labeled data compared with fully
supervised methods.
1820 Joule 8, 1820–1836, June 19, 2024 ª 2024 Elsevier Inc.
ll


--- Page 3 ---

Recently, data-driven lifetime prediction approaches have gained signiﬁcant popu-
larity; these approaches adopt machine learning techniques to establish the map-
ping of the physical measurements of LIBs to their lifetimes through investigating
the correlations in historical records.20–29 Compared with the conventional model-
based methods, data-driven approaches investigate the advantages of machine
learning to accommodate complex data patterns, thereby substantially improving
the prediction accuracy. Furthermore, they can discover the underlying correlations
between the potential impacting factors and battery lifetime in a proactive fashion,
which explores beyond the experience of human experts and provides valuable in-
sights into the research on LIBs. A major challenge of battery lifetime prediction is
that one usually aims at making an accurate prediction at an early stage, before se-
vere degradation of capacity, to meet the needs of real-world applications. To reach
this target, the prediction power of discharging capacity curve has been studied in
Severson et al.,20 which demonstrates that a prediction error of 9.1% can be achieved
through features derived from using the ﬁrst 100-cycle data. Furthermore, electro-
chemical impedance spectroscopy (EIS) has been investigated in Zhang et al.26
and Jones et al.,27 which is found to be an informative feature for early-stage lifetime
prediction associated with the Gaussian process regression model. These achieve-
ments have made revolutionary progress that can enable the timely estimation of bat-
tery health state with substantially lower costs for data acquisition. Based on the
aforementioned advances, succeeding works have also been devoted to the utiliza-
tion of modern machine learning models, such as support vector regression,30 neural
networks (NNs),31,32 and XGBoost33 to further enhance the prediction accuracy. An
accurate machine learning model for battery lifetime prediction usually needs to
be trained using a sufﬁcient amount of labeled data. An example is shown in Fig-
ure 1A, where the prediction error increases rapidly when the number of available
batteries for extracting training data reduces. However, it can be both time- and
cost-intensive to obtain the lifetime of even a single battery, and hence, the models
for battery lifetime prediction have to be trained using limited data samples in most
real-world scenarios. For instance, it may take at least 20 days to measure the lifetime
of a battery (about 1,000 cycles) using one battery testing channel.20 In addition, the
degradation patterns inside a lithium battery can be sensitive to multiple external fac-
tors such that data collected under different conditions may not share exactly the
same set of impacting features. This further increases the need for appropriate tech-
nologies for accurate learning using insufﬁcient data, since different datasets cannot
be directly used to train a single model, even within the same type of batteries.
In order to train an accurate battery lifetime prediction model with a limited number
of labeled data, regularization,34,35 and transfer learning36–38 have been studied in
the literature (Figure 1B). In general, these methods tackle the difﬁculty of data
shortage through involving knowledge from external sources for complementation.
In speciﬁc, the strategy of regularization techniques is to assume a prior statistical
distribution of model parameters (e.g., Gaussian and Laplacian distributions for
L1- and L2-norm regularization, respectively). By contrast, transfer learning methods
deﬁne the prior distribution based on the models trained in similar/related tasks.
Although these approaches can enable effective learning through a lesser amount
of data, they still have a number of limitations. As the regularization techniques
rely on the hand-crafted statistical assumption of model parameters, they can hardly
capture the complicated characteristics of real-world data. Although transfer
learning methods incorporate the knowledge from related source domains, the
gap between source and target domains remains a challenging issue to resolve.
Furthermore, the availability of data or model from related source domain cannot
be guaranteed in practice.
1State Key Laboratory of Integrated Chips and
Systems, School of Microelectronics, Fudan
University, Shanghai 200433, China
2Department of Mechanical and Energy
Engineering, Southern University of Science and
Technology, Shenzhen 518055, China
3Data Science Research Center, Duke Kunshan
University, No. 8 Duke Avenue, Kunshan, Jiangsu
Province 215316, China
4Global Institute of Future Technology, Shanghai
Jiao Tong University, No. 800 Dongchuan Road,
Shanghai 200240, China
5These authors contributed equally
6Lead contact
*Correspondence: taojun@fudan.edu.cn (J.T.),
yang.liu2@dukekunshan.edu.cn (Y.L.),
wanjy@sjtu.edu.cn (J.W.),
xinli.ece@duke.edu (X.L.)
https://doi.org/10.1016/j.joule.2024.02.020
ll
Joule 8, 1820–1836, June 19, 2024 1821
Article


--- Page 4 ---

Apart from the aforementioned techniques, another important way for learning with
insufﬁcient data is directly expanding the training dataset using data augmentation.
In this research direction, generative models are widely utilized to create synthetic
data based on the statistical distributions of real data.30 To reach this goal, a variety
of algorithms such as generative adversarial network (GAN),39 variational auto-
encoder (VAE),40 and diffusion models41 have been developed based on speciﬁc theo-
retical foundations. For instance, fast gradient sign method (FGSM) and GAN have
been utilized in Roman et al.,30 Qiu et al.,42 and Yang et al.,43 to generate synthetic
data for training the estimation models of state of health and state of charge, which
are highly relevant to the prediction of battery lifetime. Despite the advances offered,
the efﬁcacy of these methods is limited by the small data size as well since the core of
them are essentially machine learning models, which can be easily impacted by insuf-
ﬁcient training data. Furthermore, the target of generative models is usually maxi-
mizing the similarity between generated and real data other than minimizing the pre-
diction error.44 The recent popularity of human-in-loop artiﬁcial intelligence (AI) has
promoted the utilization of active learning methods45 for modeling with insufﬁcient
data, which usually mines the unlabeled data with high value and annotates them to
diversify the training data. A major limitation of active learning approaches is that
they will involve extra costs for annotation. Furthermore, the data samples are not
guaranteed to improve the modeling accuracy either, due to the gap between the met-
rics for data selection and predictive modeling, which is similar to generative models.
D
Partial-view
model
Large amount of
unlabeled data
Better trained
complete-
view model
Side
information
Few labeled
data
Model error increases
dramatically when 
there is only few
labeled data
560
A
Prior 
knowledge
Pretrained
model
Better trained model
Low-accuracy
model
Additional information
More 
labeled
data
B
Few labeled
data
Existing methods
Our method
C
Less cost and more common scenario
560
792
472
560
792
472
560
Figure 1. Background
(A) The prediction error of machine learning models increases sharply as the number of labeled samples for training decreases.
(B) Schematics of existing methods for battery life prediction: training with limited and expensive labeled data with low model accuracy and state-of-
the-art solutions with regularization or transfer learning algorithms.
(C) The RMSE results of PBCT and conventional Lasso method, in which the 20% improvement is attributed to unlabeled data.
(D) Schematic of PBCT method, in which a small partial-view model is utilized to extract side information from unlabeled data to help better train the
complete-view model. Our model enables high prediction accuracy even with only a small amount of labeled data, with unlabeled data added for co-
training with minimal overhead.
ll
1822 Joule 8, 1820–1836, June 19, 2024
Article


--- Page 5 ---

In order to tackle these challenges, this work proposes utilizing unlabeled data for
few-shot battery lifetime prediction. In the battery lifetime prediction scenario, un-
labeled data refer to the battery testing records without measurements of lifetime.
In fact, vast unlabeled data are available in a broad variety of scenarios for LIB
manufacturing, usage, and maintenance but have long been ignored for the
modeling of battery lifetime prediction. Unlabeled data have a number of advan-
tages, compared with external source knowledge, including (1) the extensive avail-
ability in practical scenarios and (2) consistent data pattern without incorrect
assumptions and cross-domain gaps. The common method to extract useful infor-
mation from unlabeled data to help model training is semi-supervised learning,
which usually estimates pseudo labels of the unlabeled data, using the model
trained on labeled data, and moves the high-conﬁdence ones into the labeled data-
set, to gradually enhance the prediction model.46 It has been used in multiple do-
mains such as speech recognition47 and object detection.48 However, the applica-
tion of semi-supervised learning for battery lifetime prediction is still rare.
In this work, a speciﬁc semi-supervised learning technique named partial Bayesian
co-training (PBCT)49 is utilized to facilitate the modeling of battery lifetime predic-
tion through extracting informative patterns from unlabeled data. It establishes a
partial-view model to generate initial lifetime estimations on unlabeled batteries,
which provides a guideline for the complete-view model to sufﬁciently learn the
impact of all input features and make a reliable prediction. Experiments have
been conducted on three LIB datasets20 to demonstrate the efﬁcacy of the proposed
PBCT method, where it is proven to outperform the considered baselines by up to
21.9% on battery lifetime prediction accuracy (Figure 1C). Remarkably, the pro-
posed method demonstrates great potential to achieve superior prediction accu-
racy, with reduced data acquisition costs to boot. Furthermore, we ﬁnd that the uti-
lization of unlabeled data can help identify the key impact factors of the battery
lifetime that cannot be discovered from a limited amount of labeled data. It indicates
that the proposed semi-supervised learning-based solution improves the battery
lifetime prediction on both accuracy and explainability.
It is important to note that our goal is not to simply re-implement an existing semi-
supervised learning algorithm from the literature. Instead, the proposed PBCT ﬂow
is speciﬁcally customized for battery life prediction. As the required features can be
measured by the ﬁrst 100 cycles, and the battery lifetime (i.e., the labels) must be
measured by about 1,000 cycles, PBCT is of great efﬁciency in our application of in-
terests, by eliminating the needs of measuring a large number of lifetime values. We
claim that the contribution of this work is to propose a novel solution to achieve a
high accuracy for battery lifetime prediction while maintaining a low economic
cost. To this end, the proposed PBCT method is considered among the best tech-
nical approaches owing to its high efﬁciency in utilizing unlabeled training data
and limited labeled training data and the transparency from which researchers can
draw explainable insights.
RESULTS AND DISCUSSION
The general strategy of the PBCT method is depicted in Figure 1D, where two
models, a partial-view model and a complete-view model, are established, respec-
tively. As a complete-view model considering all the features can easily be impacted
by the overﬁtting issue and can lead to inferior prediction accuracy, a partial-view
model is created based on only a subset of important input features to estimate
the pseudo labels of unlabeled data. Subsequently, it is trained again jointly with
ll
Joule 8, 1820–1836, June 19, 2024 1823
Article


--- Page 6 ---

the complete-view model based on maximum a posteriori optimization, such that
the partial-view model acts as a guideline to help derive the high-performance com-
plete-view model for ﬁnal usage.
The details of the two models are displayed in Figure 2. The complete-view model is
a linear regression model that considers all input features that cannot be fully trained
using a limited number of labeled data. To complement this situation, a linear
regression model that only considers certain important features (partial view) is es-
tablished as a partial model, which can generate a relatively robust estimation of life-
times (pseudo labels) for the unlabeled batteries based on the knowledge learned
from a limited number of labeled data. This enables the complete-view model to
draw useful insights from both labeled and unlabeled data, thereby recognizing
the complicated underlying patterns and achieving a more reliable prediction.
The learning mechanism of partial-view and complete-view models under the
PBCT framework is illustrated by the graphic model depicted in Figure 2C. In the
graphic model, the outputs of the complete-view and partial-view models are
considered as two random variables (i.e., f1 and f2, parameterized by a and b,
respectively) represented by two separate nodes connected to a consensus function
fc, which represents an ideal mapping to the prediction target. Thus, the statistical
distributions of f1 and f2 can be deﬁned based on fc such that f1-fc  N(0, s1
2I) and
f2-fc  N(0, s2
2I), where N(0, s2I) represents the multi-variate Gaussian distribution.
A
B
D
C
Figure 2. Algorithm
(A and B) Schematic and formulation of the two models used in PBCT: the complete-view model is a linear regression model that considers all extracted
features, while the partial-view model is a linear regression model that only considers a subset of features. The feature set is chosen by sequential
forward selection.
(C and D) Schematic and pseudo code illustrate the PBCT process, where a posterior distribution is obtained by co-training of the complete-view and
partial-view models on labeled and unlabeled training data. The parameters of complete-view and partial-view models are solved by maximum a
posterior estimation.
ll
1824 Joule 8, 1820–1836, June 19, 2024
Article


--- Page 7 ---

Considering the prior distributions of a and b, their posterior distributions, given the
observations on the labeled and unlabeled data, can be obtained by applying Bayes’
theorem as
pdfða; bjy; f1L; f2L; f1U; f2UÞ f exp

 u1ky  f1Lk2
2

$ exp

 u2ky  f2Lk2
2

$ exp

 u3kf1L  f2Lk2
2

$exp

 u4kf1U  f2Uk2
2

$ pdfða; bÞ
through which the model parameters a and b can be using the maximum a posteriori
optimization method, as shown in Figure 2C. The complete model is then used to
predict the lifetime of batteries once the model parameters are estimated.
To demonstrate that PBCT can be widely applicable, we conduct experiments on
three datasets with different storage time and slightly different testing conditions.20
The numbers of batteries tested in these datasets are 41 (dataset 1), 43 (dataset 2),
and 40 (dataset 3), respectively, while each dataset contains 20 input features ex-
tracted based on domain knowledge. Based on the practical needs in the real world,
we consider two scenarios in the experiment, namely ofﬂine and online conditions. In
the ofﬂine scenario, one is given a closed set of data, such that the unlabeled data
samples at hand are exactly the ones to be predicted. Thus, the data for testing
are directly utilized as the unlabeled data for training. By contrast, the online sce-
nario deﬁnes an open situation, where the test dataset is not available before the
model is trained. In this scenario, the prediction models need to be trained using
available labeled and unlabeled data and applied to the unknown upcoming data.
Detailed schematics for both ofﬂine and online scenarios can be found in Figure S1.
Based on the aforementioned nature of these setups, we refer to the labeled and un-
labeled data used for model training as labeled training data and unlabeled training
data, respectively, where the test data are unlabeled training data as well in the off-
line scenario. Furthermore, we adopt the logarithm of battery lifetime as the predic-
tion target of models other than predicting the lifetime directly, since it presents
stronger linear correlations with the important features.20 Thus, all the comparisons
in this work are conducted in the logarithm domain. However, one can obtain the
estimation of battery lifetime by applying an inverse logarithmic transform on the
model output.
Performance of complete model in PBCT
The performance evaluation experiments are divided into three sets, where dataset
1, dataset 2, and dataset 3 are used in each set of experiments, respectively. Each set
of experiments is further divided into the ofﬂine and online scenarios. In the ofﬂine
scenario, we ﬁx the number of unlabeled training data and evaluate the prediction
accuracy for the cases given a different number of labeled training data. To imple-
ment this, we randomly chose 25 data samples from the considered dataset as
test data (i.e., unlabeled training data). Subsequently, we randomly sampled 7–15
data samples from the remaining part as labeled training data, where we intend to
observe the improvement of modeling accuracy when the number of labeled
training data increases. The accuracy of the trained model is evaluated using the
root-mean-square error (RMSE) on the test data. In order to alleviate the ﬂuctuation
of testing results induced by random sampling, we repeated each random sampling
of labeled/unlabeled training data combination for 200 trials, such that the reported
RMSE is computed as the median of those in all trials. In the online scenario, we
randomly selected 10 data samples for testing and 7–15 data samples as labeled
training data, while keeping the rest as unlabeled training data, in each trial. As
more randomness will be involved in the online scenario, we increased the number
of repeats to 450 and computed the median of RMSE over the trials. As the numbers
ll
Joule 8, 1820–1836, June 19, 2024 1825
Article


--- Page 8 ---

of labeled training data are scarce in our experimental setup, the classic regression
approaches to handle few-shot scenarios, including Lasso34 and Elastic net,35 are
used as the baselines. The experimental results corresponding to the ofﬂine sce-
narios are shown in Figures 3A–3C, where we can observe that the proposed
PBCT method outperforms the baselines given different numbers of labeled training
data. In speciﬁc, when the number of labeled training data is 10, PBCT outperforms
Lasso by 9.8%, 21.9%, and 18.3%, respectively, on datasets 1–3. A similar trend can
be observed from the experimental results in the online scenario as shown in
Figures 3D–3F, where the PBCT method outperforms the baselines in all cases on
datasets 2 and 3 and in most cases when the number of labeled training samples
is rare on dataset 1. We can also observe from Figure 3 that the test RMSE increases
substantially when the size of labeled training data decreases due to the overﬁtting
issue induced by the shortage of data. However, the prediction error of PBCT in-
creases less rapidly, compared with Lasso and Elastic net, such that it outperforms
the baselines for all cases in ofﬂine scenario and most cases in online scenario. As
the Lasso and Elastic net methods alleviate the overﬁtting issue by regularization
only, PBCT further incorporates extra information from unlabeled training data,
thereby avoiding the potential bias induced by insufﬁcient data and statistical
assumption and demonstrating a superior performance on the robustness to
overﬁtting.
Apart from the classic Lasso and Elastic net models, we have also implemented an
NN model with 2 hidden layers, where each hidden layer contains 10 nodes, as
another baseline due to the recent popularity of deep learning techniques. As the
NN model needs to be trained on limited training data, dropout50 is incorporated
to alleviate the overﬁtting issue. Through comparison with NN, we aimed to demon-
strate that the proposed linear regression-based models can achieve superior
Figure 3. Experimental results on modeling accuracy
(A–F) Experimental results of RMSE vs. number of labeled training data in ofﬂine (A–C) and online
(D–F) scenarios of PBCT and baseline methods on three datasets. Given the same number of
labeled training data, the PBCT method outperforms almost all the baseline methods in both
ofﬂine and online scenarios.
ll
1826 Joule 8, 1820–1836, June 19, 2024
Article


--- Page 9 ---

prediction accuracy in the considered scenarios with limited training data, although
deep learning models are more powerful in investigating complex data patterns. We
have also compared the PBCT method with a classic semi-supervised learning
method named Hessian energy semi-supervised regression (HSSR).51 Through com-
parison with HSSR, we aimed to demonstrate that the PBCT method is among the
best techniques to ﬁt the semi-supervised learning-based solution in this work
because of its high effectiveness to simultaneously utilize unlabeled training data
and limited labeled training data. Furthermore, we also compared it with the
approach using a generative model. Speciﬁcally, we trained a generative model us-
ing VAE, based on available labeled data, to generate synthetic battery testing data.
Subsequently, the synthetic data and real data are simultaneously used to train a
Lasso model for battery lifetime prediction. The VAE model used in this experiment
consists of two NNs with a single hidden layer containing 16 units as encoder and
decoder, respectively. Similar to other approaches, we repeated these baselines
for 200 and 450 random trials, respectively, for ofﬂine and online scenarios. The me-
dian of RMSEs over the trials is shown in Figures 3A–3F. As expected, PBCT outper-
forms NN, HSSR, and Lasso with VAE in all the considered scenarios. Another signif-
icant advantage of PBCT over HSSR is that HSSR can only be applied in the ofﬂine
fashion, where all test data are visible and can be used as unlabeled training data,
due to the limitations of its design strategy. By contrast, the PBCT method can ﬂex-
ibly adapt to a variety of application scenarios to support practical needs in the in-
dustry. Through analyzing the results of Lasso trained using both real and synthetic
data, it is important to note that it even performs worse than Lasso trained with only
real data in many scenarios. Once again, this demonstrates the limitation of gener-
ative models; that is, they can be impacted by the shortage of data and cannot guar-
antee the improvement of accuracy because of the gap between optimization tar-
gets. In addition to the median of RMSEs, we also present a detailed distribution
of the prediction errors, using a boxplot, to demonstrate the prediction robustness
of PBCT, where the median, upper and lower quartiles, and statistical upper and
lower bounds are shown for each case. The corresponding results are depicted in
Figure S2.
Economic analysis
To quantitatively demonstrate the advantages of the proposed PBCT method for
battery life prediction, we analyzed the time and cost for sampling the data required
in each method through the experimental results of the ofﬂine scenarios discussed in
the last section. It can be concluded that to achieve the same accuracy, the PBCT
method requires less labeled training data and a low cycle cost (Figures 4A–4C),
which is estimated by the median of the cycle costs from 200 repeated experiments.
The detailed distribution of the prediction errors, using a boxplot, is also depicted in
Figure S3. For each trial, the cycle cost is obtained by summing up the lifetime of all
labeled training data. The reduced number of cycles signiﬁcantly saves time, cost,
and energy involved in the battery cycling experiments. For fair comparison, we esti-
mated the cost of the cycling experiments by the cost of renting battery cycling
channels. The detailed estimation process of time and economic costs is summa-
rized in Figure S4 and Notes S1 and S2. As shown in Figure 4D, to achieve the target
accuracy RMSE% 0.10, PBCT needs a low cycle cost, compared with the Lasso
method. In dataset 2, to achieve the target accuracy RMSE % 0.10, PBCT requires
7,700.5 cycles (RMSE of 0.099 when the number of cycles is 7,700.5), while Lasso
needs more than 10,537 cycles (RMSE of 0.105 when the number of cycles is
10,537), as shown in Figures 4B and 4E. As a result, simply applying the PBCT algo-
rithm can save up to 28,36.5 cycles, that is, $4,685.1, compared with the Lasso
ll
Joule 8, 1820–1836, June 19, 2024 1827
Article


--- Page 10 ---

method, which is equivalent to 26.9% of the total economic costs for using the Lasso
method.
Explainability analysis
A reliable machine learning model should offer not only the prediction outputs but
also the basis for making the corresponding predictions to help understand the
physical impact of the input factors in practical scenarios, thereby establishing trust
in making important decisions. Although a number of machine learning models are
able to quantitatively analyze the impact of each input feature taking advantage of
the high transparency, another critical issue is to provide a physically understand-
able basis for prediction, namely, generating predictions based on input features
with physical importance. However, this can hardly be accomplished using a
limited set of labeled training data owing to the potential bias for evaluating the
correlations between the input features and regression target. By contrast, our
proposed semi-supervised learning-based solution with PBCT method can simulta-
neously utilize both labeled and unlabeled data for training, which incorporates ex-
tra information to help appropriately identify the features with high importance,
compared with using labeled data alone, and analyze their contributions to the
prediction outputs.
Since the complete-view prediction model of PBCT is a linear regression model,
the interpretability can be achieved by analyzing the importance of each feature
for life prediction through the weight of each feature. To obtain statistically mean-
ingful data, we weightedly summed the absolute values of the model coefﬁcients
in a feature-wise fashion along 200 trials of the ofﬂine-scenario experiments in the
three datasets, where the weight of each trial is the inverse of the corresponding
RMSE. For each trial, we randomly chose 25 data samples from the considered
Table 1 | Saved cost of PBCT over Lasso
Estimated saved 
cycle cost
Estimated saved 
time cost (hour)
Estimated saved 
economic value ($)
dataset1
1373.5
1215.0
2268.6
dataset2
2836.5
2509.2
4685.1
dataset3
4206.0
3720.6
6947.1
A
B
CC
D
E
Figure 4. Economic analysis of PBCT and baseline methods
(A–C) RMSE vs. number of cycles used in labeled training data in ofﬂine scenario with three datasets.
(D) Estimated cycle cost required for PBCT and baseline method to achieve the same accuracy (RMSE = 0.10).
(E) The estimated cost savings of PBCT in terms of cycle cost, time cost, and economic costs.
ll
1828 Joule 8, 1820–1836, June 19, 2024
Article


--- Page 11 ---

dataset as test data (i.e., unlabeled training data). Subsequently, we randomly
sampled 10 data samples from the remaining part as labeled training data. As
shown in Figure 5, the weights of the features C1–C3, C14, and C18 are much
higher than those of the others. In fact, C1–C3 are the minimum value, mean value,
and standard deviation of DQ100–10(V), respectively, while DQ100–10(V) is the differ-
ence of the discharge capacity curves as a function of voltage between the 100th
and 10th cycles. In these three datasets, C1–C3 represent energy dissipation,
which is the key feature and highly correlates with the ﬁnal lifetime.20 Higher en-
ergy dissipation yields a poorer cycle life; hence, they are negatively correlated.
We have successfully rediscovered this point since these three features have
A
B
C
D
Figure 5. Feature analysis and impact of unlabeled training data
(A) Accumulated weight value vs. features plot, where key impacting features, C1–C3, C14, and C18 are identiﬁed.
(B) Test RMSE vs. number of unlabeled training data used for PBCT, where the modeling accuracy improves substantially with increased number of
unlabeled training data.
(C) Impact of unlabeled training data on feature selection, where using more unlabeled training samples shows signiﬁcant improvement in key feature
selection and RMSE.
(D) Global impact of unlabeled training data on feature selection.
ll
Joule 8, 1820–1836, June 19, 2024 1829
Article


--- Page 12 ---

extremely high rankings in accumulated weight values, as shown in Figure 5A. C14
is also a key impacting feature, which describes the battery average charging time
in the ﬁrst ﬁve cycles. As short charging time represents high charging rate, violent
electrochemical reactions,21 and intense side reactions22 in battery, fast charging
would generally shorten the lifetime of battery.23 This indicates that C14 is a crit-
ical feature that positively correlates with battery lifetime. C18 refers to the initial
internal resistance, which can be affected by numerous factors, such as the
manufacturing techniques,52 the inﬁltration state of electrolyte, the formation of
solid electrolyte interphase (SEI),24 etc. Usually, a minimal internal resistance can
contribute signiﬁcantly toward ensuring a long lifetime.25 Even though the three
datasets show multiple variations in external conditions, resulting in the ﬂuctua-
tions of feature weighting across datasets, the proposed PBCT method can stably
identify the critical impacting features (Figure 5) that are signiﬁcant to battery life-
time prediction.
Impact of unlabeled training data
As we mentioned above, the improved model accuracy of PBCT and the ability to
better identify important features are mainly owing to the complementary informa-
tion extracted from the unlabeled training data. For a more intuitive understanding,
we performed additional experiments to quantitatively analyze the effect of unla-
beled training data on modeling accuracy and feature selection in a semi-ofﬂine
setup. In the ﬁrst set of experiments, we intended to analyze the trend of modeling
accuracy as the number of unlabeled training data for training increases. To achieve
this, we randomly chose 10 data samples as the labeled training data and 25 data
samples for testing. Subsequently, six groups of unlabeled training data are picked
from the test data, the number of which increases from 0 to 25 with a stride 5. Similar
to the above experimental setups, the random sampling for each group is repeated
for 100 trials, while the median RMSE of all trials is ﬁnally reported to mitigate the
numerical bias. The experimental results are shown in Figure 5B, where we can
observe that on all three datasets, the RMSE reduces substantially as the number
of unlabeled training data increases. This demonstrates that signiﬁcant improve-
ment can be brought about by incorporating unlabeled training data for enhancing
the modeling accuracy. To present more details, boxplots are used to visualize the
median, upper and lower quartiles, and statistical upper and lower bounds of the
prediction errors for each case, as shown in Figure S5. Apart from the semi-ofﬂine
experiments, the effects for incorporating unlabeled training data on modeling ac-
curacy are also evaluated in a fully online fashion. The experimental setup and similar
results can be found in Note S3 and Figure S6.
In the second set of experiments, we aimed to analyze the impact of incorporating
unlabeled training data on feature selection. To begin our study, we initially con-
ducted supervised learning using 41 labeled data samples, which were rather suf-
ﬁcient. The selected features from this phase serve as a valuable reference for our
subsequent semi-supervised learning, where labeled data are limited. The models
produced low RMSE values and identiﬁed the following key features: C1, C3, C11,
C14, and C18 (Figure S7). These features not only demonstrate signiﬁcant physical
relevance to cycle life but also exhibit substantial overlap with the comprehensive
prediction mentioned earlier. This suggests that these features can serve as reli-
able references for further investigation. For additional information and visual rep-
resentations, please refer to Figure S7. Following this, we utilized ﬁve labeled data
samples and gradually increased the number of unlabeled data samples (0, 5, 10,
15, 20, 25) to train the semi-supervised model. The training process was repeated
199 times. We conducted a comparison of the models, based on their RMSE and
ll
1830 Joule 8, 1820–1836, June 19, 2024
Article


--- Page 13 ---

their corresponding features, as shown in Figure 5C. For the supervised model (un-
labeled dataset to 0, which is essentially Lasso), all the feature weights are so negli-
gible that we were unable to identify any dominant features. However, with the in-
clusion of unlabeled data (up to 15 samples), the semi-supervised models began to
identify relevant features, although the key features that describe energy dissipa-
tion (C1–C3), which is highly related to battery lifetime, were not identiﬁed. Once
the unlabeled data reached 20 points, the key features started to emerge, and the
model exhibited a lower RMSE. Furthermore, with an increase in the unlabeled
data from 20 to 25, not only did the number of distracting features decrease
(C13 and C19 for 20 unlabeled data samples to only C5 for 25 unlabeled data sam-
ples), but the absolute weight value also increased (C1 for 25 and C3 for 20), Fig-
ure S8. In order to globally evaluate the impact of unlabeled data on feature selec-
tion, we observed the frequency with which each feature is selected in the 199
random trials along with the increasing of unlabeled data, which is depicted in Fig-
ure 5D. The ﬁgure clearly shows that when more unlabeled data are involved for
training, the key features (i.e., C1–C3, C14, and C18) are selected with higher fre-
quencies, while the less important features remain rarely selected. This experiment
demonstrates that the inclusion of unlabeled data can indeed facilitate a superior
feature selection process under the circumstances of limited labeled data (Fig-
ure S9). The details of the model weights can be found in Figure S8. In addition,
we have also shown the range of features selected by the partial-view model in
Figure S10.
Perspectives
The successful implementation of the PBCT algorithm in battery lifetime prediction
indicates a potentially highly efﬁcient paradigm for accelerated battery R&D and
manufacturing. In real-world scenarios, a one-size-ﬁts-all protocol rarely exists in
battery R&D since cells are designed and optimized with different electrolytes, elec-
trodes, active materials, etc.52 Similarly, various parameter optimizations are
needed in their manufacturing process, such as coating, drying, and formation con-
ditions.52,53 Therefore, the use of the PBCT method can facilitate fast decision-mak-
ing in the optimization of the vast parameter space required for tailor-made
manufacturing solutions for high-quality products (Figure 6). The impact of changes
in production conditions could be measured by the battery lifetime information fed
back to the management system. PBCT has great potential to accelerate this feed-
back, with reduced battery testing time and costs. Instead of the traditional method
of performing a full-life test on all tested cells, PBCT only requires a small number of
batteries (such as 20%) for a complete-life test. Combining the unlabeled training
data obtained from limited cycle tests of the remaining batteries, a complete model
can be well trained with sufﬁcient accuracy and explainability. This model can quickly
provide feedback information to the decision-maker and greatly accelerate battery
R&D and manufacturing.
Conclusions
The ﬁeld of battery life prediction has seen signiﬁcant advancements thanks to
data-driven approaches. However, statistical models used in existing methods
often struggle to provide accurate predictions when trained with limited labeled
training data. To address this issue, we propose a semi-supervised learning
method named PBCT, which investigates the informative data patterns from a
large amount of low-cost unlabeled training data, thereby facilitating the learning
of complicated correlations and substantially improving the prediction accuracy.
Our experimental results demonstrate that PBCT signiﬁcantly outperforms conven-
tional regularized regression techniques while incurring little to no additional cycle
ll
Joule 8, 1820–1836, June 19, 2024 1831
Article


--- Page 14 ---

cost. Our cost analysis reveals that PBCT can even save a signiﬁcant amount on
economic costs. Moreover, we ﬁnd that incorporating unlabeled training data
for model training can help identify the key factors that impact battery lifetime,
which can hardly be discovered using limited labeled training data alone. Our ﬁnd-
ings facilitate efﬁcient and precise battery state estimation, thereby paving the way
for a sustainable future with energy storage in many applications including electri-
ﬁed transportation and power grids.
EXPERIMENTAL PROCEDURES
Resource availability
Lead contact
Further information and requests for resources should be directed to and will be ful-
ﬁlled by the lead contact, Prof. Jiayu Wan (wanjy@sjtu.edu.cn).
Materials availability
This study did not generate new unique materials.
Data and code availability
The source codes that support the ﬁndings of this study are available at PBCT:
https://github.com/ppguo/PBCT.git (https://doi.org/10.5281/zenodo.10650738).
The data that support the ﬁndings of this study are available at PBCT_data: https://
github.com/ppguo/PBCT_data.git (https://doi.org/10.5281/zenodo.10650760).
Methods
The dataset used in this work is an open-source dataset provided by Severson
et al.,20 which contains 124 LiFePO4/graphite A123 APR18650M1A cylinder batte-
ries with 1.1 Ah nominal capacity. The average lifetime is 806 cycles (ranging from
150 to 2,300). The dataset is divided to three sub-datasets (datasets 1–3) according
to different calendar aging and diverse fast-charging protocols. 20 early-cycle
Figure 6. A schematic shows the perspective of PBCT workﬂow for future accelerated battery R&D and manufacturing
ll
1832 Joule 8, 1820–1836, June 19, 2024
Article


--- Page 15 ---

features extracted from the measurements within the ﬁrst 100 cycles are used for life
prediction (Table S1). All experiments considered in this work are conducted on a
Linux workstation with 112-core Intel Xeon gold 6258R CPUs and 376G RAM. The
PBCT, Lasso, and Elastic net algorithms are implemented using Python3.9, while
the numpy, pandas, scikit-learn, and gurobi packages/tools are utilized for speciﬁc
functionalities.
The philosophy and major steps of the PBCT method are depicted in Figure 2, in
which two linear regression models, a complete-view model and a partial-view
model, are established. The complete-view model considers all the input features
for battery lifetime prediction, while the partial-view model is constructed based
on a subset of important features. As the complete-view model can easily be over-
ﬁtted given a limited number of labeled training data, the partial-view model can
generate a relatively robust estimation for the lifetimes of unlabeled training data
samples. Thus, it serves as a guideline that creates pseudo labels for the unlabeled
training data, which facilitates the complete-view model to be fully trained using the
information extracted from both labeled and unlabeled training data. Finally, the
complete-view model is deployed for the battery lifetime prediction in real-world
applications as it can capture more complicated dynamics by considering all the
input features globally.
A critical task of PBCT is to ﬁnd the representative subset of features for the partial-
view model that can generate reliable predictions through training on a limited num-
ber of labeled training data while avoiding overﬁtting. Therefore, regularization
needs to be applied for the training of partial-view model to ﬁlter out the interfer-
ence of less important features. In speciﬁc, this is achieved by applying the sequen-
tial forward selection method,54 which iteratively selects the most informative
feature, which can further minimize the validation error by combining with the
selected ones, from the candidate set until the pre-deﬁned stopping criterion is
reached. Details of the sequential forward selection method can be found in Note
S4. After the subset of features for constructing the partial-view model is ﬁxed,
the model parameters of complete-view and partial-view models are learned simul-
taneously, based on both labeled and unlabeled training data. The co-training
methodology for the complete-view and partial-view models can be represented us-
ing the graphic model depicted in Figure 2C. In the graphic model, the complete-
view and partial-view models are considered as two groups of random variables
(i.e., f1 and f2) represented by two distinct nodes, which are connected to a
consensus function fc that is further linked to the prediction target y. To achieve
co-learning of the two models on labeled/unlabeled training data, we build PBCT
graphical models. The graphical models specify the relationship between two views
of the data and the target y via a probabilistic link in two cases, as shown in Figure 2C.
The characteristics of each edge in the graphic model can be described using a zero-
mean multivariate Gaussian distribution, such that
fc  f1  N

0; s1
2I

fc  f2  N

0; s2
2I
 ;
(Equation 1)
and
fc  y  N

0; sc
2I

:
(Equation 2)
Furthermore, we denote the parameters of the complete-view and partial-view
models as a and b. Thus, the PBCT graphical mode is deﬁned with hyperparameters
{s1, s2, sc} and the unknown model parameters a and b. Databased on this setup, the
likelihood function of the labeled training data can be formulated as
ll
Joule 8, 1820–1836, June 19, 2024 1833
Article


--- Page 16 ---

pdfðy; f1L; f2Lja; bÞ f exp

 u1ky  f1Lk2
2

$ exp

 u2ky  f2Lk2
2

$exp

 u3kf1L  f2Lk2
2

;
(Equation 3)
while the likelihood function for the unlabeled training data can be formulated as
pdfðf1U; f2Uja; bÞfexp

 u4kf1U  f2Uk2
2

;
(Equation 4)
where the new parameters u1-u4 are deterministic functions of the hyperparameters
{s1, s2, sc}. The forms of the deterministic functions and details for deriving the re-
lationships between those parameters are included in Note S5. Assuming all sam-
ples are generated independently, the likelihood function for all training data,
including both labeled and unlabeled training data, can be represented by:
pdfðy; f1L; f2L; f1U; f2Uja; bÞ f exp

 u1ky  f1Lk2
2

$ exp

 u2ky  f2Lk2
2

$exp

 u3kf1L  f2Lk2
2

$ exp

 u4kf1U  f2Uk2
2

:
(Equation 5)
Based on Bayes’ theorem, the posterior distribution of {a, b} can be computed given
their prior distributions, as shown in Figure 2D. In our experiment, we assume the
parameter of complete-view model a subject to Laplace distribution due to the
sparse nature. Thus, the maximum a posterior estimation of the model parameters
a and b is equivalent to minimizing
Lða; bÞ = u1ky  XL$ak2
2 + u2ky  ZL$bk2
2 + u3kXL$a  ZL$bk2
2
+ u4kXU$a  ZU$bk2
2 + lkak1;
(Equation 6)
where l is the hyperparameter corresponding to the prior distribution of a. The de-
tails on the speciﬁc method to estimate the hyperparameters can be found in Note
S6.
SUPPLEMENTAL INFORMATION
Supplemental information can be found online at https://doi.org/10.1016/j.joule.
2024.02.020.
ACKNOWLEDGMENTS
This work is supported by the startup funding of Shanghai Jiaotong University and its
Global Institute of Future Technology.
AUTHOR CONTRIBUTIONS
Y.L., J.W., and X.L. conceived the idea. Y.L., J.W., X.L., J.T., and N.G. designed the
experiments. Y.L. and X.L. designed the algorithm. N.G. and S.C. performed the ex-
periments and data analysis. All authors discussed and analyzed the results. N.G.,
Y.L., J.W., and X.L. wrote and revised the paper.
DECLARATION OF INTERESTS
The authors declare no competing interests.
Received: June 23, 2023
Revised: September 25, 2023
Accepted: February 26, 2024
Published: March 14, 2024
ll
1834 Joule 8, 1820–1836, June 19, 2024
Article


--- Page 17 ---

REFERENCES
1. Bresser, D., Hosoi, K., Howell, D., Li, H., Zeisel,
H., Amine, K., and Passerini, S. (2018).
Perspectives of automotive battery R&D in
China, Germany, Japan, and the USA. J. Power
Sources 382, 176–178.
2. Dunn, B., Kamath, H., and Tarascon, J.M.
(2011). Electrical energy storage for the grid: A
battery of choices. Science 334, 928–935.
3. Nykvist, B., and Nilsson, M. (2015). Rapidly
falling costs of battery packs for electric
vehicles. Nat. Clim. Change 5, 329–332.
4. Schmuch, R., Wagner, R., Ho¨ rpel, G., Placke, T.,
and Winter, M. (2018). Performance and cost of
materials for lithium-based rechargeable
automotive batteries. Nat. Energy 3, 267–278.
5. Tian, J., Xiong, R., Shen, W., Lu, J., and Yang,
X.-G. (2021). Deep neural network battery
charging curve prediction using 30 points
collected in 10 min. Joule 5, 1521–1534.
6. Sulzer, V., Mohtat, P., Aitio, A., Lee, S., Yeh,
Y.T., Steinbacher, F., Khan, M.U., Lee, J.W.,
Siegel, J.B., Stefanopoulou, A.G., et al. (2021).
The challenge and opportunity of battery
lifetime prediction from ﬁeld data. Joule 5,
1934–1955.
7. Kim, M., Kim, I., Kim, J., and Choi, J.W. (2023).
Lifetime prediction of lithium ion batteries by
using the heterogeneity of graphite anodes.
ACS Energy Lett. 8, 2946–2953.
8. Jiang, B., Gent, W.E., Mohr, F., Das, S., Berliner,
M.D., Forsuelo, M., Zhao, H., Attia, P.M.,
Grover, A., Herring, P.K., et al. (2021). Bayesian
learning for rapid prediction of lithium-ion
battery-cycling protocols. Joule 5, 3187–3203.
9. Hu, X., Xu, L., Lin, X., and Pecht, M. (2020).
Battery lifetime prognostics. Joule 4, 310–346.
10. Guha, A., Patra, A., and Vaisakh, K.V. (2017).
Remaining useful life estimation of lithium-ion
batteries based on the internal resistance
growth model. In Indian Control Conference
(ICC), pp. 33–38.
11. Li, D.Z., Wang, W., and Ismail, F. (2014). A
mutated particle ﬁlter technique for system
state estimation and battery life prediction.
IEEE Trans. Instrum. Meas. 63, 2034–2043.
12. Ahwiadi, M., and Wang, W. (2019). An
enhanced mutated particle ﬁlter technique for
system state estimation and battery life
prediction. IEEE Trans. Instrum. Meas. 68,
923–935.
13. Christensen, J., and Newman, J. (2004). A
mathematical model for the lithium-ion
negative electrode solid electrolyte interphase.
J. Electrochem. Soc. 151, A1977.
14. Pinson, M.B., and Bazant, M.Z. (2013). Theory of
SEI formation in rechargeable batteries:
capacity fade, accelerated aging and lifetime
prediction. J. Electrochem. Soc. 160,
A243–A250.
15. Arora, P., Doyle, M., and White, R.E. (1999).
Mathematical modeling of the lithium
deposition overcharge reaction in lithium-ion
batteries using carbon-based negative
electrodes. J. Electrochem. Soc. 146,
3543–3553.
16. Yang, X.-G., Leng, Y., Zhang, G., Ge, S., and
Wang, C.-Y. (2017). Modeling of lithium plating
induced aging of lithium-ion batteries:
transition from linear to nonlinear aging.
J. Power Sources 360, 28–40.
17. Christensen, J., and Newman, J. (2005).
Cyclable lithium and capacity loss in Li-ion
cells. J. Electrochem. Soc. 152, A818.
18. Zhang, Q., and White, R.E. (2008). Capacity
fade analysis of a Lithiumion cell. J. Power
Sources 179, 793–798.
19. Ng, M.-F., Zhao, J., Yan, Q., Conduit, G.J., and
Seh, Z.W. (2020). Predicting the state of charge
and health of batteries using data-driven
machine learning. Nat. Mach. Intell. 2, 161–170.
20. Severson, K.A., Attia, P.M., Jin, N., Perkins, N.,
Jiang, B., Yang, Z., Chen, M.H., Aykol, M.,
Herring, P.K., Fraggedakis, D., etal. (2019). Data-
driven prediction of battery cycle life before
capacity degradation. Nat. Energy 4, 383–391.
21. Weng, C., Cui, Y., Sun, J., and Peng, H. (2013).
On-board state of health monitoring of lithium-
ion batteries using incremental capacity
analysis with support vector regression.
J. Power Sources 235, 36–44.
22. Weng, C., Feng, X., Sun, J., and Peng, H. (2016).
State-of-health monitoring of lithium-ion
battery modules and packs via incremental
capacity peak tracking. Appl. Energy 180,
360–368.
23. Berecibar, M., Garmendia, M., Gandiaga, I.,
Crego, J., and Villarreal, I. (2016). State of
health estimation algorithm of LiFePO4 battery
packs based on differential voltage curves for
battery management system application.
Energy 103, 784–796.
24. Berecibar, M., Devriendt, F., Dubarry, M.,
Villarreal, I., Omar, N., Verbeke, W., and Van
Mierlo, J. (2016). Online state of health
estimation on NMC cells based on predictive
analytics. J. Power Sources 320, 239–250.
25. Richardson, R.R., Birkl, C.R., Osborne, M.A.,
and Howey, D.A. (2019). Gaussian process
regression for in situ capacity estimation of
lithium-ion batteries. IEEE Trans. Ind. Inform.
15, 127–138.
26. Zhang, Y., Tang, Q., Zhang, Y., Wang, J.,
Stimming, U., and Lee, A.A. (2020). Identifying
degradation patterns of Lithiumion batteries
from impedance spectroscopy using machine
learning. Nat. Commun. 11, 1706.
27. Jones, P.K., Stimming, U., and Lee, A.A. (2022).
Impedance-based forecasting of lithium-ion
battery performance amid uneven usage. Nat.
Commun. 13, 4806.
28. Ding, R., Wang, R., Ding, Y., Yin, W., Liu, Y., Li,
J., and Liu, J. (2020). Designing AI-aided
analysis and prediction models for nonprecious
metal electrocatalyst-based proton-exchange
membrane fuel cells. Angew. Chem. 132,
19337–19345.
29. Lin, C.P., Cabrera, J., Yu, D.Y.W., Yang, F., and
Tsui, K.L. (2020). SOH estimation and SOC
recalibration of lithium-ion battery with
incremental capacity analysis & cubic
smoothing spline. J. Electrochem. Soc. 167,
090537.
30. Roman, D., Saxena, S., Robu, V., Pecht, M., and
Flynn, D. (2021). Machine learning pipeline for
battery state-of-health estimation. Nat. Mach.
Intell. 3, 447–456.
31. Wu, B., Han, S., Shin, K.G., and Lu, W. (2018).
Application of artiﬁcial neural networks in
design of lithium-ion batteries. J. Power
Sources 395, 128–136.
32. Li, P., Zhang, Z., Xiong, Q., Ding, B., Hou, J.,
Luo, D., Rong, Y., and Li, S. (2020). State-of-
health estimation and remaining useful life
prediction for the lithium-ion battery based on
a variant long short term memory neural
network. J. Power Sources 459, 228069.
33. Jafari, S., and Byun, Y.C. (2022). XGBoost-
based remaining useful life estimation model
with extended Kalman particle ﬁlter for lithium-
ion batteries. Sensors (Basel) 22, 9522.
34. Mansouri, S.S., Karvelis, P., Georgoulas, G.,
and Nikolakopoulos, G. (2017). Remaining
Useful Battery Life Prediction for UAVs based
on Machine Learning*. IFAC-Pap. 50,
4727–4732.
35. Zou, H., and Hastie, T. (2005). Regularization
and variable selection via the elastic net. J. R.
Stat. Soc. B 67, 301–320.
36. Che, Y., Deng, Z., Lin, X., Hu, L., and Hu, X.
(2021). Predictive battery health management
with transfer learning and online model
correction. IEEE Trans. Veh. Technol. 70,
1269–1277.
37. Pan, D., Li, H., and Wang, S. (2022). Transfer
learning-based hybrid remaining useful life
prediction for lithium-ion batteries under
different stresses. IEEE Trans. Instrum. Meas.
71, 1–10.
38. Che, Y., Stroe, D.I., Hu, X., and Teodorescu, R.
(2023). Semi-supervised self-learning-based
lifetime prediction for Batteries. IEEE Trans.
Ind. Inform. 19, 6471–6481.
39. Goodfellow, I., Pouget-Abadie, J., Mirza, M.,
Xu, B., Warde-Farley, D., Ozair, S., Courville, A.,
and Bengio, Y. (2014). Generative adversarial
nets. In Advances in Neural Information
Processing Systems, 27.
40. Kingma, D.P., and Welling, M. (2014). Auto-
encoding variational bayes. In Proceedings of
the International Conference on Learning
Representations.
41. Rombach, R., Blattmann, A., Lorenz, D., Esser,
P., and Ommer, B. (2022). High-resolution
image synthesis with latent diffusion models. In
Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition,
pp. 10674–10685.
42. Qiu, X., Wang, S., and Chen, K. (2023). A
conditional generative adversarial network-
based synthetic data augmentation technique
for battery state-of-charge estimation. Appl.
Soft Comput. 142, 110281.
43. Yang, G., Ma, Q., Sun, H., and Zhang, X. (2022).
State of health estimation based on GAN-
LSTM-TL for lithium-ion batteries. Int. J.
Electrochem. Sci. 17, 221128.
44. Zheng, C., Wu, G., and Li, C. (2023). Toward
understanding generative data augmentation.
ll
Joule 8, 1820–1836, June 19, 2024 1835
Article


--- Page 18 ---

In Advances in Neural Information Processing
Systems, 36.
45. Zhu, R., Chen, Y., Peng, W., and Ye, Z.S. (2022).
Bayesian deep-learning for RUL prediction: an
active learning perspective. Reliab. Eng. Syst.
Saf. 228, 108758.
46. Chapelle, O., Scho¨ lkopf, B., and Zien, A. (2006).
Semi-supervised Learning (The MIT Press).
47. Karita, S., Watanabe, S., Iwata, T., Delcroix, M.,
Ogawa, A., and Nakatani, T. (2019). Semi-
supervised end-to-end speech recognition
using text-to-speech and autoencoders. In
ICASSP 2019–2019 IEEE International
Conference on Acoustics, Speech and Signal
Processing (ICASSP), pp. 6166–6170.
48. Jeong, J., Lee, S., Kim, J., and Kwak, N.
(2019). Consistency-based semi-supervised
learning for object detection. In Advances
in Neural Information Processing
Systems, 32.
49. Nguyen, C.M., Li, X., Blanton, R.D., and Li, X.
(2020). Partial Bayesian co-training for virtual
metrology. IEEE Trans. Ind. Inform. 16,
2937–2945.
50. Srivastava, N., Hinton, G., Krizhevsky, A.,
Sutskever, I., and Salakhutdinov, R. (2014).
Dropout: A simple way to prevent neural
networks from overﬁtting. J. Mach. Learn. Res.
15, 1929–1958.
51. Kim, K., Steinke, F., and Hein, M. (2009).
Semi-supervised regression using hessian
energy with an application to semi-
supervised dimensionality reduction. In
Advances in Neural Information Processing
Systems, 22.
52. Liu, Y., Zhang, R., Wang, J., and Wang, Y.
(2021). Current and future lithium-ion battery
manufacturing. iScience 24, 102332.
53. Weng, A., Mohtat, P., Attia, P.M., Sulzer, V.,
Lee, S., Less, G., and Stefanopoulou, A. (2021).
Predicting the impact of formation protocols
on battery lifetime immediately after
manufacturing. Joule 5, 2971–2992.
54. Pudil, P., Novovicova´, J., and Kittler, J. (1994).
Floating search methods in feature selection.
Pattern Recognit. Lett. 15, 1119–1125.
ll
1836 Joule 8, 1820–1836, June 19, 2024
Article
