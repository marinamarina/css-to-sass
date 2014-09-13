# CSS-to-SASS converter

Have you ever had to migrate legacy CSS to new systems? All the cool guys are using SASS now - and converting CSS to SASS by hand is a laborious, error-prone process we shouldn't have to worry about anymore.

Introducting the *CSS-to-SASS converter*, written in Python. Still an early prototype at this stage, but it works.

## Usage

```
git clone https://github.com/marinamarina/css-to-sass.git

cd css-to-sass
```

Input and output data are located in the data folder
Place your css code into the file data/main.css

```
chmod +x run.py
python run.py

You can find the converted data in main.scss file
```
## Variable arguments
If you would like to specify other file locations, you can use this command:

→ python run.py data/my_file.css data/my_file.scss

(This is as far as I've got so far. Amend the code to your requirements as necessary.)

## Example input and output

Converts

```css
#my_element ul.test {
    list-style-type: none
}

#my_element ul.test {
    color: white;
    background: black;
}

#my_element ul.test .list-item a {
    text-decoration: none;
}

#my_element ul.test .list-item:last-child a {
    font-weight: bold;
}
```

into

```sass
#my_element ul.test {
    
    list-style-type: none;
    color: white;
    background: black;

    .list-item a {

        text-decoration: none;

        &:last-child {
            font-weight: bold;
        }
    }
}
```
