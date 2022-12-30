#!/usr/bin/env python
# coding: utf-8

# # Course schedule
# 
# Here is the current week-by-week schedule 📅 . We may adjust as we go along. To get started, we're going to create the calendar of weeks for the course programmatically rather than manually!
# 
# The course will meet on Monday and Wednesday from 3:30 to 5:20 PM EST. 

# In[1]:


# import modules
import pandas as pd
import re
import numpy as np


# tell python to display output and print multiple objects
from IPython.display import display, HTML
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# create range b/t start and end date of course
start_date = pd.to_datetime("2022-09-12")
end_date = pd.to_datetime("2022-11-15")
st_alldates = pd.date_range(start_date, end_date)

# subset to days in that range equal to Monday or Wednesday
st_mw = st_alldates[st_alldates.day_name().isin(['Monday', 'Wednesday'])]

# create DataFrame with that information
st_dates = [re.sub("2022\\-", "", str(day.date())) for day in st_mw] 
course_sched = pd.DataFrame({'dow': st_mw.day_name(),
                             'date': st_dates})
course_sched['day_date'] = course_sched.dow.astype(str) + " " + \
            course_sched.date.astype(str) 

# display the resulting date sequence
display(course_sched.day_date)


# The next few blocks of code creates the actual schedule content by joining the above list of dates with course concepts. 
# 
# **Click "show" to see the underlying code!**

# In[2]:


# create basic schedule content

# list of concepts
concepts = ["Course intro. and checking software setup",
            "Pandas: aggregation, joins, lambda, user-defined functions",
            "More Pandas",
            "Workflow basics: command line, JupyterHub, Github workflow",
            "Introduction to merging",
            "Regular expressions (Regex)",
            "Probabilistic matching",
            "Text as data: part one",
            "Text as data: part two",
            "Catchup/more text as data",
            "APIs",
            "More APIs (Twitter)",
            "Supervised machine learning: part 1",
            "Supervised machine learning: part 2",
            "SQL",
            "Web-scraping",
            "Catchup/more web-scraping",
            "Final project work session",
            "Final presentations"]

# check that concepts match number of weeks
assert len(course_sched.day_date) == len(concepts)

# combine dates with concepts
course_sched_concepts = pd.DataFrame({'Date': course_sched.day_date,
                                     'Concepts': concepts})

df = course_sched_concepts.copy()

print(df)


# In[3]:


# add DataCamp modules to schedule, matching to concepts conditionally
match_col = "Concepts" # concepts column to match on

tomatch = [df[match_col] == "Pandas: aggregation, joins, lambda, user-defined functions",
           df[match_col] == "Introduction to merging",
           df[match_col] == "Probabilistic matching",
           df[match_col] == "Supervised machine learning: part 1"]

# define DataCamp modules
modules = ["Data Manipulation with Pandas",
           "Joining Data with pandas",
           "Regular Expressions for Pattern Matching",
           "Supervised Learning with scikit-learn"]

'''
**Optional DataCamp courses & chapters for further learning:**

- Intermediate python: loops
- Python data science toolbox (Part 1)
- Object-Oriented Programming in Python: OOP Fundamentals
- Regular expressions in Python (first three chapters)
- Introduction to natural language processing in Python
- Introduction to databases in Python
- Intermediate importing data in python
- Intermediate SQL queries
- Web scraping in python
- Introduction to data visualization with MatPlotLib
- Introduction to data visualization with ggplot2
'''

df["DataCamp module(s) (if any)"] = np.select(tomatch, 
                                              modules, 
                                              default = "")


# In[4]:


# add assignments to schedule, matching to dates/concepts conditionally
date_col = "Date" # date column to match on

due_dates = [df[date_col] == "Wednesday 09-21",
             df[date_col] == "Wednesday 10-05",
             df[date_col] == "Wednesday 10-19",
             df[date_col] == "Wednesday 11-02",
             df[date_col] == "Monday 11-14"]

# define assignments
assignments = ["Problem set one (due Sunday 09-25)",
               "Problem set two (due Sunday 10-09)",
               "Final project milestone 1 (due Friday 10-21);<br>Problem set three (due Sunday 10-23)",
               "Problem set four (due Friday 11-04);<br>Final project milestone 2 (due Sunday 11-06) ",
               "Problem set five (due Friday 11-18);<br>Final project presentation (paper due Tuesday 11-22)"]

df["Due (11:59 PM EST unless otherwise specified)"] = np.select(due_dates,
                                                                assignments,
                                                                default = "")


# In[5]:


HTML(df.to_html(index=False, escape = False))

