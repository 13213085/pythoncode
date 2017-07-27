# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 08:39:43 2017

@author: 29907
"""
#batch_update.py - update python packages in bulk

import pip,subprocess

for dist in pip.get_installed_distributions():
    subprocess.call('pip install '+dist.project_name,shell=True)