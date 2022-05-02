import requests
import json
from datetime import datetime as dt
import os
import matplotlib.pyplot as plt

class SolarDB():

    def __init__(self):
        self.__baseURL = "https://solardb.univ-reunion.fr/api/v1/"
        self.__cookies = ""
        token = os.environ.get('SolarDBToken')
        if token is not None:
            self.login(token)
            self.status()
        else:
            print("You will need to use your token to log in SolarDB")    
    

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
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
            print(json.loads(res.content)["message"])
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("login -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("login -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("login -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("login -> Request Error: ",err)

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
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
            print(json.loads(res.content)["message"])
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("register -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("register -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("register -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("register -> Request Error: ",err)

    def status(self):
        """
        This method is used to verify that you are still logged in.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
        ConnectionError
            If the program is unable to connect to SolarDB
        TimeOutError
            If the SolarDB response is too slow
        RequestException
            In case an error that is unaccounted for happens
        """

        try:
            res = requests.get(self.__baseURL + "status", cookies = self.__cookies)
            print(json.loads(res.content)["message"])
        except requests.exceptions.ConnectionError as errc:
            print("status -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("stauts -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("stauts -> Request Error: ",err)

    def logout(self):
        """
        This method is used to log out of SolarDB.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
            print(json.loads(res.content)["message"])
            self.__cookies = None
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
        except requests.exceptions.ConnectionError as errc:
            print("logout -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("logout -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("logout -> Request Error: ",err)


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
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
            print("All data sites succesfully extracted from SolarDB")
            return sites
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getAllSites -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getAllSites -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getAllSites -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getAllSites -> Request Error: ",err)

    def getAllTypes(self):
        """
        This method is used to recover all the data types contained in SolarDB.

        Returns
        -------
            A list containing the dat types extracted from SolarDB.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
            print("All data types sucesfully extracted from SolarDB")
            return types
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getAllTypes -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getAllTypes -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getAllTypes -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getAllTypes -> Request Error: ",err)

    def getAllSensors(self, sites = None, types = None):
        """
        A method used to the different sensors contained in SolarDB into a list. If the sites and/or types are defined, the method will extract only the sensors corresponding to the specified request.

        Parameters
        ----------
        sites : list[str]
            This list is used to specify the sites in which we will search the sensors.
        types : list[str]
            This list is used to specify sensor types to recover.

        Returns
        -------
        A list containing the sensors recovered

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
            print("All sensors succesfully extracted from SolarDB")
            return sensors
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getAllSensors -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getAllSensors -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getAllSensors -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getAllSensors -> Request Error: ",err)

    def getData(self, sites = None, types = None, sensors = None, start = None, stop = None, aggrFn = None, aggrEvery = None):
        """
        A method used to search and recover the data associated to one or more sites, sensors and/or types present in SolarDB. Using the paramters 'aggrFn' and 'aggrEvery' it is possible to apply an aggregation to the data extracted.

        Parameters
        ----------
        sites : list[str]
            This list is used to specify the sites in which we will search the data.
        types : list[str]
            This list is used to specify sensor types used to recover the data.
        sensors : list[str]
            This list is used to specify the sensors used to recover the data.
        start : str
            This string specifies the starting date for the data recovery. it can either follow a date format (e.g RFC3339) or work as a substraction of a time value from now (e.g '-4y' = four years ago). It is set to 24h ago by default
        stop : str
            This string specifies the ending date for the data recovery. it can either follow a date format (e.g RFC3339) or work as a substraction of a time value from now (e.g '-4y' = four years ago). it is set to now by default.
        aggrFn : str
            This string represents the function to apply for the aggregation (e.g 'mean', 'count', 'min', 'max'). If different from None, it is necessary to specify the aggregation period
        aggrEvery : str
            This string represents the period for the aggregation (e.g '1mo' = every month). If different from None it is necessary to specify the aggregation function.

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
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
            args += "&sensor=" + ','.join(sensors)
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
                print("Data succesfully recovered")
                return data
            else:
                print("There is no data for this particular request")
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getData -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getData -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getData -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getData -> Request Error: ",err)

    def getBounds(self, sites = None, types = None, sensors = None):
        """
        A method used to search and recover the temporal bounds associated to one or more sites, sensors and/or types contained in SolarDB.

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
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
            args += "&sensor" + ','.join(sensors)
        if args != "":
            query += "?" + args
        
        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            bounds = json.loads(res.content)["data"]
            if bounds:
                print("Bounds succesfully recovered")
                return bounds
            else:
                print("The bounds defined by this request do not exist")
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getBounds -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getBounds -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getBounds -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getBounds -> Request Error: ",err)


    ## Methods to recover the metadata ----------------------------------------------------
    
    def getCampaigns(self, ids = None, name = None, territory = None, alias = None):
        """
        A method used to recover the different campaigns that took place during the IOS-Net project. Specifying the id, name, territory and/or alias will narrow down the campaigns recovered.

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
            A dictionary containing the campaigns' metadata.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
                print("Campaign metadata succesfully recovered")
                return campaigns
            else:
                print("The campaigns defined by this request do not exist")
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getCampaigns -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getCampaigns -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getCampaigns -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getCampaigns -> Request Error: ",err)

    def getInstruments(self, ids = None, name = None, label = None, serial = None):
        """
        A method used to recover the different instruments used in the IOS-Net project. Specifying the id, name, label and/or serial number will narrow down the instruments recovered.

        Parameters
        ----------
        sites : list[str]
            This list is used to specify the sites for which we will search the instruments.
        types : list[str]
            This list is used to specify sensor types used to recover the instruments.
        sensors : list[str]
            This list is used to specify the sensors used to recover the instruments.

        Returns
        -------
            A dictionary containing the instruments' metadata.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
                print("Instrument metadata succesfully recovered")
                return instruments
            else:
                print("The intstruments defined by this request do not exist")
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getInstruments -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getInstruments -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getInstruments -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getInstruments -> Request Error: ",err)

    def getMeasures(self, ids = None, name = None, dtype = None):
        """
        A method used to recover the different measure types used in the IOS-Net project. Specifying the id, name and/or data type will narrow down the measures recovered.

        Parameters
        ----------
        sites : list[str]
            This list is used to specify the sites for which we will search the measures.
        types : list[str]
            This list is used to specify sensor types used to recover the measures.
        sensors : list[str]
            This list is used to specify the sensors used to recover the measures.

        Returns
        -------
            A dictionary containing the measures' metadata

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
        if args != "":
            query + "?" + args
        
        try:
            res = requests.get(query, cookies=self.__cookies)
            res.raise_for_status()
            measures = json.loads(res.content)["data"]
            if measures:
                print("Measure metadata succesfully recovered")
                return measures
            else:
                print("The measures defined by this request do not exist")
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getMeasures -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getMeasures -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getMeasures -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getMeasures -> Request Error: ",err)

    def getModels(self, ids = None, name = None, dtype = None):
        """
        A method used to recover the models used in the IOS-Net project. Specifying the id, name and/or data type will narrow down the models recovered.

        Parameters
        ----------
        sites : list[str]
            This list is used to specify the sites for which we will search the models.
        types : list[str]
            This list is used to specify sensor types used to recover the models.
        sensors : list[str]
            This list is used to specify the sensors used to recover the models.

        Returns
        -------
            A dictionary containing the models' metadata.

        Raises
        ------
        HTTPError
            If the responded HTTP Status is between 400 and 600 (i.e there is a problem with the request or the server)
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
                print("Models metadata succesfully recovered")
                return models
            else:
                print("The measures defined by this request do not exist")
        except requests.exceptions.HTTPError:
            message = json.loads(res.content)["message"]
            print("getModels -> HTTP Error: ", message)
        except requests.exceptions.ConnectionError as errc:
            print("getModels -> Connection Error:",errc)
        except requests.exceptions.Timeout as errt:
            print("getModels -> Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print("getModels -> Request Error: ",err)




# if __name__=="__main__":
#     d = SolarDB()
#     d.login("b64ed57ae6d2d599ce66af58e9bad0bd1abe76d4")
#     print("\n\nTests concerning the data\n\n")
#     print(d.getAllSites()[0])
#     print(d.getAllTypes()[-1])
#     print(d.getAllSensors()[1])
#     print(d.getData(types=["DHI"], start="-2mo", aggrFn="count", aggrEvery="2d").keys())
#     print(d.getBounds(types=["DHI","RR"]))
#     print("\n\nTests concerning the metadata\n\n")
#     print(d.getCampaigns())
#     print(d.getInstruments())
#     print(d.getMeasures())
#     print(d.getModels())
#     d.status()
#     d.logout()
#     d.status()