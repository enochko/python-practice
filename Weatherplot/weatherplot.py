'''
Plot Melbourne, Australia weather observations from Bureau of Meteorology (BOM).
'''

import requests
from datetime import datetime
import matplotlib.pyplot as plt

# Get Melbourne Weather Observations
url = 'http://www.bom.gov.au/fwo/IDV60901/IDV60901.95936.json'
headers = {'User-Agent': 'Mozilla/5.0'} # BOM requires user-agent, else 403
r = requests.get(url, headers=headers)
print(f"Request status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()['observations']

# Extract header information
site_id = response_dict['header'][0]['main_ID']
site_name = response_dict['header'][0]['name']
site_state = response_dict['header'][0]['state']

print(f'Weather at {site_id} {site_name}, {site_state}:')

# Explore information about the observations.
observations_list = response_dict['data']
observations_list = observations_list[::-1] # Sort to chronological order
print(f"Obeservations returned: {len(observations_list)}")

# Extract date, time, and air temperature observations
obs_datetime, obs_date, obs_time, temp = [], [], [], []
for observation in observations_list:
    obs_datetimestr = observation['local_date_time_full']
    obs_datetimedata = datetime.strptime(obs_datetimestr, '%Y%m%d%H%M%S')
    obs_datetime.append(obs_datetimedata)
    obs_date.append(obs_datetimedata.strftime('%Y-%m-%d'))
    obs_time.append(obs_datetimedata.strftime('%H:%M'))
    temp.append(observation['air_temp'])

# Plot air temperature observations
plt.plot(obs_time[0:48], temp[0:48], obs_time[48:96], temp[48:96], obs_time[96:], temp[96:])
plt.legend([obs_date[0], obs_date[48], obs_date[96]])
plt.title(f'Air Temperature at {site_id} {site_name}, {site_state}.')
plt.xlabel('Time')
plt.xticks(obs_time[0:48:2], rotation=-45)
plt.ylabel('Air temperature °C')
plt.show()