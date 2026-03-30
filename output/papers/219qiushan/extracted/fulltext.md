# Page 1

Interpretable Molecular Dynamics–Machine 
Learning Framework for Hydrogen Uptake 
Mechanism in Magnesium 
Qiushan Huang1, a, Zhi-Qian Zhang2, b, Yue Cui1, c 
1National University of Singapore, Singapore 
2Institute of High Performance Computing, A*STAR Research Entities, Singapore, 138632 
aqiushan@u.nus.edu, bzhangz@a-star.edu.sg, ccuiyue@nus.edu.sg 
Abstract. We present an interpretable molecular dynamics-machine learning (MD-ML) study 
that investigates the effects of surface accumulation, history-dependent kinetics, and dislocation 
structure in shaping the staged hydrogen uptake kinetics of magnesium. Using molecular dy-
namics simulation, Mg spheres with specified dislocation networks are subjected to external H 
injection under different programmed temperature schedules and initial external hydrogen 
pressure, yielding hydrogen uptake time series across various temperatures, external hydrogen 
pressure and dislocation structure conditions. The MD model predicts a 26% volumetric expan-
sion of magnesium, which is consistent with experimental observation of approximate 30% 
volume expansion from Mg to MgH2. The simulation results reveal a three-stage hydrogen 
uptake mechanism of "surface accumulation - accelerated bulk diffusion - stabilized bulk diffu-
sion" into Mg. The diffusion rate is found to depend on temperature, external hydrogen pres-
sure, and dislocation structure. A transformer machine learning model is developed to predict 
the hydrogen uptake rate using 29 physical variables. The model achieves excellent prediction 
with R2=0.9925, RMSE=1.985×10−2. Interpretability analyses identify that hydrogen uptake 
rate is history-dependent and external hydrogen pressure as the dominant drivers, with screw-
dislocation also exerting a significant influence on the diffusion rate. These results provide 
important and novel insights on the hydrogen uptake mechanism in Mg and furnish quantitative 
guidance for microstructure engineering for effective solid-state hydrogen storage. 
Keywords: Molecular Dynamics Simulation, Solid State Hydrogen Storage, Hydrogen Uptake 
Rate, Dislocation Structure, Machine Learning, Transformer, Time series forecasting 
1 
Introduction 
Hydrogen is widely regarded as a key component of future energy systems owing to 
its cleanliness and renewability. In the context of solid-state hydrogen storage (SSHS), 
magnesium and its hydride (MgH2) have long attracted attention because of their high 
gravimetric storage capacity and low cost [1]. Experimental and theoretical studies 
show that the early formation of a surface MgH2 hydride layer during the hydrogen 
uptake process suppresses bulk hydrogen diffusion since the diffusion of hydrogen in 
MgH2 layer is significantly slower than that in Mg [2-4]. This results the accumulation 
of hydrogen atoms surrounding Mg surface before bulk diffusion takes place [4]. 
Hence, a three-stage uptake mechanism of "surface accumulation - accelerated bulk 
diffusion - stabilized bulk diffusion" is commonly reported from experiment [4-5].

# Page 2

