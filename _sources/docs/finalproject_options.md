---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(finalproject_options)=

# Project Options

You will select one of three options for your final project:


## 1. Social Impact Practicum topic: Training medical students to work with Intellectual and Developmental Disabilities (IDD)

With support from the [Dartmouth Center for Social Impact](https://students.dartmouth.edu/social-impact/), one option for your final project is to complete a [Social Impact Practicum](https://students.dartmouth.edu/social-impact/programs-initiatives/students/social-impact-practicums-sips) (SIP): a chance for you to use your data science skills to help a real-world organization. 

Your partner and data provider for the Social Impact Practicum will be the National Center for START Services (NCSS) at the Institute on Disability at University of New Hampshire (UNH). The START (Systemic, Therapeutic, Assessment, Resources, and Treatment) model advanced at UNH is a comprehensive model of service supporting the optimization of independence, treatment, and community living for individuals with IDD and mental health needs. You can find more information about the Center for Start Services [here](https://centerforstartservices.org/) and [here](https://iod.unh.edu/projects/center-start-services). To get a look at the START program in action, check out [this documentary (66 mins)](https://centerforstartservices.org/START-film).

If you choose this project option, you have two options. The first is to analyze the results of medical student training for prescribing to folks with Intellectual and Developmental Disabilities (IDD). The second is to study a large dataset on experiences and outcomes for START participants.

### SIP Option 1: Medical training data

This option addresses an important issue in public health: *How do medical professionals interact with patients with IDD, and how can medical student training improve this?* Here is more information from the project partner:

> As part of a strategic initiative to develop best practices for prescribers who work with patients with IDD and mental health concerns (IDD_MH), NCSS/UNH has begun piloting training content with medical students (residents, fellows and second/third year medical students) at the Geisel School of Medicine at Dartmouth, the medical school and the University of Puerto Rico, and Franklin Pierce University’s Physician Assistant Program.  This includes a 6 hours of trainings based on the recently published [Integrated Mental Health Treatment Guidelines for Prescribers in Intellectual and Developmental Disabilities](https://centerforstartservices.org/IDD-MH-Prescribing-Guidelines) as well as pre- and post-evaluation data.

> The START program at UNH would like students of QSS 20 to analyze this training evaluation data to assess strengths and growth points as well as recommend changes based on the data which could improve efficacy, retention, impact, or all of the above.  (For example, the training videos which include the lived experience of individuals are already scoring higher, so that is one already-identified place where small changes to the content delivery medium could improve results).

> At present (Fall 2022), there are 200+ evaluations of 40+ medical students, and by November we expect this number to grow to 300+ evaluations from 60+ distinct medical students.

The training was six hours in length, and students evaluated the program by answering multiple choice and open-ended questions. You can view the [program evaluation surveys here](https://drive.google.com/drive/folders/1csAgglJta0Nbriyl358LKBwecVgKlbwb?usp=sharing) or see the [general SIP proposal](https://docs.google.com/document/d/1zctCWNn5S3PaZGCyKkKo0lnMBxiYUiDv/edit?usp=sharing&ouid=106209867651452643666&rtpof=true&sd=true) for more info.

Here are a few broad questions you could investigate if choosing this option: 

_Is this working?_

* Changes in perspectives and depth of understanding toward IDD?
* Consider training outcomes from ranking questions (e.g., with regression) and free-form text (e.g., topic models)
* Connect with participant demographics

_What training components matter most?_

* Expert presentation & best practices
* Guest speakers with personal experience of IDD
* Other training elements suggested in open-ended questions


### SIP Option 2: START Information Reporting System (SIRS)

These data include about 13,000 START participants from 2013 to 2021. The more detailed files include only the cohort of participants from 2019 to 2020. These data include: 
* Encounters with law enforcement
* Emergency visits
* Physical restraint during crises
* Demographics
* Intake info

Here are a few broad questions you could investigate if choosing this option: 

**Over full SIRS data**:
* What is the composition of START participants by race, gender, and living situation, and how do these correlate with disadvantage in terms of family background, crisis events, or aggressive behavior?
* How often do START participants encounter law enforcement or exhibit aggressive or self-harming behaviors, and how have these changed over time? 
* How did trends in START participation (e.g., hospital visits) change with the COVID pandemic compared with the previous, longer time scale (back to 2010)?

**Over 2019-2020 cohort**:
General question: *How have those with disabilities fared during COVID-19 and what racial inequalities do we see in its impact?*
* Did the COVID lockdowns increase suicidal ideation over time, e.g. through decreased access to mental health support or stress related to living situations?
* Did the COVID lockdowns introduce challenges due to encounters with law enforcement, who sometimes respond inappropriately to young adults with disabilities (e.g., they may refer them to Emergency Departments with excessive frequency)?
* What themes emerge in the Family Experiences with Severe Mental Illness Scale (FEIS) open responses (e.g., through topic modeling), such as desire for higher caregiver involvement and/or caregiver receptivity to this desire---and how do these themes vary with family demographics or other background factors?

You can view the [data dictionary here](https://docs.google.com/spreadsheets/d/1HV5kl3IOzWen91LkHBcFZi3so_angRf8/edit?usp=sharing&ouid=106209867651452643666&rtpof=true&sd=true). 

**These options require working in a group.**


## 2. Deeper dive into felony sentencing data used in problem sets 1 and 2

In the first two problem sets, you used and got familiar with the Cook County State Attorney’s Office Felony Sentencing Data to investigate racial disparities in sentence length and within-judge disparities. With this project option, you’d do a deeper dive into the felony sentencing data to address another question, such as:
1. more rigorous analyses of disparities using causal inference techniques
2. analyses of other fields in the data (e.g., neighborhood disparities; how judge demographics relate to sentencing behavior)

**This option requires working in a group.**


## 3. Use Senior Thesis/independent project 

If you're already pursuing a significant research project, you may use this course to advance an existing work in progress, covering parts and analysis you might not include otherwise. 

The project needs to align with the [evaluation criteria](https://github.com/jhaber-zz/QSS20_public/blob/main/finalproj_guidelines/final_project_rubric.csv) — e.g., it must result in data you can share with us, a repo you can share, and a 10-page CS-style report.

Please choose this option with caution as you will be held to same grading standard as groups of 3-4. Moreover, unless you have already made substantial progress on an independent project, you probably won't be able to finish it in one short quarter.

**You can complete this option either individually or in a group** (i.e., by focusing on one person’s project and getting group help).