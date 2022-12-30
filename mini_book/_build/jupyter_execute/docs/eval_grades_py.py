#!/usr/bin/env python
# coding: utf-8

# # Evaluation and grading
# 
# ## Summary and grading policy
# 
# You will have four cumulative late days for assignments, that can be apportioned as you see fit between the different problem sets. Late days cannot be used for the final project or final presentation. If you run over and have not submitted a problem set by the following class, I ask that you not attend class as not to see the answers. There will be a deduction of 10 percentage points for each late day after you have used your allowed late days.
# 
# Grades may be curved if there are no students receiving A's on the non-curved grading scale. 

# In[1]:


## import modules
import pandas as pd

from IPython.display import display, HTML

grade_summary = pd.DataFrame({'Assignments':
                ["Datacamp modules",
                  "Five problem sets",
                  "Final project",
                  "Team player/participation"],
                'Percentage':
                [5, 
                 50,
                 35,
                 10],
                             }) 

HTML(grade_summary.to_html(index=False))


# ## Details
# 
# ### Datacamp modules to support programming topics (5% of grade)
# 
# The DataCamp modules are mainly to support your work on the problem sets and final project by giving you additional practice prior to our in-class activities. As a result, they will be graded on a "complete" and "incomplete" basis, regardless of how many points you received on the assignment itself. This means that you shouldn't get stuck partway through, since you can always ask to be shown the answer with a points deduction. Conversely, if the concepts are review, these should be very quick to complete, but if you'd prefer to skip, you can talk to me and I will reapportion the 5\% to your second problem set.
# 
# 
# ### Five problem sets (50% of total grade; 10-20% each)
# 
# DataCamp provides a very smooth introduction to programming, in the sense that they provide you with example code that gets you ~80\% of the way to the solution, with you needing to apply that code to reach the other ~20\%. 
# 
# In contrast, the problem sets will assess your ability to apply the concepts to data that is substantially messier, and problems that are substantially more difficult, than the ones in DataCamp. More details on the problem sets will be provided the week before each is released, but here's the rough workflow:
# 
# - Access the problem set and data via GitHub or Jhub
# - Work to produce the following outputs for each problem set:
#   - A raw `.ipynb` with the code for the problem set
#   - A compiled pdf that displays that code and also answers the written questions. These written questions will involve using some LaTeX syntax for equations and formatting.
#   - When applicable (e.g., part of the problem set is run in script form), a supporting `.py` file
#   
# The problem sets will be graded on both accuracy and programming style. For instance, by our second problem set, you will have learned to write functions. The problem set will be designed to test those concepts and if you revert, for instance, to writing repeated code that could be replaced with a function, points will be deducted even if that inefficient code arrives at the correct answer. 
# 
# Your lowest problem set grade of the five will be dropped.
# 
# 
# ### Final project (35% of grade)
# 
# You will work on a project that integrates the concepts we are covering into an applied data science project. The end product will be a final status-update presentation, a 10-page scientific report, and a complete GitHub repository. See the "Project Components" page for more information on these outputs.
# 
# 
# ### Team player/participation (10% of grade)
# 
# Data science is a highly collaborative activity in the real world, and you should think of your classmates as resources rather than as competition. This part of your grade will reflect:
# 
# - Interacting during class, e.g. asking and answering questions
# - Participation in class coding activities in small groups
# - Contributions to your group's final project 
# - Activity on Piazza to help classmates and advance class learning by asking and answering questions, editing others' questions, etc.
