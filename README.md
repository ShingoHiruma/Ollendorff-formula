# Ollendorff_formula
## Homogenization method in numerical electromagnetism
<img src="https://github.com/ShingoHiruma/Ollendorff_formula/assets/49121385/1049528b-7416-4a09-9798-0391a8d95220" width="50%">

## Complex permeability based on Ollendorff formula
The extended Ollendorff formula is used to obtain the macroscopic complex permeability of the composite materials, which is given by
$$\langle\dot\mu_r\rangle=1+\frac{\eta(\dot\mu_r -1)}{1+N(1-\eta)(\dot\mu_r-1)} $$
where $\dot\mu_r, N, \eta,$ are the complex permeability, diamagnetic constant, and the filling factor. 
Since the complex permeability $\dot\mu_r$ can be obtained analytically by solving the Maxwell equation, the method using the extended Ollendorff formula is classified as the semi-analytical method.

## List of complex permeability
### Plate
$$\dot\mu_r=\mu_r \frac{\tan{z}}{z}$$
### Cylinder
$$\dot\mu_r=\mu_r\frac{J_1(z)}{zJ_1'(z)}=\mu_r\frac{1}{\frac{zJ_0(z)}{J_1(z)}-1}$$
### Sphere
$$\dot\mu_r=\mu_r\frac{2j_1(z)}{j_1(z)+zj_1'(z)}=\mu\frac{2(z-\tan{z})}{(1-z^2)\tan{z}-z}$$

where $z=ka=a\sqrt{-j\omega\sigma\mu}$, $J_n(z)$ is the n-th order Bessel function of the first kind, and $j_n(z)$ is the n-th order spherical Bessel function of the first kind.
