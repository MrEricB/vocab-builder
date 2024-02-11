
# Vocab Builder API

A Flask API for learning new words, specifically for the [GRE](https://en.wikipedia.org/wiki/Graduate_Record_Examinations). This API is part of a project for school.




## How to run it

To run this project:

Clone the repository into your working directory:
```bash
  git clone https://github.com/MrEricB/vocab-builder.git
```
Move into the cloned directory:
```bash
cd vocab-builder
```
**Optional:** Create virtual development enviroment

Here we will use [pipenv](https://gist.github.com/bradtraversy/c70a93d6536ed63786c434707b898d55)

```bash
pipenv install -r requierments.txt
```
Else install packages:
```bash
pip install -r requierments.txt
```
Once everythin is installed the API can now be run.

By defualt this runs on port 5000
```bash
python app.py
```



## API Reference

#### Get a random word to define

```http
  GET /randomword
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `None` | | Returns a random word |

#### Get random defintion

```http
  GET /whatis
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `None`      |  | Returns a definition of a random word |


#### Get definition of word
```http
  GET /define/word
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `word`      | `string` | Returns the definition of word |




## Roadmap

- Add [SQLite](https://www.sqlite.org/index.html) database

- Add functionality for usres to add their own words and definitions

