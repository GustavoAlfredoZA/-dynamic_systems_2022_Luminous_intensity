# -dynamic_systems_2022_Luminous_intensity
## Definition
Exercise for the evaluaci.

### Writed by: Gustavo Alfredo Zárate Acosta (GustavoZA20@hotmail.com)
Information Technology in Sciences student at ENES Morelia, UNAM.

## Introduction
Evaluation exercise of a dynamic system of Luminous intensity and Optical depth.

## Methodology

We first implement the following equation from Planck's law of blackbody radiation
Where h is Planck's constant, c is the speed of light in a vacuum, k is Boltzmann's constant, v is the frequency of electromagnetic radiation, and T is the absolute temperature of the body.
![Results](planck.png)
Then the absorption coefficient equation for thermal electrons is implemented, where n_e is the number density of electrons, T is the absolute temperature of the object.
![Results](opacity.png)
Then in the system the optical depth is defined,
where we define dx as the difference between two height values, to the height path, also using the previously defined opacity function.
![Results](optical_depth.png)
For luminous intensity we define the following function where t_v is the previously defined optical depth and we use the black body radiation function as our S_v function.
![Results](luminous_intensity.png)
And we use the data from the file data1.csv as parameters of our system

## Requiriments
This proyect use Python v. 3.8,
### Libraries
1. Numpy
     - ```pip3 install numpy==1.61.2```
2. Matplotlib
     - ```pip3 install matplotlib==3.0.2```
3. Scipy
     - ```pip3 install scipy==1.6.2```
4. Pandas
     - ```pip3 install matplotlib==1.2.4```


## Run
  Create an image called 'examen_SD.png' and display it in an interactive window
  ```bash
   $ python examen_SD.py
  ```
### Results
![Results](examen_SD.png)

## References
- [Matplotlib](https://matplotlib.org/2.1.2/) Documentation.
- [Dynamic System 2022 course](https://github.com/giccunam/dynamicsystems2022)as.
- [Scipy Constants] (https://pythonguides.com/scipy-constants/)
- [Radiacion de cuerpo negro] (https://es.wikipedia.org/wiki/Radiaci%C3%B3n_de_cuerpo_negro#La_ley_de_Planck_de_la_radiaci%C3%B3n_del_cuerpo_negro)
- [Constante_de_Planck] (https://es.wikipedia.org/wiki/Constante_de_Planck)
- [Plasma oscillation] (https://en.wikipedia.org/wiki/Plasma_oscillation)
- [Profundidad optica] (https://es.wikipedia.org/wiki/Profundidad_%C3%B3ptica)
-  STRUCTURE OF THE SOLAR CHROMOSPHERE. III. MODELS OF THE EUV BRIGHTNESS
COMPONENTS OF THE QUIET SUN J. E. Vernazza, E. H. Avrett, R. Loeser. 1981
- Radio EMISSION FROM THE SUN AND STARS. George A. Dulk 1985.