2 
Meanwhile, dislocations in the microstructure may provide a fast diffusion channel 
[6]. The presence of dislocation changes the local stress field and interface nucleation 
dynamics due to hydrogen-dislocation interactions [7-8]. Existing hydrogen uptake 
models by Jander, Chou, and JMAK [9-11] which describe the average behavior us-
ing classical mechanism equations, did not consider the effect of dislocation structure 
and the mechanism of stage transitions and history-dependent kinetics during the 
uptake process. Understanding these factors are essential for realistic modeling of the 
hydrogen uptake process in Mg, which in turn has direct significance for improving 
hydrogen uptake rate by microstructure design and optimizing hydrogen storage per-
formance. 
To address these issues, we develop an integrated molecular dynamic (MD)–
machine learning (ML) framework, aiming to reveal the influence of dislocation 
structure on the Mg hydrogen uptake behaviour. With large-scale MD simulation data 
and algorithms paying specific attention to the stage transitions and history-dependent 
kinetics, this statistically robust and physically interpretable predictive model accu-
rately quantifies the three-stage uptake process and the relationship between disloca-
tion structure and hydrogen uptake rate. It offers a transferable modeling paradigm for 
subsequent microstructure engineering and process optimization for experimental 
systems. 
2 
Molecular Dynamics Simulation 
2.1 
Simulation setup 
All MD simulations were performed using the Large-scale Atomic/Molecular Mas-
sively Parallel Simulator (LAMMPS). We employed an angular-dependent potential 
(ADP) for the Mg–H interactions [12]. Mg spheres with radius of 2 nm to 25 nm were 
generated as the initial configuration shown in Fig. 1a (top). This sphere was placed at 
the center of a cubic simulation box with periodic boundaries and vacuum space 
around it. 
 
Fig. 1. (a) Typical initial pristine HCP magnesium configuration (top) and amorphous magnesium 
configuration at 1300 K (bottom). (b) Final dislocation network configuration at 300 K (blue line: 
screw dislocation, red line: edge dislocation). (c) 2-dimensional section view of the initial hydrogen 
injection (top), and final equilibrium uniform hydrogen distribution (bottom).

# Page 3

3 
To generate an array of different realistic dislocation structures inside the Mg spheres, 
we employed a stochastic thermal-quenching procedure, where different dislocation 
network structures are formed when different Gaussian-distributed initial velocities 
are assigned to all atoms at the beginning of the thermal-quenching process. The tem-
perature is increased instantaneously to 1300 K (above the melting point of Mg) for 
the simulation box, and kept constant for 1 ns, resulting an amorphous Mg structure 
depicted in Fig. 1a (bottom). The system was then cooled to 300 K over 10 ns at a 
cooling rate of 1×10¹² K/s under NVT ensemble. This rapid quenching and solidifica-
tion process results polycrystalline Mg with dislocation networks. Fig. 1b shows the 4 
typical dislocation networks among the 380 of Mg sphere final configurations at 300 
K prepared from the stochastic thermal-quenching procedure. Crystal structures and 
dislocations are identified using Dislocation Extraction Algorithm (DXA) method 
[13]. The final configurations can be grouped into 3 categories, namely edge-
dominated, screw-dominated, and mixed-type based on the fraction of screw disloca-
tion as shown in Fig. 1b.  
Hydrogen atoms are added into the system for the simulation of hydrogen uptake 
in Mg. The number of H atoms added is 1.99 times the number of Mg atoms in the 
sphere, such that the stoichiometric coefficient x is approaching 2 in MgHx, ensuring 
the MgH2 configuration is achieved when Mg fully absorbs H. The hydrogen atoms 
are injected into a controllable space located near the simulation box boundary, estab-
lishing an initial high-concentration H reservoir close to the boundary as shown in Fig. 
1c (top). After equilibration at 300 K for 0.5ns, the boundary of the H reservoir was 
opened, allowing H atoms to diffuse rapidly throughout the simulation box under an 
NVT ensemble. This process established a uniform distribution of H atoms through-
out the box with approximately uniform initial external H pressure, as shown in Fig. 
1c (bottom). To impose different target initial external H pressures, the simulation 
box size is changed following the ideal gas law of P= nkBT/V. As hydrogen was taken 
into Mg, the subsequent instantaneous external H pressure decreased naturally, mim-
icking Sieverts device for the consumption of hydrogen from a finite reserve [14]. 
During the hydrogen uptake process, the temperature of the whole system was gradu-
ally increased, kept constant at various levels and then decreased back to 300 K, as 
shown in Fig. 2a, to investigate the effect of temperature on the hydrogen uptake rate. 
Each uptake process lasted 8~12 ns, which, under most conditions, enabled the major-
ity of the Mg sphere to convert to MgH2 within the specified time. 
 
