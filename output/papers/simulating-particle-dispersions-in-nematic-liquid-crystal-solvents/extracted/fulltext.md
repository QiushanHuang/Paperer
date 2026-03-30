# Page 1

VOLUME 87, NUMBER 7
P H Y S I C A L R E V I E W L E T T E R S
13 AUGUST 2001
Simulating Particle Dispersions in Nematic Liquid-Crystal Solvents
Ryoichi Yamamoto*
Department of Chemistry, University of Cambridge, Lensﬁeld Road, Cambridge, CB2 1EW, United Kingdom
(Received 15 April 2001; published 27 July 2001)
A new method is presented for mesoscopic simulations of particle dispersions in nematic liquid-crystal
solvents. It allows efﬁcient ﬁrst-principles simulations of the dispersions involving many particles with
many-body interactions mediated by the solvents. A simple demonstration is shown for the aggregation
process of a two dimensional dispersion.
DOI: 10.1103/PhysRevLett.87.075502
PACS numbers: 61.30.Cz, 61.20.Ja, 61.30.Jf
Dispersions of small particles in host ﬂuids such as col-
loidal suspensions and emulsions are of considerable tech-
nological importance, and often appear in our everyday
life in paints, foods, and drugs. Many kinds of exotic in-
teractions between particles mediated by the host ﬂuids are
possible, including screened Coulombic [1], depletion [1],
ﬂuctuation induced [2], and surface induced [3] forces. A
striking example occurs when spherical particles are im-
mersed in a liquid-crystal solvent in the nematic phase. For
a single particle, the orientation of the solvent molecules is
distorted due to the anchoring of the solvent molecules at
the particle surface. Extensive studies have been done on
this effect, and several characteristic conﬁgurations of the
nematic ﬁeld around a spherical particle have been iden-
tiﬁed [4–9]. When the strength of anchoring is increased
so that normal anchoring is preferred, the solvent changes
from quadrupolar to dipolar symmetries around the par-
ticle. When more than two particles are immersed in the
solvent, long-range anisotropic interactions are induced be-
tween particles due to elastic deformations of the nematic
ﬁeld [10–13]. The anisotropic interactions can have a pro-
nounced effect not only on the local correlations of the par-
ticles [10], but also on their phase behavior [14–17] and
on their mechanical properties [15].
Since analytical approaches for investigating these kinds
of complex materials are extremely difﬁcult, computer
simulations are essential to investigate their static and dy-
namical properties.
In most dispersions, the host ﬂuid
molecules are much smaller and move much faster than
the dispersed particles. This enables us to assume that the
host ﬂuid is in local equilibrium for any given particle con-
ﬁgurations, and thus it is usually a good idea to use some
coarse grained mesoscopic descriptions for the host ﬂuids
rather than treating them as fully microscopic molecules
[18]. In the case of charged colloidal suspensions, a meso-
scopic method for the ﬁrst-principles simulations can be
derived by treating the counterions as a charge density
[19]. For the particle dispersions in nematic solvents con-
sidered here, the mesoscopic coarse grained free energy
for the nematic solvent is well known to be the Frank free
energy [20], and the total free energy F of the system con-
sists of the following two parts: the bulk term Fel which
presents elastic energy of the nematic and the surface term
Fs which determines anchoring of the nematic ﬁeld at the
particle surface. Let nr be the director, a common di-
rection on which solvent molecules are aligned on average
with a constraint jnrj  1. F can be given by function-
als of nr for a given particle conﬁguration R1 ·· · RN:
F nr; R1 · ·· RN  K
2
Z
dr = ? n2 1 = 3 n2
1 W
2
I
dS 1 2 n ? n2 , (1)
where K is the Frank constant with the single elastic con-
stant approximation, W is the surface anchoring constant,
and n is the unit vector normal to the colloidal surface
[6,7]. The saddle-splay elastic term [7] is not considered
in Eq. (1). The integral in the ﬁrst term, Fel, runs over
the whole solvent volume excluding the particles, and that
in the second term, Fs, runs over all solvent-particle in-
terfaces. A simple scaling argument tells us Fel ~ Kad22
and Fs ~ Wad21 with a and d being the particle radius
and the system dimension, respectively, thus the physics
should be determined by the ratio FsFel ~ WaK.
Although this type of free energy functional is sufﬁcient
for performing Monte Carlo simulations where only
values of F are needed for a given particle conﬁgura-
tion, it is not useful for molecular dynamics (MD) or
Brownian-type simulations because the coupling between
solvent and the particles is given implicitly by limiting
the integration space in both Fel and Fs. This produces
mathematical singularities at the interface when one
calculates the force, fPS
i
 2≠F ≠Ri, acting on each
