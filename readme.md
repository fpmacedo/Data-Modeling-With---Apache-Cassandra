
# Project: Data Modeling with Apache Cassandra

> by Filipe Macedo 14 February 2020

![](images/cassandra.jpg)


## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

![](images/etl_diagram.png)

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions. Her role is to create a database for this analysis and to test her database by running queries given to her by the analytics team from Sparkify to create the results.

## Project Description

In this project, I applied what I've learned on data modeling with Apache Cassandra and completed an ETL pipeline using Python. To complete the project, I needed to model my data by creating tables in Apache Cassandra to run queries. I was provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.

I've been provided with a project template that took care of all the imports and provided a structure for ETL pipeline I need to process this data.

![](images/image_event_datafile_new.jpg)

## Datasets

In this project, I worked with one dataset: `event_data`: this directory of csv files is partitioned by date. Here are examples of filepaths to two files in the dataset:

`event_data/2018-11-08-events.csv`

`event_data/2018-11-09-events.csv`

## ETL Pipeline

Extract, transform, load (ETL) is the general procedure of copying data from one or more sources into a destination system which represents the data differently from the sources or in a different context than the sources.

1. In a terminal, run `python create_tables.py` to reset the tables in the sparkifydb database.
2. In a terminal, run `python etl.py` to process all the datasets.


