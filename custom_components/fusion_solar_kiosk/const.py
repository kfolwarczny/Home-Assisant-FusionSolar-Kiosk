"""Constants for FusionSolar Kiosk."""
# Base constants
DOMAIN = 'fusion_solar_kiosk'


# Configuration
CONF_KIOSKS = 'kiosks'


# Fusion Solar Kiosk API response attributes
ATTR_DATA = 'data'
ATTR_FAIL_CODE = 'failCode'
ATTR_SUCCESS = 'success'
ATTR_DATA_REALKPI = 'realKpi'
# Data attributes
ATTR_REALTIME_POWER = 'curPower'
ATTR_TOTAL_CURRENT_DAY_ENERGY = 'dailyCapacity'
ATTR_TOTAL_CURRENT_MONTH_ENERGY = 'monthCapacity'
ATTR_TOTAL_CURRENT_YEAR_ENERGY = 'yearCapacity'
ATTR_TOTAL_LIFETIME_ENERGY = 'allCapacity'


# Possible ID suffixes
ID_REALTIME_POWER = 'realtime_power'
ID_TOTAL_CURRENT_DAY_ENERGY = 'total_current_day_energy'
ID_TOTAL_CURRENT_MONTH_ENERGY = 'total_current_month_energy'
ID_TOTAL_CURRENT_YEAR_ENERGY = 'total_current_year_energy'
ID_TOTAL_LIFETIME_ENERGY = 'total_lifetime_energy'


# Possible Name suffixes
NAME_REALTIME_POWER = 'Realtime Power'
NAME_TOTAL_CURRENT_DAY_ENERGY = 'Total Current Day Energy'
NAME_TOTAL_CURRENT_MONTH_ENERGY = 'Total Current Month Energy'
NAME_TOTAL_CURRENT_YEAR_ENERGY = 'Total Current Year Energy'
NAME_TOTAL_LIFETIME_ENERGY = 'Total Lifetime Energy'
