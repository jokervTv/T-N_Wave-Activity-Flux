# -*-coding:utf-8-*-

"""
Caculating the T-N Wave-Activity Flux
derived by Takaya and Nakamura (JAS,2001).
"""

import numpy as np


def tnf2d(u_c, v_c, phi_c, phi, lat, lon, p_lev):
    """Caculating the horizontal T-N Wave-Activity Flux
    derived by Takaya and Nakamura (JAS,2001).

    Parameters

    u_c : array_like
        climate average background of meridional wind.

    v_c : array_like
        climate average background of zonal wind.

    phi_c : array_like
        climate average background of geopotential.

    phi : array_like
        geopotential in the analysis period.

    lat : array_like
        latitude.
        
    lon : array_like
        longitude.

    p_lev : float
        level.
        unit: hPa

    Return

    px : meridional T-N wave activity flux

    py : zonal T-N wave activity flux

    Note
        
        u_c, v_c, phi_c, phi, lat, lon must have the same shape.
        
        px, py have the same shape with u_c ...
    """

    a       = 6.37e6  # Earth Radius
    omega   = 7.292e-5  # Rotational angular velocity of the Earth

    dlon = np.gradient(lon) * np.pi / 180.0
    dlat = np.gradient(lat) * np.pi / 180.0

    # Coriolis parameter: f = 2 * omgega * sin(lat)
    f = np.array(
        list(map(lambda x: 2 * omega * np.sin(x * np.pi / 180.0), lat)))
    cos_lat = np.array(
        list(map(lambda x: np.cos(x*np.pi / 180.0), lat)))

    # Pertubation stream-function
    psi_p = ((phi - phi_c).T / f).T

    # partial differential terms
    dpsi_dlon       = np.gradient(psi_p, dlon[1])[1]
    dpsi_dlat       = np.gradient(psi_p, dlat[1])[0]
    d2psi_dlon2     = np.gradient(dpsi_dlon, dlon[1])[1]
    d2psi_dlat2     = np.gradient(dpsi_dlat, dlat[1])[0]
    d2psi_dlondlat  = np.gradient(dpsi_dlat, dlon[1])[1]

    termxu = dpsi_dlon * dpsi_dlon - psi_p * d2psi_dlon2
    termxv = dpsi_dlon * dpsi_dlat - psi_p * d2psi_dlondlat
    termyv = dpsi_dlat * dpsi_dlat - psi_p * d2psi_dlat2

    # coefficient
    p     = p_lev / 1000.0
    magU  = np.sqrt(u_c ** 2 + v_c ** 2)
    coeff = ((p * cos_lat) / (2 * magU.T)).T

    # x-component of TN-WAF
    px = (coeff.T / (a * a * cos_lat)).T * \
        (((u_c.T) / cos_lat).T * termxu + v_c * termxv)
    # y-component of TN-WAF
    py = (coeff.T / (a * a)).T * \
        (((u_c.T) / cos_lat).T * termxv + v_c * termyv)

    return px, py
