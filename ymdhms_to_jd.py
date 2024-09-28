# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
#  Converts ECEF vector components to SEZ
#  See "Fundamentals of Astrodynamics and Applications, Fourth Edition" by
#  David A. Vallado, pages 172-173
# Parameters:
# year: year
# month: month
# day: day
# hour: hour
# minute: minute
# second: second
#
# Output:
#  Prints the fractional julian date
#
# Written by Elise Turka
# Other contributors: None
#
# This work is licensed under CC BY-SA 4.0

# import Python modules
import math # math module
import sys  # argv

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions


# initialize script arguments
year = float('nan') # ECEF x in SEZ frame
month = float('nan') # ECEF y in SEZ frame
day = float('nan') # ECEF z in SEZ frame
hour = float('nan') # ECEF x-position
minute = float('nan') # ECEF y-position
second = float('nan') # ECEF z-position

# parse script arguments
if len(sys.argv)==7:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
else:
  print(\
   'Usage: '\
   'python3 ecef_to_llh.py year month day hour minute second'\
  )
  exit()


if month <= 2:
  year = year - 1
  month = month+12

A = year//100
B = 2-A+(A//4)

JD = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5

frac_of_day = hour/24+minute/1440+second/86400

jd_frac = JD+frac_of_day;

print(jd_frac)