Fig. 2. (a) Illustration of commonly used temperature time history curves. (b) Typical atomic config-
uration for the three-stage hydrogen uptake process with surface accumulation (left), accelerated bulk 
diffusion (middle), and stabilized bulk diffusion (right) (Blue spheres = H; Red spheres = Mg). (c) 
The evolution of H layer volume in the Mg sphere under different temperature and initial external H 
pressure conditions.

# Page 4

4 
2.2 
Hydrogen Uptake Mechanism 
A three-stage hydrogen uptake process is observed for nearly all simulations except in 
cases with extremely low initial external H pressure. This three-stage uptake process 
can be quantified by the H layer volume which is the volume difference between the 
Mg sphere and the Mg + H layer sphere. The hydrogen first accumulates on the Mg 
sphere surface forming a thin MgH2 layer as shown in Fig. 2b. Such accumulation can 
be reflected by the sharp increase of H layer volume demonstrated in Fig. 2c, limiting 
the diffusion of H into the bulk Mg. After significant amount of H atoms accumulated, 
the H atoms overcome the surface barrier and bulk diffusion occurs into Mg interior 
accompanied by the volume expansion of the Mg surface region and an increase in 
atomic spacing. This bulk diffusion can be further divided into accelerated diffusion 
stage and stabilized diffusion stage, as shown in Fig. 2b. The decrease of H layer 
volume after reaching peak value in Fig. 2c marks the net bulk diffusion stage, with 0 
final H layer volume indicating the depletion of the accumulated H layer due to com-
plete H bulk diffusion at the surface, marking a transition to the stabilized bulk diffu-
sion stage exclusively within the Mg interior. This three-stage uptake mechanism of 
surface accumulation, accelerated bulk diffusion and stabilized bulk diffusion agrees 
well with the shell effect experimental observations [4,15], qualitatively verifying the 
MD model in this work. Meanwhile, volumetric expansion of 26% is observed for the 
Mg sphere, which is consistent with experimental findings [5]. 
Temperature and initial external H pressure play an important role in the mecha-
nism of initial surface accumulation. It can be observed that moderate temperature 
and initial external H pressure produce a higher H layer volume as shown in Fig. 2c, 
suggesting a stronger accumulation effect. At the same initial external H pressure 
shown in Fig. 2c (left), a lower temperature typically results a more pronounced sur-
face accumulation. However, once the temperature increases above a certain threshold, 
the effect of temperature is not dominant. At a high temperature of 600 K, the highest 
H layer volume occurs at moderate initial external H pressure of 20 atm demonstrated 
from Fig. 2c (right). This is because the accumulation rate of H on the Mg surface is 
significantly slower than the bulk diffusion rate into the sphere when the initial exter-
nal hydrogen pressure is low, and the temperature is high. Conversely, when the ini-
tial external hydrogen pressure is high, despite higher deposition rate of H atoms on 
the Mg surface assisted by the high instantaneous pressure, diffusion rate of H into the 
bulk Mg is also higher since H atoms overcome more readily the surface barrier due 
to the combined effect of high instantaneous pressure and temperature, making the 
surface accumulation less apparent. 
2.3 
Hydrogen Uptake Rate (HUR) 
Fig. 3a plots the temporal evolution of the total hydrogen uptake, represented by the 
stoichiometric coefficient x in MgH2, under various initial external H pressures while 
the system temperature is increased to 600 K. At the initial stage (0-0.5 ns), H is in-
jected into the H reservoir, and the Mg sphere remains isolated without contact with H. 
Subsequently (at 0.5 ns), hydrogen begins to diffuse rapidly and is taken by the Mg 
sphere. The stoichiometric coefficient x increases faster with higher initial external H

# Page 5

