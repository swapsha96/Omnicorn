# Omnicorn
**3D-HST** is a near-infrared spectroscopic survey with the Hubble Space Telescope designed to study the physical processes that shape galaxies in the distant Universe. The dataset accessible through this interface includes UV through mid-infrared photometry and spectroscopy in the five deep extragalactic 3D-HST/CANDELS fields: AEGIS, COSMOS, GOODS-N, GOODS-S and UDS. For further information, please see our data release [webpage](http://3dhst.research.yale.edu/Data.php). 

The main observations of the 3D-HST survey covered ~600 square arcminutes of well-studied extragalactic survey fields (AEGIS, COSMOS, GOODS-S, UKIDSS-UDS) with two orbits of primary WFC3/G141 grism coverage and two to four orbits with ACS/G800L coverage. Observations of the GOODS-N field taken in Cycle 17 (PI: Wiener, GO-11600) were also included. Ancillary observations spanning the UV through the mid-IR were combined with the grism spectroscopy to produce a unified dataset. The final release includes: 

- Extracted WFC3 2D and 1D spectra for ~250,000 objects
- Redshifts based on joint fits for the grism spectra and photometry for ~100,000 objects down to JH=26
- Emission line fits for to all major emission lines down to JH=26
- Best redshift catalog combining the spectroscopic, grism and photometric redshifts in the five fields
- Stellar masses, UV+IR, star formation rates, rest-frame colors in 22 bands for the grism redshift and best redshift catalogs
- Extracted ACS 2D and 1D spectra for ~25,000 objects

## Installation

If you want to develop SunPy you will need to install from git. The best way to install the package is using git:
```
$ git clone https://github.com/swapsha96/omnicorn.git
$ cd omnicorn
$ pip install -e .
```

# Usage

```
>>> import omnicorn     
>>> omnicorn.singleobject('aegis.12387.v41')
{'morphology': [{'filter_type': 'J', 'q': 0.0362, 'delta_magnitude': 0.193028, 'dn': 1.7456, 'magnitude': 25.7746, 'filter_name': 'F125W', 'n': 2.7199, 're': 0.174102, 'dpa': 23.9991, 'dq': 0.18743, 'pa': -40.9379, 'sn': 12.1193, 're_err': 0}, {'filter_type': 'H', 'q': 0.2907, 'delta_magnitude': 0.191205, 'dn': 1.88851, 'magnitude': 25.4836, 'filter_name': 'F160W', 'n': 3.8793, 're': 0.307542, 'dpa': 16.5247, 'dq': 0.139175, 'pa': -64.3636, 'sn': 13.7472, 're_err': 0}], 'meta': [{'objectsReturned': 1}], 'photometry': [{'magnitude': 25.8971107262, 'filter_name': 'F160W'}, {'magnitude': 26.0359892376, 'filter_name': 'F125W'}], 'results': [{'dec': 53.0513382, '3dhst_id': 'aegis.12387.v41', 'flux_radius': 3.304, 'y_centroid': 5286.4, 'ra': 215.20823669, 'x_centroid': 7775.2, 'id': 32505}]}
```

# To Do

- [ ] Add more useful functions. E.g. `list_of_fields()`.
- [ ] Support for Python2

Please let us know if you have suggestions for further improvements or any other ideas.
