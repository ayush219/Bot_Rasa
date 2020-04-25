# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd

class ActionPopulationDensity(Action):
    def name(self) -> Text:
        return "action_population_density"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city_name = tracker.get_slot("location")
        df= pd.read_csv('populationdata.csv')         
        population_density=df[df['city']==city_name]['population'].values[0]/df[df['city']==city_name]['area'].values[0]
        dispatcher.utter_message(text="Population density of " + city_name +" is " + str(population_density))
        return [] 

class ActionPopulation(Action):
    def name(self) -> Text:
        return "action_population"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city_name = tracker.get_slot("location")
        df=pd.read_csv('populationdata.csv')                      
        population= df[df['city']==city_name]['population'].values[0]
        dispatcher.utter_message(text="Population of "  +city_name +" is " + str(population))
        return []

class Area(Action):
    def name(self) -> Text:
        return "action_area"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        city_name = tracker.get_slot("location")
        df= pd.read_csv('populationdata.csv')        
        area=df[df['city']==city_name]['area'].values[0]
        dispatcher.utter_message(text="Area size of " +city_name +" is " + str(area))
        return []