5 
pressure. When diffusion is complete, the stoichiometric coefficient x reaches 2, con-
sistent with the requirements of the interatomic potential used in our simulation.  
 
Fig. 3. (a) Temporal evolution of total hydrogen-uptake at 600 K under various initial external H 
pressure. (b) Evolution of hydrogen uptake rate and instantaneous external H pressure at 300 K under 
various initial external H pressure. (c) Evolution of hydrogen uptake rate at 10 atm under various 
temperatures. (d) Comparison of dislocation networks (blue line: screw dislocation, red: edge dislo-
cation) and corresponding hydrogen uptake rate. 
The hydrogen uptake rate (HUR) is defined as the slope of the total hydrogen uptake 
curve in Fig. 3a. Fig. 3b shows the HUR (solid lines, left axis) and instantaneous ex-
ternal H pressures (dotted lines, right axis) for five initial external H pressures of 5, 10, 
15, 20, and 30 atm at 300 K. We observe that the HUR often exhibits two distinct 
peaks. The first peak correspond to the initial diffusion stage when initial external H 
pressure is high. The second peak occurs after the instantaneous external H pressure 
has decreased for a period of time. Notably, the HUR keeps rising for several 
timesteps before reaching the second peak while the instantaneous external pressure is 
already falling—an effect most pronounced at lower initial external pressures—
indicating that the kinetics are governed not only by the instantaneous external pres-
sure but also by the evolving surface hydride morphology during the Mg–H interac-
tion, possibly related to crack-assisted permeation reported for Mg thin films [3,16]. 
Temperature also has a strong effect on HUR. At a given nominal initial external H 
pressure of 10 atm, heating leads to a pronounced increase in the HUR from 300 K to 
500 K (Fig. 3c). However, the temperature effect becomes insignificant beyond 500 K, 
showing that the process is no longer strongly controlled by temperature. 
A statistical survey of models with varying dislocation lengths, types, and spatial 
arrangements reveals that the geometric character of dislocations has a pronounced 
impact on hydrogen uptake. As shown in Fig. 3d, a sphere with a total dislocation 
length of ~621 Å and an interwoven network exhibits a higher HUR than a counter-
part with ~981 Å of more uniformly aligned dislocations, especially in the accelerated 
diffusion stage. This indicates that dislocation type and distribution, rather than length 
alone, dominate the effectiveness of diffusion pathways.

# Page 6

6 
3 
Machine Learning Model 
3.1 
Methodology 
The machine learning model consists of a short-window Transformer encoder with an 
MLP regressor, optimized with a physics-aware loss that incorporates a mean-squared 
error, a non-negativity penalty, and a stabilized variance-weighted term, as shown in 
Fig. 4. We aggregate time series from MD simulations of Mg spheres into a multivar-
iate dataset with 29 physical variables, including temperature, instantaneous external 
H pressure, H concentrations in the simulation box, x in MgHx, surface and volume 
of both Mg and Mg+H spheres, and dislocation structure such as lengths, densities, 
and geometric fractions. The prediction target is the HUR, formulated as a single-
output regression. To capture stage transitions, we combine Pruned Exact Linear 
Time (PELT) segmentation with the physical parameter H layer volume, and change-
point-aware weighting is placed on samples near change points to emphasize stage 
transitions. Meanwhile, Nonlinear Autoregressive with eXogenous inputs (NARX) 
lags encode uptake history, embedding the inertia and memory effects that character-
ize hydrogen uptake. These design choices capture stage transitions and temporal 
inertia, yielding a framework more closely aligned with physical observations than 
conventional sequence models. 
 
