# LiDARSpectra
## Add-on for Blender

## Introduction
Welcome to **LiDARSpectra add-on**, an innovative Blender add-on designed to simulate Light Spectral Information. This add-on is built upon the VI-Suite, leveraging its features.

## Prerequisites
Before installing LiDARSpectra add-on, ensure that you have Blender installed on your computer. This add-on requires Blender version `2.93.11` or later. Additionally, it is based on the VI-Suite add-on, which must be installed prior to installing our add-on.

## Installation Instructions

### Step 1: Install Blender
Download and install Blender if you haven't already. Blender can be downloaded from [Blender's official website](https://www.blender.org/download/).

### Step 2: Install VI-Suite
1. Download the VI-Suite add-on from [VI-Suite's GitHub repository](https://github.com/rgsouthall/vi-suite06) or the provided source.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click `Install` and navigate to the downloaded VI-Suite `.zip` file.
4. Select the file and click `Install Add-on`.
5. Ensure that the VI-Suite add-on is enabled by checking the box next to its entry in the add-ons list.

### Step 3: Install LiDARSpectra
1. Download the LiDARSpectraAddon.zip, light and reflectance databases, or use your own database.
2. You might want to setup your own paths of database in **Specfunc.py** in the add-on files.
3. Repeat the steps as you did with VI-Suite to install. Open Blender, go to `Edit > Preferences > Add-ons`, click `Install`, navigate to your downloaded `.zip` file, select and install it.
4. Enable **VI-Spectra** by checking the box next to it in the add-ons list.

## Usage
After installation, you can select the surfaces/objects in the scene and assign them different attributes in the GUI. You need to have at least one light sensor object in the scene. After it, click **Calculate** button to generate the spectral information.


## Acknowledgements
Please reference our paper:
