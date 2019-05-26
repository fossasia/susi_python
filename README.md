# Python Wrapper for the Susi AI API

This is part of the SUSI.AI project which aims to implement a full infrastructure for Free and Open Source Smart Speaker and Personal Assistants. This sub-project implements an API for the AI server, https://github.com/fossasia/susi_server

## Project Overview 

The whole SUSI.AI ecosystem consists of the following parts:
```
 * server back-end
 |_ susi_server        (the brain of the infrastructure, a server which computes answers from queries)
 |_ susi_skill_data    (the knowledge of the brain, a large collection of skills provided by the SUSI.AI community)
 
 * android front-end
 |_ susi_android       (Android application which is a client for the susi_server at https://api.susi.ai)
 
 * iOS front-end
 |_ susi_iOS           (iOS application which is a client for the susi_server at https://api.susi.ai)
 
 * Content Management System for the SUSI.AI Skills - Home of the SUSI.AI community
 |_ accounts.susi.ai   (React Application, User Account Management for the CMS)
 |_ chat.susi.ai       (React Application, a client for the susi_server at https://api.susi.ai)
 |_ susi_skill_cms     (React Application, the content management system for susi skills)
 
 * Smart Speaker - Software to turn a Raspberry Pi into a Personal Assistant
 | Several sub-projects come together in this device
 |_ susi_installer     (Framework which can install all parts on a RPi and also is able to create SUSIbian disk images)
 |_ susi_python        (Python API for the susi_server at https://api.susi.ai)
 |_ susi_server        (The same server as on api.susi.ai, hostel locally for maximum privacy. No cloud needed)
 |_ susi_skill_data    (The skills as provided by susi_server on api.susi.ai; pulled from the git repository automatically)
 |_ susi_linux         (a state machine in python which uses susi_python, Speech-to-text and Text-to-speech functions)
```
This projects covers the client API function to access the susi_server either hosted locally or on api.susi.ai
Currently the wrapper supports basic chat and auth functionalities.

## Usage
For usage sample refer: [sample.py](sample.py)

## Roadmap
Implement all queries supported by Susi AI API like Maps,Charts etc. and provide an easy interface to access them in Python.
