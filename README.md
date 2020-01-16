# Python Wrapper for the SUSI.AI API

Master: [![Build Status](https://travis-ci.org/fossasia/susi_python.svg?branch=master)](https://travis-ci.org/fossasia/susi_python)
Development: [![Build Status](https://travis-ci.org/fossasia/susi_python.svg?branch=development)](https://travis-ci.org/fossasia/susi_python)
[![Join the chat at https://gitter.im/fossasia/susi_hardware](https://badges.gitter.im/fossasia/susi_hardware.svg)](https://gitter.im/fossasia/susi_hardware?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Twitter Follow](https://img.shields.io/twitter/follow/susiai_.svg?style=social&label=Follow&maxAge=2592000?style=flat-square)](https://twitter.com/susiai_)

The susi_python repository holds the Python wrapper for SUSI.AI which covers the client API function to access the susi_server either hosted locally or on https://api.susi.ai. This sub-project implements an API for the AI server, https://github.com/fossasia/susi_server. Currently the wrapper supports basic chat and auth functionalities. 

The SUSI.AI project provides a full infrastructure for a Free and Open Source Smart Speaker and Personal Assistants. 

## Project Overview 

The SUSI.AI ecosystem consists of the following parts:
```
 * Web Client and Content Management System for the SUSI.AI Skills - Home of the SUSI.AI community
 |_ susi.ai   (React Application, User Account Management for the CMS, a client for the susi_server at https://api.susi.ai the content management system for susi skills)
 
 * server back-end
 |_ susi_server        (the brain of the infrastructure, a server which computes answers from queries)
 |_ susi_skill_data    (the knowledge of the brain, a large collection of skills provided by the SUSI.AI community)
 
 * android front-end
 |_ susi_android       (Android application which is a client for the susi_server at https://api.susi.ai)
 
 * iOS front-end
 |_ susi_iOS           (iOS application which is a client for the susi_server at https://api.susi.ai)
 
 * Smart Speaker - Software to turn a Raspberry Pi into a Personal Assistant
 | Several sub-projects come together in this device
 |_ susi_installer     (Framework which can install all parts on a RPi and Desktops, and also is able to create SUSIbian disk images)
 |_ susi_python        (Python API for the susi_server at https://api.susi.ai or local instance)
 |_ susi_server        (The same server as on api.susi.ai, hosted locally for maximum privacy. No cloud needed)
 |_ susi_skill_data    (The skills as provided by susi_server on api.susi.ai; pulled from the git repository automatically)
 |_ susi_linux         (a state machine in python which uses susi_python, Speech-to-text and Text-to-speech functions)
 |_ susi.ai            (React Application, the local web front-end with User Account Management, a client for the local deployment of the susi_server, the content management system for susi skills)
```


## Usage
For usage sample refer: [sample.py](sample.py)

## Roadmap
Implement all queries supported by Susi AI API like Maps,Charts etc. and provide an easy interface to access them in Python.