particle mediated by the nematic solvents.
Calculating
the force is crucial for performing efﬁcient simulations
of many particle systems.
Another serious problem of
this type of functional is that in order to give correct
boundary conditions at the particle-solvent interface,
one has to use appropriate coordinates for performing
grid-based numerical simulations rather than the usual
Cartesian coordinates. This is generally difﬁcult for par-
ticles with nonspherical shapes or for systems involving
many particles even when each particle has a spherical
shape. Also this makes the use of the periodic boundary
condition difﬁcult.
075502-1
0031-90070187(7)075502(4)$15.00
© 2001 The American Physical Society
075502-1

# Page 2

VOLUME 87, NUMBER 7
P H Y S I C A L R E V I E W L E T T E R S
13 AUGUST 2001
To overcome these problems, we have modiﬁed Eq. (1) by using a smooth interface between the solvent and the par-
ticles so that the coupling is given explicitly in the integrants through the interface. The new free energy functional we
propose is
F qr; R1 · · · RN 
K
4R2c
Z
dr
√
1 2
NX
i1
fir
!
tanhR2
c=aqbg2
1 Wj
2
Z
dr
NX
i1
∑d 2 1
d
=afi2 2 =afi=bfiqab
∏
,
(2)
where a,b, g [ x, y, z and the summation convention
is used.
The explicit form of the interfacial proﬁle fi
between dispersed particles and solvents is given by
fir  1
2
µ
tanha 2 jr 2 Rij
j
1 1
∂
,
(3)
with the particle radius a and the interface thickness
j. Note that this reduces to Eq. (1) if Rc, j ! 0. Very
recently, a similar idea of using smooth interface was pro-
posed for treating the hydrodynamic forces acting on par-
ticles dispersed in simple liquids [21]. In our case, the free
energy is given by functionals of a traceless and symmet-
ric second-rank tensor qabr  narnbr 2 dabd
rather than the director nr to take into account the sym-
metry of the nematic director 1n $ 2n automatically.
The semiempirical functional form 1R2
c tanhR2
c · · · is
applied in Eq. (2) to avoid the mathematical divergence
of the elastic free energy density at the defect centers and
to limit its value to Df  KR2
c, which is the correct
energy density difference between isotropic and nematic
states, in the defect core regions of size Rc. Another way
to avoid the divergence would be to use the Landau–
de Gennes–type free energy with an order parameter
Qabr  Qrqabr, but this requires a prohibitively
small lattice spacing near the defect points [22].
The simulation procedure is as follows. (i) For a given
particle conﬁguration R1 · · · RN, we obtain the interface
proﬁle fir by Eq. (3). Then we can calculate the stable
(or metastable) nematic conﬁgurations q
0
abr which sat-
isfy the equilibrium condition
dF
dqabr
Ç
qabrq
0
abr
 0
(4)
under the director constraint nar2  1.
One can
perform this by numerical iterations such as the steepest
descent or the conjugate gradient method.
(ii) Once
q
0
abr is obtained, the force acting on each particle
mediated by the nematic solvents follows directly from
the Hellmann-Feynman theorem,
fPS
i R1 · · · RN  2≠F q
0
abr;R1 · · · RN
≠Ri
(5)

K
4R2c
Z
dr ≠fi
≠R tanhR2
c=aq
0
bg2
1 Wj
Z
dr ≠=afi
≠Ri
=bfiq
0
ab .
(6)
This form is very convenient because we can compute
both ≠fi≠Ri and ≠=afi≠Ri at any time since fi
is an analytical function of Ri. (iii) Finally, we update
the particle positions according to appropriate equations
of motion such as
mi
d2Ri
dt2
 fPP
i
1 fPS
i
1 fH
i 1 fR
i ,
(7)
where fPP
i
is the force due to direct particle-particle interac-
tions (hard or soft sphere for instance), and fH
i and fR
i are
the hydrodynamic and random forces. Repeating the steps
(i)–(iii) enables us to perform ﬁrst-principles mesoscopic
simulations for the dispersions containing many particles
without neglecting many-body interactions.
We have performed simple simulations for a two dimen-
sional (2D) system to demonstrate our simulation proce-
dure. The system has 100 3 100 lattice sites in a square
box with a linear length L  100. Other physical parame-
ters are chosen rather arbitrarily as Rc  1, a  5, and
j  2, where the unit of length is the lattice spacing l.
Since the nematic conﬁgurations in 2D can be expressed
by a single scalar ﬁeld ur, the tilt angle of the director
against the horizontal x direction, Eq. (4) then reduces to
dF
dur  ≠qabr
≠ur
dF
dqabr  0 ,
(8)
with qxx  cos2u 2 12, qyy  sin2u 2 12, and qxy 
qyx  cosu sinu.
The boundary condition is ﬁxed at
ur  0 at the edge of the box to avoid rotations of the
reference frame. We ﬁrst calculated stable nematic con-
ﬁgurations around a single particle for different WaK,
and found two stable conﬁgurations. The ﬁrst conﬁgura-
tion, which we refer to as weak anchoring, contains no
topological defect. In the second conﬁguration, which we
refer to as strong anchoring, the particle is accompanied
by two 212 charge point defects. Typical examples of
the weak and strong anchoring are shown in Fig. 1(a) with
WaK  10 and Fig. 1(b) with WaK  20, respec-
tively. The distance between the defects and the particle
center is about 1.3a.
We note that both conﬁgurations
possess quadrupolar symmetries, and the latter would
correspond to the Saturn ring conﬁguration in three
dimensional (3D) systems. Although in principle particles
can be accompanied by one 21 charge hedgehog defect
in 2D as well as in 3D, such conﬁgurations are unstable in
the present 2D system since the elastic penalty of having
m point defects with charge c scales as mKc2. This was
directly conﬁrmed by recent simulations with perfect
normal anchoring [22] and also by our simulations. The
075502-2
075502-2

# Page 3

VOLUME 87, NUMBER 7
P H Y S I C A L R E V I E W L E T T E R S
13 AUGUST 2001
(a)
(b)
FIG. 1.
Director
conﬁgurations
around
a
single
particle
for (a) the weak anchoring case without defect obtained at
WaK  10 and (b) the strong anchoring case accompanied
by two 212 charge point defects indicated with the crosses
obtained at WaK  20. The white disks indicate the particles
with radius a  5. Only 9% of the total system is shown for
display purpose.
total free energies F W are plotted in Fig. 2 as functions
of WaK.
While both conﬁgurations can coexist in
the narrow transition regime 11 # WaK # 12.5, our
model predicts a clear ﬁrst-order transition from the weak
anchoring to the strong anchoring around WaK 	 11.5.
We next simulated the aggregation and ordering process
of 30 colloidal particles after the isotropic to nematic tran-
sition of the solvent occurred. Here we used the periodic
boundary condition and set WaK  20 so that each par-
ticle is accompanied by two 212 charge defects. Other
parameters are the same as in the previous single particle
case. The simulation was performed starting from a ran-
dom particle conﬁguration which is a typical conﬁguration
101
102
0
1
2
3
F / W
Wa / K
Weak
Strong anchoring
transition region
anchoring
FIG. 2.
The total free energies for the single particle cases
as functions of the strength of the anchoring constant WaK.
Our model predicts a ﬁrst-order transition from weak to strong
anchoring around WaK 	 11.5.
when the solvent is in the isotropic phase K  0. We
then set K  1 and calculated fPS
i
according to the present
procedure. The particle conﬁgurations were updated by
numerically solving the steepest descent equation,
z dRi
dt
 fPS
i
1 fPP
i ,
(9)
which is obtained by simply substituting d2Ridt2  0,
fR
i  0, and fH
i  2zdRidt in Eq. (7). z  1 is a fric-
tion constant and thus the off-diagonal components of
the hydrodynamic interaction was not considered. Here
we obtain fPP
i
 2≠EPP≠Ri from the repulsive part of
the Lennard-Jones potential, EPP  0.4
PN21
i1
PN
ji11 3
2ajri 2 rjj12 2 2ajri 2 rjj6 1 14 truncated at
the minimum distance jri 2 rjj  276a, to avoid the par-
ticles overlapping each other within the core radius 	
a. Snapshots from the present simulation are shown in
Fig. 3(a) for an aggregation stage, and in Fig. 3(b) at a
later time, where the particles are forming ordered clusters
due to the anisotropic attractions between them. Note is
added that only up to two particle simulations have been
done so far [7] and simulations of more than three particles
would be extremely difﬁcult or almost impossible by other
methods ever proposed.
In summary, we have developed an extremely powerful
simulation method to investigate particle dispersions inter-
acting via anisotropic solvents. We proposed a free energy
functional which is suitable for MD-type simulations. The
following modiﬁcations have been made to the usual Frank
free energy functional.
(i) The free energy is given by
a functional of a tensor q rather than a vector n to take
into account symmetry of the nematic director 1n $ 2n.
(ii) The coupling between the nematic solvent and par-
ticles at the interfaces is introduced explicitly through a
smooth interface so that we can analytically calculate the
force acting on each particle mediated by the host by tak-
ing derivatives of the free energy according to the par-
ticle positions. (iii) The value of the free energy density
is limited semiempirically to avoid a mathematical diver-
gence in the defect centers. We have performed demon-
strations for a 2D dispersion and conﬁrmed that the method
works well even when the system contains point defects.
Applications of this method to 3D systems should have
no theoretical difﬁculties, but require heavier computa-
tion. This should allow the simulation of the chaining of
the particles caused by the possible dipolar symmetry of
the nematic conﬁgurations around a single particle. Al-
though we have shown only simple demonstrations of the
method by performing simulations of the 2D system in this
Letter, simulations with physically more interesting situa-
tions such as systems with noncircular particles, asymmet-
ric particle pairs with different particle size, or particles
with non-normal anchoring as well as more realistic simu-
lations in 3D systems are now underway.
075502-3
075502-3

# Page 4

VOLUME 87, NUMBER 7
P H Y S I C A L R E V I E W L E T T E R S
13 AUGUST 2001
FIG. 3.
The aggregation and ordering process of colloidal par-
ticles when the solvent exhibits the isotropic K  0 to nematic
K  1 phase transition at t  0. Snapshots (a) in an aggre-
gation stage t  10 and (b) at a later time t  100, where
ordering of the particles is observed. Each particle is accompa-
nied by two 212 charge point defects. Darkness presents the
value of q2
xx. Black and white correspond to q2
xx  0 and 0.25,
respectively. Those correspond also to u  0.25p, 0.75p, and
u  0, 0.5p, p as shown in the gradation map.
The author thanks Professor J. P. Hansen and Dr. A.
Louis for helpful discussions. He acknowledges also the
Ministry of Education, Culture, Sports, Science and Tech-
nology of Japan for supporting his stay in Cambridge in
20002001. Calculations have been carried out at the Hu-
man Genome Center, Institute of Medical Science, Univer-
sity of Tokyo, and the Supercomputer Center, Institute of
Solid State Physics, University of Tokyo.
*Permanent address: Department of Physics, Kyoto Univer-
sity, Kyoto 606-8502 Japan.
Email address: ryoichi@scphys.kyoto-u.ac.jp
[1] W. B. Russel, D. A. Saville, and W. R. Schowalter, Col-
loidal Dispersions (Cambridge University Press, Cam-
bridge, 1995).
[2] V. M. Mostepanenko and N. N. Trunov, The Casimir Effect
and its Application (Clarendon Press, Oxford, 1997).
[3] A. Borˇstnik, H. Stark, and S. Žumer, Phys. Rev. E 60, 4210
(1999).
[4] E. M. Terentjev, Phys. Rev. E 51, 1330 (1995).
[5] S. Ramaswamy, R. Nityananda, V. A. Raghunathan, and
J. Prost, Mol. Cryst. Liq. Cryst. 288, 175 (1996).
[6] R. W. Ruhwandl and E. M. Terentjev, Phys. Rev. E 56, 5561
(1997).
[7] H. Stark, Eur. Phys. J. B 10, 311 (1999); H. Stark, J. Stelzer,
and R. Bernhard, Eur. Phys. J. B 10, 515 (1999).
[8] O. Mondain-Monval, J. C. Dedieu, T. Gulik-Krzywicki, and
P. Poulin, Eur. Phys. J. B 12, 167 (1999).
[9] Y. G. Gu and N. L. Abbott, Phys. Rev. Lett. 85, 4719
(2000).
[10] P. Poulin, H. Stark, T. C. Lubensky, and D. A. Weitz, Sci-
ence 275, 1770 (1997); P. Poulin, V. Cabuil, and D. A.
Weitz, Phys. Rev. Lett. 79, 4862 (1997); P. Poulin and
D. A. Weitz, Phys. Rev. E 57, 626 (1998).
[11] R. W. Ruhwandl and E. M. Terentjev, Phys. Rev. E 55, 2958
(1997).
[12] T. C. Lubensky, D. Pettey, N. Currier, and H. Stark, Phys.
Rev. E 57, 610 (1998).
[13] B. I. Lev and P. M. Tomchuk, Phys. Rev. E 59, 591 (1999).
[14] V. A. Raghunathan, P. Richetti, and D. Roux, Langmuir
12, 3789 (1996); V. A. Raghunathan, P. Richetti, D. Roux,
F. Nallet, and K. Sood, Langmuir 16, 4720 (2000).
[15] S. P. Meeker, W. C. K. Poon, J. Crain, and E. M. Terentjev,
Phys. Rev. E 61, R6083 (2000); V. J. Anderson, E. M. Ter-
entjev, S. P. Meeker, J. Crain, and W. C. K. Poon, Eur. Phys.
J. E 1, 11 (2001); V. J. Anderson and E. M. Terentjev, Eur.
Phys. J. E 1, 21 (2001).
[16] J. C. Loudet, P. Barios, and P. Poulin, Nature (London) 407,
611 (2000).
[17] J. Yamamoto and H. Tanaka, Nature (London) 409, 321
(2001).
[18] J. L. Billeter and R. A. Pelcovits, Phys. Rev. E 62, 711
(2000).
[19] H. Löwen, P. A. Madden, and J. P. Hansen, Phys. Rev. Lett.
68, 1081 (1992); H. Löwen, J. P. Hansen, and P. A. Madden,
J. Chem. Phys. 98, 3275 (1993).
[20] P. G. de Gennes and J. Prost, The Physics of Liquid Crys-
tals (Clarendon, Oxford, 1993), 2nd ed.
[21] H. Tanaka and T. Araki, Phys. Rev. Lett. 85, 1338 (2000).
[22] J. Fukuda and H. Yokoyama, Eur. Phys. J. E 4, 389 (2001).
075502-4
075502-4
