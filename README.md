# pySolarDB
Python library to access LE2P solar database SolarDB

Source code accessible via the github repository: https://github.com/LE2P/pySolarDB

## Installation

Using pip

```sh
pip install pysolardb
```

__Suggestion__: You will need a token to allow data access.

In the following, we  will use an instance of the `SolarDB` class as an example.

```sh
from pysolardb.SolarDB import SolarDB
solar=SolarDB()
# to disable the messages when recevoring data and metadata
solar.show_message = False
```

Keep in mind that the requests will sometimes result in empty answers. Leaving `show_message = True` will help in finding such cases.

## Utils methods: Register, Login, Status and Logout

__Note__: You can configure the '~/.bashrc' file in your home directory to allow the library to automatically recover and use your authentication token.

In the '~/.bashrc' file:

```sh
export SolarDBToken=YOUR_AUTHENTICATION_TOKEN
```

### Register

If you do not already possess a token, use the `register` method to recieve a new one by email:

```sh
solar.register(email="YOUR_EMAIL_ADDRESS")
```

### Login

Assuming you did not configure your '~/.bashrc' file, logged out or just received your token, you will need to use the `login` method before being able to access the solar data:

```sh
solar.login(token="YOUR_AUTHENTICATION_TOKEN")
```

### Status

```sh
solar.status()
```

### Logout

```sh
solar.logout()
```

## Recovering the sites, types and sensors list

### Sites

```sh
solar.getAllSites()
```

### Types

```sh
solar.getAllTypes()
```

### Sensors

```sh
solar.getAllSensors()
# to search only the diffuse irradiance sensors at Le Port Mairie
solar.getAllSensors(sites=["leportmairie"], types=["DHI"])
```

## Data collection

__Note__: The following data recovery methods will return empty dictionaries unless they recieve at least one site, type and/or sensor ID as parameters.

### Raw data recovery

```sh
# get the last 2 months global irradiance values from Vacaos and Plaine Des Palmistes Parc National taking the average value for each day
data = solar.getData(sites=["plaineparcnational","vacoas"], types=["GHI"], start="-2mo", aggrFn="mean", aggrEvery="1d")
```

The data can then be used to plot the evolution of the global irradiance:

```sh
import matplotlib.pyplot as plt
from datetime import datetime as dt

# extract the dates and values for Vacoas from the 'data' dictionary
vacoas_sensors = solar.getAllSensors(sites=["vacoas"], types=["GHI"])[0]
dates = data["vacoas"][vacoas_sensors]["dates"]
values = data["vacoas"][vacoas_sensors]["values"]

# put the dates to a datetime format
dates = [dt.strptime(date, "%Y-%m-%dT%H:%M:%SZ") for date in dates]

# plot the average global irradiance per day for the last 2 months
plt.figure()
plt.plot(dates, values)
plt.show()
```

### Get the sensors' active period for specific sites

```sh
# get the temporal bounds of each sensor at Le Port Mairie and Piton Des Neiges
solar.getBounds(sites=["leportmairie", "pitondesneiges"])
```

## Metadata recovery

### Recover the campaigns' metadata

```sh
solar.getCampaigns()
# get the campaigns' metadata for Mauritius
solar.getCampaigns(territory="Mauritius")
```

### Extract the instruments' metadata

```sh
solar.getInstruments()
```

### Get the measures' metadata

```sh
solar.getMeasures()
# get the metadat for UV measures
solar.getMeasures(type="UVAB")
```

### Recover the models' metadata

```sh
solar.getModels()
```