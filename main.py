# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


######################################################
# Paper: file:///C:/Users/andre/Downloads/remotesensing-13-00861-v3.pdf
# Tuna location varaibles
# * Surface Temperatue
# * Sea Surface Salinity
# * Sea Surface Height (Depth)
# * Mixed Layer Depth
https://resources.marine.copernicus.eu/product-detail/MULTIOBS_GLO_PHY_TSUV_3D_MYNRT_015_012/DATA-ACCESS
# * Clorophyll a Concentration
# * finite-size Lyapunov exponents (Add Later)
##################################


import requests
import pandas
from sklearn.li~near_model import LinearRegression, LogisticRegression
#Linear for num-catches, logisitc for probability of fish, dont know which one will work yet



data_link = "https://nrt.cmems-du.eu/motu-web/Motu?action=describeproduct&service=GLOBAL_ANALYSIS_FORECAST_PHY_001_024-TDS&product=cmems_mod_glo_phy_anfc_merged-uv_PT1H-i"
data = requests.get(data_link).content