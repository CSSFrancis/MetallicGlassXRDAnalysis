import pyFAI
import pyFAI.calibrant

wavelength = 1.5404e-10
Corundum = pyFAI.calibrant.get_calibrant("alpha_Al2O3")
Corundum.set_wavelength(wavelength)
print(len(Corundum.get_dSpacing()))

pixelsize = 6.8e -05



#calb = pyFAI.multi_geometry.MultiGeometry()