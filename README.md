# EDSA Sprint: Analyse - Analyse_package

## Introduction

Analyse_package is a small Python package that allows one to do 7 basic data analyses on lists (functions 1-3)
and pandas.DataFrame structured twitter data (fucntions 4-7). Each analysis/function has specific 
input/output as seen in their respective dosctrings.

Note: This package was created as part of team 7's project deliverables for the Analyse sprint at the 
Explore Data Science Academy (Johannesburg July 2020 cohort)
and is not intended for use outside of this learning environment.

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* This package is written in Pyhon3 and requires a complementary interpreter.
* This packages requires the latest (as of 2020/08/04) versions of Numpy and Pandas.
	* https://numpy.org/
	* https://pandas.pydata.org/

## Installing Analyse_package

To install Analyse_package, follow these steps:

We reccomend installing this package with conda (from anaconda). 
Read more about the anaocnda project at https://www.anaconda.com/

Alternatively a simpler install using pip:

```
pip install git+https://github.com/JacCars/Analyse_package
```

## Using Analyse_package

To use Analyse_package, follow these steps:
```
import Analyse_package as team7
```
Function 1: dictionary_of_metrics
```
team7.dictionary_of_metrics(<your_input_list>)
```
Function 2: five_num_summary
```
team7.five_num_summary(<your_input_list>)
```
Function 3: date_parser
```
team7.date_parser(<your_input_list>)
```
Function 4: extract_municipality_hashtags
```
team7.extract_municipality_hashtags(<your_input_dataframe>)
```
Function 5: number_of_tweets_per_day
```
team7.number_of_tweets_per_day(<your_input_dataframe>)
```
Function 6: word_splitter
```
team7.extract_municipality_hashtags(<your_input_dataframe>)
```
Function 7: stop_words_remover
```
team7.stop_words_remover(<your_input_dataframe>)
```
## Contributing to Analyse_package
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
No external contributors necessary. This is a limited package with no future updates planned.

See https://help.github.com for further reading on GitHub.

## Contributors

Thanks to the following people who have contributed to this project:

* Bukelwa Mqhamane   | mabum7@gmail.com
* Jacques Carstens   | carstensjacques3@gmail.com
* Katleho Mokhele    | katleho@southatlantic.net
* Maria Rakau        | mariarakau@gmail.com
* Simangele Maphanga | Simangeleinno@gmail.com


## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: MIT (https://opensource.org/licenses/MIT).
