# Neural-Style-Transfer

It is a deep learning technique used to blend the stylization of a style reference image into the given context image. Hence, we can paint any image like any beautiful artwork!


## Technique

This algorithm can be easily applied using OpenCV-python and pre-trained models trained by Justin Johnson. His method works quite fast, but it requires to explicitly train a network in specific to the style reference image. He has provided 11 style reference models. To generate your own style model, you can check it out [here](https://github.com/jcjohnson/fast-neural-style).


## Results

Original image

<img src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/input/house.jpg" />
<br />


Different style transfers:

1. candy

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/candy.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/candy_house.jpg" />
</div>
<br /><br />

2. composition_vii

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/composition_vii.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/composition_vii_house.jpg" />
</div>
<br /><br />

3. feathers

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/feathers.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/feathers_house.jpg" />
</div>
<br /><br />

4. la_muse

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/la_muse.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/la_muse_house.jpg" />
</div>
<br /><br />

5. mosaic

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/mosaic.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/mosaic.jpg" />
</div>
<br /><br />

6. starry_night

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/starry_night.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/starry_night_house.jpg" />
</div>
<br /><br />

7. the_scream

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/the_scream.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/the_scream_house.jpg" />
</div>
<br /><br />

8. the_wave

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/the_wave.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/the_wave_house.jpg" />
</div>
<br /><br />

9. udnie

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/styles/udnie.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/udnie_house.jpg" />
</div>
<br /><br />


Difference between instance_norm and eccv16 models:

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/la_muse_house.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/la_muse1_house.jpg" />
</div>
<br /><br />

<div style="float:left"><img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/starry_night_house.jpg" />
<img width="45%" src="https://github.com/Sudarshana2000/Neural-Style-Transfer/blob/master/images/output/starry_night1_house.jpg" />
</div>
<br /><br />
