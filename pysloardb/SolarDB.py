import requests
import json
import os
import logging

class SolarDB():

    def __init__(self):
        self.__baseURL = "https://solardb.univ-reunion.fr/api/v1/"
        self.__cookies = None
        self.logger = logging.getLogger(__name__)
        self.setloggerLevel(logging.INFO)
        ## Automatically logs in SolarDB if the token is saved in the '~/.bashrc' file
        token = os.environ.get('SolarDBToken')
        if token is not None:
            self.login(token)
        else:
            self.logger.warning("You will need to use your token to log in SolarDB")    

    def setloggerLevel(self, val):
        # remove all handlers
        while self.logger.hasHandlers():
            self.logger.removeHandler(self.logger.handlers[0])
        self.logger.setLevel(val)
        __ch = logging.StreamHandler()
        __ch.setLevel(val)
        self.logger.addHandler(__ch)

    ## Methods to log in SolarDB----------------------------------------------------------

    def login(self, token):
        """
        This method is used to log in the SolarDB API.

        Parameters
        ----------
        token : str
            This string is used as a key to log in SolarDB.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        try:
            res = requests.get(self.__baseURL + "login?token=" + token)
            res.raise_for_status()
            self.__cookies = res.cookies
            self.logger.debug(json.loads(res.content)["message"])
        except requests.exceptions.HTTPError:
            self.logger.warning("login -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("login -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("login -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("login -> Request Error: ",err)

    def register(self, email):
        """
        This method is used get the key (AKA the token) to log in SolarDB. It sends a mail to the user which contains the token.

        Parameters
        ----------
        email : str
            This string represents the user's mail address.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        try:
            res = requests.get(self.__baseURL + "register?email=" + email)
            res.raise_for_status()
            self.logger.debug(json.loads(res.content)["message"])
        except requests.exceptions.HTTPError:
            self.logger.warning("register -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("register -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("register -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("register -> Request Error: ",err)

    def status(self):
        """
        This method is used to verify if you are still logged in. It becomes obsolete id the logging level is higher than INFO.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        try:
            res = requests.get(self.__baseURL + "status", cookies = self.__cookies)
            self.logger.info(json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("status -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("stauts -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("stauts -> Request Error: ",err)

    def logout(self):
        """
        This method is used to log out of SolarDB.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        try:
            res = requests.get(self.__baseURL + "logout", cookies = self.__cookies)
            res.raise_for_status()
            self.logger.debug(json.loads(res.content)["message"])
            self.__cookies = None
        except requests.exceptions.HTTPError:
            self.logger.warning("logout -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("logout -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("logout -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("logout -> Request Error: ",err)


    ## Methods to recover the data -------------------------------------------------------

    def getAllSites(self):
        """
        This method is used to recover all the sites contained in SolarDB.

        Returns
        -------
            A list containing the sites extracted from SolarDB.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        sites = []
        try:
            res = requests.get(self.__baseURL + "data/sites", cookies=self.__cookies)
            res.raise_for_status()
            for i in range(len(json.loads(res.content)["data"])):
                sites.append(json.loads(res.content)["data"][i])
            self.logger.debug("All data sites successfully extracted from SolarDB")
            return sites
        except requests.exceptions.HTTPError:
            self.logger.warning("getAllSites -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getAllSites -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getAllSites -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getAllSites -> Request Error: ",err)

    def getAllTypes(self):
        """
        This method is used to recover all the data types contained in SolarDB.

        Returns
        -------
            A list containing the data types extracted from SolarDB.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        types = []
        try:
            res = requests.get(self.__baseURL + "data/types", cookies=self.__cookies)
            res.raise_for_status()
            for i in range(len(json.loads(res.content)["data"])):
                types.append(json.loads(res.content)["data"][i])
            self.logger.debug("All data types successfully extracted from SolarDB")
            return types
        except requests.exceptions.HTTPError:
            self.logger.warning("getAllTypes -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getAllTypes -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getAllTypes -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getAllTypes -> Request Error: ",err)

    def getAllSensors(self, sites = None, types = None):
        """
        A method used recover to the different sensors contained in SolarDB. If the sites and/or types are defined, the method will extract only the sensors corresponding to the specified request.

        Parameters
        ----------
        sites : list[str]
            This list is used to specify the sites in which we will search the sensors.
        types : list[str]
            This list is used to specify sensor types to recover.

        Returns
        -------
        A list containing the sensors extracted from SolarDB

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """
        sensors = []
        query = self.__baseURL + "data/sensors"
        args = ""
        if sites is not None:
            args += "&site=" + ','.join(sites)
        if types is not None:
            args += "&type=" + ','.join(types)
        if args != "":
            query += "?" + args
        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            for i in range(len(json.loads(res.content)["data"])):
                sensors.append(json.loads(res.content)["data"][i])
            self.logger.debug("All sensors successfully extracted from SolarDB")
            return sensors
        except requests.exceptions.HTTPError:
            self.logger.warning("getAllSensors -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getAllSensors -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getAllSensors -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getAllSensors -> Request Error: ",err)

    def getData(self, sites = None, types = None, sensors = None, start = None, stop = None, aggrFn = None, aggrEvery = None):
        """
        A method used to search and recover the data associated to one or more sites, sensors and/or types present in SolarDB. Using the paramters 'aggrFn' and 'aggrEvery', it is possible to apply an aggregation to the data extracted.

        Parameters
        ----------
        sites : list[str]
            This list is used to specify the sites for which we will search the data.
        types : list[str]
            This list is used to specify sensor types used to recover the data.
        sensors : list[str]
            This list is used to specify the sensors used to recover the data.
        start : str
            This string specifies the starting date for the data recovery. it can either follow a date format (e.g RFC3339) or work as a substraction of a time value from now (e.g '-4y' = four years ago). It is set to 24h ago by default.
        stop : str
            This string specifies the ending date for the data recovery. it can either follow a date format (e.g RFC3339) or work as a substraction of a time value from now (e.g '-4y' = four years ago). It is set to the current date (flux function 'now()') by default.
        aggrFn : str
            This string represents the function to apply for the aggregation (e.g 'mean', 'count', 'min', 'max'). If different from None, it is necessary to specify the aggregation period
        aggrEvery : str
            This string represents the period for the aggregation (e.g '1mo' = every month while '10m' = every 10 minutes). If different from None it is necessary to specify the aggregation function.

        Returns
        -------
            A dictionary containing the data per site and sensor. It is structured as follows:
            data{
                site{
                    sensor{
                        dates:  [...]
                        values: [...]
                    }
                }
            }

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """
        query = self.__baseURL + "data/json"
        args = ""
        if sites is not None:
            args += "&site=" + ','.join(sites)
        if types is not None:
            args += "&type=" + ','.join(types)
        if sensors is not None:
            args += "&sensorid=" + ','.join(sensors)
        if start is not None:
            args += "&start=" + start
        if stop is not None:
            args += "&stop=" + stop
        if aggrFn is not None:
            args += "&aggrFn=" + aggrFn
        if aggrEvery is not None:
            args += "&aggrEvery=" + aggrEvery
        if args != "":
            query += "?" + args

        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            data = json.loads(res.content)["data"]
            if data:
                self.logger.debug("Data successfully recovered")
            else:
                self.logger.info("There is no data for this particular request")
            return data
        except requests.exceptions.HTTPError:
            self.logger.warning("getData -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getData -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getData -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getData -> Request Error: ",err)

    def getBounds(self, sites = None, types = None, sensors = None):
        """
        A method used to search and recover the temporal bounds associated to one or more sites, sensors and/or types present in SolarDB.

        Parameters
        ----------
        sites : list[str]
            This list is used to specify the sites for which we will search the bounds.
        types : list[str]
            This list is used to specify sensor types used to recover the bounds.
        sensors : list[str]
            This list is used to specify the sensors used to recover the bounds.

        Returns
        -------
            A dictionary containing the bounds per site and sensor. It is structured as follows:
            data{
                site{
                    sensor{
                        start:  "..."
                        stop:   "..."
                    }
                }
            }

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        bounds = None
        query = self.__baseURL + "data/json/bounds"
        args = ""
        if sites is not None:
            args += "&site=" + ','.join(sites)
        if types is not None:
            args += "&type=" + ','.join(types)
        if sensors is not None:
            args += "&sensorid=" + ','.join(sensors)
        if args != "":
            query += "?" + args
        
        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            bounds = json.loads(res.content)["data"]
            if bounds:
                self.logger.debug("Bounds successfully recovered")
            else:
                self.logger.info("The bounds defined by this request are null")
            return bounds
        except requests.exceptions.HTTPError:
            self.logger.warning("getBounds -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getBounds -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getBounds -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getBounds -> Request Error: ",err)


    ## Methods to recover the metadata ----------------------------------------------------
    
    def getCampaigns(self, ids = None, name = None, territory = None, alias = None):
        """
        A method used to recover the different campaigns that took place during the IOS-Net project. Specifying the id, name, territory and/or alias will narrow down the campaigns recovered.

        Parameters
        ----------
        ids : str
            This string is the identity key. It corresponds to the '_id' field in the Mongo 'campaigns' collection.
        name : str
            This corresponds to the station official name and is associated to the 'name' field in the Mongo 'campaigns' collection.
        territory : str
            This string represents the territory name and is associated to the 'territory' field in the Mongo 'campaigns' collection.
        alias : str
            This string is the site practical name (which is used for data extraction) and is associated to the 'alias' field in the Mongo 'campaigns' collection.

        Returns
        -------
            A dictionary containing the campaigns' metadata.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        campaigns = None
        query = self.__baseURL + "metadata/campaigns"
        args = ""
        if ids is not None:
            args += "&id=" + ids
        if name is not None:
            args += "&name=" + name
        if territory is not None:
            args += "&territory=" + territory
        if alias is not None:
            args += "&alias=" + alias
        if args != "":
            query + "?" + args
        
        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            campaigns = json.loads(res.content)["data"]
            if campaigns:
                self.logger.debug("Campaign metadata successfully recovered")
            else:
                self.logger.info("The campaigns defined by this request do not exist")
            return campaigns
        except requests.exceptions.HTTPError:
            self.logger.warning("getCampaigns -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getCampaigns -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getCampaigns -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getCampaigns -> Request Error: ",err)

    def getInstruments(self, ids = None, name = None, label = None, serial = None):
        """
        A method used to recover the different instruments used in the IOS-Net project. Specifying the id, name, label and/or serial number will narrow down the instruments recovered.

        Parameters
        ----------
        ids : str
            This string is the identity key. It corresponds to the '_id' field in the Mongo 'instruments' collection.
        name : str
            This corresponds to the station official name and is associated to the 'name' field in the Mongo 'instruments' collection.
        label : str
            This string represents the instrument's label and is associated to the 'label' field in the Mongo 'instruments' collection.
        serial : str
            This string is the instrument's serial number and is associated to the 'serial' field in the Mongo 'instruments' collection.

        Returns
        -------
            A dictionary containing the instruments' metadata.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        instruments = None
        query = self.__baseURL + "metadata/instruments"
        args = ""
        if ids is not None:
            args += "&id=" + ids
        if name is not None:
            args += "&name=" + name
        if label is not None:
            args += "&label=" + label
        if serial is not None:
            args += "&serial=" + serial
        if args != "":
            query + "?" + args
        
        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            instruments = json.loads(res.content)["data"]
            if instruments:
                self.logger.debug("Instrument metadata successfully recovered")
            else:
                self.logger.info("The intstruments defined by this request do not exist")
            return instruments
        except requests.exceptions.HTTPError:
            self.logger.warning("getInstruments -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getInstruments -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getInstruments -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getInstruments -> Request Error: ",err)

    def getMeasures(self, ids = None, name = None, dtype = None, nested = None):
        """
        A method used to recover the different measure types used in the IOS-Net project. Specifying the id, name and/or data type will narrow down the measures recovered.

        Parameters
        ----------
        ids : str
            This string is the identity key. It corresponds to the '_id' field in the Mongo 'measures' collection.
        name : str
            This corresponds to the station official name and is associated to the 'name' field in the Mongo 'measures' collection.
        dtype : str
            This string represents the data type and is associated to the 'type' field in the Mongo 'measures' collection.
        nested : bool
            This boolean, which is false by default, indicates whether the user wants to recieve all the metadata or only key metadata information associated to the measures.

        Returns
        -------
            A dictionary containing the measures' metadata

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        measures = None
        query = self.__baseURL + "metadata/measures"
        args = ""
        if ids is not None:
            args += "&id=" + ids
        if name is not None:
            args += "&name=" + name
        if dtype is not None:
            args += "&type=" + dtype
        if nested is not None:
            args += "&nested=" + str(nested)
        if args != "":
            query + "?" + args
        
        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            measures = json.loads(res.content)["data"]
            if measures:
                self.logger.debug("Measure metadata successfully recovered")
            else:
                self.logger.info("The measures defined by this request do not exist")
            return measures
        except requests.exceptions.HTTPError:
            self.logger.warning("getMeasures -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getMeasures -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getMeasures -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getMeasures -> Request Error: ",err)

    def getModels(self, ids = None, name = None, dtype = None):
        """
        A method used to recover the models used in the IOS-Net project. Specifying the id, name and/or data type will narrow down the models recovered.

        Parameters
        ----------
        ids : str
            This string is the identity key. It corresponds to the '_id' field in the Mongo 'models' collection.
        name : str
            This corresponds to the station official name and is associated to the 'name' field in the Mongo 'models' collection.
        dtype : str
            This string represents the data type and is associated to the 'type' field in the Mongo 'models' collection.

        Returns
        -------
            A dictionary containing the models' metadata.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e if there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        models = None
        query = self.__baseURL + "metadata/models"
        args = ""
        if ids is not None:
            args += "&id=" + ids
        if name is not None:
            args += "&name=" + name
        if dtype is not None:
            args += "&type=" + dtype
        if args != "":
            query + "?" + args
        
        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            models = json.loads(res.content)["data"]
            if models:
                self.logger.debug("Models metadata successfully recovered")
            else:
                self.logger.info("The measures defined by this request do not exist")
            return models
        except requests.exceptions.HTTPError:
            self.logger.warning("getModels -> HTTP Error: ", json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            self.logger.warning("getModels -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            self.logger.warning("getModels -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            self.logger.warning("getModels -> Request Error: ",err)
