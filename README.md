# Project-Data-Processing


## Description

Pre-process data and upload to couchDB


## Requirements
> Make sure you have python 3.7 or higher correctly installed
- Install the required library

  `pip install -r requirements.txt`


## Contents
This repository contains:
- script used to pre-processing and upload data
- data used in this project:
  - sudo data
  - Geographical data of [LGA](https://public.opendatasoft.com/explore/dataset/georef-australia-local-government-area/export/?disjunctive.ste_code&disjunctive.ste_name&disjunctive.lga_code&disjunctive.lga_name&sort=-year)/[STATES](https://public.opendatasoft.com/explore/dataset/georef-australia-state/information/?disjunctive.ste_code&disjunctive.ste_name) maintained by [Opendatasoft](https://public.opendatasoft.com/explore/?sort=modified)
  - 5000 sample twitter data with location info 
- map-reduced function used in couchDB 


## Data Processing Steps

- Filter the twiiters that do not contain `full_name`
- Match the `full_name` with `lga_code` and `state_code`
  - handle special case. For the case like `full_name=Victoria, Australia`, `state_code=2, lga_code=0`
  - Remove the twitters that outside Australia
- Extract the useful fields
- Change the data structure for easy computation in the back-end
- Doing basic calculation
