# Mandelbrot set

The Mandelbrot set is visualized on the [complex plane](https://en.wikipedia.org/wiki/Complex_plane), where it is calculated until it either hits the maximum iteration number or diverges. The escape time (number of iterations) determines the pixel value and, in this example, is assigned a color corresponding to the number of iterations it takes to escape. The points where the Mandelbrot set exists are colored black, while points outside the set are assigned colors based on how long they take to diverge.

<center>
<img src="../assets/mandelbrot_whole.png" alt="entire mandelbrot set width="300" height="300">
</center>

**The iterative formula**:
$$ z\_{n+1} = z\_n^2 + z\_0 $$
$$ z\_0 = 1 $$

---

```cpp
while(iterations < MAX_ITER &&(z_real * z_real + z_imaginary * z_imaginary) <= 2.0)
```

```cpp
int mandelbrot(double real, double imaginary){
    int iterations = 0 ;
    double z_real = 0.0  , z_imaginary = 0.0;

    while (iterations < MAX_ITER && (z_real * z_real + z_imaginary * z_imaginary) <= 2.0) {
        double z_real_next = z_real * z_real - z_imaginary * z_imaginary + real;
        z_imaginary       = 2.0 * z_real * z_imaginary + imaginary;
        z_real            = z_real_next;
        iterations++;
    }

    return iterations;
}
```

## Deep Dive

---

### Optimizing Space using Row-Major

Inorder to save space and to prepare for the bitmap generation we use a row major format this is how we will store the color channels for each pixel.
[Row-Major](https://en.wikipedia.org/wiki/Row-_and_column-major_order#:~:text=In%20row%2Dmajor%20order%2C%20the,column%20in%20column%2Dmajor%20order.)

```cpp
    std::vector<uint8_t> image(WIDTH * HEIGHT * 3); 
```

---

### Converting Complex Numbers to Cartesian Coordinates

the mandelbrot set is plotted on the complex plane, where each point is represented by

$$c = x + yi$$

- X: real part, mapped to the horixontal axis
- Y: imaginary part, mapped to the vertical axis
  
To display the Mandelbrot set on the Cartesian plane, we use a linear mapping that translates points from the complex plane. The set is confined to the region where the real axis spans [-2, 2] and the imaginary axis spans [-2, 2], as points outside this area diverge too quickly to contribute to the set.

[Plotting Algoritums](https://en.wikipedia.org/wiki/Plotting_algorithms_for_the_Mandelbrot_set)

---

### Coloring

Once the number of iterations has been calculated, we can apply coloring to the data. Two different methods are used to achieve this, each producing drastically different outcomes. A quadratic weight function is used to determine the value of each color. Additionally, a color multiplier is applied to adjust the ratio of colors, allowing for greater control over the final appearance.

```cpp
    r = static_cast<uint8_t>(color_mut[0] * (1 - iter_normal)  * iter_normal * 255);
    g = static_cast<uint8_t>(color_mut[1] * (1 - iter_normal)  * iter_normal * 255);
    b = static_cast<uint8_t>(color_mut[2] * (1 - iter_normal)  * iter_normal * 255);
```

<div style="display: flex; gap: 10px; justify-content: center;">
    <img src="../assets/mandelbrot_whole _linear_color.png" alt="Image 1" style="width: 45%; height: auto;">
    <img src="../assets/quadratic_color_weights.png" alt="Image 2" style="width: 50%; height: 50%;">
</div>

As you can see from the images in this example, the color is much more banded, meaning there are more distinct lines in the images, and the colors are not blended as much. The graph on the left represents the colors based on the number of iterations.

```cpp
    r = static_cast<uint8_t>(color_mut[0] * (1 - iter_normal) * iter_normal * iter_normal * iter_normal * 255);
    g = static_cast<uint8_t>(color_mut[1] * (1 - iter_normal) * iter_normal * iter_normal * 255);
    b = static_cast<uint8_t>(color_mut[2] * (1 - iter_normal) * iter_normal * 255);

```

<div style="display: flex; gap: 10px; justify-content: center;">
    <img src="../assets/mandelbrot_whole.png" alt="Image 1" style="width: 45%; height: auto;">
    <img src="../assets/higher_order_quadratic.png" alt="Image 2" style="width: 50%; height: 50%;">
</div>

Even though the iteration numbers remain unchanged, we get completely different results by altering the way we color the set. In this example, we use a higher-order polynomial. The graph shows how each of the red, green, and blue values is calculated. The blue values have a parabolic shape, making blue the dominant color, even though it has a low color multiplier of only 4 in this example.

---

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
