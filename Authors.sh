#!/bin/bash

git shortlog --summary --numbered --email | cut -c8- >> AUTHORS
