import laserfun as lf

pulse = lf.Pulse(pulse_type='sech', fwhm_ps=0.050, center_wavelength_nm=1550,
                 time_window_ps=7, npts=2**12, epp=50e-12)

fiber1 = lf.Fiber(0.010, center_wl_nm=1550, dispersion_format='GVD',
                  dispersion=(-0.12, 0, 5e-6), gamma_W_m=1)

results = lf.NLSE(pulse, fiber1)

results.plot()