Fig. 4. A NARX-augmented Transformer forecasting architecture. Raw time series are annotated by 
stage, divided into windows, standardized, and augmented with lagged ground-truth inputs according 
to the NARX (mechanism B). A Transformer encoder is followed by an MLP to predict the next 
value HUR(t+1). Training uses a variance-weighted MSE (via clipped log-variance) with change-
point-aware per-sample weights w(t) (Mechanism A) and a non-negativity penalty. Evaluation in-
volves RMSE and  under teacher-forcing one-step evaluation with group-by-file shuffle splits, along 
with SHAP and attention maps for interpretability. 
The joint train/test scatter plot in Fig. 5a nearly coincides with the identity line, with 
R2=0.9948 
and 
RMSE=1.715×10−2 
for 
training 
and 
R2=0.9925 
and 
RMSE=1.985×10−2 for testing, indicating close alignment between the ML predic-
tions and the MD ground truth for HUR across the full dynamic range. Residuals are 
narrowly distributed and strongly concentrated around zero (Fig. 5b), indicating that 
prediction errors are minimal and largely unbiased. Such consistent accuracy is

# Page 7

7 
achieved by two key mechanisms that consider stage transitions and history depend-
ency, as detailed in the Methodology section. 
 
Fig.5. (a) Joint train/test scatter plot of predicted versus true HUR. (b) Histogram of prediction resid-
uals, with the red line indicating zero prediction error. 
We further predict the HUR time history using the ML model. Each ML predicted 
HUR at current step was recursively fed back as the NARX-lag input for the subse-
quent step, while the remaining input variables were kept at their ground truth values. 
Fig. 6a illustrates a representative case for the majority of samples. The prediction is 
excellent with high R2 value. The overall trend of the curve shows good agreement 
with the ground truth and the change points of HUR are well captured. However, the 
predicted curve is over-smoothed, failing to account for local fluctuations. The R2 for 
this recursive prediction is relatively lower than the one-step-ahead prediction due to 
error accumulation. The model also shows great generalizability. To enable fair cross-
sample comparison, we introduce a peak-normalized metric, NRMSEpeak. When test-
ing on a large dimension sphere (Fig. 6b), the ground truth HUR shows a different 
trend not seen before in the training dataset, yet excellent prediction capturing the 
trend and change point with relatively high R2 and NRMSEpeak is achieved. This 
means that rather than pure time-history relationship, the ML model learns some un-
derlying physics to predict the trend not seen before. The ML model has the potential 
to be generalized across different length scales. 
 
Fig.6. ML predicted HUR time history curves of the test set for (a) a typical case. (b) a larger-size 
Mg sphere not in the training set. (blue line: ground truth time history; orange line: ML predicted 
time history)  
Overall, the model demonstrates robust predictive accuracy and great generalizability, 
accounting for the effects of dislocation structure, temperature, and pressure condi-
tions. This capability enables rapid HUR predictions for given conditions without 
additional MD simulations, offering a computationally efficient approach for large-
scale or rapid tasks, such as microstructure optimization.

# Page 8

8 
In addition to the superior predictive power, the learned structure signals a clear 
history-dependent mechanism in hydrogen uptake kinetics. Fig. 7a shows the SHAP 
analysis where the lagged HUR terms yt-1 and yt-2 are ranked highest as the two most 
influential features. It indicates a history-dependent kinetics in the observed variable 
set: the present HUR depends strongly on recent uptake history—namely, the surface 
accumulation and evolution of the interfacial MgH2 layer. A DeepLIFT time-by-
feature heatmap in Fig. 7b further shows attribution concentrated in the later portion 
of the input window, indicating that recent signals (≈1–3 time steps) supply the domi-
nant predictive information, which agrees with the SHAP finding. 
 
