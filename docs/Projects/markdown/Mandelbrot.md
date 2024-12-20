# Mandelbrot set

The Mandelbrot set is visualized on the [complex plane](https://en.wikipedia.org/wiki/Complex_plane), where it is calculated until it either hits the maximum iteration number or diverges. The escape time (number of iterations) determines the pixel value and, in this example, is assigned a color corresponding to the number of iterations it takes to escape. The points where the Mandelbrot set exists are colored black, while points outside the set are assigned colors based on how long they take to diverge.

<center>
<img src="/docs/assets/mandelbrot_whole.png" alt="entire mandelbrot set width="300" height="300">
</center>

**The iterative formula**:
$$ z\_{n+1} = z\_n^2 + z\_0 $$
$$ z\_0 = 1 $$

[Plotting Algoritums](https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set)

## Deep Dive

---

### Optimizing Space using Row-Major

Inorder to save space and to prepare for the bitmap generation we use a row major format this is how we will store the color channels for each pixel.
[Row-Major](https://en.wikipedia.org/wiki/Row-_and_column-major_order#:~:text=In%20row%2Dmajor%20order%2C%20the,column%20in%20column%2Dmajor%20order.)

```cpp
    std::vector<uint8_t> image(WIDTH * HEIGHT * 3); 
```

### Converting Complex Numbers to Cartesian Coordinates

the mandelbrot set is plotted on the complex plane, where each point is represented by

$$c = x + yi$$

- X: real part, mapped to the horixontal axis
- Y: imaginary part, mapped to the vertical axis

---
Linear Mapping 
The mandel brot set only exits with in the area of Real axis: [-2,2] and Imaginary:[2,-2] this is because anoy points outside this will diverge too quickly.

---

### Coloring

a quadraic weight funtion is used to set the value of each color a color mutiplyer is used allow the ratio of colors to be changed

```cpp
    r = static_cast<uint8_t>(color_mut[0] * (1 - iter_normal)  * iter_normal * 255);
    g = static_cast<uint8_t>(color_mut[1] * (1 - iter_normal)  * iter_normal * 255);
    b = static_cast<uint8_t>(color_mut[2] * (1 - iter_normal)  * iter_normal * 255);
```

<div style="display: flex; gap: 10px; justify-content: center;">
    <img src="/docs/assets/mandelbrot_whole _linear_color.png" alt="Image 1" style="width: 45%; height: auto;">
    <img src="/docs/assets/quadratic_color_weights.png" alt="Image 2" style="width: 50%; height: 50%;">
</div>

As you can see from the images in this example the color 

```cpp
    r = static_cast<uint8_t>(color_mut[0] * (1 - iter_normal) * iter_normal * iter_normal * iter_normal * 255);
    g = static_cast<uint8_t>(color_mut[1] * (1 - iter_normal) * iter_normal * iter_normal * 255);
    b = static_cast<uint8_t>(color_mut[2] * (1 - iter_normal) * iter_normal * 255);

```


<div style="display: flex; gap: 10px; justify-content: center;">
    <img src="/docs/assets/mandelbrot_whole.png" alt="Image 1" style="width: 45%; height: auto;">
    <img src="/docs/assets/higher_order_quadratic.png" alt="Image 2" style="width: 50%; height: 50%;">
</div>

even tho the iteration number are unchanged we have compleatly differnt result by chnaging the way we color the set.

## To-Do List

### Visual Settings

- Experiment with color settings:
  - Aim for a palette with more orange and red tones instead of black and blue.
- Add more color iteration options for customization.

### Features

- Expand the fractals collection:
  - Julia.

### Website

- Update the website:
  - Include the new fractals and color options.
  - Replace outdated images with updated visuals.
