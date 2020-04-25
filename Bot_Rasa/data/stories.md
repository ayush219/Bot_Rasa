## greet
* greet
  - utter_greet

## goodbye
* bye
  - utter_bye
    
## questions on population
* greet
  - utter_greet
* population{"location":"mumbai"}  
  - action_population  
* bye
  - utter_bye

## questions on population_2
* greet
  - utter_greet
* population
  - utter_asklocation
* population{"location":"mumbai"} 
  - action_population 
* bye
  - utter_bye
  
## questions on area
* greet
  - utter_greet
* area{"location":"mumbai"}
  - action_area
* bye
  - utter_bye
  
## questions on area_2
* greet
  - utter_greet
* area
  - utter_asklocation
* area{"location":"mumbai"} 
  - action_area
* bye
  - utter_bye

## questions on population density
* greet
  - utter_greet
* population_density{"location":"mumbai"}
  - action_population_density
* bye
  - utter_bye
  
## questions on population density_2
* greet
  - utter_greet
* population_density 
  - utter_asklocation
* population_density{"location":"mumbai"} 
  - action_population_density
* bye
  - utter_bye