Fig.7. (a) SHAP analysis of the top 10 most influential features (the magnitude reflects relative 
importance; positive values indicate promotion, negative values indicate inhibition). (b) DeepLIFT 
time–feature attribution heatmap where the magnitude reflects the absolute relative contribution of 
each feature at a given time 
The next most important factors from SHAP analysis include instantaneous external 
H pressure and screw dislocation structure such as the total screw dislocation density 
and the mean screw dislocation length within Mg+H, indicating that instantaneous 
external pressure and dislocation structure are indeed crucial for HUR. However, the 
mass conservation variables—such as Mg/ H content inside the sphere and certain 
dislocation-class indicators (e.g., total dislocation length and screw dislocation densi-
ty) differ in rank and weight between the SHAP and DeepLIFT methods. Such dis-
crepancy reflects the intrinsic methodological differences between the two methods. 
DeepLIFT is more sensitive to instantaneous features, while SHAP reflects global 
average effects. We therefore treat them as complementary evidence supporting the 
conclusion that the HUR is history-dependent and determined by both instantaneous 
external pressure and dislocation structures. 
The MD model provides important insights and interpretability for the MD simula-
tion. These key factors identified by our machine learning model are consistent with 
the MD observations. The history dependency shown in the ML model explains the 
observed three-stage uptake kinetics of surface accumulation, accelerated bulk diffu-
sion and stabilized bulk diffusion from MD simulations. When the interfacial MgH2 
layer has accumulated rapidly in the recent past, its thickness and defect structure can 
modify permeability and trapping kinetics. The HUR may decline with delay even 
after the instantaneous external H pressure begins to drop (Fig. 3b). This accounts for 
the experimental observation of decreasing instantaneous external pressure while the 
HUR continues to rise [15]. The prominence of screw dislocations in both SHAP and 
DeepLIFT further suggests that screw dislocations act as short-circuit pathways or 
local nucleation sites, which is consistent with experimental evidence [8,17]. By con-
trast, edge dislocation indicators play a smaller role, implying that dislocation struc-

# Page 9

9 
ture, rather than total length, governs diffusion efficiency. This aligns with the obser-
vations in Fig. 3b.  
4 
Summary 
This study proposes an MD-ML integrated framework that investigates the kinetics of 
hydrogen uptake in Mg. Three-stage uptake kinetics is observed for the hydrogen 
uptake process. The hydrogen uptake rate is found to be dependent on temperature, 
initial external H pressure and dislocation structures from MD simulation. The ML 
model, incorporating NARX lags and change-point-aware weighting, successfully 
represents the history dependency and stage transitions of the hydrogen uptake pro-
cess which was not considered in previous studies. As a result, exceptional prediction 
of HUR is achieved by the ML model with R²= 0.9925 and RMSE= 1.985 × 10-2. 
Furthermore, the learnt ML model provides important insights and interpretability of 
the hydrogen uptake process. By using SHAP and DeepLIFT, both identifies the his-
tory dependent kinetic terms, instantaneous external H pressure and screw disloca-
tions as the key factors affecting the HUR. It explains the three-stage uptake kinetics 
and the importance of dislocation structure observed in MD simulation. 
The proposed MD-ML framework provides a simulation tool to predict HUR fast 
without the need of running computationally expensive MD simulation. More im-
portantly, the insights and key factors identified by the MD-ML framework provide 
critical guidance for microstructural and process parameter optimization to improve 
the efficiency of solid state hydrogen storage. The current MD-ML frame work has 
high transferability. It can be further extended for the prediction of other variables 
such as diffusion fluxes and phase fractions. Symbolic regression based on this 
framework is also possible to obtain closed-form relationships for hydrogen uptake 
process. These will provide further knowledge and more fundamental understanding 
of the Mg-H interaction, for application of solid state hydrogen storage. 
References 
[1] 
Wei, T.Y., Lim, K.L., Tseng, Y.S., & Chan, S.L.I.: A review on the characterization of 
hydrogen in hydrogen storage materials. Renewable and Sustainable Energy Reviews 79, 
1122–1133 (2017).  
[2] 
Xie, X.B., Chen, M., Hu, M.M., Wang, B.L., Yu, R.H., & Liu, T.: Recent advances in 
magnesium-based hydrogen storage materials with multiple catalysts. International Jour-
nal of Hydrogen Energy, 44, 10694–10712 (2019). 
[3] 
Karst, J., Sterl, F., Linnenbank, H., Weiss, T., Hentschel, M., & Giessen, H.: Watching in 
situ the hydrogen diffusion dynamics in magnesium on the nanoscale. Science Advances, 
6(19), eaaz0566 (2020). 
[4] 
Kitagawa, Y., & Tanabe, K.: Development of a kinetic model of hydrogen absorption and 
desorption in magnesium and analysis of the rate-determining step. Chemical Physics 
Letters, 699, 132–138 (2018).

# Page 10

10 
[5] 
Lyu, J., Kudiiarov, V., & Lider, A.: Experimentally observed nucleation and growth 
behavior of Mg/MgH₂ during de/hydrogenation of MgH₂/Mg: A review. Materials, 
15(22), 8004 (2022). 
[6] 
Heuser, B. J., Trinkle, D. R., Jalarvo, N., et al.: Direct measurement of hydrogen disloca-
tion pipe diffusion in deformed polycrystalline Pd using quasielastic neutron scattering. 
Physical Review Letters, 113, 025504 (2014). 
[7] 
Brocks, W., Falkenberg, R., & Scheider, I.: Coupling aspects in the simulation of hydro-
gen-induced stress-corrosion cracking. Procedia IUTAM, 3, 11–24 (2012). 
[8] 
Vittori Antisari, M., Aurora, A., Mirabile Gattia, D., & Montone, A.: On the nucleation 
step in the Mg–MgH₂ phase transformation. Scripta Materialia, 61, 1064–1067 (2009). 
[9] 
Pang, Y., & Li, Q.: A review on kinetic models and corresponding analysis methods for 
hydrogen storage materials. International Journal of Hydrogen Energy, 41(40), 18072–
18087 (2016). 
[10] Chou, K. C., Li, Q., Lin, Q., Jiang, L. J., & Xu, K. D.: Kinetics of absorption and desorp-
tion of hydrogen in alloy powder. International Journal of Hydrogen Energy, 30(3), 301–
309 (2005). 
[11] Luo, Q., Li, J. D., Li, B., Liu, B., Shao, H. Y., & Li, Q.: Kinetics in Mg-based hydrogen 
storage materials: Enhancement and mechanism. Journal of Magnesium and Alloys, 7(1), 
58–71 (2019). 
[12] Smirnova, D., Starikov, S., & Vlasova, A. M.: LAMMPS ADP potential for the Mg–H 
system developed by Smirnova, Starikov and Vlasova (2018) (v000). OpenKIM (2022).  
[13] Stukowski, A., Bulatov, V. V., & Arsenlis, A.: Automated identification and indexing of 
dislocations in crystal interfaces. Modelling and Simulation in Materials Science and En-
gineering, 20(8), 085007 (2012). 
[14] Broom, D. P.: Hydrogen storage materials: The characterisation of their storage proper-
ties. Springer. 
[15] Rydén, J., Hjörvarsson, B., Ericsson, T., Karlsson, E., Krozer, A., & Kasemo, B.: Unusu-
al kinetics of hydride formation in Mg/Pd sandwiches, studied by hydrogen profiling and 
quartz crystal microbalance measurements. Journal of the Less-Common Metals, 152(2), 
295–309 (1989). 
[16] Wirth, E., Munnik, F., Pranevičius, L. L., & Milčius, D.: Dynamic surface barrier effects 
on hydrogen storage capacity in Mg–Ni films. Journal of Alloys and Compounds, 475(1–
2), 917–922 (2009). 
[17] Chen, Y.-S., Huang, C., Liu, P.-Y., Yen, H.-W., Niu, R., Burr, P., Moore, K. L., 
Martínez-Pañeda, E., Atrens, A., & Cairney, J. M.: Hydrogen trapping and embrittlement 
in metals – A review. International Journal of Hydrogen Energy, 136, 789–821 (2025).
